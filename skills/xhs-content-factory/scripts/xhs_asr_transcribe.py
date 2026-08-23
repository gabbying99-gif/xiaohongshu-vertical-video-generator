import json
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from faster_whisper import WhisperModel


def fmt_time(seconds: float) -> str:
    seconds = max(0.0, float(seconds))
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: xhs_asr_transcribe.py <asset-dir> [model-size]", file=sys.stderr)
        return 2

    asset_dir = Path(sys.argv[1])
    model_size = sys.argv[2] if len(sys.argv) > 2 else "small"
    video_path = asset_dir / "video.mp4"
    audio_path = asset_dir / "audio_16k.wav"
    transcript_path = asset_dir / "transcript.txt"
    segments_path = asset_dir / "transcript_segments.json"

    if not video_path.exists():
        raise FileNotFoundError(video_path)

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(video_path),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-acodec",
            "pcm_s16le",
            str(audio_path),
        ],
        check=True,
    )
    if not audio_path.exists():
        raise RuntimeError("ffmpeg did not create audio file")

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(audio_path),
        language="zh",
        vad_filter=True,
        beam_size=5,
    )

    rows = []
    lines = ["【ASR逐字稿】"]
    for segment in segments:
        text = segment.text.strip()
        if not text:
            continue
        rows.append({"start": segment.start, "end": segment.end, "text": text})
        lines.append(f"{fmt_time(segment.start)}-{fmt_time(segment.end)} {text}")

    transcript_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    segments_path.write_text(
        json.dumps(
            {
                "language": info.language,
                "language_probability": info.language_probability,
                "duration": info.duration,
                "model_size": model_size,
                "segments": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "audio": str(audio_path),
                "transcript": str(transcript_path),
                "segments": len(rows),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: xhs_extract_video_cover.py <asset-dir> [timestamp]", file=sys.stderr)
        return 2

    asset_dir = Path(sys.argv[1])
    timestamp = sys.argv[2] if len(sys.argv) > 2 else "00:00:01"
    video_path = asset_dir / "video.mp4"
    cover_path = asset_dir / "video_cover.jpg"

    if not video_path.exists():
        raise FileNotFoundError(video_path)

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-ss",
            timestamp,
            "-i",
            str(video_path),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(cover_path),
        ],
        check=True,
    )
    if not cover_path.exists():
        raise RuntimeError("ffmpeg did not create video cover")

    print(str(cover_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

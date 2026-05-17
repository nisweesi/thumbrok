import subprocess
from pathlib import Path

from models import MomentWithImage, MomentsResponseFormat


def take_snippet(start: float, end: float, filename: str) -> str:
    """
    Take a single video frame at the midpoint between start and end times.
    Returns the output image filename.
    """
    # Compute midpoint time in seconds
    mid = (start + end) / 2.0
    # Format time as seconds with millisecond precision
    mid_str = f"{mid:.3f}"
    base = Path(filename).stem

    output_dir = Path("frames")
    output_dir.mkdir(parents=True, exist_ok=True)

    output = output_dir / f"{base}_{mid_str}.jpg"

    # Build ffmpeg command to capture one frame
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-ss",
        mid_str,
        "-i",
        filename,
        "-frames:v",
        "1",
        "-q:v",
        "2",
        output,
    ]
    # Execute ffmpeg and raise on failure
    subprocess.run(cmd, check=True)
    return str(output)


# loop through the json and take a sinppet in the middle second between the start and end point
def take_snippets(
    moments_response: MomentsResponseFormat, filename: str
) -> list[MomentWithImage]:
    """
    Given a moments JSON (path or dict) and a video filename,
    extract one screenshot per moment at the midpoint time.
    Returns list of output image filenames.
    """
    moments_with_images = []

    for moment in moments_response.moments:
        image_path = take_snippet(start=moment.start, end=moment.end, filename=filename)

        moments_with_images.append(
            MomentWithImage(
                start=moment.start,
                end=moment.end,
                reason=moment.reason,
                thumbnail_text=moment.thumbnail_text,
                visual_idea=moment.visual_idea,
                image_path=image_path,
            )
        )

    return moments_with_images

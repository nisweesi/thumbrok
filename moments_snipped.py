import json
import subprocess
from pathlib import Path


def take_snippet(start: float, end: float, filename: str) -> str:
    """
    Take a single video frame at the midpoint between start and end times.
    Returns the output image filename.
    """
    # Compute midpoint time in seconds
    mid = (start + end) / 2.0
    # Format time as seconds with millisecond precision
    mid_str = f"{mid:.3f}"
    # Prepare output filename: <video_stem>_<mid>.jpg
    base = Path(filename).stem
    output = f"{base}_{mid_str}.jpg"
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
    return output


# loop through the json and take a sinppet in the middle second between the start and end point
def take_snippets(moments_json, filename: str) -> list[str]:
    """
    Given a moments JSON (path or dict) and a video filename,
    extract one screenshot per moment at the midpoint time.
    Returns list of output image filenames.
    """
    # Load JSON data if a file path is provided
    if isinstance(moments_json, str):
        with open(moments_json, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = moments_json
    moments = data.get("moments", [])
    outputs: list[str] = []
    for moment in moments:
        start = moment.get("start")
        end = moment.get("end")
        # Validate times
        if start is None or end is None:
            continue
        try:
            img = take_snippet(float(start), float(end), filename)
            outputs.append(img)
        except Exception:
            # Skip failed snippets
            continue
    return outputs

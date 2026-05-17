# transcript service
import whisper
from datetime import timedelta, datetime
import srt
import json


def transcribe(filename: str):
    model = whisper.load_model("base")

    result = model.transcribe(filename, language="en")

    subs = []

    for i, seg in enumerate(result["segments"]):
        subs.append(
            srt.Subtitle(
                index=i + 1,
                start=timedelta(seconds=round(seg["start"], 3)),
                end=timedelta(seconds=round(seg["end"], 3)),
                content=seg["text"],
            )
        )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    with open(f"{filename}_{timestamp}.srt", "w", encoding="utf-8") as f:
        f.write(srt.compose(subs))

    with open(f"{filename}_{timestamp}.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

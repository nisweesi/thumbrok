# transcript service
import json
import os

import whisper
from datetime import timedelta
import srt


def transcribe_video(
    filename: str, output_dir: str = "generated_transcript", lang: str = "en"
):
    model = whisper.load_model("base")

    result = model.transcribe(filename, language=lang, fp16=False)

    subtitle = []
    segments = []

    for i, seg in enumerate(result["segments"]):
        segment = {
            "index": i + 1,
            "start": round(seg["start"], 3),
            "end": round(seg["end"], 3),
            "content": seg["text"].strip(),
        }

        segments.append(segment)

        subtitle.append(
            srt.Subtitle(
                index=i + 1,
                start=timedelta(seconds=round(seg["start"], 3)),
                end=timedelta(seconds=round(seg["end"], 3)),
                content=seg["text"],
            )
        )

    transcript_json = {
        "filename": filename,
        "language": lang,
        "segments": segments,
    }

    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(filename))[0]

    generated_filename = os.path.join(output_dir, f"generated_transcript_{base_name}")

    with open(f"{generated_filename}.srt", "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitle))

    with open(f"{generated_filename}.json", "w", encoding="utf-8") as f:
        json.dump(transcript_json, f, ensure_ascii=False, indent=2)

    return transcript_json

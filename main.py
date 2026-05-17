from transcript import transcribe
from grok import moments_generator
from moments_snipped import take_snippets


def main():
    video_name = input("Enter the video name with the extensions (e.g. mp4): ")

    if not video_name:
        raise ValueError("Enter a video name")

    transcription = transcribe(video_name)
    transcription_json = moments_generator(transcription)
    take_snippets(transcription_json, video_name)


if __name__ == "__main__":
    main()

from transcript import transcribe
from grok import moments_generator


def main():
    video_name = input("Enter the video name with the extensions (e.g. mp4): ")

    if not video_name:
        raise ValueError("Enter a video name")

    transcription = transcribe(video_name)
    moments_generator(transcription)


if __name__ == "__main__":
    main()

import asyncio
import os

from xai_sdk import AsyncClient

from thumbnails_generator import generate_thumbnail
from transcript import transcribe_video
from grok import moments_generator, moment_prompts_generator
from moments_snipped import take_snippets


async def main():
    client = AsyncClient(api_key=os.getenv("XAI_API_KEY"))

    video_uploaded = input("Enter the video name with the extensions (e.g. mp4): ")

    if not video_uploaded:
        raise ValueError("Enter a video name")

    transcript_json = transcribe_video(video_uploaded)

    moments_response = await moments_generator(client, transcript_json)

    moments_with_images = take_snippets(moments_response, video_uploaded)

    moments_with_prompts = await moment_prompts_generator(
        client, transcript_json, moments_with_images
    )

    for moment in moments_with_prompts:
        output_path = await generate_thumbnail(
            client=client,
            image_prompt=moment.image_prompt,
            image_path=moment.image_path,
            output_dir="generated_images",
        )

    print(f"Generated thumbnail: {output_path}")


if __name__ == "__main__":
    asyncio.run(main())

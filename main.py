import asyncio

from transcript import transcribe
from grok import moments_generator, moment_prompts_generator
from moments_snipped import take_snippets

from xai_sdk import AsyncClient

from thumbnails_generator import generate_thumbnail

import os


async def main():
    client = AsyncClient(api_key=os.getenv("XAI_API_KEY"))

    video_name = input("Enter the video name with the extensions (e.g. mp4): ")

    if not video_name:
        raise ValueError("Enter a video name")

    transcript_json = transcribe(video_name)

    moments_response = await moments_generator(client, transcript_json)

    moments_with_images = take_snippets(moments_response, video_name)

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

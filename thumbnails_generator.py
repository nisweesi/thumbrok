import base64
import os
import uuid

import aiofiles
from pathlib import Path

from xai_sdk import AsyncClient

GROK_IMAGINE_IMAGES = "grok-imagine-image"


def image_file_to_data_url(image_path: str) -> str:
    path = Path(image_path)

    suffix = path.suffix.lower()
    if suffix in [".jpg", ".jpeg"]:
        mime_type = "image/jpeg"
    elif suffix == ".png":
        mime_type = "image/png"
    else:
        raise ValueError(f"Unsupported image type: {suffix}")

    with open(path, "rb") as f:
        image_bytes = f.read()

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{image_base64}"


async def generate_thumbnail(
    client: AsyncClient, image_prompt, image_path, output_dir="generated_images"
) -> str:
    image_url = image_file_to_data_url(image_path)

    response = await client.image.sample(
        model=GROK_IMAGINE_IMAGES, prompt=image_prompt, image_url=image_url
    )

    image_data = await response.image

    # create a folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # generate a random file name
    filename = os.path.join(output_dir, f"generated_image_{uuid.uuid4().hex[:5]}.png")

    async with aiofiles.open(filename, "wb") as f:
        await f.write(image_data)

    return filename

import base64
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

client = OpenAI()

def text_to_image(prompt, number_of_images):
    """
    Generate a image from a text
    """
    img = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        n=number_of_images,
        size="1024x1024",
        quality="high"
    )

    date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    path_name = f"src/output/{date}"
    os.makedirs(path_name, exist_ok=True)

    for i, image_data in enumerate(img.data):
        image_bytes = base64.b64decode(image_data.b64_json)
        with open(f"{path_name}/output_{i+1}.png", "wb") as f:
            f.write(image_bytes)

    list_images = os.listdir(path_name)
    list_images = [f"{path_name}/{image}" for image in list_images]

    return list_images

def image_and_text_to_image(prompt, image_path_input, number_of_images):
    """
    Generate a image from a text and a image or images
    """

    result = client.images.edit(
        model="gpt-image-1",
        image=image_path_input,
        prompt=prompt,
        n=number_of_images
    )

    datetime_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    path_name = f"src/output/{datetime_now}"
    os.makedirs(path_name, exist_ok=True)

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    # Save all generated images to files
    for i, image_data in enumerate(result.data):
        image_base64 = image_data.b64_json
        image_bytes = base64.b64decode(image_base64)
        with open(f"{path_name}/output_edit_{i+1}.png", "wb") as f:
            f.write(image_bytes)

    list_images = os.listdir(path_name)
    list_images = [f"{path_name}/{image}" for image in list_images]

    return list_images

# teste
# path_input = open("image.png", "rb")
# image_and_text_to_image("Crie uma peça publicitário para o lançamento do novo porsche 911, use a imagem anexada como referencia mais crie uma nova a partir do zero", path_input, 2)
# text_to_image("Crie uma peça publicitário para o lançamento do novo macbook com preço de 1000 usd", 2)

import requests
from PIL import Image
from io import BytesIO
from config import HF_API_KEY

API_URL= "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image_from_text(prompt: str) -> Image.Image:
    headers={"Authorization":f"Bearer {HF_API_KEY}"}
    payload={"inputs":prompt}

    try:
        response=requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        if "image" in response.headers.get("Content-Type",""):
            image=Image.open(BytesIO(response.content))
            return image
        else:
            raise Exception("The response is not an image. It might be an error message.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    
def main():
    print("Welcome to the Text-to_Image Generator!")
    print("Type 'exit' to quit the program.\n")

    while True:
        prompt=input("Enter a description for the image you want to generate:\n").strip()
        if prompt.lower()=="exit":
            print("Goodbye:")
            break
        print("\n Generating image...\n")
        try:
            image=generate_image_from_text(prompt)
            image.show()

            save_option=input("Do you want to save this image? (yes/no): ").strip().lower()
            if save_option == "yes":
                file_name=input("Enter a name for the image file (without extension): ").strip()
                image.save(f"{file_name}.png")
                print(f"Image save as {file_name}.png\n")

        except Exception as e:
            print(f"An error occured: {e}\n")

        print("-"*80 + "\n")

if __name__=="__main__":
    main()
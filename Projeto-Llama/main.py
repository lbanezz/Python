import requests
import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def ask_about_image(image_path, question):
    image_base64 = encode_image_to_base64(image_path)

    payload = {
        "model": "llava",
        "prompt": question,
        "images": [image_base64]
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload, stream=True)

    print("\n🧠 Resposta da IA:")
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'), end='')

# Exemplo de uso
ask_about_image("imagem.jpg", "O que está acontecendo nesta imagem?")

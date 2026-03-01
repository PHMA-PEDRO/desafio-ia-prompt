import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
resposta = requests.get(url)

if resposta.status_code == 200:
    for modelo in resposta.json().get('models', []):
        if 'generateContent' in modelo.get('supportedGenerationMethods', []):
            print(modelo['name'])
else:
    print("Erro ao buscar modelos:", resposta.text)
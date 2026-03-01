import os
import json
import requests
from dotenv import load_dotenv
from services.cache import obter_resposta_em_cache, armazenar_resposta_no_cache

# Carrega as variáveis do arquivo .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
MODEL_NAME = "gemini-2.5-flash"

def gerar_conteudo_gemini(prompt_texto):
    """
    Envia o prompt para a API do Google Gemini, garantindo o retorno em JSON.
    Verifica primeiro se a resposta já existe no cache local.
    """
    if not API_KEY:
        raise ValueError("Chave da API não encontrada. Verifique o arquivo .env.")

    # 1. Verifica se o prompt já foi processado antes (Cache Hit)
    resposta_cache = obter_resposta_em_cache(prompt_texto)
    if resposta_cache:
        print("[CACHE] Resposta carregada localmente (economizou uma requisição!)")
        return resposta_cache

    # 2. Se não estiver no cache, prepara a requisição para a API
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "contents": [{"parts": [{"text": prompt_texto}]}],
        "generationConfig": {
            "responseMimeType": "application/json",
        }
    }

    try:
        # Fazendo a requisição HTTP POST
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        dados_resposta = response.json()
        texto_gerado = dados_resposta["candidates"][0]["content"]["parts"][0]["text"]
        
        # Limpeza de precaução: remove blocos de markdown caso a IA os envie
        texto_limpo = texto_gerado.strip()
        if texto_limpo.startswith("```json"):
            texto_limpo = texto_limpo[7:]
        elif texto_limpo.startswith("```"):
            texto_limpo = texto_limpo[3:]
            
        if texto_limpo.endswith("```"):
            texto_limpo = texto_limpo[:-3]
            
        # Converte a string limpa para um dicionário Python
        resultado_json = json.loads(texto_limpo.strip())
        
        # 3. Salva a nova resposta no cache antes de retornar
        armazenar_resposta_no_cache(prompt_texto, resultado_json)
        
        return resultado_json
        
    except requests.exceptions.RequestException as e:
        print(f" Erro de comunicação com a API: {e}")
        return None
    except json.JSONDecodeError:
        print(" A API não retornou um JSON válido. Retorno bruto:")
        print(texto_gerado)
        return None
    except KeyError:
        print(" Estrutura de resposta inesperada da API.")
        return None
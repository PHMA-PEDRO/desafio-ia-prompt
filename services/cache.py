import json
import os
import hashlib

CACHE_FILE = "data/cache.json"

def _gerar_hash(texto):
    return hashlib.md5(texto.encode('utf-8')).hexdigest()

def carregar_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_cache(cache_data):
    # Garante que a pasta data exista
    if not os.path.exists('data'):
        os.makedirs('data')
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=4)

def obter_resposta_em_cache(prompt):
    cache = carregar_cache()
    prompt_hash = _gerar_hash(prompt)
    return cache.get(prompt_hash)

def armazenar_resposta_no_cache(prompt, resposta):
    cache = carregar_cache()
    prompt_hash = _gerar_hash(prompt)
    cache[prompt_hash] = resposta
    salvar_cache(cache)
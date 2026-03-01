import json
import os
import time
from services.api_client import gerar_conteudo_gemini
from prompts.builder import (
    prompt_explicacao_conceitual, prompt_exemplos_praticos, prompt_perguntas_reflexao, prompt_resumo_visual,
    prompt_explicacao_basico, prompt_exemplos_basico, prompt_perguntas_basico, prompt_resumo_basico
)

def carregar_alunos():
    with open('data/alunos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_resultado(aluno_nome, topico, conteudo, versao):
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        
    timestamp = int(time.time())
    # O nome do arquivo agora salva qual versão do prompt foi usada para manter o histórico
    nome_arquivo = f"outputs/resultado_{versao}_{aluno_nome}_{timestamp}.json"
    
    dados_salvar = {
        "aluno": aluno_nome,
        "topico": topico,
        "versao_prompt": versao,
        "conteudo_gerado": conteudo
    }
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_salvar, f, indent=4, ensure_ascii=False)
    
    print(f"\n Arquivo salvo com sucesso em: {nome_arquivo}")

def executar_geracao():
    try:
        alunos = carregar_alunos()
    except FileNotFoundError:
        print(" Erro: Arquivo data/alunos.json não encontrado.")
        return
    
    print("="*50)
    print(" GERADOR DE CONTEÚDO EDUCATIVO COM IA")
    print("="*50)
    
    print("\nSelecione um perfil de aluno:")
    for i, aluno in enumerate(alunos):
        print(f"[{i+1}] {aluno['nome']} ({aluno['idade']} anos - {aluno['nivel_conhecimento']})")
    
    escolha = int(input("\nDigite o número do aluno: ")) - 1
    aluno_selecionado = alunos[escolha]
    
    topico = input("Digite o tópico que deseja ensinar: ")

    print("\nQual motor de prompt você deseja usar?")
    print("[1] OTIMIZADO (Usa Persona, Contexto do Aluno e Chain-of-Thought)")
    print("[2] BÁSICO (Prompt genérico, sem contexto - Modo Comparação)")
    escolha_versao = input("Escolha a versão (1 ou 2): ")

    print(f"\n  Gerando material sobre '{topico}'...")
    
    if escolha_versao == '1':
        versao = "otimizado"
        print(" 1/4 Gerando explicação conceitual...")
        explicacao = gerar_conteudo_gemini(prompt_explicacao_conceitual(aluno_selecionado, topico))
        print(" 2/4 Gerando exemplos práticos...")
        exemplos = gerar_conteudo_gemini(prompt_exemplos_praticos(aluno_selecionado, topico))
        print(" 3/4 Gerando perguntas de reflexão...")
        perguntas = gerar_conteudo_gemini(prompt_perguntas_reflexao(aluno_selecionado, topico))
        print(" 4/4 Gerando resumo visual...")
        resumo = gerar_conteudo_gemini(prompt_resumo_visual(aluno_selecionado, topico))
    else:
        versao = "basico"
        print(" 1/4 Gerando explicação (Básico)...")
        explicacao = gerar_conteudo_gemini(prompt_explicacao_basico(topico))
        print(" 2/4 Gerando exemplos (Básico)...")
        exemplos = gerar_conteudo_gemini(prompt_exemplos_basico(topico))
        print(" 3/4 Gerando perguntas (Básico)...")
        perguntas = gerar_conteudo_gemini(prompt_perguntas_basico(topico))
        print(" 4/4 Gerando resumo (Básico)...")
        resumo = gerar_conteudo_gemini(prompt_resumo_basico(topico))
    
    resultado_final = {
        "1_explicacao": explicacao,
        "2_exemplos": exemplos,
        "3_perguntas": perguntas,
        "4_resumo": resumo
    }
    
    salvar_resultado(aluno_selecionado['nome'], topico, resultado_final, versao)
    print(" Geração concluída!")

if __name__ == "__main__":
    executar_geracao()
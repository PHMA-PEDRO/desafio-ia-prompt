# prompts/builder.py

def criar_contexto_aluno(aluno):
    """Cria a string base de contexto usando os dados do JSON do aluno."""
    return f"Seu aluno se chama {aluno['nome']}, tem {aluno['idade']} anos. O nível de conhecimento dele é {aluno['nivel_conhecimento']} e ele tem um estilo de aprendizado {aluno['estilo_aprendizado']}."

def prompt_explicacao_conceitual(aluno, topico):
    """1. Explicação conceitual usando Chain-of-Thought."""
    contexto = criar_contexto_aluno(aluno)
    return f"""Você é um professor experiente em Pedagogia.
{contexto}
Sua tarefa é explicar o tópico '{topico}'.

Pense passo a passo (chain-of-thought) sobre como adaptar a linguagem e o nível de profundidade antes de dar a resposta final.

Responda ESTRITAMENTE neste formato JSON:
{{
    "raciocinio_didatico": "seu pensamento passo a passo sobre como ensinar este aluno",
    "explicacao_final": "o texto da explicação adaptada"
}}"""

def prompt_exemplos_praticos(aluno, topico):
    """2. Exemplos práticos contextualizados."""
    contexto = criar_contexto_aluno(aluno)
    return f"""Você é um tutor criativo.
{contexto}
Crie 2 exemplos práticos sobre o tópico '{topico}' que façam sentido para a realidade e idade de alguém com o perfil deste aluno.

Responda ESTRITAMENTE neste formato JSON:
{{
    "exemplo_1": "texto do primeiro exemplo",
    "exemplo_2": "texto do segundo exemplo"
}}"""

def prompt_perguntas_reflexao(aluno, topico):
    """3. Perguntas de reflexão para pensamento crítico."""
    contexto = criar_contexto_aluno(aluno)
    return f"""Você é um mentor acadêmico.
{contexto}
Crie 3 perguntas de reflexão sobre '{topico}' para estimular o pensamento crítico, no nível exato de compreensão do aluno.

Responda ESTRITAMENTE neste formato JSON:
{{
    "perguntas": ["pergunta 1", "pergunta 2", "pergunta 3"]
}}"""

def prompt_resumo_visual(aluno, topico):
    """4. Resumo em formato visual (ASCII ou descrição)."""
    contexto = criar_contexto_aluno(aluno)
    return f"""Você é um especialista em design instrucional.
{contexto}
Crie um esquema visual em arte ASCII (como um fluxograma simples ou mapa mental de texto) que resuma o tópico '{topico}'.

Responda ESTRITAMENTE neste formato JSON:
{{
    "diagrama_ascii": "seu desenho em ascii aqui"
}}"""

def prompt_explicacao_basico(topico):
    """Prompt básico (ruim) para fins de comparação."""
    return f"""Explique o tópico '{topico}'.
Responda ESTRITAMENTE neste formato JSON:
{{ "explicacao": "sua explicação aqui" }}"""

def prompt_exemplos_basico(topico):
    return f"""Dê 2 exemplos práticos sobre '{topico}'.
Responda ESTRITAMENTE neste formato JSON:
{{ "exemplo_1": "texto do exemplo 1", "exemplo_2": "texto do exemplo 2" }}"""

def prompt_perguntas_basico(topico):
    return f"""Crie 3 perguntas sobre '{topico}'.
Responda ESTRITAMENTE neste formato JSON:
{{ "perguntas": ["pergunta 1", "pergunta 2", "pergunta 3"] }}"""

def prompt_resumo_basico(topico):
    return f"""Faça um resumo sobre '{topico}'.
Responda ESTRITAMENTE neste formato JSON:
{{ "resumo": "texto do resumo" }}"""
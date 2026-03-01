# 🧠 Gerador de Conteúdo Educativo com IA

[cite_start]Este projeto é uma aplicação CLI desenvolvida em Python para o Desafio Técnico de Estágio em IA e Engenharia de Prompt[cite: 1, 19, 26]. [cite_start]O sistema utiliza a API do Google Gemini (gemini-2.5-flash) para gerar materiais educativos altamente personalizados com base no perfil do aluno e no tópico desejado[cite: 4, 8, 20].

## 🎯 Funcionalidades Implementadas

[cite_start]O motor de prompt gera 4 tipos de conteúdos otimizados[cite: 9]:
1. [cite_start]**Explicação Conceitual:** Utiliza a técnica de *Chain-of-Thought* para adaptar a linguagem ao aluno[cite: 11, 41].
2. [cite_start]**Exemplos Práticos:** Contextualizados para a idade e realidade do perfil selecionado[cite: 12].
3. [cite_start]**Perguntas de Reflexão:** Focadas em estimular o pensamento crítico[cite: 13].
4. [cite_start]**Resumo Visual:** Geração de diagramas ou mapas mentais em formato texto/ASCII[cite: 15].

**Diferenciais Técnicos:**
* [cite_start]⚙️ **Sistema de Cache Local:** Intercepta prompts já processados (via hash MD5) para evitar chamadas redundantes à API, economizando recursos e tempo de resposta[cite: 29, 71].
* [cite_start]🔒 **Saída Estruturada Forte:** Uso do `responseMimeType: "application/json"` nativo do Gemini para garantir que a saída da IA não quebre a aplicação com formatações inesperadas[cite: 16, 42].
* [cite_start]🗂️ **Persistência de Dados:** Todos os materiais gerados são salvos automaticamente na pasta `/outputs` em formato JSON estruturado com timestamp[cite: 16, 48].

## 📁 Estrutura do Projeto

```text
desafio-ia-prompt/
├── data/
│   ├── alunos.json                # Perfis dos alunos (mock)
│   └── cache.json                 # Armazenamento do cache local
├── outputs/                       # Resultados gerados salvos com timestamp
├── prompts/
│   └── builder.py                 # Funções de construção dinâmica dos prompts
├── services/
│   ├── api_client.py              # Integração com a API do Google Gemini
│   └── cache.py                   # Lógica de validação de cache MD5
├── samples/                       # Exemplos de outputs JSON gerados para avaliação
├── .env                           # Chaves de API locais
├── .gitignore                     # Arquivos ignorados pelo versionamento
├── main.py                        # Ponto de entrada e interface CLI
├── PROMPT_ENGINEERING_NOTES.md    # Documentação das estratégias de IA utilizadas
├── README.md                      # Documentação principal
└── requirements.txt               # Dependências do Python

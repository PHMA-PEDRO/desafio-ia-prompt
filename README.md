# 🧠 Gerador de Conteúdo Educativo com IA

Este projeto é uma aplicação CLI desenvolvida em Python para o Desafio Técnico de Estágio em IA e Engenharia de Prompt. O sistema utiliza a API do Google Gemini (gemini-2.5-flash) para gerar materiais educativos altamente personalizados com base no perfil do aluno e no tópico desejado.

## 🎯 Funcionalidades Implementadas

O motor de prompt gera 4 tipos de conteúdos otimizados:
1. **Explicação Conceitual:** Utiliza a técnica de *Chain-of-Thought* para adaptar a linguagem ao aluno.
2. **Exemplos Práticos:** Contextualizados para a idade e realidade do perfil selecionado.
3. **Perguntas de Reflexão:** Focadas em estimular o pensamento crítico.
4. **Resumo Visual:** Geração de diagramas ou mapas mentais em formato texto/ASCII.

**Diferenciais Técnicos:**
* ⚙️ **Sistema de Cache Local:** Intercepta prompts já processados (via hash MD5) para evitar chamadas redundantes à API, economizando recursos e tempo de resposta.
* 🔒 **Saída Estruturada Forte:** Uso do `responseMimeType: "application/json"` nativo do Gemini para garantir que a saída da IA não quebre a aplicação com formatações inesperadas.
* 🗂️ **Persistência de Dados:** Todos os materiais gerados são salvos automaticamente na pasta `/outputs` em formato JSON estruturado com timestamp.

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

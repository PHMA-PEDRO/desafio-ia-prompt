# Notas de Engenharia de Prompt

[cite_start]Este documento detalha as estratégias e técnicas de Engenharia de Prompt aplicadas no desenvolvimento do Motor de Geração de Conteúdo Educativo[cite: 35, 90]. [cite_start]O objetivo principal foi garantir que a IA (Google Gemini 2.5 Flash) gerasse respostas altamente personalizadas, didáticas e estritamente formatadas[cite: 3].

## 1. Técnicas Aplicadas

[cite_start]A arquitetura dos prompts foi desenhada combinando quatro técnicas principais exigidas nos requisitos do sistema[cite: 38]:

### A. Persona Prompting
[cite_start]Em cada uma das quatro funções geradoras, a IA assume um papel específico e coerente com a tarefa[cite: 39]:
* [cite_start]**Explicação Conceitual:** "Você é um professor experiente em Pedagogia." [cite: 39]
* **Exemplos Práticos:** "Você é um tutor criativo."
* **Perguntas de Reflexão:** "Você é um mentor acadêmico."
* **Resumo Visual:** "Você é um especialista em design instrucional."
Isso calibra o vocabulário e o tom da resposta antes mesmo da geração do conteúdo começar.

### B. Context Setting (Injeção de Contexto)
[cite_start]Os dados estruturados do arquivo `alunos.json` são dinamicamente injetados no início de cada prompt[cite: 31, 32, 40]. [cite_start]A IA recebe o nome, idade, nível de conhecimento e estilo de aprendizado do aluno [cite: 33, 34][cite_start], permitindo que as metáforas e a complexidade do texto sejam adaptadas sob medida[cite: 4, 8].

### C. Chain-of-Thought (Pensamento Passo a Passo)
[cite_start]Aplicado com maior ênfase na geração da **Explicação Conceitual**[cite: 11, 41]. 
Para evitar que a IA entregasse uma resposta genérica, o prompt exige que o modelo detalhe seu raciocínio didático em um campo JSON específico (`raciocinio_didatico`) antes de formular a `explicacao_final`. [cite_start]Isso força a IA a planejar a aula, analisar o perfil do aluno e, só então, escrever o texto[cite: 5, 41].

### D. Output Formatting (Formatação de Saída Estruturada)
[cite_start]Para garantir a integração perfeita com a aplicação e a persistência de dados [cite: 16, 48][cite_start], a técnica de formatação de saída foi aplicada de forma rigorosa[cite: 42]. 
* O uso do parâmetro `responseMimeType: "application/json"` na requisição da API garante o formato.
* O prompt define explicitamente a estrutura de chaves esperada (ex: `{"exemplo_1": "...", "exemplo_2": "..."}`).

---

## 2. Diferenças Estruturais dos 4 Prompts

O sistema não utiliza um prompt gigante para gerar tudo. [cite_start]O design foi dividido em quatro prompts menores e especializados [cite: 9, 44, 45][cite_start], o que diminui a alucinação da IA e aumenta a qualidade do retorno final[cite: 64]:

1. [cite_start]**Explicação:** Foca no sequenciamento lógico (Chain-of-Thought) e adaptação de linguagem[cite: 11].
2. [cite_start]**Exemplos Práticos:** Foca em conectar o tópico com o cotidiano da faixa etária do aluno[cite: 12].
3. [cite_start]**Reflexão:** Foca em questionamentos abertos que estimulam o pensamento crítico, em vez de respostas de "sim/não"[cite: 13].
4. [cite_start]**Resumo Visual:** Foca na abstração do conhecimento através de representações visuais descritivas ou arte ASCII, ideal para alunos com estilo de aprendizado visual[cite: 15, 34].

## 3. Análise Comparativa de Resultados (A/B Testing)

[cite_start]Para validar a eficácia do motor de prompts estruturado, foi desenvolvido um modo de "Prompt Básico" (sem persona, sem contexto do aluno e sem chain-of-thought)[cite: 49]. O teste foi realizado com o tópico "Derivada" para a aluna "Mariana" (22 anos, nível intermediário, estilo leitura-escrita).

Abaixo estão as principais diferenças observadas que comprovam o valor das técnicas aplicadas:

### A. Qualidade da Explicação Conceitual
* **Prompt Básico:** Retornou uma definição engessada e enciclopédica de livro de cálculo: *"Matematicamente, a derivada é definida como o limite da razão incremental quando o incremento da variável independente tende a zero."* Não houve adaptação de linguagem.
* **Prompt Otimizado:** Graças ao *Chain-of-Thought*, a IA planejou a aula antes de escrever. Ela iniciou saudando a aluna, explicou o conceito usando a analogia do velocímetro de um carro (taxa de variação instantânea) e detalhou o passo a passo das regras de derivação (como a regra da potência), respeitando o estilo "leitura-escrita" exigido.

### B. Relevância dos Exemplos Práticos
* **Prompt Básico:** Trouxe exemplos genéricos e abstratos com variáveis soltas, como a clássica função de posição no tempo `s(t)` e o custo marginal na economia `C(q)`.
* **Prompt Otimizado:** Contextualizou a matemática para o cotidiano de uma jovem de 22 anos. O primeiro exemplo modelou a taxa de crescimento de assinantes de um serviço de streaming de música, e o segundo otimizou a taxa de absorção de conhecimento em horas de estudo.

### C. Perguntas de Reflexão
* **Prompt Básico:** Gerou perguntas de memorização típicas de prova: *"Qual é a definição geométrica...?"* ou *"Quais são as principais regras...?"*.
* **Prompt Otimizado:** A persona do "mentor acadêmico" gerou questionamentos focados em raciocínio crítico abstrato, perguntando como o sinal da derivada (positivo ou negativo) informa o comportamento do cenário real.

### D. Engajamento Visual
* **Prompt Básico:** Ignorou o pedido implícito de estruturação visual e retornou um parágrafo de texto corrido como "resumo".
* **Prompt Otimizado:** A persona do "designer instrucional" desenhou com sucesso um mapa mental estruturado em arte ASCII no terminal, hierarquizando os conceitos, símbolos e regras básicas, entregando um valor visual massivo.

**Conclusão da Análise:** A ausência de técnicas de engenharia de prompt resulta em um conteúdo genérico que ignora as necessidades do usuário final. A injeção de contexto aliada ao *Persona Prompting* e *Chain-of-Thought* transformou uma simples chamada de API em uma experiência educacional adaptativa de alto valor.
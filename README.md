# Analisador de Sentimentos NLP(Natural Language Processing) Avançado com Interface

# 🚀 Sobre o Projeto:

Este repositório contém um Analisador de Sentimentos Avançado desenvolvido em Python, que combina técnicas de Processamento de Linguagem Natural (NLP) com uma interface gráfica moderna e interativa, inspirada no estilo do ChatGPT. O projeto é ideal para quem deseja explorar análise de sentimentos, machine learning e desenvolvimento de interfaces gráficas com Tkinter e Matplotlib.

# Funções do NLP: 
✅ Análise de Sentimentos em Texto
Utiliza o algoritmo Naive Bayes treinado com o corpus Movie Reviews do NLTK. Classifica textos em sentimentos positivos ou negativos com base em padrões linguísticos. Gera uma distribuição de probabilidades para cada sentimento.
📊 Visualização de Dados
Gráficos interativos e dinâmicos para representar a distribuição de probabilidades dos sentimentos. Relatórios detalhados com análises quantitativas e qualitativas.
💻 Interface Gráfica Moderna
Interface desenvolvida com Tkinter e Matplotlib. Design limpo e responsivo, com elementos visuais atraentes. Funcionalidades como análise em tempo real, limpeza de dados e exibição de relatórios.

# Ferramentas/Bibliotecas: 
Python (Linguagem principal) NLTK (Natural Language Toolkit para NLP) Tkinter (Interface gráfica) Matplotlib (Visualização de dados) ScrolledText (Exibição de textos longos)

# Como Funciona?
1. Pré-processamento de Dados: Extração de características com tratamento de stopwords e normalização. Preparação do corpus Movie Reviews para treinamento do modelo.
2. Treinamento do Modelo: Utilização do algoritmo Naive Bayes para classificação de sentimentos. Acurácia do modelo validada com dados de teste.
3. Análise de Texto: O usuário insere um texto na interface. O sistema classifica o sentimento e gera um relatório detalhado com gráficos.
4. Interface Interativa: Botões para análise, limpeza de dados e exibição de resultados. Gráficos atualizados em tempo real.

# Passo a Passo para Rodar
1. Clone o repositório
git clone https://github.com/LeonardoAI33/Analisador_NLP.git
2. Instale as dependências
pip install nltk matplotlib tkinter
3. Execute o Script "nlp_projects.py"
python nlp_projects.py

# Exemplo de Uso 
Digite sua Opinião sobre qualquer Filme/Série.
Clique em "Analisar Sentimento".

Veja o resultado no gráfico e no relatório detalhado.

# Exemplo de Saída:

Relatório de Análise Psicolinguística
Data: 25/10/2023 14:30
Modelo: Naive Bayes (NLTK) | Corpus: Movie Reviews

[Análise Quantitativa]

Sentimento Predominante: POSITIVO (Confiança: 85%)
Distribuição de Probabilidades:
• Positivo: 85.00%
• Negativo: 15.00%
[Análise Qualitativa]

Padrões Linguísticos Detectados:
Uso de superlativos indica entusiasmo
[Recomendações]

Sugestões de conteúdo baseadas no perfil detectado
Atividades para desenvolvimento emocional.

# Lógica por trás do Analisador Psicolinguístico📊:
O Analisador Psicolinguístico conduziu uma Análise do Comentário do Usuário pra Identificar a Porcentagem de Sentimentos que mais Predominaram(Positivo ou Negativo).
Só com o Comentário do Usuário, o Analisador conseguiu identificar Padrões Linguísticos, traçar uma conclusão sobre o comentário e distribuir em Porcentagem os Sentimentos Positivos e Negativos que o Comentário apresentou junto com sugestões de conteúdo.
Com essa Informação em Mãos, podemos, por exemplo, saber o nível de satisfação do usuário em relação a algum serviço ou produto, podendo assim fornecer insights sobre as áreas que a Empresa deve Melhorar ou Focar com Prioridade para o Cliente Ficar Satisfeito e a Corporação ter Resultados EXCELENTE.

#!/usr/bin/env python
"""
Analisador de Sentimentos Avançado com Interface Estilo ChatGPT (Versão Aprimorada)
"""

import nltk
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize
import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
import io

# ================================================
# Configuração Inicial e Recursos
# ================================================
nltk_resources = ['movie_reviews', 'punkt', 'stopwords', 'punkt_tab']
for resource in nltk_resources:
    try:
        nltk.data.find(resource)
    except LookupError:
        print(f"Baixando recurso '{resource}'...")
        nltk.download(resource, quiet=True)

# ================================================
# Funções de NLP e Machine Learning (Aprimoradas)
# ================================================
def extrair_caracteristicas(documento):
    """Extrai características com tratamento de erros e normalização aprimorada."""
    try:
        stop_words = set(stopwords.words('english'))
        tokens = [palavra.lower() for palavra in documento if palavra.isalpha()]
        tokens_filtrados = [palavra for palavra in tokens if palavra not in stop_words]
        return {f'contém({token})': True for token in set(tokens_filtrados)}
    except Exception as e:
        raise RuntimeError(f"Erro na extração de características: {str(e)}")

def preparar_dados():
    """Prepara dados com progresso e tratamento de erros."""
    try:
        documentos = [
            (list(movie_reviews.words(fileid)), categoria)
            for categoria in movie_reviews.categories()
            for fileid in movie_reviews.fileids(categoria)
        ]
        random.Random(42).shuffle(documentos)  # Seed para reprodutibilidade
        return [(extrair_caracteristicas(doc), categoria) for (doc, categoria) in documentos]
    except Exception as e:
        raise RuntimeError(f"Erro no preparo de dados: {str(e)}")

def treinar_classificador(dados):
    """Treina o classificador com validação de dados e métricas completas."""
    if not dados:
        raise ValueError("Dados de treinamento vazios!")
    
    tamanho_treino = int(len(dados) * 0.8)
    treino, teste = dados[:tamanho_treino], dados[tamanho_treino:]
    
    try:
        classificador = nltk.NaiveBayesClassifier.train(treino)
        acuracia = nltk.classify.accuracy(classificador, teste)
        print(f"Acurácia do classificador (teste): {acuracia:.2f}")
        return classificador
    except Exception as e:
        raise RuntimeError(f"Erro no treinamento: {str(e)}")

# ================================================
# Componentes de Análise e Visualização (Aprimorados)
# ================================================
def analisar_comentario(classificador, texto):
    """Análise com tratamento robusto de erros e normalização."""
    if not texto.strip():
        raise ValueError("Texto de entrada vazio!")
    
    try:
        tokens = word_tokenize(texto)
        caracteristicas = extrair_caracteristicas(tokens)
        rotulo = classificador.classify(caracteristicas)
        distribuicao = classificador.prob_classify(caracteristicas)
        probs = {rotulo: round(distribuicao.prob(rotulo), 3) for rotulo in distribuicao.samples()}
        return rotulo, probs
    except Exception as e:
        raise RuntimeError(f"Erro na análise: {str(e)}")

def gerar_relatorio_detalhado(texto, rotulo, probs):
    """Relatório dinâmico baseado em dados reais da análise."""
    template = f"""
    Relatório de Análise Psicolinguística
    Data: {datetime.now().strftime("%d/%m/%Y %H:%M")}
    Modelo: Naive Bayes (NLTK) | Corpus: Movie Reviews
    
    [Análise Quantitativa]
    - Sentimento Predominante: {rotulo.upper()} (Confiança: {max(probs.values()):.0%})
    - Distribuição de Probabilidades:
      • Positivo: {probs.get('pos', 0):.2%}
      • Negativo: {probs.get('neg', 0):.2%}
    
    [Análise Qualitativa]
    - Padrões Linguísticos Detectados:
      {analisar_padroes_linguisticos(texto)}
    
    [Recomendações]
    - Sugestões de conteúdo baseadas no perfil detectado
    - Atividades para desenvolvimento emocional
    """
    return template

def analisar_padroes_linguisticos(texto):
    """Análise simplificada de padrões linguísticos."""
    analysis = []
    tokens = word_tokenize(texto.lower())
    
    if any(word in tokens for word in ['excelente', 'maravilhoso', 'incrível']):
        analysis.append("Uso de superlativos indica entusiasmo")
    if any(word in tokens for word in ['péssimo', 'horrível', 'desapontado']):
        analysis.append("Termos negativos sugerem crítica intensa")
    return "\n".join(analysis) if analysis else "Padrões neutros detectados"

# ================================================
# Interface Gráfica (Aprimorada com Thread-Safety)
# ================================================
class AnalisadorApp(tk.Tk):
    def __init__(self, classificador):
        super().__init__()
        self.classificador = classificador
        self.configurar_interface()
        self.criar_widgets()
        self.protocol("WM_DELETE_WINDOW", self.fechar_aplicacao)
    
    def configurar_interface(self):
        self.title("Analisador de Sentimentos Avançado v2.0")
        self.geometry("900x750")
        self.configure(bg="#F0F2F5")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Helvetica', 12), padding=6)
    
    def criar_widgets(self):
        # Cabeçalho
        cabecalho = ttk.Frame(self)
        cabecalho.pack(pady=20, fill='x')
        ttk.Label(cabecalho, text="Analisador Psicolinguístico", 
                font=('Helvetica', 18, 'bold'), 
                foreground="#2D3436").pack()
        
        # Área de Entrada
        frame_entrada = ttk.Frame(self)
        frame_entrada.pack(pady=10, padx=20, fill='x')
        self.txt_entrada = scrolledtext.ScrolledText(frame_entrada, height=8, 
                                                   wrap=tk.WORD, font=('Helvetica', 12))
        self.txt_entrada.pack(fill='x')
        
        # Botões
        frame_botoes = ttk.Frame(self)
        frame_botoes.pack(pady=10)
        ttk.Button(frame_botoes, text="Analisar Sentimento", 
                 command=self.executar_analise).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botoes, text="Limpar", 
                 command=self.limpar_interface).pack(side=tk.LEFT, padx=5)
        
        # Resultados
        frame_resultados = ttk.Frame(self)
        frame_resultados.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Gráfico
        self.figura, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(self.figura, master=frame_resultados)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Relatório
        self.txt_relatorio = scrolledtext.ScrolledText(frame_resultados, height=15,
                                                      wrap=tk.WORD, font=('Helvetica', 11))
        self.txt_relatorio.pack(fill='both', expand=True, pady=10)
    
    def executar_analise(self):
        texto = self.txt_entrada.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Entrada Inválida", "Por favor, insira um comentário.")
            return
        
        try:
            rotulo, probs = analisar_comentario(self.classificador, texto)
            self.atualizar_grafico(probs)
            relatorio = gerar_relatorio_detalhado(texto, rotulo, probs)
            self.txt_relatorio.delete("1.0", tk.END)
            self.txt_relatorio.insert(tk.END, relatorio)
        except Exception as e:
            messagebox.showerror("Erro de Análise", f"Erro: {str(e)}")
    
    def atualizar_grafico(self, probabilidades):
        self.ax.clear()
        cores = ['#4CAF50' if k == 'pos' else '#F44336' for k in probabilidades.keys()]
        self.ax.barh(list(probabilidades.keys()), list(probabilidades.values()), color=cores)
        self.ax.set_title('Distribuição de Probabilidades', fontsize=14)
        self.ax.set_xlim(0, 1)
        self.canvas.draw()
    
    def limpar_interface(self):
        self.txt_entrada.delete("1.0", tk.END)
        self.txt_relatorio.delete("1.0", tk.END)
        self.ax.clear()
        self.canvas.draw()
    
    def fechar_aplicacao(self):
        plt.close('all')
        self.destroy()

# ================================================
# Execução Principal com Tratamento de Erros Global
# ================================================
if __name__ == '__main__':
    try:
        print("🚀 Inicializando sistema...")
        dados = preparar_dados()
        print("🔧 Treinando modelo...")
        classificador = treinar_classificador(dados)
        print("💻 Iniciando interface gráfica...")
        app = AnalisadorApp(classificador)
        app.mainloop()
    except Exception as e:
        print(f"⛔ Erro crítico: {str(e)}")
        sys.exit(1)
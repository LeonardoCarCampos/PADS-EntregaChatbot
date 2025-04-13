# ========== chatbot.py ==========

# 1. Bibliotecas padrão do Python para instalação e verificação de pacotes
import subprocess
import sys
import importlib.util
import platform
import os

# 2. Bibliotecas para manipulação e análise de dados
import pandas as pd
import numpy as np
import datetime

# 3. Modelo semântico para embeddings de linguagem
from sentence_transformers import SentenceTransformer, util

# 4. Biblioteca de NLP para análise de sentimentos
from textblob import TextBlob

# 5. Tokenização de frases
import nltk

# 6. Visualização de gráficos
import matplotlib.pyplot as plt


# 7. Instalação automática de pacotes, se necessário
pkgs = {
    'pandas': 'pandas',
    'numpy': 'numpy',
    'sentence_transformers': 'sentence-transformers',
    'textblob': 'textblob',
    'shiny': 'shiny',
    'matplotlib': 'matplotlib'
}
for name, pip_name in pkgs.items():
    if importlib.util.find_spec(name) is None:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pip_name])

# 8. Correção de certificados para MacOS
if platform.system() == "Darwin":
    cert_script = "/Applications/Python 3.11/Install Certificates.command"
    if os.path.exists(cert_script):
        subprocess.call(["sh", cert_script])


# 9. Verificação do recurso de tokenização do NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


# 10. Carregamento dos datasets da Olist
path = "C:/Users/Predator/Desktop/insper"
produtos = pd.read_csv(f"{path}/olist_products_dataset.csv")
itens_pedidos = pd.read_csv(f"{path}/olist_order_items_dataset.csv")
pedidos = pd.read_csv(f"{path}/olist_orders_dataset.csv")
avaliacoes = pd.read_csv(f"{path}/olist_order_reviews_dataset.csv")
categorias_trad = pd.read_csv(f"{path}/product_category_name_translation.csv")



# 11. Pré-processamento dos dados de produtos
produtos = produtos.merge(categorias_trad, on='product_category_name', how='left')
produtos.rename(columns={
    'product_id_lenght': 'product_id_length',
    'product_description_lenght': 'product_description_length'
}, inplace=True)
produtos['unique_name'] = produtos['product_category_name_english'].fillna('Unknown') + " #" + produtos.groupby('product_id').ngroup().astype(str)
product_name_dict = dict(zip(produtos['product_id'], produtos['unique_name']))


# 12. Junção das tabelas para formar o dataset consolidado
dados = itens_pedidos \
    .merge(produtos, on='product_id', how='left') \
    .merge(pedidos, on='order_id', how='left') \
    .merge(avaliacoes, on='order_id', how='left')

# 13. Filtra apenas os produtos da categoria de informática
dados_info = dados[dados['product_category_name_english'] == 'computers_accessories'].copy()
dados_info.dropna(subset=['product_id', 'review_comment_message'], inplace=True)



# 14. Criação do corpus textual a partir dos comentários
corpus = (
    dados_info['product_id'].astype(str) + ". " +
    dados_info['review_comment_message'].astype(str)
).tolist()


# 15. Geração dos embeddings com modelo de linguagem
modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
embeddings_corpus = modelo.encode(corpus, convert_to_tensor=True)


# 16. Conversão de datas e cálculo de sentimento dos comentários
dados_info['order_purchase_timestamp'] = pd.to_datetime(dados_info['order_purchase_timestamp'])
dados_info['sentimento'] = dados_info['review_comment_message'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# 17. Métricas gerais
nota_media = round(dados_info['review_score'].mean(), 2)
sentimento_medio = round(dados_info['sentimento'].mean(), 2)


# 18. Top 10 produtos mais vendidos
mais_vendidos = (
    dados_info.groupby('product_id')
    .size()
    .sort_values(ascending=False)
    .head(10)
)

nomes_top = produtos[produtos['product_id'].isin(mais_vendidos.index)][['product_id', 'unique_name']]
mais_vendidos_nomes = mais_vendidos.reset_index().merge(nomes_top, on='product_id', how='left')
mais_vendidos_nomes['nome_legivel'] = mais_vendidos_nomes['unique_name'].fillna("Produto Desconhecido")

top_vendas_formatado = ", ".join([
    f"{row['nome_legivel']} ({row[0]} vendas)" for _, row in mais_vendidos_nomes.iterrows()
])


# 19. Função para salvar log das interações
def log_interacao(mensagem, resposta, usuario="anonimo"):
    timestamp = datetime.datetime.now().isoformat()
    with open("log_chat.csv", "a", encoding="utf-8") as f:
        f.write(f"{timestamp};{usuario};{mensagem};{resposta}\n")


# 20. Função principal do chatbot
# Verifica se há intenção direta ou usa busca semântica nos comentários
def responder(mensagem: str, usuario_id=None):
    mensagem_lower = mensagem.lower()

    if any(p in mensagem_lower for p in ["produto mais vendido", "produtos mais vendidos", "top produtos vendidos"]):
        return {"type": "plot", "plot_id": "mais_vendidos"}

    elif any(p in mensagem_lower for p in ["evolução de vendas", "vendas por mês", "gráfico de vendas"]):
        return {"type": "plot", "plot_id": "vendas_mensais"}

    elif any(p in mensagem_lower for p in ["distribuição de notas", "notas dos clientes", "avaliação dos clientes"]):
        return {"type": "plot", "plot_id": "distribuicao_notas"}

    elif any(p in mensagem_lower for p in ["maiores preços", "produtos mais caros", "preços mais altos"]):
        return {"type": "plot", "plot_id": "precos_altos"}

    elif any(p in mensagem_lower for p in ["preço dos mais vendidos", "preço dos produtos mais vendidos"]):
        return {"type": "plot", "plot_id": "preco_mais_vendidos"}

    elif any(p in mensagem_lower for p in ["maior faturamento", "produtos mais faturaram", "mais geraram receita", "top faturamento"]):
        return {"type": "plot", "plot_id": "top_faturamento"}

    elif "nota média" in mensagem_lower:
        resposta = f"A nota média dos produtos da categoria informática é {nota_media}."
        log_interacao(mensagem, resposta, usuario=usuario_id)
        return {"type": "text", "content": resposta}

    elif any(p in mensagem_lower for p in ["sentimento", "clientes satisfeitos", "feedback dos clientes"]):
        resposta = f"A média de sentimento dos comentários é {sentimento_medio:.2f}, indicando uma percepção positiva geral."
        log_interacao(mensagem, resposta, usuario=usuario_id)
        return {"type": "text", "content": resposta}

    elif any(p in mensagem_lower for p in ["reclamação", "reclamam", "problemas relatados"]):
        resposta = "As principais reclamações envolvem atrasos na entrega e produtos com defeito, segundo os comentários analisados."
        log_interacao(mensagem, resposta, usuario=usuario_id)
        return {"type": "text", "content": resposta}

    # Fallback: análise semântica
    embedding_input = modelo.encode(mensagem, convert_to_tensor=True)
    resultados = util.semantic_search(embedding_input, embeddings_corpus, top_k=1)

    if not resultados or not resultados[0]:
        resposta = "Desculpe, não encontrei nenhuma informação relevante sobre isso nos comentários dos clientes."
    else:
        idx = resultados[0][0]['corpus_id']
        texto = corpus[idx]
        product_id = texto.split('.')[0]
        nome_legivel = product_name_dict.get(product_id, 'Produto Desconhecido')
        resposta = texto.replace(product_id, nome_legivel)

    log_interacao(mensagem, resposta, usuario=usuario_id)
    return {"type": "text", "content": resposta}


# 21. Funções auxiliares de visualização de gráficos
def plot_mais_vendidos():
    fig, ax = plt.subplots()

    # Definir cores: top 1 em laranja, os outros em azul
    cores = [ "#F7941D" if i == 0 else "#1E4D91" for i in range(len(mais_vendidos_nomes)) ]

    # Criar gráfico horizontal
    ax.barh(
        mais_vendidos_nomes['nome_legivel'],
        mais_vendidos_nomes[0],
        color=cores
    )

    # Títulos e rótulos
    ax.set_title("Top 10 Produtos Mais Vendidos", fontsize=14, fontweight='bold')
    ax.set_xlabel("Quantidade de Vendas")
    ax.set_ylabel("Produto")

    # Inverter eixo Y para mostrar o top 1 no topo
    ax.invert_yaxis()

    return fig

def plot_vendas_mensais():
    df = dados_info.copy()
    df['mes'] = df['order_purchase_timestamp'].dt.to_period('M')
    vendas_mensais = df.groupby('mes').size()

    fig, ax = plt.subplots()
    vendas_mensais.plot(kind='line', marker='o', ax=ax, color='#1E4D91')  # azul olist

    ax.set_title("📆 Evolução de Vendas Mensais", fontsize=14, weight='bold')
    ax.set_xlabel("Mês")
    ax.set_ylabel("Total de Vendas")
    fig.autofmt_xdate()

    # Destaque visual: preencher entre dez/2017 e mar/2018
    inicio = '2017-12'
    fim = '2018-03'
    destaque = vendas_mensais[inicio:fim]

    ax.fill_between(
        destaque.index.to_timestamp(),
        destaque.values,
        color='orange',
        alpha=0.3,
        label='Período em destaque'
    )

    # Texto com valor acumulado
    acumulado = destaque.sum()
    ax.annotate(
        f"{acumulado} vendas",
        xy=(destaque.index[-1].to_timestamp(), destaque.values[-1]),
        xytext=(40, 0),
        textcoords="offset points",
        fontsize=9,
        ha='left',
        va='center',
        bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.5),
        arrowprops=dict(arrowstyle="->", color='gray', lw=1)
    )

    ax.legend()
    plt.tight_layout()
    return fig



def plot_distribuicao_notas():
    fig, ax = plt.subplots()
    dados_info['review_score'].value_counts().sort_index().plot(kind='bar', ax=ax)
    ax.set_title("Distribuição das Notas dos Clientes")
    ax.set_xlabel("Nota")
    ax.set_ylabel("Frequência")
    return fig

def plot_precos_altos():
    top_precos = (
        dados_info[['product_id', 'price']]
        .groupby('product_id').max()
        .sort_values('price', ascending=False)
        .head(5)
        .reset_index()
    )

    top_precos['nome_legivel'] = top_precos['product_id'].map(product_name_dict).fillna('Produto Desconhecido')

    fig, ax = plt.subplots(figsize=(8, 5))  # aumenta o tamanho horizontal
    ax.bar(top_precos['nome_legivel'], top_precos['price'], color="#1E4D91")
    ax.set_title("Top 5 Produtos com Maiores Preços")
    ax.set_ylabel("Preço (R$)")
    ax.set_xlabel("Produtos")

    plt.xticks(rotation=45, ha='right')  # gira os nomes para melhor visualização
    fig.tight_layout()  # ajusta layout para evitar cortes

    return fig

def plot_preco_mais_vendidos():
    merge = mais_vendidos_nomes.merge(dados_info[['product_id', 'price']], on='product_id', how='left')
    avg_price = merge.groupby('nome_legivel')['price'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))  # aumenta a largura para caber melhor
    ax.bar(avg_price['nome_legivel'], avg_price['price'], color="#1E4D91")
    ax.set_title("Preço Médio dos Produtos Mais Vendidos")
    ax.set_ylabel("Preço Médio (R$)")
    ax.set_xlabel("Produtos")

    plt.xticks(rotation=45, ha='right')  # gira os rótulos no eixo X
    fig.tight_layout()  # evita cortes nos rótulos

    return fig

def plot_top_faturamento():
    import matplotlib.pyplot as plt

    # Agrupamento e cálculo do faturamento
    faturamento = dados_info.groupby('product_id').agg({
        'price': 'sum',
        'product_id': 'count'
    }).rename(columns={'product_id': 'vendas'})
    
    faturamento['faturamento'] = faturamento['price']
    
    # Top 5 produtos por faturamento
    top_fat = faturamento.sort_values('faturamento', ascending=False).head(10).reset_index()
    top_fat['nome_legivel'] = top_fat['product_id'].map(product_name_dict).fillna('Produto Desconhecido')

    # Ordenar para barras horizontais (do menor pro maior)
    top_fat = top_fat.sort_values(by='faturamento', ascending=True)

    # Paleta: azul da Olist e destaque em laranja
    cores = ['#1E4D91'] * len(top_fat)
    cores[-1] = '#F7941D'  # Top 1 em laranja

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_fat['nome_legivel'], top_fat['faturamento'], color=cores)

    # Rótulos nas barras
    for i, valor in enumerate(top_fat['faturamento']):
        ax.text(valor + 300, i, f'R$ {valor:,.0f}', va='center', fontsize=10, color='#333333')

    # Título e estilo
    ax.set_title("💰 Top 10 Produtos com Maior Faturamento", fontsize=15, fontweight='bold')
    ax.set_xlabel("Faturamento Total (R$)", fontsize=12)
    ax.set_ylabel("")
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='x', linestyle='--', alpha=0.3)
    fig.tight_layout()

    return fig

# PADS-EntregaChatbot
# 🤖 Chatbot Inteligente com Shiny e Dados de E-commerce

Este projeto traz um chatbot interativo desenvolvido em Python com interface via [Shiny for Python](https://shiny.posit.co/py/), conectado a um modelo de linguagem e dados reais da Olist. A solução é pensada para lojistas e empreendedores que desejam gerar **insights práticos** a partir de dados de vendas e avaliações de clientes.

---

## 📂 Estrutura do Projeto

| Arquivo                    | Descrição |
|---------------------------|-----------|
| `chatbot_produto_v0.py`   | Código principal do chatbot com análise de sentimento, embeddings semânticos e geração de gráficos |
| `shiny_bot.py`            | Interface web do usuário com Shiny |
| `log_chat.csv`            | Histórico das interações feitas com o bot |
| `requirements.txt`        | Lista de dependências do projeto (pip install) |

---

## ✅ Funcionalidades

- Respostas baseadas em semântica usando `SentenceTransformer`
- Capacidade de entender variações e erros de digitação nas perguntas
- Gráficos dinâmicos gerados com `matplotlib`
- Análise de sentimento de comentários com `TextBlob`
- Interface no navegador com Shiny
- Log automático das interações do usuário
- Resumo executivo com KPIs (nota média, sentimento, etc.)

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-olist.git
cd chatbot-olist

### 2. Instale os pacotes necessários:
pip install -r requirements.txt

### 3. Inicie a interface::
python shiny_bot.py
### 4. 💬 Exemplos de Perguntas
  Você pode fazer perguntas como:

  Quais os produtos mais vendidos?

  Mostre a evolução de vendas por mês

  Qual é a nota média?

  Me mostre os produtos com maiores preços

  Como os clientes estão avaliando os produtos?

  Quais são os principais problemas relatados?

  Produtos que mais geraram receita?

### 5. 📊 Gráficos Disponíveis:
  Top 10 produtos mais vendidos

  Evolução de vendas mensais

  Distribuição de notas dos clientes

  Produtos com maiores preços

  Preço médio dos mais vendidos

  Produtos com maior faturamento

### 6. 🧠 Como o Chatbot Entende as Perguntas?
  Combina regras por palavra-chave com busca semântica

  Usa SentenceTransformer para entender a intenção por similaridade de significado

  Consulta comentários reais de clientes e retorna respostas relevantes

  Avalia o sentimento do texto com TextBlob

### 7. 🔁 Histórico de Interações
  Todas as perguntas e respostas são armazenadas automaticamente no arquivo log_chat.csv, com:

  Timestamp

  ID do usuário

  Pergunta

  Resposta gerada

### 8. 🔧 Requisitos Técnicos
  Python 3.9 ou superior

  Bibliotecas utilizadas:

  pandas

  numpy

  sentence-transformers

  textblob

  matplotlib

  nltk

  shiny

### 9. 📌 Próximos Passos (versão futura)
  Possibilidade de o usuário importar seus próprios dados (CSV)

  Geração automática de relatório em PDF ou CSV

  Campo para avaliação (feedback) da resposta

  Resumo mensal de KPIs para tomada de decisão

  Integração com APIs externas

A versão atual com suporte a CSV já representa a versão 2.0 do produto.


👤 Autor
Desenvolvido pelo Grupo 4.
Projeto para o curso de Data Visualization - Insper, 2025

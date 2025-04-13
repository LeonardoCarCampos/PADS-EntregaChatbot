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

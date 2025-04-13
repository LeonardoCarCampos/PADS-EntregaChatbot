# PADS-EntregaChatbot
# 🤖 Chatbot Inteligente com Shiny e Dados de E-commerce

Este projeto traz um chatbot interativo desenvolvido em Python com interface via [Shiny for Python](https://shiny.posit.co/py/), conectado a um modelo de linguagem e dados reais da Olist. A solução [...]

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

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/chatbot-olist.git
cd chatbot-olist
```

### 2. Instale os Pacotes Necessários
```bash
pip install -r requirements.txt
```
### 3. Inicie a interface::
```bash
python shiny_bot.py
```
### 4. 💬 Exemplos de Perguntas
```bash
  1. Você pode fazer perguntas como:

  2. Quais os produtos mais vendidos?

  3. Mostre a evolução de vendas por mês

  4. Qual é a nota média?

  5. Me mostre os produtos com maiores preços

  6. Como os clientes estão avaliando os produtos?

  7. Quais são os principais problemas relatados?

  8. Produtos que mais geraram receita?
```

### 5. 📊 Gráficos Disponíveis:
```bash
  1. Top 10 produtos mais vendidos

  2. Evolução de vendas mensais

  3. Distribuição de notas dos clientes

  4. Produtos com maiores preços

  5. Preço médio dos mais vendidos

  6. Produtos com maior faturamento
```

### 6. 🧠 Como o Chatbot Entende as Perguntas?
```bash
  1. Combina regras por palavra-chave com busca semântica

  2. Usa SentenceTransformer para entender a intenção por similaridade de significado

  3. Consulta comentários reais de clientes e retorna respostas relevantes

  4. Avalia o sentimento do texto com TextBlob
```

### 7. 🔁 Histórico de Interações
```bash
  Todas as perguntas e respostas são armazenadas automaticamente no arquivo log_chat.csv, com:

  - Timestamp

  - ID do usuário

  - Pergunta

  - Resposta gerada
```

### 8. 🔧 Requisitos Técnicos
```bash
  Python 3.9 ou superior

  Bibliotecas utilizadas:

  - pandas

  - numpy

  - sentence-transformers

  - textblob

  - matplotlib

  - nltk

  - shiny
```

### 9. 📌 Próximos Passos (versão futura)
```bash
  1. Possibilidade de o usuário importar seus próprios dados (CSV)

  2. Geração automática de relatório em PDF ou CSV

  3. Campo para avaliação (feedback) da resposta

  4. Resumo mensal de KPIs para tomada de decisão

  5. Integração com APIs externas

A versão atual com suporte a CSV já representa a versão 2.0 do produto.
```

###👤 Autor
```bash
  Desenvolvido pelo Grupo 4.
  Projeto para o curso de Data Visualization - Insper, 2025

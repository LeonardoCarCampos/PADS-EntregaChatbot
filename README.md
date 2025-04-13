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
git clone https://github.com/LeonardoCarCampos/PADS-EntregaChatbot.git
cd PADS-EntregaChatbot
```

### 2. Instale os Pacotes Necessários
Certifique-se de que você tenha o Python 3.9 ou superior instalado. Em seguida, instale as bibliotecas necessárias executando os seguintes comandos:
```bash
pip install pandas numpy datetime sentence-transformers textblob nltk matplotlib

```bash
pip install pandas numpy datetime sentence-transformers textblob nltk matplotlib
```
#### 2.a Instale as bases de dados da olist pelo Kaggle:
```bash
     1. Acesse o link do dataset oficial: Olist Brazilian E-Commerce (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
     2. Faça o download de todos os arquivos .csv disponíveis.
     3. No arquivo chatbot_produto_v0.py, localize a seção "10. Carregamento dos datasets da Olist" e edite a variável path, inserindo o diretório onde os arquivos .csv foram salvos no seu computador.
```
### 3. Inicie a interface:
```bash
python shiny_bot.py
```
#### 3.a 💬 Exemplos de Perguntas
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

### 4. 📊 Gráficos Disponíveis:
```bash
  1. Top 10 produtos mais vendidos

  2. Evolução de vendas mensais

  3. Distribuição de notas dos clientes

  4. Produtos com maiores preços

  5. Preço médio dos mais vendidos

  6. Produtos com maior faturamento
```

### 5. 🧠 Como o Chatbot Entende as Perguntas?
```bash
  1. Combina regras por palavra-chave com busca semântica

  2. Usa SentenceTransformer para entender a intenção por similaridade de significado

  3. Consulta comentários reais de clientes e retorna respostas relevantes

  4. Avalia o sentimento do texto com TextBlob
```

### 6. 🔁 Histórico de Interações
```bash
  Todas as perguntas e respostas são armazenadas automaticamente no arquivo log_chat.csv, com:

  - Timestamp

  - ID do usuário

  - Pergunta

  - Resposta gerada
```

### 7. 🔧 Requisitos Técnicos
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

### 8. 📌 Próximos Passos (versão futura)
```bash
  1. Possibilidade de o usuário importar seus próprios dados (CSV)

  2. Geração automática de relatório em PDF ou CSV

  3. Campo para avaliação (feedback) da resposta

  4. Resumo mensal de KPIs para tomada de decisão

  5. Integração com APIs externas

A versão atual com suporte a CSV já representa a versão 2.0 do produto.
```

### 9.👤 Autor
```bash
  Desenvolvido pelo Grupo 4.
  Projeto para o curso de Data Visualization - Insper, 2025

### 10.📌 Notas Técnicas Complementares

### 📋 Lista de Backlog (Entregas planejadas e realizadas)
- [x] Criar chatbot com base em dados reais da Olist
- [x] Implementar embeddings semânticos com SentenceTransformer
- [x] Adicionar análise de sentimentos com TextBlob
- [x] Desenvolver interface web com Shiny for Python
- [x] Criar gráficos dinâmicos baseados em perguntas do usuário
- [x] Registrar interações em log (log_chat.csv)
- [x] Permitir execução local com instruções detalhadas
- [x] Incluir resumo executivo com KPIs
- [ ] Implementar exportação para PDF ou CSV
- [ ] Adicionar campo de feedback do usuário
- [ ] Gerar relatórios mensais automáticos
- [ ] Integração futura com APIs externas

### ⚙️ Metodologia Aplicada
Adotamos a metodologia **Kanban**, organizando nossas tarefas em um quadro com as colunas:
- **A Fazer**
- **Em Andamento**
- **Concluído**

Essa abordagem nos permitiu visualizar claramente o progresso de cada funcionalidade e manter entregas contínuas ao longo do projeto.

### 👥 Perfil dos Participantes
- **Helio** – Computação/tecnologia e Matemátca/Etatística - Desenvolvimento da interface em Shiny e integração com o frontend. Preparação da apresentação.
- **Leonardo** – Computação/tecnologia e Matemátca/Etatística - Programação principal do chatbot, integração com modelos e análise de sentimento. Suporte na versão 2.0 da interface Shiny. Documentação, README. Preparação da apresentação.
- **Nathan** – Computação/tecnologia e Matemátca/Etatística - Preparação da apresentação. Programação principal do chatbot.  
- **João** – Área de especialidade sob estudo

### 🔗 Link para o Projeto
[https://github.com/LeonardoCarCampos/PADS-EntregaChatbot](https://github.com/LeonardoCarCampos/PADS-EntregaChatbot)


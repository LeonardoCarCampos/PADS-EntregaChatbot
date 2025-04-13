# ========== shiny_bot.py ==========

from shiny import App, ui, reactive, render
from chatbot_produto_v0 import (
    responder,
    plot_mais_vendidos,
    plot_vendas_mensais,
    plot_distribuicao_notas,
    plot_precos_altos,
    plot_preco_mais_vendidos,
    plot_top_faturamento,
    dados_info  # necessário para os resumos!
)
import tempfile
import base64
from matplotlib.figure import Figure
import pandas as pd  # você usa no df_csv e download

# ==============================
# UI
# ==============================
app_ui = ui.page_fluid(
    ui.h2("Chat Inteligente - Insights para seu Negócio"),

    ui.input_file("upload_dados", "📁 Suba seus dados (CSV)", accept=[".csv"]),
    ui.download_button("baixar_relatorio", "📥 Baixar Relatório CSV"),

    ui.div(
        ui.h4("📊 Resumo do Mês"),
        ui.output_text("total_vendas"),
        ui.output_text("nota_media"),
        style="background-color: #ffffff; padding: 10px; border-radius: 8px; margin-bottom: 15px;"
    ),

    ui.input_text("mensagem", "Digite sua pergunta:", placeholder="Ex: Quais os produtos mais vendidos?"),
    ui.input_action_button("enviar", "Enviar", class_="btn-primary"),
    ui.input_slider("feedback", "Essa resposta foi útil?", min=1, max=5, value=3),

    ui.hr(),
    ui.h4("Histórico da Conversa:"),
    ui.output_ui("resposta"),

    ui.tags.style("""
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .btn-primary {
            background-color: #1E4D91;
            border-color: #1E4D91;
        }
        h2 {
            color: #1E4D91;
        }
    """)
)

# ==============================
# Função para converter figura
# ==============================
def fig_to_base64(fig: Figure) -> str:
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
        fig.savefig(tmpfile.name, format="png", bbox_inches="tight")
        with open(tmpfile.name, "rb") as f:
            img_data = f.read()
    return base64.b64encode(img_data).decode("utf-8")

# ==============================
# Server
# ==============================
def server(input, output, session):
    historico = reactive.Value([])

    @reactive.Calc
    def df_csv():
        arquivo = input.upload_dados()
        if not arquivo:
            return None
        df = pd.read_csv(arquivo[0]["datapath"])
        return df

    @render.download(filename="relatorio.csv")
    def baixar_relatorio():
        def write_file(path):
            df = pd.DataFrame(historico.get(), columns=["mensagem"])
            df.to_csv(path, index=False)
        return write_file

    @reactive.Effect
    @reactive.event(input.feedback)
    def salvar_feedback():
        with open("feedbacks.csv", "a", encoding="utf-8") as f:
            f.write(f"{input.feedback()}\n")

    @reactive.Effect
    @reactive.event(input.enviar)
    def enviar_mensagem():
        mensagem = input.mensagem().strip()
        if mensagem:
            resultado = responder(mensagem, usuario_id="usuario_shiny")

            if resultado["type"] == "text":
                novo_historico = historico.get() + [
                    ui.tags.div(f"👤 Você: {mensagem}"),
                    ui.tags.div(f"🤖 Bot: {resultado['content']}")
                ]

            elif resultado["type"] == "plot":
                match resultado["plot_id"]:
                    case "mais_vendidos":
                        fig = plot_mais_vendidos()
                    case "vendas_mensais":
                        fig = plot_vendas_mensais()
                    case "distribuicao_notas":
                        fig = plot_distribuicao_notas()
                    case "precos_altos":
                        fig = plot_precos_altos()
                    case "preco_mais_vendidos":
                        fig = plot_preco_mais_vendidos()
                    case "top_faturamento":
                        fig = plot_top_faturamento()
                    case _:
                        fig = None

                if fig:
                    img64 = fig_to_base64(fig)
                    img_tag = ui.tags.img(src=f"data:image/png;base64,{img64}", style="max-width: 100%; height: auto;")
                    novo_historico = historico.get() + [
                        ui.tags.div(f"👤 Você: {mensagem}"),
                        ui.tags.div("🤖 Bot: Aqui está o gráfico que você pediu!"),
                        img_tag
                    ]
                else:
                    novo_historico = historico.get() + [
                        ui.tags.div(f"👤 Você: {mensagem}"),
                        ui.tags.div("🤖 Bot: Desculpe, não consegui gerar o gráfico.")
                    ]

            historico.set(novo_historico)
            session.send_input_message("mensagem", "")

    @output
    @render.ui
    def resposta():
        return historico.get()

    @output
    @render.text
    def total_vendas():
        return f"Total de vendas: {dados_info.shape[0]}"

    @output
    @render.text
    def nota_media():
        return f"Média das avaliações: {round(dados_info['review_score'].mean(), 2)}"

# ==============================
# Run App
# ==============================
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()

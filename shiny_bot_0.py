# ========== shiny_bot.py ==========

from shiny import App, ui, reactive, render
from chatbot_produto_v0 import (
    responder,
    plot_mais_vendidos,
    plot_vendas_mensais,
    plot_distribuicao_notas,
    plot_precos_altos,
    plot_preco_mais_vendidos,
    plot_top_faturamento
)
import tempfile
import base64
from matplotlib.figure import Figure

app_ui = ui.page_fluid(
    ui.h2("Chat Inteligente - Insights para seu Negócio"),
    ui.input_text("mensagem", "Digite sua pergunta:", placeholder="Ex: Quais os produtos mais vendidos?"),
    ui.input_action_button("enviar", "Enviar", class_="btn-primary"),
    ui.hr(),
    ui.h4("Histórico da Conversa:"),
    ui.output_ui("resposta"),
    style="padding: 20px; font-family: sans-serif;"
)

def fig_to_base64(fig: Figure) -> str:
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
        fig.savefig(tmpfile.name, format="png", bbox_inches="tight")
        with open(tmpfile.name, "rb") as f:
            img_data = f.read()
    return base64.b64encode(img_data).decode("utf-8")

def server(input, output, session):
    historico = reactive.Value([])

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
                pid = resultado["plot_id"]
                if pid == "mais_vendidos":
                    fig = plot_mais_vendidos()
                elif pid == "vendas_mensais":
                    fig = plot_vendas_mensais()
                elif pid == "distribuicao_notas":
                    fig = plot_distribuicao_notas()
                elif pid == "precos_altos":
                    fig = plot_precos_altos()
                elif pid == "preco_mais_vendidos":
                    fig = plot_preco_mais_vendidos()
                elif pid == "top_faturamento":
                    fig = plot_top_faturamento()
                else:
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

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()

import flet as ft
from flet_contrib.color_picker import ColorPicker

def main(page: ft.Page):
    page.title = "Teste Botão"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = True

    def atualizar_botao(e):
        botao_principal.text = texto_botao.value
        botao_principal.width = largura_botao.value
        botao_principal.height = altura_botao.value
        botao_principal.icon = ft.icons.__dict__.get(icone_botao.value)

        if estilo_botao.value == "Stadium Border":
            botao_principal.style = ft.ButtonStyle(shape=ft.StadiumBorder())
        elif estilo_botao.value == "Rounded Rectangle":
            botao_principal.style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder())
        elif estilo_botao.value == "Circle":
            botao_principal.style = ft.ButtonStyle(shape=ft.CircleBorder())

        botao_principal.bgcolor = color_picker.color
        dialogo_cor.open = False
        page.update()

    def abrir_color_picker(e):
        page.dialog = dialogo_cor
        dialogo_cor.open = True
        page.update()

    def fechar_color_picker(e):
        dialogo_cor.open = False
        page.update()

    texto_botao = ft.TextField(
        label="Texto do Botão",
        hint_text="Clique aqui!",
        value="Clique aqui!",
        on_change=atualizar_botao
    )

    largura_botao = ft.Slider(
        label="Largura: {value}",
        min=100,
        max=1000,
        value=100,
        divisions=10,
        on_change=atualizar_botao
    )

    altura_botao = ft.Slider(
        label="Altura: {value}",
        min=40,
        max=200,
        value=40,
        divisions=10,
        on_change=atualizar_botao
    )

    icone_botao = ft.Dropdown(
        options=[
            ft.dropdown.Option("ADD_HOME"),
            ft.dropdown.Option("AUTO_DELETE"),
            ft.dropdown.Option("SAVE")
        ],
        value="ADD_HOME",
        on_change=atualizar_botao
    )

    estilo_botao = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(label="Stadium Border", value="Stadium Border"),
            ft.Radio(label="Rounded Rectangle", value="Rounded Rectangle"),
            ft.Radio(label="Circle", value="Circle"),
        ]),
        value="Stadium Border",
        on_change=atualizar_botao
    )

    color_picker = ColorPicker(
        color="#FF0000",
        width=300,
    )

    dialogo_cor = ft.AlertDialog(
        content=color_picker,
        actions=[
            ft.TextButton("OK", on_click=atualizar_botao),
            ft.TextButton("Cancelar", on_click=fechar_color_picker),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    cor_botao = ft.IconButton(
        icon=ft.icons.BRUSH,
        on_click=abrir_color_picker
    )

    botao_principal = ft.ElevatedButton(
        text="Clique aqui",
        bgcolor="red",
        color="white",
        elevation=2,
        width=100,
        height=40,
    )

    page.add(
        botao_principal,
        texto_botao,
        ft.Row(controls=[ft.Text("Largura do Botão: "), largura_botao]),
        ft.Row(controls=[ft.Text("Altura do Botão: "), altura_botao]),
        ft.Row(controls=[ft.Text("Ícone do Botão: "), icone_botao]),
        ft.Row(controls=[ft.Text("Estilo do Botão: "), estilo_botao]),
        ft.Row(controls=[ft.Text("Cor de Fundo do Botão: "), cor_botao]),
    )

    atualizar_botao(None)

ft.app(target=main)

import asyncio

import flet
import ft
from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Row, Icon
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight
from datetime import datetime

from flet.controls.material.icons import Icons


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro app"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    # Funções
    def mostra_nome():
        text_display.value = f"NOME: {text_name.value}"
        text_display_cor.value = f"Cor: {text_cor.value}"
        text_display_marca.value = f"Marca: {text_marca.value}"
        text_display_cambio.value = f"Cambio: {text_cambio.value}"

        tem_erro = False

        if text_name.value:
            text_name.error = None
        else:
            tem_erro = True
            text_name.error = "Campo obrigatório"

        if text_cor.value:
            text_cor.error = None
        else:
            tem_erro = True
            text_cor.error = "Campo obrigatório"

        if text_marca.value:
            text_marca.error = None
        else:
            tem_erro = True
            text_marca.error = "Campo obrigatório"

        if text_cambio.value:
            text_cambio.error = None

        else:
            tem_erro = True
            text_cambio.error = "Campo obrigatório"

        if not tem_erro:
            text_name.value = ""
            text_cor.value = ""
            text_marca.value = ""
            text_cambio.value = ""
            navegate("/segunda_tela")

    # Navegar
    def navegate(route):
        asyncio.create_task(

            page.push_route(route)

        )

    # Gerenciar as telas(Routes)
    def route_change():
        page.views.clear()  # Limpar telas
        page.views.append(

            View(  # Tela

                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira Página",
                        bgcolor=Colors.BLUE_300,

                    ),
                    Container(
                        Column([
                            Row([

                                Icon(Icons.CAR_RENTAL),
                                text,


                            ]),
                            text_name,

                            Row([
                                Icon(Icons.COLOR_LENS),
                                text_name_cor,

                            ]),
                            text_cor,

                            Row([
                                Icon(Icons.DIRECTIONS_CAR_FILLED_OUTLINED),
                                text_name_marca,

                            ]),
                            text_marca,

                            Row([
                                Icon(Icons.ACCOUNT_TREE_OUTLINED),
                                text_name_cambio,

                            ]),
                            text_cambio,
                            bnt_save


                        ])

                    )


                ]

            )
        )

        if page.route == "/segunda_tela":
            page.views.append(

                View(  # Tela

                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda Página",
                            bgcolor=Colors.BLUE_800

                        ),
                        text_display,
                        text_display_cor,
                        text_display_marca,
                        text_display_cambio,
                        bnt_save

                    ]

                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    # Nome:
    text = Text("Nome:")
    text_display = Text("")
    text_name = TextField("")

    #Cor:
    text_name_cor = Text("Cor:")
    text_display_cor = Text("")
    text_cor = TextField("")

    # Marca

    text_name_marca = Text("Marca:")
    text_display_marca = Text("")
    text_marca = TextField("")

    # Cambio

    text_name_cambio = Text("Cambio:")
    text_display_cambio = Text("")
    text_cambio = TextField("")

    bnt_save = Button("Salvar", on_click=mostra_nome)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)

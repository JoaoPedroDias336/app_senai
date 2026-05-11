import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Icon, Text, Card, \
    Column, Container, Row, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, CrossAxisAlignment


class Carro:
    def __init__(self, nome, cor, marca, cambio, tamanho):
        self.nome = nome
        self.cor = cor
        self.marca = marca
        self.cambio = cambio
        self.tamanho = tamanho


def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo Cafeteira"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # FUNÇÕES
    # navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def icone_cambio(p1):
        if p1 == "Manual":
            return Icon(Icons.DIRECTIONS_CAR_FILLED_OUTLINED, color=Colors.BLUE_400)
        elif p1 == "Semi-automatico":
            return Icon(Icons.DIRECTIONS_CAR_ROUNDED, color=Colors.BLUE_400)
        elif p1 == "Automatico":
            return Icon(Icons.ELECTRIC_CAR_SHARP, color=Colors.BLUE_400)

    def montar_lista_padrao():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=icone_cambio(item.cambio),
                    title=item.marca,
                    subtitle=item.nome,
                    trailing=PopupMenuButton(
                        icon=Icon(Icons.MORE_VERT, color=Colors.BLUE_400),
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icon(Icons.REMOVE_RED_EYE, color=Colors.BLUE_400, ),
                                          on_click=lambda _, carro=item: ver_detalhes(carro)),

                            PopupMenuItem("Excluir", icon=Icon(Icons.DELETE, color=Colors.BLUE_400),
                                          on_click=lambda: excluir(item)),
                        ]
                    ),
                )
            )

    def ver_detalhes(carro):
        text_marca.value = carro.marca
        text_nome.value = carro.nome
        text_cor.value = carro.cor
        text_tamanho.value = carro.tamanho
        text_cambio.value = carro.cambio

        navegar("/detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        marca = input_marca.value
        nome = input_nome.value
        cor = input_cor.value
        tamanho = input_tamanho.value
        cambio = input_cambio.value

        tem_erro = False
        if marca:
            input_marca.error = None
        else:
            input_marca.error = "Campo Obrigatório"
            tem_erro = True

        if nome:
            input_nome.error = None
        else:
            input_nome.error = "Campo Obrigatório"
            tem_erro = True

        if cor:
            input_cor.error = None
        else:
            input_cor.error = "Campo Obrigatório"
            tem_erro = True

        if tamanho:
            input_tamanho.error = None
        else:
            input_tamanho.error = "Campo Obrigatório"
            tem_erro = True

        if cambio:
            input_cambio.error = None
        else:
            input_cambio.error = "Campo Obrigatório"
            tem_erro = True

        if not tem_erro:
            p1 = Carro(nome=nome.strip(), cor=cor.strip(), marca=marca.strip(), cambio=cambio.strip(), tamanho=tamanho.strip())
            lista_dados.append(p1)
        navegar("/lista_padrao")

        montar_lista_padrao()

    # gerenciar telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    flet.AppBar(
                        title="Carros",
                        bgcolor=Colors.BLUE_900

                    ),
                    list_view

                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.BLUE_900

                        ),
                        input_marca,
                        input_nome,
                        input_cor,
                        input_tamanho,
                        input_cambio,
                        btn_salvar,

                    ]
                )
            )


        elif page.route == "/detalhes":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.BLUE_900

                        ),

                        Container(
                            Column([
                                text_marca,
                                Row([
                                    Icon(Icons.ATTACH_MONEY, color=Colors.BLACK, size=20),
                                    text_nome,
                                ]),
                                Row([
                                    Icon(Icons.COLOR_LENS, color=Colors.BLACK, size=20),
                                    text_cor,
                                ]),
                                Row([
                                    Icon(Icons.FORMAT_SIZE, color=Colors.BLACK, size=20),
                                    text_tamanho,

                                ]),
                                Row([
                                    Icon(Icons.STORAGE_ROUNDED, color=Colors.BLACK, size=20),
                                    text_cambio,
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.BLUE_900,
                            padding=10,
                            border_radius=5,
                            width=400
                        )

                    ]
                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # COMPONENTES

    text_nome = Text()
    text_marca = Text()
    text_cor = Text()
    text_cambio = Text()
    text_tamanho = Text()

    input_marca = TextField(label="Digite a marca")
    input_nome = TextField(label="Digite o nome")
    input_cor = TextField(label="Digite a cor")
    input_tamanho = TextField(label="Digite o tamano")
    input_cambio = Dropdown(
        label="Cambio",
        editable=True,
        options=[
            DropdownOption("Manual"),
            DropdownOption("Semi-automatico"),
            DropdownOption("Automatico"),
        ],
    )
    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados(), color=Colors.BLUE_800)
    list_view = ListView(height=500)

    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)

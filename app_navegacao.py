import asyncio
from asyncio import create_task

import flet
from flet import ThemeMode, View, AppBar, Colors, Button


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    #funções
    #navegar

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )


    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Primeira Página",
                        bgcolor=Colors.GREY_700
                    ),
                    Button("Ir para segunda tela", on_click= lambda: navegar("/segunda_tela"),color=Colors.RED_300),

                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="Segunda Página",
                            bgcolor=Colors.GREY_700

                        )
                    ]
                )
            )

    #voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)


    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
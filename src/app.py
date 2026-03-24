import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, ElevatedButton
from flet.controls.border_radius import horizontal
from datetime import datetime
from datetime import date


def main(page: flet.Page, input_numero=None):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"

    def verficar_par_impar():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            text_par_impar.text = f" O {numero} é impar"
        else:
            text_par_impar.text = f" O {numero} é par"

    def calcular_idade():
        ano_nascimento = int(input_idade.value)
        idade = datetime.now().year - ano_nascimento

        if idade >= 18:
            text.value = f"voce tem {idade} anos e é maior de idade"
            page.update()
        else:
            text.value = f"voce tem {idade} anos e é menor de idade"
            page.update()

    # Componentes
    text = Text()
    text_par_impar = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    input_numero = TextField(label="Digite um numero", hint_text="Verficar se é par ou impar ")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_verificar = OutlinedButton("Verificar", on_click=verficar_par_impar)
    input_idade = TextField(label="Digite seu ano de nascimento")
    btn_calcular = OutlinedButton("Verificar", on_click=calcular_idade)

    # Construção da tela

    page.add(
        Column(
            [
            input_nome,
            input_sobrenome,
            btn_salvar,
            text,
            input_numero,
            text_par_impar,
            btn_verificar,
            input_idade,
            btn_calcular
            ],
            width = 400,
            horizontal_alignment = CrossAxisAlignment.CENTER
        )
    )




flet.run(main)





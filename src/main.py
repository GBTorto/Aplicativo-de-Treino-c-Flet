import flet as ft

def main(page: ft.Page):
    nome = ft.TextField(
        label="Digite seu nome:"
    )
    senha = ft.TextField(
        label="Digite sua senha",
        password=True,
        can_reveal_password=True
    )

    page.add(nome, senha)


ft.app(main)
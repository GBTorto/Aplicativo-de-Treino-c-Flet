import flet as ft

def main(page: ft.Page):
    cadastrar_treino = ft.Button(
        text="Cadastrar treino",
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_500,
            color=ft.Colors.WHITE
        ),
        on_click=lambda e: page.go("/cadastrar_treino")
    )



    page.views.append(
        ft.View(
            "/tela_principal",
            controls=[
                ft.Text("Tela Principal"),
                cadastrar_treino
            ]
        )
    )
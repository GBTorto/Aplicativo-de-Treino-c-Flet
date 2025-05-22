import flet as ft
import cadastrar_usuario

def main(page: ft.Page):

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            nome = ft.TextField(label="Digite seu nome:")
            senha = ft.TextField(label="Digite sua senha", password=True, can_reveal_password=True)

            cadastro = ft.TextButton(
                text="Cadastre-se",
                style=ft.ButtonStyle(
                    color=ft.Colors.BLUE_500,
                    padding=0,
                    overlay_color=ft.Colors.TRANSPARENT,
                ),
                on_click=lambda e: page.go("/cadastrar_usuario")
            )

            page.views.append(
                ft.View("/", controls=[nome, senha, cadastro])
            )

        elif page.route == "/cadastrar_usuario":
            cadastrar_usuario.main(page)

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)

import flet as ft
import cadastrar_usuario
import tela_principal
import cadastrar_treino
import info_exercicios
import urllib.parse
from banco_dados import verificar_usuario

def main(page: ft.Page):

    def route_change(e):
        global email, senha
        page.views.clear()

        if page.route == "/":
            email = ft.TextField(label="Digite seu email:")
            senha = ft.TextField(label="Digite sua senha", password=True, can_reveal_password=True)

            cadastro = ft.Button(
                text="Cadastre-se",
                style=ft.ButtonStyle(
                    color=ft.Colors.BLUE_500,
                    padding=0,
                    overlay_color=ft.Colors.TRANSPARENT,
                ),
                on_click=lambda e: page.go("/cadastrar_usuario")
            )

            verificar = ft.Button(
                text="Entrar",
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.GREEN_500,
                    padding=0,
                    color=ft.Colors.WHITE
                ),
                on_click=verificar_login
            )

            page.views.append(
                ft.View("/", controls=[email, senha, cadastro, verificar])
            )

        elif page.route == "/cadastrar_usuario":
            cadastrar_usuario.main(page)
        
        elif page.route == "/tela_principal":
            tela_principal.main(page, id_usuario)

        elif page.route == "/cadastrar_treino":
            cadastrar_treino.main(page, id_usuario)
        
        elif page.route.startswith("/info_exercicios"):
            parsed = urllib.parse.urlparse(page.route)
            params = urllib.parse.parse_qs(parsed.query)


            if "id" in params:
                id_exercicio = params["id"][0]
            else:
                id_exercicio = None
            
            print(id_exercicio)

            info_exercicios.main(page, id_exercicio)

        page.update()

    def verificar_login(e):
        global id_usuario

        if verificar_usuario(email.value, senha.value):
            id_usuario = verificar_usuario(email.value, senha.value)
            page.go("/tela_principal")
        else:
            print("Faça seu cadastro")

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)

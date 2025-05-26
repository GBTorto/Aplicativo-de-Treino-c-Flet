import flet as ft
from banco_dados import exercicios_usuarios

categorias = [
    "Costas",
    "Cardio",
    "Peito",
    "Antebraço",
    "Panturrilha",
    "Perna",
    "Pescoço",
    "Ombro",
    "Bíceps/Tríceps",
    "Abdomen"
]

def main(page: ft.Page, id_usuario):
    def separar_categoria():
        controles = []
        for categoria in categorias:
            banco_dados = exercicios_usuarios(categoria, id_usuario)
            if banco_dados:  # Se não for vazio
                for colunas_banco_dados in banco_dados:
                    controles.append(ft.Text(f"{colunas_banco_dados[2]}"))  # ou colunas_banco_dados[n], conforme coluna desejada
                    controles.append(ft.Button(text=f"{colunas_banco_dados[3]}"))
                    # for ex in colunas_banco_dados:
                    #     controles.append(ft.Button(text=f"{ex}"))
            else:
                pass
        return controles


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
                *separar_categoria(),
                cadastrar_treino
            ]
        )
    )
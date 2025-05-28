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
                # Adiciona o título da categoria
                controles.append(ft.Text(categoria.upper(), size=20, weight="bold"))
                
                # Adiciona os botões de exercícios
                for colunas_banco_dados in banco_dados:
                    id_exercicio = colunas_banco_dados[0]
                    nome_exercicio = colunas_banco_dados[3]  # ou [2], dependendo de onde está o nome
                    controles.append(ft.Button(text=nome_exercicio, on_click=lambda e, id=id_exercicio: page.go(f"/info_exercicios?id={id}")))
                    
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
import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro do treino"
    nome_exercicio = ft.TextField(label="Nome do Exercício")
    grupo_muscular = ft.TextField(label="Grupo Muscular")
    page.add(nome_exercicio, grupo_muscular)

if __name__ == "__main__":
    ft.app(target=main)
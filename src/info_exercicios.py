import flet as ft
import matplotlib
from banco_dados import info_exercicios, pegar_info_ou_nome_exercicio

def main(page: ft.Page, id_exercicio):
    info = pegar_info_ou_nome_exercicio(id_exercicio)

    nome_exercicio = info['nome']
    data_banco = info['data_execucao']
    series_banco = info['series']
    repeticoes_banco = info['repeticoes']
    peso_banco = info['peso']

    

    page.views.append(
        ft.View(
            route="/info_exercicios",
            controls=[
                ft.Text(nome_exercicio),
                ft.Text(f"Teste - ID do exercício: {id_exercicio}"),
                ft.Button(text="Voltar",
                        on_click=lambda e: page.go("/tela_principal"))
            ]
        )
    )
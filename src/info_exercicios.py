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

    data = ft.TextField(label="Data")
    series = ft.TextField(label="Séries", disabled=True)
    repeticoes = ft.TextField(label="Repetições", disabled=True)
    peso = ft.TextField(label="Peso", disabled=True)

    def on_data_change(e):
        series.disabled = not bool(data.value)
        repeticoes.disabled = True
        peso.disabled = True
        page.update()

    def on_series_change(e):
        repeticoes.disabled = not bool(series.value)
        peso.disabled = True
        page.update()

    def on_repeticoes_change(e):
        peso.disabled = not bool(repeticoes.value)
        page.update()

    data.on_change = on_data_change
    series.on_change = on_series_change
    repeticoes.on_change = on_repeticoes_change

    page.views.append(
        ft.View(
            route="/info_exercicios",
            controls=[
                ft.Text(nome_exercicio),
                ft.Text(f"Teste - ID do exercício: {id_exercicio}"),
                data,
                series,
                repeticoes,
                peso,
                ft.Button(text="Voltar",
                        on_click=lambda e: page.go("/tela_principal"))
            ]
        )
    )
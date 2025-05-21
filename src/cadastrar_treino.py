import flet as ft
import requests
from deep_translator import GoogleTranslator

API_KEY = "9cf8d58116mshf0fd1c5673119d3p121530jsnd08562d622dd"
API_HOST = "exercisedb.p.rapidapi.com"

correcoes_exercicios_pt = {
    "pull-up": "barra fixa",
    "push-up": "flexão de braço",
    "barbell curl": "rosca direta com barra",
    "deadlift": "levantamento terra",
    "squat": "agachamento",
    "bench press": "supino",
}

categorias_api = {
    "Costas": "back",
    "Cardio": "cardio",
    "Peito": "chest",
    "Antebraço": "lower arms",
    "Panturrilha": "lower legs",
    "Perna": "upper legs",
    "Pescoço": "neck",
    "Ombro": "shoulders",  # Corrigi para "shoulders" (deveria ser "shoulders"?)
    "Bíceps/Tríceps": "upper arms",
    "Abdomen": "waist"
}

def traduzir_exercicios(nome_en):
    nome_en = nome_en.lower()
    if nome_en in correcoes_exercicios_pt:
        return correcoes_exercicios_pt[nome_en]
    
    try:
        traducao = GoogleTranslator(source="en", target="pt").translate(nome_en)
        return traducao
    except Exception as e:
        return nome_en

def main(page: ft.Page):
    page.scroll = "auto"
    resultados = ft.Column()
    categoria_treino_lista = list(categorias_api.keys())
    
    # Variável para armazenar os dados dos exercícios
    dados_exercicios = []

    def categoria():
        return [
            ft.dropdown.DropdownOption(key=tipo, text=tipo) 
            for tipo in categoria_treino_lista
        ]
    
    def lista_exercicio(body_part):
        url = f"https://{API_HOST}/exercises/bodyPart/{body_part}"
        cabecalho = {
            "X-RapidAPI-KEY": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }

        resposta = requests.get(url, headers=cabecalho)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            print("Erro ao buscar dados da API:", resposta.status_code)
            return []
    
    def dropdown_categoria(e):
        nonlocal dados_exercicios
        selecionado_pt = e.control.value
        selecionado_en = categorias_api.get(selecionado_pt)

        if not selecionado_en:
            return
        
        dados_exercicios = lista_exercicio(selecionado_en)

        # Atualiza o dropdown de exercícios
        exercicios.options = [
            ft.dropdown.DropdownOption(
                key=ex['name'],
                text=traduzir_exercicios(ex['name'].capitalize())
            ) for ex in dados_exercicios
        ]
        
        # Habilita o dropdown de exercícios
        exercicios.disabled = False
        
        # Limpa e mostra os resultados
        resultados.controls.clear()
        for ex in dados_exercicios[:10]:  # Mostra apenas os 10 primeiros como exemplo
            resultados.controls.append(
                ft.Text(f"🏋️ {traduzir_exercicios(ex['name'].capitalize())} — Equipamento: {ex['equipment'].capitalize()}")
            )
        page.update()

    def dropdown_exercicio(e):
        exercicio_selecionado = e.control.value
        if exercicio_selecionado:
            # Limpa os resultados anteriores
            resultados.controls.clear()
            
            # Encontra o exercício selecionado nos dados
            exercicio_info = next((ex for ex in dados_exercicios 
                                if traduzir_exercicios(ex['name'].capitalize()) == exercicio_selecionado), None)
            
            if exercicio_info:
                # Mostra informações detalhadas do exercício
                resultados.controls.append(
                    ft.Text(f"🏋️ Exercício selecionado: {exercicio_selecionado}", 
                        size=18, weight="bold")
                )
                resultados.controls.append(
                    ft.Text(f"🔧 Equipamento: {traduzir_exercicios(exercicio_info['equipment'].capitalize())}")
                )
                resultados.controls.append(
                    ft.Text(f"📝 Instruções:", weight="bold")
                )
                # Quebra as instruções em parágrafos
                instrucoes = exercicio_info.get('instructions', '').split('. ')
                for instr in instrucoes:
                    if instr.strip():
                        resultados.controls.append(ft.Text(f"• {instr}"))
            
            page.update()

    categoria_treino = ft.Dropdown(
        width=400,
        hint_text="Digite ou selecione uma categoria...",
        options=categoria(),
        on_change=dropdown_categoria,
        autofocus=True,
        enable_search=True,  # Propriedade correta para pesquisa
        text_size=14,
        content_padding=10,
        border_color=ft.Colors.BLUE_500,  # Sintaxe CORRETA para v0.28.2
        border_radius=10,
        elevation=8,
        prefix_icon=ft.Icons.SEARCH,  # Sintaxe CORRETA para v0.28.2
    )

    exercicios = ft.Dropdown(
        width=400,
        hint_text="Digite ou selecione um exercício...",
        options=[],
        on_change=dropdown_exercicio,
        disabled=True,
        enable_search=True,  # Propriedade correta para pesquisa
        text_size=14,
        content_padding=10,
        border_color=ft.Colors.GREEN_500,  # Sintaxe CORRETA
        border_radius=10,
        elevation=8,
        prefix_icon=ft.Icons.FITNESS_CENTER,  # Sintaxe CORRETA
    )
    page.add(
        ft.Row([categoria_treino, exercicios], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Text("Exercícios:", size=20, weight="bold"),
        resultados
    )

ft.app(main)
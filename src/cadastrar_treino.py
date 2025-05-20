import flet as ft

def main(page: ft.Page):
    categoria_treino_lista = ["Costas", "Cardio", "Peito", "Antebraço", "Panturrilha", "Perna", "Pescoço", "Ombro", "Bíceps/Tríceps", "Abdomen"]

    def categoria():
        opcao = []
        for tipo in categoria_treino_lista:
            opcao.append(ft.DropdownOption(
                        key=tipo,
                        content=ft.Text(
                            value=tipo
                        )
                    )
                )
        
        return opcao

    colors = [
        ft.Colors.RED,
        ft.Colors.BLUE,
        ft.Colors.YELLOW,
        ft.Colors.PURPLE,
        ft.Colors.LIME,
    ]

    def get_options():
        options = []
        for color in colors:
            options.append(
                ft.DropdownOption(
                    key=color.value,
                    content=ft.Text(
                        value=color.value,
                        color=color,
                    ),
                )
            )
        return options

    def dropdown_changed(e):
        e.control.color = e.control.value
        page.update()
    
    def dropdown_categoria(e):
        print(f"Categoria selecionada: {e.control.value}")
        page.update()

    categoria_treino = ft.Dropdown(
        editable=True,
        label="Categoria",
        options=categoria(),
        on_change=dropdown_categoria
    )
    dd = ft.Dropdown(
        editable=True,
        label="Color",
        options=get_options(),
        on_change=dropdown_changed,
    )

    page.add(dd, categoria_treino)


ft.app(main)
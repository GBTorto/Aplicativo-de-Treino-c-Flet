import flet as ft
import re
from banco_dados import banco_dados_usuarios

def main(page: ft.Page):
    def senha_valida(senha):
        tem_numero = re.search(r"\d", senha)
        tem_maiuscula = re.search(r"[A-Z]", senha)
        tem_caracteres_especiais = re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha)
    
        return bool(tem_numero and tem_maiuscula and tem_caracteres_especiais)
    
    def email_valido(email):
        tem_arroba = re.search(r"[@]", email)
        tem_ponto_com = re.search(r"\.com", email)

        return bool(tem_arroba and tem_ponto_com)

    email = ft.TextField(label="Digite seu email")
    nome = ft.TextField(label="Digite seu nome")
    senha = ft.TextField(label="Digite sua senha",
                    password=True,
                    can_reveal_password=True)
    
    mensagem = ft.Text(color=ft.Colors.RED)

    def tentar_cadastrar(e):
        if not email_valido(email.value):
            mensagem.value = "Email inválido"
        elif not nome.value:
            mensagem.value = "Digite um nome"
        elif not senha_valida(senha.value):
            mensagem.value = "Senha inválida: precisa conter número, letra maiúscula e caractere especial."
        else:
            # mensagem.value = "Cadastro realizado com sucesso!"
            banco_dados_usuarios(email.value, nome.value, senha.value)
            page.go("/tela_principal")
            # Aqui você pode chamar a função que salva os dados, etc.
        page.update()

    botao_cadastrar = ft.ElevatedButton("Cadastrar", on_click=tentar_cadastrar)
    botao_voltar = ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/"))

    page.views.append(
        ft.View(
            "/cadastrar_usuario",
            controls=[
                ft.Text("Página de Cadastro de Usuário"),
                email,
                nome,
                senha,
                mensagem,
                botao_cadastrar,
                botao_voltar
            ]
        )
    )
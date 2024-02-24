import flet as ft
from models import Cliente
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///cadastro.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def main(page: ft.Page):
    page.title = 'Cadastro de clientes'
    lista_clientes = ft.ListView(expand=1, auto_scroll=True)

    def cadastro(e):
        try:
            novo_cliente = Cliente(name=user_input.value, age=age_input.value)
            session.add(novo_cliente)
            session.commit()
            lista_clientes.controls.append(ft.Container(

                ft.Text(user_input.value),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            ))
            txt_erro.visible = False
            txt_sucess.visible = True
        except:
            txt_erro.visible = True
            txt_sucess.visible = False
            print('Erro ao cadastrar')

        page.update()
        print('Cliente cadastrado com sucesso')
        
    txt_erro = ft.Container(
        ft.Text('Erro ao cadastrar cliente'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_sucess = ft.Container(ft.Text(
        'Cliente cadastrado com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    txt_erro_delete = ft.Container(
        ft.Text('Erro ao deletar cliente'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_sucess_delete = ft.Container(ft.Text(
        'Cliente excluido com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)

    txt_titulo = ft.Text('Dados do cliente',)
    input_v = ft.Text()
    user_input = ft.TextField(label="Nome",
                            icon=ft.icons.SUPERVISOR_ACCOUNT, text_align=ft.TextAlign.LEFT)
    age_input = ft.TextField(label="Idade",
                            icon=ft.icons.NUMBERS, text_align=ft.TextAlign.LEFT)
    btn_submit = ft.ElevatedButton(text="Cadastrar", on_click=cadastro )

    for i in session.query(Cliente).all():
        lista_clientes.controls.append(
            ft.Container(
                ft.Text(i.name),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )

        )

    page.add(txt_erro, txt_sucess,txt_erro_delete, txt_sucess_delete, txt_titulo, user_input, age_input,
            btn_submit, input_v, lista_clientes)


ft.app(target=main)

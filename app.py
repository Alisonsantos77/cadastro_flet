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
    # def button_clicked(e):
    #     input_v.value = f"Nome: '{user_input.value}' e senha: '{
    #         age_input.value}'."
    #     page.update()
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
        
    # def delete_cliente(e, cliente_id):
    #     cliente = session.query(Cliente).get(cliente_id)
    #     try:
    #         if cliente:
    #             session.delete(cliente)
    #             session.commit()
    #         txt_erro_delete.visible = False
    #         txt_sucess_delete.visible = True

    #     except:
    #         txt_erro_delete.visible = True
    #         txt_sucess_delete.visible = False
    #         print('Erro ao excluir')
    #     page.update()
    #     print('Excluido com sucesso')
            
            
    def close_anchor(e):
        text = f"{e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")


    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Busque clientes...",
        view_hint_text="Escolha o cliente entre as sugestões...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f"Nome:{i.name}| Idade:{i.age}"), on_click=close_anchor, data=i)
            for i in session.query(Cliente).all()
        ],
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.OutlinedButton(
                    "Open Search View",
                    on_click=lambda _: anchor.open_view(),
                ),
            ],
        ),
        anchor,
    )

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
    btn_submit = ft.ElevatedButton(text="Submit", on_click=cadastro)
    btn_delete = ft.ElevatedButton(text="Apagar")

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
            btn_submit,btn_delete, input_v, lista_clientes)


ft.app(target=main)

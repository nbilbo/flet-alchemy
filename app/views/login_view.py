import flet as ft
from app.forms.login_form import LoginForm


class LoginView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.form = LoginForm()
        content = ft.Column()
        container = ft.Container()

        content.width = 500
        content.alignment = ft.MainAxisAlignment.CENTER
        content.controls.append(self.form)

        container.content = content
        container.expand = 1
        container.border = None
        self.controls.append(container)

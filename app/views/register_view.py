import flet as ft
from app.forms import RegisterForm


class RegisterView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.form = RegisterForm()
        content = ft.Column()
        container = ft.Container()

        content.width = 500
        content.alignment = ft.MainAxisAlignment.CENTER
        content.controls.append(self.form)

        # container.border = ft.border.all(5, ft.colors.BLACK)
        container.expand = 1
        container.content = content
        self.controls.append(container)

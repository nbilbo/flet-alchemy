import flet as ft
from app.forms.logout_form import LogoutForm


class LogoutView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.form = LogoutForm()
        content = ft.Column()
        container = ft.Container()

        content.width = 500
        content.alignment = ft.MainAxisAlignment.CENTER
        content.controls.append(self.form)

        container.content = content
        container.expand = 1
        container.border = ft.border.all(5, ft.colors.BLACK)
        self.controls.append(container)

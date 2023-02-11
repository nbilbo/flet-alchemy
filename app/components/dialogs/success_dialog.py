import flet as ft
from app.components.dialogs.generic_dialog import GenericDialog


class SuccessDialog(GenericDialog):
    def __init__(self, title: str, message: str) -> None:
        super().__init__(title, message)
        self.icon.name = ft.icons.CHECK

import flet as ft
from app.components.snacks.generic_snack import GenericSnack


class SuccessSnack(GenericSnack):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.icon.name = ft.icons.CHECK
        self.bgcolor = ft.colors.GREEN

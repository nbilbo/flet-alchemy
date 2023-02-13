import flet as ft


class GenericSnack(ft.SnackBar):
    def __init__(self, message: str) -> None:
        super().__init__(content=ft.Row())
        self.text = ft.Text()
        self.icon = ft.Icon()

        self.text.value = message
        self.text.weight = ft.FontWeight.NORMAL
        self.text.size = 14
        self.text.expand = True

        self.icon.name = ft.icons.PALETTE
        self.icon.size = 14

        self.content.controls.append(self.icon)
        self.content.controls.append(self.text)

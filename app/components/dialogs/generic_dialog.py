import flet as ft


class GenericDialog(ft.AlertDialog):
    def __init__(self, title: str, message: str) -> None:
        super().__init__()
        self.title = ft.Text()
        self.message = ft.Text()
        self.icon = ft.Icon()

        self.title.value = title
        self.title.expand = True
        self.title.text_align = ft.TextAlign.CENTER
        self.title.font_family = 'Akira'
        self.title.size = 30

        self.message.value = message
        self.message.expand = True
        self.message.text_align = ft.TextAlign.CENTER
        self.message.font_family = 'Roboto-Medium'
        self.message.size = 20

        self.icon.name = ft.icons.PALETTE
        self.icon.size = 30

        content = ft.Row()
        content.controls.append(self.icon)
        content.controls.append(self.message)
        self.content = content

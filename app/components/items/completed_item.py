import flet as ft


class CompletedItem(ft.Row):
    def __init__(self, identification: int, description: str) -> None:
        super().__init__()
        self.identification = identification
        self.text = ft.Text()
        self.incomplete_button = ft.TextButton()
        self.delete_button = ft.IconButton()

        self.text.value = description
        self.text.expand = True
        self.text.text_align = ft.TextAlign.CENTER
        self.text.font_family = 'Roboto-Medium'
        self.text.weight = ft.FontWeight.BOLD
        self.text.size = 14

        self.incomplete_button.text = 'Incomplete'
        self.incomplete_button.icon = ft.icons.CANCEL

        self.delete_button.tooltip = 'Delete'
        self.delete_button.icon = ft.icons.DELETE
        self.delete_button.icon_color = ft.colors.RED

        self.controls.append(self.text)
        self.controls.append(self.incomplete_button)
        self.controls.append(self.delete_button)

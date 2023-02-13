import flet as ft


class IncompletedItem(ft.Row):
    def __init__(self, identification: int, description: str) -> None:
        super().__init__()
        self.identification = identification
        self.text = ft.Text()
        self.complete_button = ft.TextButton()
        self.delete_button = ft.IconButton()

        self.text.value = description
        self.text.expand = True
        self.text.text_align = ft.TextAlign.CENTER
        self.text.font_family = 'Roboto-Medium'
        self.text.size = 12

        self.complete_button.text = 'Complete'
        self.complete_button.icon = ft.icons.CHECK

        self.delete_button.tooltip = 'Delete'
        self.delete_button.icon = ft.icons.DELETE
        self.delete_button.icon_color = ft.colors.RED

        self.controls.append(self.text)
        self.controls.append(self.complete_button)
        self.controls.append(self.delete_button)

import flet as ft


class GenericBanner(ft.Banner):
    def __init__(self, page: ft.Page, message: str) -> None:
        super().__init__()
        self.page = page
        self.leading = ft.Icon()
        self.content = ft.Text()
        self.confirm_button = ft.TextButton()

        self.leading.name = ft.icons.PALETTE
        self.leading.size = 30

        self.content.value = message
        self.content.weight = ft.FontWeight.BOLD

        self.confirm_button.text = 'Confirm'
        self.confirm_button.on_click = self.confirm_button_action
        self.actions.append(self.confirm_button)

    def confirm_button_action(self, event) -> None:
        self.open = False
        self.page.update()

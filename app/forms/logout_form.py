import flet as ft


class LogoutForm(ft.Column):
    def __init__(self) -> None:
        super().__init__()

        self.title = ft.Text()
        self.login_button = ft.TextButton()

        self.title.value = 'Logout'
        self.title.style = ft.TextThemeStyle.TITLE_LARGE
        self.title.expand = True
        self.title.text_align = ft.TextAlign.CENTER

        self.login_button.text = 'Sign In Again'
        self.login_button.icon = ft.icons.DOOR_BACK_DOOR
        self.login_button.expand = True

        self.controls.append(ft.Row([self.title]))
        self.controls.append(ft.Row([self.login_button]))

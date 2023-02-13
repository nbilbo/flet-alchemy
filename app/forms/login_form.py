import flet as ft


class LoginForm(ft.Column):
    def __init__(self) -> None:
        super().__init__()
        self.title = ft.Text()
        self.username_field = ft.TextField()
        self.password_field = ft.TextField()
        self.login_button = ft.OutlinedButton()
        self.register_button = ft.TextButton()

        self.title.value = 'Sign In'
        self.title.font_family = 'Cartis'
        self.title.size = 20
        self.title.expand = True
        self.title.text_align = ft.TextAlign.CENTER

        self.username_field.label = 'Username'
        self.username_field.expand = True
        self.username_field.text_size = 12

        self.password_field.label = 'Password'
        self.password_field.expand = True
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.text_size = 12

        self.login_button.text = 'Sign In'
        self.login_button.icon = ft.icons.DOOR_BACK_DOOR
        self.login_button.expand = True

        self.register_button.text = "Don't have an account? register here"
        self.register_button.expand = True

        self.controls.append(ft.Row([self.title]))
        self.controls.append(ft.Row([self.username_field]))
        self.controls.append(ft.Row([self.password_field]))
        self.controls.append(ft.Row([self.login_button]))
        self.controls.append(ft.Row([self.register_button]))

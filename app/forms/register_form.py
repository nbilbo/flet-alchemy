import flet as ft


class RegisterForm(ft.Column):
    def __init__(self) -> None:
        super().__init__()
        self.title = ft.Text()
        self.username_field = ft.TextField()
        self.email_field = ft.TextField()
        self.password_field = ft.TextField()
        self.register_button = ft.OutlinedButton()
        self.login_button = ft.TextButton()

        self.title.value = 'Sign Up'
        self.title.font_family = 'Akira'
        self.title.size = 20
        self.title.expand = True
        self.title.text_align = ft.TextAlign.CENTER

        self.username_field.label = 'Username'
        self.username_field.expand = True
        self.username_field.text_size = 14

        self.email_field.label = 'Email'
        self.email_field.expand = True
        self.email_field.text_size = 14

        self.password_field.label = 'Password'
        self.password_field.expand = True
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.text_size = 14

        self.register_button.text = 'Sign Up'
        self.register_button.icon = ft.icons.SAVE
        self.register_button.expand = True

        self.login_button.text = 'Already have an account? login here'
        self.login_button.expand = True

        self.controls.append(ft.Row([self.title]))
        self.controls.append(ft.Row([self.username_field]))
        self.controls.append(ft.Row([self.email_field]))
        self.controls.append(ft.Row([self.password_field]))
        self.controls.append(ft.Row([self.register_button]))
        self.controls.append(ft.Row([self.login_button]))

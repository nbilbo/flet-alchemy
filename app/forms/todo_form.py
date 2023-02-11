import flet as ft


class TodoForm(ft.Column):
    def __init__(self) -> None:
        super().__init__()
        self.title = ft.Text()
        self.description_field = ft.TextField()
        self.add_button = ft.FloatingActionButton()

        self.title.value = 'Register a new todo here'
        self.title.font_family = 'Cartis'
        self.title.size = 40
        self.title.expand = True
        self.title.text_align = ft.TextAlign.CENTER

        self.description_field.label = 'Whats need to be done?'
        self.description_field.expand = True

        self.add_button.icon = ft.icons.ADD
        self.add_button.shape = ft.CircleBorder()

        self.controls.append(ft.Row([self.title]))
        self.controls.append(ft.Row([self.description_field, self.add_button]))

import flet as ft
from app.components.appbar import AppBar
from app.forms.todo_form import TodoForm
from app.tabs.completed_tab import CompletedTab
from app.tabs.incompleted_tab import IncompletedTab


class HomeView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.form = TodoForm()
        self.tabs = ft.Tabs()
        self.completed_tab = CompletedTab()
        self.incompleted_tab = IncompletedTab()
        self.appbar = AppBar()
        content = ft.Column()
        container = ft.Container()

        self.tabs.expand = True
        self.tabs.animation_duration = 700
        self.tabs.tabs.append(self.incompleted_tab)
        self.tabs.tabs.append(self.completed_tab)

        content.width = 800
        content.alignment = ft.MainAxisAlignment.CENTER
        content.controls.append(self.form)
        content.controls.append(self.tabs)

        container.content = content
        container.expand = 1
        self.controls.append(container)

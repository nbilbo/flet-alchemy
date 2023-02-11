import flet as ft
from app.components.items.completed_item import CompletedItem


class CompletedTab(ft.Tab):
    def __init__(self) -> None:
        super().__init__()
        self.text = 'Completed'
        self.icon = ft.icons.CHECK
        self.listview = ft.ListView()
        content = ft.Column()
        container = ft.Container()

        self.listview.expand = True
        self.listview.auto_scroll = True
        self.listview.spacing = 20

        content.controls.append(self.listview)
        container.content = content
        container.expand = 1
        self.content = container

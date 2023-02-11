import flet as ft
from app.components.items.incompleted_item import IncompletedItem


class IncompletedTab(ft.Tab):
    def __init__(self) -> None:
        super().__init__()
        self.text = 'Incompleted'
        self.listview = ft.ListView()
        self.icon = ft.icons.CANCEL
        content = ft.Column()
        container = ft.Container()

        self.listview.expand = True
        self.listview.auto_scroll = True
        self.listview.spacing = 20

        content.controls.append(self.listview)
        container.content = content
        container.expand = 1
        self.content = container

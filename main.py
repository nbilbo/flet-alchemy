import flet as ft
from app.application import Application


if __name__ == '__main__':
    # ft.app(target=Application, assets_dir='./assets')
    ft.app(target=Application, view=ft.WEB_BROWSER, assets_dir='./assets')

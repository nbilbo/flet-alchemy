import flet as ft

from flet_alchemy.constructor import Constructor


def main(page: ft.Page) -> None:
    Constructor(page)


if __name__ == '__main__':
    # ft.app(target=main)
    ft.app(target=main, view=ft.WEB_BROWSER)

import flet as ft

def main(page: ft.Page):
    page.title = "Cafetería Zafiro"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#2b1b12"  # fondo café oscuro

    titulo = ft.Text(
        "☕ Cafetería Zafiro",
        size=30,
        weight="bold",
        color="#f5e6cc"
    )

    subtitulo = ft.Text(
        "Disfruta el mejor café ☕",
        size=16,
        color="#d2b48c"
    )

    def card_producto(nombre, precio, imagen):
        return ft.Container(
            content=ft.Column([
                ft.Image(src=imagen, width=200, height=150, fit=ft.ImageFit.COVER),
                ft.Text(nombre, size=18, weight="bold", color="white"),
                ft.Text(f"${precio}", color="#ffd700"),
                ft.ElevatedButton("Comprar", bgcolor="#8b4513", color="white")
            ], alignment="center"),
            bgcolor="#3e2723",
            padding=10,
            border_radius=15,
            width=220
        )

    productos = ft.Row(
        [
            card_producto(
                "Espresso",
                500,
                "https://images.unsplash.com/photo-1511920170033-f8396924c348"
            ),
            card_producto(
                "Cappuccino",
                750,
                "https://images.unsplash.com/photo-1509042239860-f550ce710b93"
            ),
            card_producto(
                "Latte",
                650,
                "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085"
            ),
            card_producto(
                "Torta de Chocolate",
                1200,
                "https://images.unsplash.com/photo-1605478909547-7f1b6b4b4e3b"
            ),
        ],
        alignment="center",
        wrap=True
    )

    page.add(
        ft.Column(
            [
                titulo,
                subtitulo,
                ft.Divider(color="#d2b48c"),
                productos
            ],
            horizontal_alignment="center"
        )
    )

ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
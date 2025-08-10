import flet as ft
from time import strftime

def main(page: ft.Page):
    page.title = "MetroX"
    page.bgcolor = ft.Colors.CYAN_900
    page.window.full_screen=True
  
    # Header
    header = ft.Container(
        content=ft.Stack([
            ft.Container(
                ft.Image(src="logo.png", width=220, height=220),
                alignment=ft.alignment.center_left,
                expand=True
            ),
        
            ft.Container(
                ft.Text("Sistema de Recargas", size=60, color="black", font_family="Poppins", weight="bold"),
                alignment=ft.alignment.center,
                expand=True
            ),
                
            ft.Container(
                ft.Text(strftime("%H:%M %p"), color="#B00020", weight="bold", size=40),
                alignment=ft.alignment.center_right,
                expand=True,
                padding=30
            ),
        ]),
        bgcolor="white",
        padding=15,
        height=175,
        border_radius=ft.border_radius.only(top_left=10, top_right=10),
    )

    left_panel = ft.Container(
        content=ft.Column([
            ft.Container(
                content=ft.Stack([

                    ft.Image(src="card.png", width=450, height=450),

                    ft.Container(
                        ft.Text("Saldo Actual:", size=50, color="black", weight="bold"),
                        left=480,
                        top=55
                    ),
                ]),
                width=950, 
                bgcolor="#f2f2f3",
                expand=True,
                border_radius=5,
                padding=20,
            ),
            
            ft.Container(
                ft.Row([
                    ft.Image(src="time.gif", width=60, height=60),
                    ft.Text("Esperando tarjeta", size=50, color="black", weight="bold"),
                ], alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                bgcolor="#f2f2f3", 
                height=100,
                border_radius=5,  
            ),
        ],
        spacing=20 
        ),
        bgcolor="white",
        border_radius=10,
        padding=20,
        height=650
    )
    
    right_panel = ft.Container(
        content=ft.Column([
            ft.Container(
                ft.Image(src="seÃ±al.gif", width=450, height=450),
                alignment=ft.alignment.center,
                padding=25
            ),
            ft.Container(
                ft.Text("Posicione su tarjeta\nMetrox en el sensor", size=50, color="#B00020", weight="bold"),
                alignment=ft.alignment.center,
                bgcolor="#f2f2f3",
                height=70,
                border_radius=5,
                expand=True
            ),
        
        ]),
        bgcolor="white",
        border_radius=10,
        expand=True,
        padding=20
    )

    # ðŸ”· Fila principal: saldo + historial
    middle_section = ft.Row(
    controls=[
        # â¬…ï¸ Columna izquierda: left_panel + monedas
        ft.Column([
            left_panel,
            ft.Row(
                controls=[ft.Image(src="coins.png", width=550, height=550)],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        expand=True 
        ),

        # âž¡ï¸ Columna derecha: solo right_panel
        ft.Column([
            right_panel,
        ],
        expand=True
        )
    ],
    expand=True
    )
    
    # ðŸ“¦ Estructura vertical
    page.add(
        ft.Column(
            controls=[
                header,
                middle_section,
            ],
            expand=True  # Abarca toda la altura si se desea
        )
    )

ft.app(main)




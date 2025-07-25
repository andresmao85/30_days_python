import reflex as rx

config = rx.Config(
    app_name="my_app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
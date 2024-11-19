
from nicegui import ui, app

from OpenPostbud.pages import login

HORIZONTAL_RULE = '<hr style="width: 2px; height: 1.75rem; display: inline-block; background: white">'


def header():
    theme()

    with ui.header():
        logo = ui.label("📯 OpenPostbud 📯").classes("text-3xl text-bold cursor-pointer")
        logo.on("click", lambda: ui.navigate.to("/"))

        ui.link("Forside", "/").classes(replace='text-lg text-white')
        ui.html(HORIZONTAL_RULE)
        ui.link("Ny Forsendelse", "/send_post").classes(replace='text-lg text-white')
        ui.html(HORIZONTAL_RULE)
        ui.link("Forsendelser", "/forsendelser").classes(replace='text-lg text-white')
        ui.html(HORIZONTAL_RULE)
        ui.link("Tjek Tilmelding", "/tjek_tilmelding").classes(replace='text-lg text-white')

        ui.space()
        ui.label(app.storage.user['user_id']).classes('text-lg text-white')
        ui.button("Log Ud", on_click=login.logout, color="white").classes("text-primary")


def theme():
    ui.colors(primary="#cc0000")
    ui.input.default_props("filled")
    ui.textarea.default_props("filled")

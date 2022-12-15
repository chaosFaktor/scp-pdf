import ui
import shared



while True:
    ui.mainMenu()
    try:
        ui.mainMenu()
    except:
        shared.escape()
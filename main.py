import ui
import shared



while True:
    try:
        ui.mainMenu()
    except Exception as ex:
        raise ex
        shared.escape()

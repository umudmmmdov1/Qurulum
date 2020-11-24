from json import loads
from rich.prompt import Prompt
from . import logo, console, bilgi

def importlang ():
    console.clear()
    logo()
    bilgi("\n\[1] Azərbaycanca\n\[2] Türkçe\n\[3] English\n\[4] Pусский")
    Dil = Prompt.ask("[bold yellow]Xaiş bir dil seçin / Please select a language[/]", choices=["1", "2", "3", "4"], default="1")

    if Dil == "1":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "AZ"
        TZ = "Asia/Baku"
    elif Dil == "2":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "3":
        COUNTRY = "United Kingdom"
        LANGUAGE = "EN"
        TZ = "Europe/London"
    elif Dil == "4":
        COUNTRY = "Russia"
        LANGUAGE = "RU"
        TZ = "Asia/Moscow"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./dto_installer/language/{LANGUAGE}.dtojson", "r").read())["STRINGS"]

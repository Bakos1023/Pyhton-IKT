import json
import os
from fajl_foprogram import *
from foglalas_kezeles import *

# Szerepkör kezelés
def belepes():
    print("\nVálasszon szerepkört:")
    print("1. Vendég")
    print("2. Pincér")
    print("3. Ellenőr")
    valasztas = int(input("Adja meg a választását (1/2/3): ").strip())

    if valasztas == 1:
        return "vendeg"
    elif valasztas == 2:
        return "pincer"
    elif valasztas == 3:
        return "ellenor"
    else:
        print("Érvénytelen választás.")
        return belepes()

# Fájlba mentés
def mentes_foglalasok(foglalasok, fajlnev="foglalasok.json"):
    with open(fajlnev, "w", encoding="utf-8") as f:
        json.dump(foglalasok, f, ensure_ascii=False, indent=4)
    print("A foglalások sikeresen mentve lettek.")

# Fájl betöltése
def betoltes_foglalasok(fajlnev="foglalasok.json"):
    if os.path.exists(fajlnev):
        with open(fajlnev, "r", encoding="utf-8") as f:
            foglalasok = json.load(f)
        return foglalasok
    else:
        return []  # Ha nincs fájl, akkor üres listát adunk vissza

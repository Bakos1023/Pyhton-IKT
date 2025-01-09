
# mento.py modul
import os
from csaba_fo_program import *
from tibi_szerepkor import *
from vanda_foglalasok import *

def mentes_foglalasok(foglalasok, fajlnev="ellenor.txt"):
    # Foglalások mentése fájlba
    with open("ellenor.txt", "w", encoding="utf-8") as f:
        for foglalas in foglalasok:
            line = f"{foglalas['foglalas_szam']};{foglalas['nap']};{foglalas['ora']};{foglalas['meret']};{foglalas['fogyasztas'] if foglalas['fogyasztas'] is not None else ''}\n"
            f.write(line)
    print("A foglalások sikeresen mentve lettek.")

def betoltes_foglalasok(foglalasok, fajlnev="ellenor.txt"):
    # Foglalások betöltése fájlból
    foglalasok = []
    if os.path.exists(fajlnev):
        with open(fajlnev, "r", encoding="utf-8") as fajlnev:
            for line in fajlnev:
                szam, nap, ora, meret, fogyasztas = line.strip().split(';')
                foglalasok.append({
                    "foglalas_szam": int(szam),
                    "nap": nap,
                    "ora": int(ora),
                    "meret": int(meret),
                    "fogyasztas": float(fogyasztas) if fogyasztas else None
                })
    return foglalasok

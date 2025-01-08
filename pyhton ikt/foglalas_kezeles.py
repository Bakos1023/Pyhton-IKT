import json 
import os 
from fajl_foprogram import *
from  f_lista_szerepek_fogy import *

# Asztaltípusok és azok maximális kapacitásai
asztalok = {
    2: 10,  # 10 db 2 személyes asztal
    4: 5,   # 5 db 4 személyes asztal
    6: 3    # 3 db 6 személyes asztal
}
# Foglalás menedzselés
def uj_foglalas(foglalasok, nap, ora, meret):
    if not (10 <= ora <= 22):
        print("Hibás időpont. Csak 10 és 22 óra között foglalhat.")
        return

    if meret not in asztalok:
        print("Hibás asztalméret. Csak 2, 4 vagy 6 személyes asztal foglalható.")
        return

    if telthaz(foglalasok, nap, ora, meret):
        print("Sajnos az adott időpontra nincs szabad asztal.")
        return

    foglalasok.append({"foglalas_szam": len(foglalasok) + 1, "nap": nap, "ora": ora, "meret": meret, "fogyasztas": None})
    print("Foglalás sikeresen rögzítve.")

def telthaz(foglalasok, nap, ora, meret):
    foglalt = 0
    for foglalas in foglalasok:
        if foglalas["nap"] == nap and foglalas["ora"] == ora and foglalas["meret"] == meret:
            foglalt += 1
    
    max_foglalas = 0
    if meret in asztalok:
        max_foglalas = asztalok[meret]
    
    return foglalt >= max_foglalas

def foglalasok_listaja(foglalasok):
    print("\nFoglalások listája:")
    for foglalas in foglalasok:
        fogyasztas = "Nincs adat" if foglalas["fogyasztas"] is None else f"{foglalas['fogyasztas']} Ft"
        print(f"Foglalás szám: {foglalas['foglalas_szam']} - {foglalas['nap']} {foglalas['ora']} óra, {foglalas['meret']} személyes, Fogyasztás: {fogyasztas}")

def fogyasztas_hozzaadasa(foglalasok):
    foglalasok_listaja(foglalasok)
    index_input = input("Adja meg a foglalás számát, amelyhez fogyasztást szeretne hozzáadni: ").strip()
    
    # A bemenet validálásának eltávolítása
    index = int(index_input) - 1  # Mivel a lista indexelése 0-tól kezdődik, a foglalás szám 1-től indul
    
    if 0 <= index < len(foglalasok):
        fogyasztas = input("Adja meg a fogyasztás összegét (Ft): ").strip()
        foglalasok[index]["fogyasztas"] = float(fogyasztas)
        print("Fogyasztási összeg rögzítve.")
    else:
        print("Érvénytelen foglalás szám.")

def fogyasztasos_foglalasok(foglalasok):
    print("\nFoglalások fogyasztási összeggel:")
    for foglalas in foglalasok:
        if foglalas["fogyasztas"] is not None:
            print(f"Foglalás szám: {foglalas['foglalas_szam']} - {foglalas['nap']} {foglalas['ora']} óra, {foglalas['meret']} személyes, Fogyasztás: {foglalas['fogyasztas']} Ft")

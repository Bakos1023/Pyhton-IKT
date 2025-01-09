
import os
from csaba_fo_program import*
from tibi_szerepkor import*
from tibi_mento import*
# foglalasok.py modul

asztalok = {
    2: 10,  # 10 db 2 személyes asztal
    4: 5,   # 5 db 4 személyes asztal
    6: 3    # 3 db 6 személyes asztal
}

def uj_foglalas(foglalasok, nap, ora, meret):
    # Ellenőrzi az időpont érvényességét
    if not (10 <= ora <= 22):
        print("Hibás időpont. Csak 10 és 22 óra között foglalhat.")
        return

    # Ellenőrzi az asztalméret érvényességét
    if meret not in asztalok:
        print("Hibás asztalméret. Csak 2, 4 vagy 6 személyes asztal foglalható.")
        return

    # Teltház ellenőrzése
    if telthaz(foglalasok, nap, ora, meret):
        print("Sajnos az adott időpontra nincs szabad asztal.")
        return

    # Új foglalás hozzáadása
    foglalasok.append({"foglalas_szam": len(foglalasok) + 1, "nap": nap, "ora": ora, "meret": meret, "fogyasztas": None})
    print("Foglalás sikeresen rögzítve.")

def telthaz(foglalasok, nap, ora, meret):
    # Ellenőrzi, hogy az adott időpontra van-e szabad asztal
    foglalt = sum(1 for foglalas in foglalasok if foglalas["nap"] == nap and foglalas["ora"] == ora and foglalas["meret"] == meret)
    return foglalt >= asztalok.get(meret, 0)

def foglalasok_listaja(foglalasok):
    # Kilistázza az összes foglalást
    print("\nFoglalások listája:")
    for foglalas in foglalasok:
        fogyasztas = "Nincs adat" if foglalas["fogyasztas"] is None else f"{foglalas['fogyasztas']} Ft"
        print(f"Foglalás szám: {foglalas['foglalas_szam']} - {foglalas['nap']} {foglalas['ora']} óra, {foglalas['meret']} személyes, Fogyasztás: {fogyasztas}")

def fogyasztas_hozzaadasa(foglalasok):
    # Hozzáad egy fogyasztási összeget a foglaláshoz
    foglalasok_listaja(foglalasok)
    index = int(input("Adja meg a foglalás számát, amelyhez fogyasztást szeretne hozzáadni: ").strip()) - 1
    if 0 <= index < len(foglalasok):
        fogyasztas = float(input("Adja meg a fogyasztás összegét (Ft): ").strip())
        foglalasok[index]["fogyasztas"] = fogyasztas
        print("Fogyasztási összeg rögzítve.")
    else:
        print("Érvénytelen foglalás szám.")


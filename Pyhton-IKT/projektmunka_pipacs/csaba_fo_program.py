# fo_program.py
import os
from vanda_foglalasok import*
from tibi_mento import*
from tibi_szerepkor import*
from csaba_fo_program import*

def fogyasztasos_foglalasok(foglalasok):
    # Foglalások listázása fogyasztási összeggel és teljes összeg kiszámítása
    print("\nFoglalások fogyasztási összeggel:")
    teljesosszeg = 0
    for foglalas in foglalasok:
        if foglalas["fogyasztas"] is not None:
            print(f"Foglalás szám: {foglalas['foglalas_szam']} - {foglalas['nap']} {foglalas['ora']} óra, {foglalas['meret']} személyes, Fogyasztás: {foglalas['fogyasztas']} Ft")
            teljesosszeg += foglalas["fogyasztas"]
    borravalo = teljesosszeg * 0.15
    osszeg = teljesosszeg + borravalo
    print(f"\nÖsszes fogyasztás: {teljesosszeg:.2f} Ft")
    print(f"Szervizdíj (15%): {borravalo:.2f} Ft")
    print(f"Teljes összeg: {osszeg:.2f} Ft")

def fo_program():
    foglalasok = betoltes_foglalasok("ellenor.txt")
    while True:
        print("\nÉttermünk asztalfoglalási rendszere\n")
        szerepkor = belepes()
        if szerepkor == "vendeg":
            nap = input("Adja meg a napot (hétfő, kedd, szerda, csütörtök, péntek, szombat, vasárnap): ").strip().lower()
            ora = int(input("Adja meg az időpontot (10-22 óra között): ").strip())
            meret = int(input("Adja meg az asztal méretét (2, 4, 6 személyes): ").strip())
            uj_foglalas(foglalasok, nap, ora, meret)
        elif szerepkor == "pincer":
            fogyasztas_hozzaadasa(foglalasok)
        elif szerepkor == "ellenor":
            fogyasztasos_foglalasok(foglalasok)
        ujra = input("\nNyomjon Entert az újrakezdéshez, vagy írjon be bármit a kilépéshez: ").strip()
        if ujra:
            break
    mentes_foglalasok(foglalasok "ellenor.txt")

if __name__ == "__main__":
        fo_program()

# Fájlba mentés
import json
import os 
from foglalas_kezeles import *
from f_lista_szerepek_fogy import *

# Főprogram
def fo_program():
    foglalasok = betoltes_foglalasok()  # A foglalásokat a fájlból töltjük be

    while True:
        print("\nÉttermünk asztalfoglalási rendszere\n")
        szerepkor = belepes()

        if szerepkor == "vendeg":
            print("\nFoglalás indítása:")
            nap = input("Adja meg a napot - csak a zárójelben megadott formátumot tudjuk elfogadni (hétfő, kedd, szerda, csütörtök, péntek, szombat, vasárnap): ").strip().lower()
            ora = int(input("Adja meg az időpontot (10-22 óra között): ").strip())
            meret = int(input("Adja meg az asztal méretét (2, 4, 6 személyes): ").strip())
            uj_foglalas(foglalasok, nap, ora, meret)

        elif szerepkor == "pincer":
            print("\nFogyasztási összeg hozzáadása:")
            fogyasztas_hozzaadasa(foglalasok)

        elif szerepkor == "ellenor":
            print("\nEllenőrzési mód:")
            fogyasztasos_foglalasok(foglalasok)

        ujra = input("\nNyomjon Entert az újrakezdéshez, vagy írjon be bármit a kilépéshez: ").strip()
        if ujra != "":
            break

    mentes_foglalasok(foglalasok)  # A foglalásokat mentjük a program végén

fo_program()
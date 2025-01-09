
# szerepkor.py modul
from csaba_fo_program import *
from vanda_foglalasok import *
from tibi_mento import *

def belepes():
    # Szerepkör kiválasztása
    print("\nVálasszon szerepkört:")
    print("1. Vendég")
    print("2. Pincér")
    print("3. Ellenőr")
    valasztas = input("Adja meg a választását (1/2/3): ").strip()
    if valasztas == '1':
        return "vendeg"
    elif valasztas == '2':
        return "pincer"
    elif valasztas == '3':
        return "ellenor"
    else:
        print("Érvénytelen választás.")
        return belepes()

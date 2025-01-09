Bevezetés

Ez a dokumentum a Pipacs Étterem foglalási alkalmazásának követelmény specifikációja.

A dokumentum célja
A dokumentum teljeskörűen leírja az alkalmazás funkcionális működését. Bemutatja az alkalmazást használó felhasználói csoportokat.

Hatókör
A dokumentum a foglalási alkalmazás funkcióiról szól. Nem célunk a futtató számítógép és a rendszer egyéb hardver elemeinek bemutatása, sem a külső kapcsolódó rendszerek ismertetése sem.

Általános leírás
A Pipacs Étterem Budapest egyik legújabb étterem, ahol a nemzetközi gasztronómia tendenciáit követve kívánnak maradandó élményt nyújtani a betérő vendégeknek. A gördülékeny vendéglás érdekében készült ez az alkalmazás. A szoftver lehetővé teszi, hogy a vendégek egy adott hétre vonatkozóan előre tudjanak időpontot foglalni. A pincérek fogyasztást tudnak rögzíteni a foglalásokhoz. Az ellenőr pedig le tudja kérni a foglalásokhoz tartozó fogyasztásokat.

Definíciók, rövidítések
Vendég: - aki az alkalmazást használja
Pincér: - fogyasztást tud rögzíteni a foglaláshoz
Ellenőr: - le tudja kérni a foglaláshoz rögzített fogyasztásokat
Részletes funkcionális működés

Foglalási folyamat

1.	Indulás
o	A program a foglalás indításakor bekéri a felhasználó nevét, a foglalás napját, az időpontot és az asztalméretet.
o	A foglalási adatok ellenőrzése után a rendszer megvizsgálja, hogy a kért időpontra és asztalméretre van-e szabad kapacitás.
2.	Foglalás ellenőrzése és rögzítése
o	Ha a megadott időpontban és asztalméretben van szabad asztal, a foglalás sikeresen rögzítésre kerül, és a következő üzenet jelenik meg:
	„Kedves (név), szeretettel várjuk a foglalt időpontban.”
o	Ha nincs szabad asztal, a rendszer értesíti a felhasználót, és alternatív időpontokat ajánl fel az adott napon belül.

4.	Alternatív időpontok kezelése
o	A felhasználónak lehetősége van új időpontot megadni az ajánlott szabad időpontok közül.
o	Ha az új időpont is foglalt, a program ismételten visszatér az alternatív időpont ajánlásához.

Programspecifikus működés

1.	Asztalkapacitás kezelése
o	Az étterem asztalai különböző méretűek:
	2 személyes: 10 db
	4 személyes: 5 db
	6 személyes: 3 db
o	A foglalások során a rendszer figyelembe veszi az adott időpontban rendelkezésre álló szabad asztalok számát.

3.	Főbb funkciók
o	Új foglalás: A uj_foglalas függvény ellenőrzi az időpont és asztalméret érvényességét, valamint azt, hogy van-e elérhető kapacitás. Siker esetén a foglalás mentésre kerül.
o	Teltház ellenőrzése: A telthaz függvény összeveti a megadott időponthoz tartozó foglalások számát az asztaltípus maximális kapacitásával.
o	Foglalások listázása: A foglalasok_listaja függvény segítségével az összes foglalás áttekinthető.
o	Fogyasztási összeg rögzítése: A fogyasztas_hozzaadasa függvény lehetővé teszi a pincérek számára, hogy a vendégek fogyasztását rögzítsék.
o	Fogyasztási adatok ellenőrzése: A fogyasztasos_foglalasok függvény listázza azokat a foglalásokat, amelyekhez fogyasztási adat tartozik, ezeket összesiti és 15% szervizdíjjal megemeli.

5.	Felhasználói szerepkörök
o	Vendég: Új foglalást rögzíthet.
o	Pincér: Rögzítheti a vendégek fogyasztási összegét.
o	Ellenőr: Lekérdezheti az összes fogyasztási adatot tartalmazó foglalást.
6.	Adatok mentése és betöltése
o	A foglalásokat a program .txt formátumban menti, így az adatok a program újraindítása után is elérhetőek.

Felhasználói interakciók
•	A program folyamatos visszajelzéseket ad a felhasználóknak, például:
o	Érvényes foglalás esetén megerősítő üzenetet.
o	Hibás adatbevitel esetén figyelmeztetést, például „Hibás időpont” vagy „Nincs szabad asztal”.
•	A felhasználók választásai alapján a rendszer képes a folyamatot ismételten végrehajtani vagy a foglalásokat frissíteni.


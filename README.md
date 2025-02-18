# Házi Feladat Beküldési Útmutató

## Bevezetés

Ebben a kurzusban minden házi feladatot a GitHub Classroomon keresztül fogsz beküldeni. A következő útmutató segít neked a házi feladatok elkészítésében és beküldésében PyCharm IDE használatával.

## PyCharm Beállítása

1. **Klónozás PyCharm-ban**:
   - Nyisd meg a PyCharm-ot, majd válaszd a **"Get from Version Control"** lehetőséget.
   - Illeszd be a GitHub repozitóriumod URL-jét, amit a feladat elfogadása után kaptál.
   - Válaszd ki a mappát, ahova a repozitóriumot klónozni szeretnéd, majd kattints a **"Clone"** gombra (a default beállítás sokszor használható).

2. **Projekt beállítása**:
   - Miután a repozitóriumot klónoztad, a projekt automatikusan megnyílik PyCharm-ban.

## Feladat Megoldása

1. **Feladat implementálása**:
   - A feladatokat a `src` mappában találod. Ezekben vannak elkészítve a feladatok a függvények fejlécével együtt. Csak ezeket a fájlokat módosítsd, de a függvények neveit ne változtasd meg. 

2. **Tesztelés (opcionális)**:
   - A megoldásod helyességét tesztfájlokkal ellenőrizheted, amelyek a `tests/` mappában találhatóak.
   - A tesztek futtatásához kattints jobb egérgombbal a `tests/` mappára vagy a tesztfájlokra, és válaszd a **"Run 'pytest in tests'"** lehetőséget.
   - A tesztfájlokat ne változtasd meg!

## Beküldés

1. **Változtatások commitálása és pusholása**:
   - Miután befejezted a feladatot és a tesztek sikeresen lefutottak, commitáld a változtatásokat.
   - A commitáláshoz kattints a **"Commit"** gombra a bal felső sarokban, jelöld meg az összes fájlt, amelyben változásokat csináltál (valószínűleg csak egy ilyen fájl lesz, pl. assignment.py), írj egy rövid üzenetet (pl. "Feladat megoldva"), majd kattints a **"Commit and push"** gombra.
   - Ezzel a változásaid felkerülnek a GitHub repozitóriumba.

2. **Ellenőrzés**:
   - A pusholás után menj a GitHub repozitóriumod "Actions" fülére, ahol ellenőrizheted az automatikus tesztek eredményét.
   - A sikeres beküldésről és a tesztek eredményeiről itt kapsz visszajelzést.

## Gyakori Hibák és Megoldásuk

- **Commit elmaradt**: Győződj meg róla, hogy minden változtatásodat commitáltad, mielőtt pusholsz.
- **Push sikertelen**: Ellenőrizd az internetkapcsolatot, vagy próbáld meg újra a pusholást.
- **Teszt hibák**: Ha a tesztek hibát jeleznek, ellenőrizd a megoldásodat, majd commitáld és pushold újra a javításokat.

## További Segítség

- Ha bármilyen kérdésed vagy problémád merülne fel, kérj segítséget órán, vagy nézz utána online.

Sok sikert a munkához!

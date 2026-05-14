# Notesnik — Beležnica z GUI

Preprosta namizna aplikacija za pisanje in shranjevanje zapiskov, narejena v Pythonu s knjižnico tkinter.

---

## Kaj počne

Aplikacija ti omogoča ustvarjanje, urejanje in brisanje zapiskov z naslovom, vsebino in časovnim žigom. Zapiski so shranjeni lokalno v JSON datoteki in se ohranijo med zagoni programa.

---

## Funkcionalnosti

- Dodajanje novega zapiska z naslovom in vsebino
- Odpiranje in urejanje obstoječih zapiskov
- Brisanje zapiskov
- Samodejno shranjevanje ob vsakem zapisu ali izbrisu
- Zapiski so prikazani kot gumbi v mrežni postavitvi

---

## Shramba podatkov

Zapiski se samodejno shranijo v:

```
C:\Users\<tvoje_ime>\Documents\Notesnik\zapiski.json
```

Mapa se ustvari samodejno ob prvem zagonu, če še ne obstaja.

---

## Zahteve

- Python 3.x
- Knjižnica `tkinter` (vključena v standardno namestitev Pythona)

Nobenih dodatnih namestitev ni potrebno.

---

## Zagon

```bash
python NotesnikGUI.py
```

---

## Ikona (neobvezno)

Aplikacija poskuša naložiti ikono iz:

```
C:\python\Notesnik\fotke\zvezek.png
```

Če datoteka ne obstaja, se program zažene brez ikone brez napake.

---

## Prevajanje v .exe

Aplikacija je pripravljena za pakiranje v samostojno `.exe` datoteko s PyInstallerjem. Ukaz je že vključen kot komentar na dnu kode:

```bash
pyinstaller --onefile --windowed --icon="C:\python\Notesnik\ICON.ico" NotesnikGUI.py
```

- `--onefile` — vse pakira v eno `.exe` datoteko
- `--windowed` — skrije konzolno okno pri zagonu
- `--icon` — nastavi ikono aplikacije (pot do `.ico` datoteke)



> **Opomba:** Pred pakiranjem namesti PyInstaller z ukazom `pip install pyinstaller`.

---

## Odvisnosti

| Knjižnica | Namen |
|-----------|-------|
| `tkinter` | GUI — vgrajeno v Python |
| `json` | Shranjevanje zapiskov |
| `datetime` | Časovni žig ob shranjevanju |
| `os`, `sys` | Upravljanje poti in datotek |

---

## Licenca

MIT — uporabi kot želiš.

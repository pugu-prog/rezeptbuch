# Famill-Rezeptbuch – Anleitung für Claude

**Sprache der Rezepte und der Webseite: Lëtzebuergesch.** Rezepte, die in einer
anderen Sprache kommen (Deutsch, Französisch, Foto, Link …), auf Luxemburgisch
übertragen. Die JSON-Feldnamen bleiben wie unten (deutsch).

Dieses Repository ist das gemeinsame Rezeptbuch von **Guy, Louis und Jacques**.
Alle drei fügen Rezepte über ihren eigenen Claude-Zugang hinzu. Die Webseite
(GitHub Pages) baut sich nach jedem Push automatisch neu:
https://pugu-prog.github.io/rezeptbuch/

## Ein Rezept hinzufügen

1. **Eine Datei pro Rezept** in `rezepte/`, Dateiname = Slug des Titels:
   klein, ohne Umlaute/Sonderzeichen, Bindestriche statt Leerzeichen.
   Beispiel: „Bomi hire Kéiskuch“ → `rezepte/bomi-hire-keiskuch.json`.
   Vorher prüfen, ob es die Datei schon gibt – dann nicht überschreiben,
   sondern nachfragen (oder `-2` anhängen).
2. **Nur diese eine neue Datei** anlegen/ändern. Keine andere Datei anfassen
   (kein Index, keine Webseite) – der Index entsteht automatisch.
3. **Vorher checken:** das fertige Rezept dem Nutzer kurz zeigen und bestätigen
   lassen. Wenn lokal möglich, `python3 scripts/build_index.py` laufen lassen
   (prüft Format, Kategorie, Schwierigkeit).
4. Committen und pushen – am liebsten direkt auf `main`. In einer
   Cloud-Sitzung (claude.ai/code) einfach auf dem eigenen Branch pushen,
   **kein Pull Request nötig**: die Action `rezept-uebernehmen.yml` übernimmt
   Branches, die nur `rezepte/*.json` ändern, automatisch nach `main`. Commit-Nachricht: `Rezept: <Titel> (<Autor>)`.
5. Danach dem Nutzer den Link geben:
   `https://pugu-prog.github.io/rezeptbuch/#/rezept/<slug>`
   (ist nach ca. 1 Minute online).

Wer ist der Autor? Den Nutzer fragen, falls nicht klar: `Guy`, `Louis` oder `Jacques`.

## Format (JSON, UTF-8)

```json
{
  "titel": "Gromperekichelcher",
  "autor": "Guy",
  "kategorie": "Haaptplat",
  "portionen": 4,
  "zeit_minuten": 40,
  "schwierigkeit": "einfach",
  "tags": ["lëtzebuergesch", "vegetaresch"],
  "beschreibung": "Een oder zwee Sätz, ëm wat et geet.",
  "zutaten": [
    "1 kg mielzeg Gromperen",
    "2 Ënnen",
    { "gruppe": "Fir ze broden", "liste": ["Sonneblummenueleg"] }
  ],
  "schritte": [
    "Gromperen schielen a fein raffen.",
    "…"
  ],
  "tipps": "Optional: Tipps, Varianten.",
  "quelle": "Optional: Bomi / Buch / URL",
  "bild": "Optional: URL zu engem Foto",
  "hinzugefuegt": "2026-10-25"
}
```

Pflichtfelder: `titel`, `autor`, `kategorie`, `zutaten`, `schritte`.

- `kategorie` – genau eins von: `Fréistéck`, `Virspeis`, `Zopp`, `Zalot`,
  `Haaptplat`, `Bäilag`, `Dessert`, `Kuch & Gebäck`, `Snack`, `Gedrénks`, `Anescht`.
- `schwierigkeit` – `einfach`, `mëttel` oder `schwéier`.
- `zutaten` – Strings mit Menge vorne („200 g Miel“). Für Abschnitte
  (Deeg / Fëllung …) ein Objekt `{ "gruppe": "…", "liste": [ … ] }`.
- `schritte` – ein String pro Arbeitsschritt, ohne Nummer davor.
- `hinzugefuegt` – heutiges Datum, `JJJJ-MM-TT`.
- Unbekannte Felder weglassen statt leer lassen.

Wenn der Nutzer ein Foto, einen Screenshot, ein PDF oder eine Webseite
schickt: Rezept daraus abtippen, in dieses Format bringen, kurz zeigen und
dann committen. Bei Webrezepten die URL als `quelle` eintragen.

## Rezept ändern oder löschen

Bestehende Datei in `rezepte/` bearbeiten bzw. löschen. Commit-Nachricht:
`Rezept geändert: <Titel>` / `Rezept gelöscht: <Titel>`.
Rezepte anderer Familienmitglieder nur ändern, wenn der Nutzer es ausdrücklich will.

## Technik (nur zur Info)

- `index.html` – die Webseite (statisch, kein Build-Tool).
- `.github/workflows/pages.yml` – prüft alle JSON-Dateien, baut
  `rezepte.json` und veröffentlicht die Seite. Ist eine Datei ungültig,
  schlägt der Lauf fehl und die alte Version bleibt online.
- `scripts/build_index.py` – Prüfung + Index (lokal testbar:
  `python3 scripts/build_index.py`).

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
  "tipps": ["Optional: ein Tipp pro Eintrag", "Varianten …"],
  "notizen": [{ "autor": "Louis", "datum": "2026-10-26", "text": "Mit Chili noch besser." }],
  "quelle": "Optional: Bomi / Buch / URL",
  "bild": "bilder/gromperekichelcher.jpg",
  "hinzugefuegt": "2026-10-25"
}
```

Pflichtfelder: `titel`, `autor`, `kategorie`, `zutaten`, `schritte`.

- `kategorie` – genau einer der Namen aus `kategorien.json` (z. B. `Kaffi drénken`,
  `Haaptplat`, `Kuch & Gebäck`, `Gedrénks` …).
- `schwierigkeit` – `einfach`, `mëttel` oder `schwéier`.
- `zutaten` – Strings mit Menge vorne („200 g Miel“). Für Abschnitte
  (Deeg / Fëllung …) ein Objekt `{ "gruppe": "…", "liste": [ … ] }`.
- `schritte` – ein String pro Arbeitsschritt, ohne Nummer davor.
- `hinzugefuegt` – heutiges Datum, `JJJJ-MM-TT`.
- Unbekannte Felder weglassen statt leer lassen.

**Bilder:** Schickt der Nutzer ein Foto vom Gericht (oder ein Rezeptblatt mit
Bild), als `bilder/<slug>.jpg` speichern (gleicher Slug wie die Rezeptdatei,
lange Seite höchstens 1600 px, JPEG) und im Rezept `"bild": "bilder/<slug>.jpg"`
eintragen. Bild und Rezept im selben Commit. Ohne Foto das Feld weglassen.
Ein abfotografiertes Rezeptblatt/Zettel zusätzlich als
`bilder/<slug>-rezeptblat.jpg` speichern und `"rezeptblat"` setzen.
**Keine Bilder von fremden Webseiten verlinken** (z. B. Chefkoch blockiert das,
und die Rechte fehlen) – Bilder immer als Datei in `bilder/` speichern.
Fremde Fotos nur mit freier Lizenz (z. B. Wikimedia Commons CC0/CC BY) und
mit `"bild_quelle": "Foto: <Autor>, <Lizenz> – <URL>"`.

Wenn der Nutzer ein Foto, einen Screenshot, ein PDF oder eine Webseite
schickt: Rezept daraus abtippen, in dieses Format bringen, kurz zeigen und
dann committen. Bei Webrezepten die URL als `quelle` eintragen.

## Notizen & Verbesserungen zu Rezepten der anderen

Louis und Jacques (und Guy) sollen an allen Rezepten mitarbeiten können:

- **Notiz / Idee / Anmerkung** („mit Chili probiert, super“, „weniger Zucker reicht“):
  in der Rezeptdatei an die Liste `notizen` anhängen –
  `{ "autor": "<Name>", "datum": "<JJJJ-MM-TT>", "text": "<Notiz auf Lëtzebuergesch>" }`.
  Bestehende Notizen nie löschen oder umschreiben.
  Commit-Nachricht: `Notiz: <Titel> (<Autor>)`.
- **Verbesserung direkt im Rezept** (Menge, Schritt, Tipp ändern): nur wenn der
  Nutzer das ausdrücklich will. Dann die Änderung machen **und** zusätzlich eine
  Notiz anhängen, was geändert wurde und warum (z. B. „Zucker vun 200 op 150 g –
  Louis“), damit der ursprüngliche Autor es nachvollziehen kann.
  Commit-Nachricht: `Rezept verbessert: <Titel> (<Autor>)`.
- `autor` des Rezepts bleibt immer der ursprüngliche Autor.

## Sprachliche Korrekturen (Lëtzebuergesch)

Guy, Louis und Jacques dürfen **überall** sprachliche Korrekturen machen –
Rechtschreibung, Grammatik, besseres luxemburgisches Wort:

- **in Rezepten** (`rezepte/*.json`): auch in Rezepten der anderen, ohne
  nachzufragen. Nur die Sprache ändern, nicht Mengen/Inhalt. Keine Notiz nötig.
- **auf der Webseite** (`index.html`): nur sichtbare Texte ersetzen (Überschriften,
  Knöpfe, Anleitung „Matmaachen“) – kein Code, kein HTML-Umbau, kein Design.
  Achtung bei Apostrophen in JavaScript-Strings mit `'…'`: dort `’` verwenden.
- **Kategorien** (`kategorien.json`): Namen korrigieren; dann in allen Rezepten
  mit dieser Kategorie den Namen im selben Commit mitändern.
- Zuerst dem Nutzer eine kurze Liste „alt → neu“ zeigen und bestätigen lassen.
- Commit-Nachricht: `Korrektur: <was> (<Autor>)`.

Die Automatik übernimmt solche Branches nach einem Test (Seite lädt, alle
Rezepte erscheinen) selbst nach `main`.

## Rezept ändern oder löschen

Bestehende Datei in `rezepte/` bearbeiten bzw. löschen. Commit-Nachricht:
`Rezept geändert: <Titel>` / `Rezept gelöscht: <Titel>`.
Rezepte anderer Familienmitglieder löschen nur, wenn der ursprüngliche Autor einverstanden ist.

## Technik (nur zur Info)

- `index.html` – die Webseite (statisch, kein Build-Tool).
- `.github/workflows/pages.yml` – prüft alle JSON-Dateien, baut
  `rezepte.json` und veröffentlicht die Seite. Ist eine Datei ungültig,
  schlägt der Lauf fehl und die alte Version bleibt online.
- `scripts/build_index.py` – Prüfung + Index (lokal testbar:
  `python3 scripts/build_index.py`).

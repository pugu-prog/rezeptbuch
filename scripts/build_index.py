#!/usr/bin/env python3
"""Prüft alle Rezepte in rezepte/*.json und schreibt den Index nach <out>/rezepte.json."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KATEGORIEN = {"Frühstück", "Vorspeise", "Suppe", "Salat", "Hauptgericht", "Beilage",
              "Dessert", "Backen", "Snack", "Getränk", "Sonstiges"}
PFLICHT = ("titel", "autor", "kategorie", "zutaten", "schritte")


def pruefen(pfad, r):
    fehler = [f"Pflichtfeld fehlt: {f}" for f in PFLICHT if not r.get(f)]
    if r.get("kategorie") and r["kategorie"] not in KATEGORIEN:
        fehler.append(f"unbekannte Kategorie: {r['kategorie']}")
    if not isinstance(r.get("zutaten", []), list) or not isinstance(r.get("schritte", []), list):
        fehler.append("zutaten und schritte müssen Listen sein")
    return [f"{pfad.name}: {f}" for f in fehler]


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    rezepte, fehler = [], []
    for pfad in sorted((ROOT / "rezepte").glob("*.json")):
        try:
            r = json.loads(pfad.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fehler.append(f"{pfad.name}: ungültiges JSON ({e})")
            continue
        fehler += pruefen(pfad, r)
        r["slug"] = pfad.stem
        rezepte.append(r)
    if fehler:
        print("\n".join(fehler), file=sys.stderr)
        sys.exit(1)
    rezepte.sort(key=lambda r: r.get("hinzugefuegt", ""), reverse=True)
    out.mkdir(parents=True, exist_ok=True)
    (out / "rezepte.json").write_text(json.dumps(rezepte, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rezepte)} Rezepte -> {out / 'rezepte.json'}")


if __name__ == "__main__":
    main()

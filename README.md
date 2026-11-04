# Ginaa

Ginaa stands for "Ginaa is not an acronym." It's a desktop app that generates random things for D&D game masters.

## What it generates

- **NPCs:** name, suggested race and age, quirk, description, wants, secret, and what they're carrying. Lists cover general, small town, outskirts, and underdark settings. "Story" mode keeps an NPC's details consistent with each other; "chaotic" mode mixes them freely.
- **Taverns:** name, feel, and decor.
- **Items:** random, bad, and useless items.
- **Potions:** label, bottle, color, look, smell, taste, strength, effect, and an optional side effect.
- **Treasure:** filtered by rarity and category, with as many results as you ask for.
- **Traps:** mechanical, magical, or a chaotic mix.
- **Books:** title, color, condition, and smell, from several title lists.
- **Prophecies, wild magic effects, creepy and random occurrences, and combat spice.**

Use **Save** to write everything in the output window to a `.txt` file.

## Setup

Python 3 is required. A virtual environment is optional but recommended.

```
python -m venv venv
venv\Scripts\activate          (Windows)
source venv/bin/activate       (macOS / Linux)

pip install -r requirements.txt
```

## Run

From the root of the repo:

```
python ginaa.py
```

The UI is loaded directly from `raw_ui_files/ginaa_gui.ui` at runtime, so there is no separate UI build step. Edit that `.ui` file in Qt Designer to change the UI.

Each generator can also be run on its own from the repo root, for example:

```
python -m generators.npc_generator
```

## Build a standalone app

```
python scripts/build.py
```

This uses PyInstaller to build an app for the OS you run it on (`dist/Ginaa.exe` on Windows, `dist/Ginaa.app` on macOS, `dist/Ginaa` on Linux). PyInstaller can't cross-compile, so build on each OS you want to ship to.

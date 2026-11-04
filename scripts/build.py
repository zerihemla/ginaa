"""
Build Ginaa into a standalone, runnable app for the current OS using PyInstaller.

Usage (from the root of the ginaa directory):
    pip install -r requirements.txt
    python scripts/build.py        (Windows: python scripts\\build.py)

Output:
    Windows: dist/Ginaa.exe
    macOS:   dist/Ginaa.app
    Linux:   dist/Ginaa

PyInstaller can't cross-compile, so run this on each OS you want a build for.
"""

import os
import platform
import sys

# This script lives in <repo>/scripts/, so the repo root is one level up.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = "Ginaa"


def build():
    try:
        import PyInstaller.__main__
    except ImportError:
        sys.exit("PyInstaller is not installed. Run: pip install -r requirements.txt")

    ui_file = os.path.join(ROOT, "raw_ui_files", "ginaa_gui.ui")

    args = [
        os.path.join(ROOT, "ginaa.py"),
        "--name", APP_NAME,
        "--onefile",       # single runnable file
        "--windowed",      # no console window behind the GUI
        "--noconfirm",     # overwrite previous builds without asking
        "--clean",         # clear PyInstaller's cache before building
        "--distpath", os.path.join(ROOT, "dist"),
        "--workpath", os.path.join(ROOT, "build"),
        "--specpath", os.path.join(ROOT, "build"),
        # The .ui file is loaded at runtime, so bundle it with the app.
        "--add-data", f"{ui_file}{os.pathsep}raw_ui_files",
        # Make sure the project's own packages are found.
        "--paths", ROOT,
    ]

    print(f"Building {APP_NAME} for {platform.system()} ({platform.machine()})...")
    PyInstaller.__main__.run(args)

    ext = {"Windows": ".exe", "Darwin": ".app"}.get(platform.system(), "")
    print(f"\nDone! Your app is at: {os.path.join(ROOT, 'dist', APP_NAME + ext)}")


if __name__ == "__main__":
    build()

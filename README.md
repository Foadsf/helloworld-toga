# Toga Hello World

A minimal, cross-platform GUI application written in Python using [BeeWare/Toga](https://beeware.org/).

[![Release](https://github.com/Foadsf/helloworld/actions/workflows/release.yml/badge.svg)](https://github.com/Foadsf/helloworld/actions/workflows/release.yml)

## Project Structure


```
toga-hello/
├── .github/
│   └── workflows/
│       └── release.yml      # CI/CD for cross-platform builds
├── icons/
│   └── README.md            # Icon requirements
├── src/
│   └── helloworld/
│       ├── **init**.py      # Package marker
│       ├── **main**.py      # Execution entry point
│       └── app.py           # Main application logic
├── tests/
│   └── **init**.py
├── https://www.google.com/search?q=LICENSE
├── pyproject.toml           # Briefcase configuration
└── README.md
```

## Prerequisites (Linux Mint 22 / Ubuntu 24.04+)

This project relies on GTK bindings. **Note:** Ubuntu 24.04 and Linux Mint 22 have moved to `girepository-2.0`. You must install the correct development headers:

```bash
sudo apt update
sudo apt install -y git python3-dev python3-venv \
    libgirepository-2.0-dev \
    libcairo2-dev gir1.2-gtk-3.0 pkg-config
```

> **Legacy Systems:** If you are on Ubuntu 22.04 or older, use `libgirepository1.0-dev` instead.

## Installation

1. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```


2. **Install Briefcase (The packaging tool):**

```bash
pip install briefcase
```


3. **Install the project in editable mode:**
This ensures `briefcase` can find your code logic in `src/`.

```bash
pip install -e .
```



## Usage

### Run with Briefcase (Recommended)

This emulates the full packaging environment (icon handling, metadata, etc.).

```bash
briefcase dev
```

### Run directly (Quick Testing)

Since this is a standard Python package with a `__main__.py` entry point, you can also run it using standard Python modules:

```bash
python -m helloworld
```

## Packaging

To bundle this application for distribution, use `briefcase`.

### Local Builds

```bash
# Linux AppImage (Portable single-file executable)
briefcase create linux appimage
briefcase build linux appimage
briefcase package linux appimage

# Windows (Must run on Windows)
briefcase create windows app
briefcase build windows app
briefcase package windows app

# macOS (Must run on macOS)
briefcase create macOS app
briefcase build macOS app
briefcase package macOS app --adhoc-sign

# Android (Requires Android SDK - Briefcase handles this)
briefcase create android
briefcase build android
briefcase package android
```

### Automated Releases (CI/CD)

This repository includes a GitHub Action (`.github/workflows/release.yml`) that automatically builds binaries for Linux, Windows, macOS, and Android whenever you push a version tag.

1. **Commit your changes:**

```bash
git add .
git commit -m "Your commit message"
git push origin main
```


2. **Trigger a release:**

```bash
git tag -f v0.1.0
git push -f origin v0.1.0
```


*(Note: The `-f` force flag is useful if you are re-triggering the same version tag during testing).*

The workflow builds:

* **Linux:** `.AppImage` (portable)
* **Windows:** `.msi` installer
* **macOS:** `.dmg` disk image (ad-hoc signed)
* **Android:** Debug `.apk`
* **iOS:** Xcode project archive (for manual building)

## Code Signing Notes

| Platform | CI Default | Production Requirement |
| --- | --- | --- |
| **Linux** | Unsigned | None (AppImage is portable) |
| **Windows** | Unsigned | Code signing certificate ($200-500/yr) to remove "Unknown Publisher" warning. |
| **macOS** | Ad-hoc | Apple Developer ID ($99/yr) + Notarization is required to bypass Gatekeeper. |
| **Android** | Debug key | Release keystore (free, self-generated) for Play Store. |
| **iOS** | Build only | Apple Developer Program ($99/yr) required for `.ipa` creation. |

See `.github/workflows/release.yml` for secrets configuration details.

## License

MIT License - see [LICENSE](LICENSE) for details.

# Toga Hello World

A minimal, cross-platform GUI application written in Python using [BeeWare/Toga](https://beeware.org/).

## Prerequisites (Linux Mint 22 / Ubuntu 24.04)

This project relies on `girepository-2.0`. You must install the system development headers before installing the Python requirements.

```bash
sudo apt update
sudo apt install git python3-dev python3-venv \
    libgirepository-2.0-dev \
    libcairo2-dev gir1.2-gtk-3.0 pkg-config -y

```

## Installation

1. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate

```


2. **Install Python dependencies:**
```bash
pip install toga

```



## Usage

To run the application in developer mode:

```bash
python app.py

```

## Packaging

To bundle this application for distribution (AppImage, Android APK, etc.), you will need to install `briefcase` and run the build commands:

```bash
pip install briefcase
briefcase dev   # Runs in dev mode
briefcase create
briefcase build
briefcase run

```

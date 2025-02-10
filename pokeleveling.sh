#!/bin/bash

pyinstaller --clean --windowed --add-data "*.png;." pokeleveling.py

pyinstaller --onefile --clean --windowed --add-data "Assets/Background/*.png;Assets/Background" --add-data "Assets/Battle/*.png;Assets/Battle" --add-data "Assets/Foreground/*.png;Assets/Foreground" --add-data "Assets/Player/*.png;Assets/Player" --add-data "Assets/Pokemon/*.png;Assets/Pokemon" --add-data "Assets/Tiles/*.png;Assets/Tiles" pokeleveling.py
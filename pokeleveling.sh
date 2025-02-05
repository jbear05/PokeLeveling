#!/bin/bash

pyinstaller --onefile --clean --windowed --add-data "Assets\*.png:." game.py 2>&1 | tee build.log
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pokeleveling.py'],
    pathex=[],
    binaries=[],
    datas=[('Assets/Background/*.png', 'Assets/Background'), ('Assets/Battle/*.png', 'Assets/Battle'), ('Assets/Foreground/*.png', 'Assets/Foreground'), ('Assets/Player/*.png', 'Assets/Player'), ('Assets/Tiles/*.png', 'Assets/Tiles')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pokeleveling',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

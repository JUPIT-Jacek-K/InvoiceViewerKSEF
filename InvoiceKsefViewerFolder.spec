# -*- mode: python ; coding: utf-8 -*-
added_files = [
         ( 'Graphics\\Icons', 'Graphics\\Icons' ),
         ( 'KSEF_Wzory\\FA_1', 'KSEF_Wzory\\FA_1' ),
         ( 'KSEF_Wzory\\FA_2', 'KSEF_Wzory\\FA_2' ),
         ( 'KSEF_Wzory\\FA_3', 'KSEF_Wzory\\FA_3' ),
]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
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
    [],
    exclude_binaries=True,
    name='InvoiceKsefViewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    name='InvoiceKsefViewer',
)

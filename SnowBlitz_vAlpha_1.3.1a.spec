# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/home/rugerclaus/snowgame/main.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/rugerclaus/snowgame/font/*.ttf', 'font'), ('/home/rugerclaus/snowgame/images/*', 'images'), ('/home/rugerclaus/snowgame/sounds/*', 'sounds'), ('/home/rugerclaus/snowgame/entities/*', 'entities'), ('/home/rugerclaus/snowgame/FSM/*', 'FSM'), ('/home/rugerclaus/snowgame/ui/*', 'ui'), ('/home/rugerclaus/snowgame/menu.py', '.'), ('/home/rugerclaus/snowgame/main.py', '.'), ('/home/rugerclaus/snowgame/mode.py', '.'), ('/home/rugerclaus/snowgame/sound.py', '.'), ('/home/rugerclaus/snowgame/notes.txt', '.')],
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
    name='SnowBlitz_vAlpha_1.3.1a',
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

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['2048.py'],
             pathex=['D:\\python\\pycharm\\untitled\\Lib\\site-packages', 'C:\\Users\\28340\\Desktop\\游戏应用程序\\2048'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas +=[('2048.ico','C:\\Users\\28340\\Desktop\\游戏应用程序\\2048\\2048.ico','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('2048.ico','C:\\Users\\28340\\Desktop\\游戏应用程序\\2048\\2048.ico','DATA')],
          name='2048',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,icon='2048.ico' )

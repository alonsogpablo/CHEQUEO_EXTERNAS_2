# -*- mode: python -*-

block_cipher = None


a = Analysis(['CHEQUEA_EXTERNAS_HUA3G_RS_EN_RED_ERI3G.py'],
             pathex=['C:\\Users\\palonso0\\PycharmProjects\\CHEQUEO_EXTERNAS\\EXTERNAS EN ERI3G_PROD'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='CHEQUEA_EXTERNAS_HUA3G_RS_EN_RED_ERI3G',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='CHEQUEA_EXTERNAS_HUA3G_RS_EN_RED_ERI3G')

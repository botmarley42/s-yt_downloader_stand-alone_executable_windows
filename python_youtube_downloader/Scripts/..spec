# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['.'],
             pathex=['C:\\Users\\Marty\\Desktop\\python_youtube_downloader\\Scripts'],
             binaries=[],
             datas=[('C:/Users/Marty/AppData/Roaming/Python/Python37/Scripts/ffmpeg.exe', '. C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/yt_dl_gui.py C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/yt_resources.py -n Youtube_and_SoundCloudDownloader')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='.',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Marty\\PycharmProjects\\python_youtube_downloader\\youtube_downloader\\images\\youtube_dl_icon.ico')

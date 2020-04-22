# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/yt_dl_gui.py'],
             pathex=['C:\\Users\\Marty\\Desktop\\python_youtube_downloader\\Scripts'],
             binaries=[],
             datas=[('C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/icons/soundcloud-logo.png', '.'), ('C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/icons/youtube-logo.png', '.'), ('C:/Users/Marty/AppData/Roaming/Python/Python37/Scripts/ffmpeg.exe', '.'), ('C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/version.xml', '.')],
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
          name='yt_dl_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\Marty\\PycharmProjects\\python_youtube_downloader\\youtube_downloader\\icons\\youtube_dl_icon.ico', manifest='C:\\Users\\Marty\\PycharmProjects\\python_youtube_downloader\\youtube_downloader\\version.xml')

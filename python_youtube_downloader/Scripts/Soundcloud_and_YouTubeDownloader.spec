# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/yt_dl_gui.py'],
             pathex=['C:\\Users\\Marty\\Desktop\\s-yt_downloader_stand-alone_executable_windows\\python_youtube_downloader\\Scripts'],
             binaries=[],
             datas=[('C:/Users/Marty/PycharmProjects/python_youtube_downloader/youtube_downloader/ytdl_resources/ffmpeg.exe', '.')],
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
          name='Soundcloud_and_YoutubeDownloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , version='C:\\Users\\Marty\\Desktop\\soundcloud_and_yt_downloader_version_info.txt', icon='C:\\Users\\Marty\\PycharmProjects\\python_youtube_downloader\\youtube_downloader\\ytdl_resources\\youtube_dl_icon.ico')

# s-yt_downloader_stand-alone_executable_windows
A Soundcloud and Youtube Downloader stand-alone Executable for Windows

The Pyinstaller to freeze python packages into stand-alone executables, 
under Windows can be started by using the "python_youtube_downloader\Scripts\startpyinstaller.bat".
The Pyinstaller settings can be configured here.

The main python source code can be found in "youtube_downloader\yt_dl_gui.py"

The yt_resources.py file is a result of the Resource Compiler for PyQt5 and contains the logos of soundcloud etc. in
resource object code. The original resources like the logos .png, .icon etc. can be found in the "youtube_downloader\ytdl_resources" directory.

The "soundcloud_and_yt_downloader_version_info.txt" is used as a version file for the application in Windows. You can see those information if you view the details of the app.

used Python Version: 3.7.3

The following modules/plugins for python were used:

pyInstaller in Version 3.6

pyQt5 in Version 5.13.1

youtube_dl in Version/Commit 2020.03.24

This app is based on a different project from the user dstftw: https://github.com/ytdl-org/youtube-dl

All rights belong to the creator of this project.

FFMpeg is used to convert the .webm into .mp3: www.ffmpeg.org

ffmpeg version git-2019-10-19-31aafda


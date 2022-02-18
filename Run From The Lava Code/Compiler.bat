@echo off
title Pyinstaller Compiler - Start
echo Make sure pyinstaller,python,pip are installed.
echo Press any key to compile the main.py code.
pause >nul
title Pygame Compiler - Compiling
echo Wait
echo .
goto UserActions

:UserActions
set /p menu="Do You have pyinstaller? [Y/N]"
       if %menu%==Y goto compile
       if %menu%==y goto compile
       if %menu%==N goto DownloadPyinstaller
       if %menu%==n goto DownloadPyinstaller
       

:DownloadPyinstaller
echo waiting..
echo ....
echo ....
cls
pip install pyinstaller 
cls
pip3 install pyinstaller
cls
echo DONE!! press any key.
pause >nul
cls
goto compile

:compile
echo Press any key to compile
pause >nul
cls
pyinstaller -w --onefile main.py --windowed
cls
echo _
echo DONE!
echo _
echo Press any key to exit
pause >nul
exit

:: Terminai
:: AI running at terminal
@echo off
setlocal

set batfiledir=%~dp0
set appdir=%batfiledir:~0,-5%

:: ativar ambiente
set envdir=%appdir%\env\
if exist %envdir% (
    call %envdir%Scripts\activate.bat
)

:: src
set srcdir=%appdir%\src\
cd %srcdir%

:: app
set terminaipy=%srcdir%terminai.py
set arg1=%1
set arg2=%2

:: run terminai
python %terminaipy% %arg1% %arg2%

endlocal
:: Terminai
:: AI running at terminal
@echo off
setlocal

set currentdir=%cd%
set srcdir=%currentdir:~0,-4%\src\
cd %srcdir%
set terminaipy=%currentdir:~0,-4%\src\terminai.py
set arg1=%1
set arg2=%2
:: run terminai
python %terminaipy% %arg1% %arg2%

endlocal
@echo off
for /f "tokens=1,2 delims==" %%a in (config.ini) do (
if %%a==HasPython set haspython=%%b
)

if %haspython%==yes goto yes
echo make sure python 3.10 is installed for best results.
echo.
pause
cls
python Main.py
goto end

:yes
python Main.py

:end
pause
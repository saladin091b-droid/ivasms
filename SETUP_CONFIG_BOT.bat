@echo off
echo ========================================
echo   IVA SMS SELENIUM BOT LAUNCHER
echo ========================================
echo.

REM Check if credentials are set
findstr /C:"your_email@example.com" ivsms_auto.py >nul
if %errorlevel% == 0 (
    echo WARNING: Credentials not set!
    echo.
    echo Please run: python setup_credentials.py
    echo OR edit ivsms_auto.py manually
    echo.
    pause
    exit
)

echo Starting Selenium Bot...
echo Browser will open automatically
echo.
python setup_credentials.py
pause

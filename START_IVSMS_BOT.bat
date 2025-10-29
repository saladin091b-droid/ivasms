@echo off
echo ========================================
echo   IVA SMS SELENIUM BOT LAUNCHER
echo ========================================
echo.

REM Check if configuration is complete in ivsms_auto.py
set NEED_SETUP=0

REM Email placeholder
findstr /C:"EMAIL = \"your_email@example.com\"" ivsms_auto.py >nul && set NEED_SETUP=1

REM Password placeholder
findstr /C:"PASSWORD = \"your_password\"" ivsms_auto.py >nul && set NEED_SETUP=1

REM Telegram token placeholder
findstr /C:"BOT_TOKEN = \"your_bot_token\"" ivsms_auto.py >nul && set NEED_SETUP=1

REM Common default chat id example (adjust if you keep placeholder)
findstr /C:"CHAT_ID = -1001234567890" ivsms_auto.py >nul && set NEED_SETUP=1

if %NEED_SETUP%==1 (
    echo WARNING: Configuration not complete!
    echo.
    echo Please run:     python setup_credentials.py
    echo Or edit:        ivsms_auto.py  (set EMAIL, PASSWORD, BOT_TOKEN, ADMIN_ID, CHAT_ID)
    echo.
    pause
    exit /b 1
)

echo Config OK. Starting Selenium Bot...
echo Browser will open automatically
echo.
python ivsms_auto.py
echo.
echo Bot exited. Press any key to close.
pause >nul

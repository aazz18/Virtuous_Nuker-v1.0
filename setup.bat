@echo off
title VNuker Setup
color 0D

echo [~] Setting up your VNuker...
echo.

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Python is not installed. Please install Python 3.x from https://www.python.org/downloads/
    pause
    exit /b
)

echo [~] Upgrading pip...
python -m pip install --upgrade pip

echo [~] Installing required dependencies..
pip install discord.py
pip install pystyle

echo.
echo [+] Setup Complete!
echo.

pause

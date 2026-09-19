@echo off
title FLY CONTROL - Full Dependency Installer
color 0A

echo.
echo ============================================================
echo              FLY CONTROL - MODULE INSTALLER
echo ============================================================
echo.
echo This installer installs ALL Python modules used by the
echo original FLY CONTROL project, including:
echo.
echo  - DJI Tello / easyTello control
echo  - OpenCV and NumPy
echo  - Face detection
echo  - YOLO object recognition dependencies
echo  - Keyboard control
echo  - Voice control + microphone support
echo  - Colorama / ASCII terminal interface
echo  - Notification sounds
echo.
echo ============================================================
echo.

where py >nul 2>&1
if %errorlevel%==0 (
    set "PY=py"
) else (
    where python >nul 2>&1
    if %errorlevel%==0 (
        set "PY=python"
    ) else (
        echo [ERROR] Python was not found.
        echo Please install Python 3.9 or newer and enable
        echo "Add Python to PATH" during installation.
        echo.
        pause
        exit /b 1
    )
)

echo [1/4] Checking Python...
%PY% --version
if %errorlevel% neq 0 (
    echo [ERROR] Python could not be started.
    pause
    exit /b 1
)

echo.
echo [2/4] Upgrading pip, setuptools and wheel...
%PY% -m pip install --upgrade pip setuptools wheel
if %errorlevel% neq 0 (
    echo [WARNING] Package manager upgrade returned an error.
    echo Continuing with dependency installation...
)

echo.
echo [3/4] Installing ALL FLY CONTROL dependencies...
%PY% -m pip install -r "%~dp0requirements.txt"
if %errorlevel% neq 0 (
    echo.
    echo ============================================================
    echo [ERROR] Some packages could not be installed.
    echo ============================================================
    echo.
    echo Common causes:
    echo  - Unsupported Python version
    echo  - Internet connection problem
    echo  - Missing Microsoft C++ Build Tools
    echo  - Audio package installation problem
    echo.
    echo Try running this file again after fixing the issue.
    echo.
    pause
    exit /b 1
)

echo.
echo [4/4] Verifying the main modules...
%PY% -c "import cv2, numpy, colorama, art, keyboard, speech_recognition, djitellopy, easytello; print('Core modules: OK')"
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] One or more core imports failed.
    echo Check the error above.
) else (
    echo Core modules: OK
)

echo.
echo ============================================================
echo                  INSTALLATION COMPLETE
echo ============================================================
echo.
echo FLY CONTROL dependencies are installed.
echo.
echo Voice control:
echo   SpeechRecognition + PyAudio were installed through
echo   SpeechRecognition[audio].
echo.
echo Tello control:
echo   djitellopy + easytello installed.
echo.
echo You can now run the FLY CONTROL launcher/project.
echo.
pause

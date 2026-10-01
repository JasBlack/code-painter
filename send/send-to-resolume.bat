@echo off
rem Code Painter by JAS.BLACK - sender (Windows): offers the painting to Resolume (or any VJ app) as a Spout source
rem called "Code Painter". Double-click it, then switch on "send" in the studio's out panel. Close this window to stop.
rem The first time it sets itself up (a minute): it needs Python 3.9 or newer from python.org.
setlocal
cd /d "%~dp0"
if defined CP_SEND_VENV (set "VENV=%CP_SEND_VENV%") else (set "VENV=%LOCALAPPDATA%\code-painter-send")
if exist "%VENV%\Scripts\python.exe" "%VENV%\Scripts\python.exe" -c "import SpoutGL, websockets, PIL" >nul 2>&1 && goto run
set "PY="
where py >nul 2>&1 && set "PY=py -3"
if not defined PY where python >nul 2>&1 && set "PY=python"
if not defined PY (
  echo The sender needs Python 3.9 or newer: install it from https://www.python.org/downloads/
  echo ^(tick "Add python.exe to PATH"^), then double-click send-to-resolume.bat again.
  pause & exit /b 1
)
echo First run: setting up the sender (about a minute)...
if exist "%VENV%" rmdir /s /q "%VENV%"
%PY% -m venv "%VENV%" || goto fail
"%VENV%\Scripts\python.exe" -m pip install --upgrade --quiet pip
"%VENV%\Scripts\python.exe" -m pip install --quiet SpoutGL PyOpenGL websockets Pillow || goto fail
:run
"%VENV%\Scripts\python.exe" send-to-resolume.py %*
echo The sender stopped.
pause
exit /b 0
:fail
echo Setting up failed (see above). Check the internet connection and try again.
pause
exit /b 1

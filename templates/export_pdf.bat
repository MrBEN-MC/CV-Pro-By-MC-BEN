@echo off
setlocal
cd /d "%~dp0"
title CV High-Quality PDF Exporter (Windows)
echo ============================================================
echo CV High-Quality PDF Exporter (Windows & macOS Standard)
echo Target: ~1 MB to 3 MB Vector A4 PDFs
echo ============================================================
echo.

:: Try running Python if installed
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python export_pdf.py %*
    goto :done
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    py export_pdf.py %*
    goto :done
)

where python3 >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python3 export_pdf.py %*
    goto :done
)

echo Python is not detected in your PATH.
echo Looking for Microsoft Edge directly...

set "EDGE="
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" set "EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" set "EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if exist "%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe" set "EDGE=%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"

if defined EDGE (
    echo Found Microsoft Edge: %EDGE%
    echo Rendering templates to high-quality PDF...
    for %%F in (template_*.html) do (
        echo Converting %%F to PDF...
        "%EDGE%" --headless --disable-gpu --no-sandbox --run-all-compositor-stages-before-draw --print-to-pdf-no-header --print-to-pdf="%~dp0%%~nF.pdf" "file:///%~dp0%%F"
    )
    echo [DONE] All PDFs exported successfully.
) else (
    echo Could not locate Microsoft Edge or Python automatically.
    echo Please install Python 3 or Microsoft Edge.
)

:done
echo.
pause

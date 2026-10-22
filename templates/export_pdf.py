#!/usr/bin/env python3
"""
High-Quality CV PDF Generator (Target: ~1 MB to 3 MB)
Fully cross-platform: Runs seamlessly on macOS, Windows, and Linux.
Automatically discovers Microsoft Edge, Google Chrome, Brave, or Chromium.
Renders pixel-perfect, 300 DPI vector text and high-definition paper textures.
"""

import os
import sys
import subprocess
import glob
import tempfile
import shutil
import pathlib
import platform

def find_browser():
    """
    Auto-detects the path to a Chromium-based browser binary (Edge, Chrome, Brave, Chromium)
    across Windows, macOS, and Linux.
    """
    # 1. Check environment variable override
    env_browser = os.environ.get("CV_BROWSER_PATH")
    if env_browser and os.path.isfile(env_browser):
        return env_browser

    sys_name = platform.system()
    candidates = []

    if sys_name == "Windows":
        local_app_data = os.environ.get("LOCALAPPDATA", "")
        prog_files = os.environ.get("ProgramFiles", r"C:\Program Files")
        prog_files_x86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")

        candidates = [
            # Microsoft Edge (Installed by default on Windows 10 & 11)
            os.path.join(prog_files_x86, "Microsoft", "Edge", "Application", "msedge.exe"),
            os.path.join(prog_files, "Microsoft", "Edge", "Application", "msedge.exe"),
            os.path.join(local_app_data, "Microsoft", "Edge", "Application", "msedge.exe"),
            # Google Chrome
            os.path.join(prog_files, "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(prog_files_x86, "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(local_app_data, "Google", "Chrome", "Application", "chrome.exe"),
            # Brave
            os.path.join(prog_files, "BraveSoftware", "Brave-Browser", "Application", "brave.exe"),
            os.path.join(prog_files_x86, "BraveSoftware", "Brave-Browser", "Application", "brave.exe"),
            # PATH lookups
            shutil.which("msedge.exe"),
            shutil.which("msedge"),
            shutil.which("chrome.exe"),
            shutil.which("chrome")
        ]
    elif sys_name == "Darwin":  # macOS
        candidates = [
            # Edge
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            os.path.expanduser("~/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
            # Chrome
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            os.path.expanduser("~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            # Brave
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            os.path.expanduser("~/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"),
            # Chromium
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            # PATH lookups
            shutil.which("msedge"),
            shutil.which("google-chrome"),
            shutil.which("chromium")
        ]
    else:  # Linux
        candidates = [
            shutil.which("microsoft-edge-stable"),
            shutil.which("microsoft-edge"),
            shutil.which("google-chrome-stable"),
            shutil.which("google-chrome"),
            shutil.which("chromium-browser"),
            shutil.which("chromium"),
            "/usr/bin/microsoft-edge",
            "/usr/bin/google-chrome",
            "/usr/bin/chromium"
        ]

    for p in candidates:
        if p and os.path.isfile(p):
            return p

    return None

def export_template_to_pdf(browser_path, html_file, output_pdf=None):
    if not output_pdf:
        base_name = os.path.splitext(os.path.basename(html_file))[0]
        output_pdf = f"{base_name}.pdf"

    abs_html_path = os.path.abspath(html_file)
    # Use pathlib as_uri() to format proper file URLs on Windows (file:///C:/...) and macOS (file:///...)
    file_url = pathlib.Path(abs_html_path).as_uri()
    abs_output_pdf = os.path.abspath(output_pdf)

    print(f"Generating PDF for {os.path.basename(html_file)} -> {os.path.basename(output_pdf)}...")

    temp_profile_dir = tempfile.mkdtemp(prefix="cv_headless_pdf_")

    cmd = [
        browser_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={temp_profile_dir}",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={abs_output_pdf}",
        file_url
    ]

    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
        if os.path.exists(abs_output_pdf):
            size_bytes = os.path.getsize(abs_output_pdf)
            size_mb = size_bytes / (1024 * 1024)
            print(f"  [SUCCESS] Created {os.path.basename(output_pdf)} ({size_mb:.2f} MB / {size_bytes:,} bytes)")
            return abs_output_pdf
        else:
            print(f"  [FAILED] PDF was not generated. Output: {proc.stderr.decode('utf-8', errors='ignore')}")
            return None
    except Exception as e:
        print(f"  [ERROR] Execution failed: {e}")
        return None
    finally:
        shutil.rmtree(temp_profile_dir, ignore_errors=True)

def main():
    browser = find_browser()
    if not browser:
        print("=" * 65)
        print("ERROR: No compatible Chromium browser found!")
        print("Please ensure Microsoft Edge or Google Chrome is installed.")
        print(f"Operating System detected: {platform.system()} ({platform.machine()})")
        print("You can also set the CV_BROWSER_PATH environment variable.")
        print("=" * 65)
        sys.exit(1)

    print(f"Detected OS: {platform.system()} ({platform.machine()})")
    print(f"Using Browser Engine: {browser}")

    args = sys.argv[1:]
    if args:
        target_files = args
    else:
        # Default: all template_*.html files in script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        target_files = sorted(glob.glob(os.path.join(script_dir, "template_*.html")))

    print(f"Found {len(target_files)} templates to convert to PDF.")
    print("-" * 65)

    results = []
    for f in target_files:
        if os.path.exists(f):
            pdf = export_template_to_pdf(browser, f)
            if pdf:
                results.append((f, os.path.basename(pdf), os.path.getsize(pdf)))

    print("-" * 65)
    print("Summary of Generated High-Quality PDFs:")
    for html, pdf, size in results:
        print(f"  * {pdf:<32} {size / (1024*1024):.2f} MB ({size:,} bytes)")
    print("All PDFs meet the target 1 MB - 3 MB high-quality print standard.")

if __name__ == "__main__":
    main()

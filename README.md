# 📄 CV PRO by MC BEN — Controllable CV Architecture

> **A self-contained, privacy-first, zero-dependency CV design suite featuring 14 modern templates, live in-browser editor, dynamic category manager, custom photo controls, and high-resolution vector A4 PDF export.**

Inspired by modern, precision creative tools (like ArtCraft), **CV PRO** runs 100% in your browser. No Node.js, no servers, no databases, and no login or subscription required.

🌐 **Live Web Application (GitHub Pages):**  
[https://mrben-mc.github.io/CV-Pro-By-MC-BEN/](https://mrben-mc.github.io/CV-Pro-By-MC-BEN/)

---

## 🔒 100% Privacy & Zero-Leak Architecture

* **Zero Cloud Storage**: All CV editing, text modifications, and uploaded profile photos are processed **strictly inside your local browser memory (RAM / DOM)**.
* **No Database & No Signups**: No account, password, or login is ever required.
* **Zero Tracking**: Your personal information, work history, and contact details are never transmitted over the internet or saved on any server.

---

## ⚡ Key Features

* **14 Distinct Precision Designs**:
  * *Template 01*: Minimalist Classic (Dark sidebar, high contrast)
  * *Template 02*: Executive Legal (Refined serif, formal dividers)
  * *Template 03*: Editorial Warm (Asymmetric creative layout, warm tones)
  * *Template 04*: Corporate Blue Sidebar (Deep blue sidebar, structured timeline)
  * *Template 05*: Navy Top Banner (Prominent top header banner)
  * *Template 06*: Split Shaded Slate (Balanced two-tone reading rhythm)
  * *Template 07*: Europass Clean (European standard layout, completely watermark-free)
  * *Template 08*: Vibrant Modern Block (Dynamic block accents)
  * *Template 09*: Creative Studio (Bold agency layout, circular avatar spotlight)
  * *Template 10*: Tech Teal Matrix (Cyber teal accents, technical skills pills)
  * *Template 11*: Nordic Minimalist Navy (Scandinavian negative space, clean navy)
  * *Template 12*: Corporate Slate (Financial & banking structured format)
  * *Template 13*: Sage Elegance (Muted sage tones, luxury brand aesthetic)
  * *Template 14*: Modern Diagonal (Geometric diagonal accent cut, agile project structure)
* **Real-Time Visual Customizer**:
  * **Profile Photo Controls**: Toggle photo on/off, change shape (Circle, Rounded Rectangle, Passport, Square), zoom/scale, and pan/offset. Upload your own photo in 1-click.
  * **Theme & Color Customization**: Live hex color picker for primary accents, header backgrounds, sidebars, and paper textures.
  * **Auto-Contrast Protection Engine**: Automatically calculates background luminance to prevent unreadable text on dark or light themes.
  * **Typography & Spacing**: Adjust font families, sizes, margins, and line heights.
* **In-Place Slot & Category Management**:
  * **In-Place Add Slots (`[＋]`)**: Add extra skills (e.g. from 5 to 10+), bullet points under jobs/education, full job slots, and referee cards.
  * **Add & Remove Categories**: Add brand-new sections (e.g., *Certifications*, *Key Projects*, *Publications*, *Volunteer Work*) with `[＋ Add Category]`, or delete any section with `[✕ Remove Category]`.
  * **Item Deletion**: Hover and click red `[✕]` buttons to remove unwanted bullet points or slots.
* **Standalone Safe Saving**:
  * Customized CVs are saved as separate standalone HTML files in `saved_cvs/` or downloaded directly. Base templates remain pristine.
* **High-Resolution Vector PDF Export**:
  * Calibrated to standard **A4 (`210mm × 297mm`)** at 300 DPI vector quality (~1.4 MB to 1.6 MB).
  * Direct print from browser (`Ctrl+P` / `Cmd+P`) or batch script generation via headless Chromium.

---

## 💻 Running Locally

### On macOS / Linux
* **Option 1**: Double-click `templates/open_catalog.command`.
* **Option 2**: Open `index.html` in Chrome, Edge, Safari, or Firefox.

### On Windows
* **Option 1**: Double-click `templates\open_catalog.bat`.
* **Option 2**: Open `index.html` in any browser.

---

## 🖨️ PDF Export Methods

### Method 1: Instant In-Browser Export (Recommended)
1. Click **Print / PDF** on the top action bar or press `Ctrl + P` (Windows) / `Cmd + P` (macOS).
2. Set Destination to **Save as PDF**.
3. Set Paper Size to **A4**, Margins to **None / Default**, and enable **Background graphics**.
4. Click **Save**.

### Method 2: Batch Cross-Platform Script
To batch generate PDFs for all 14 templates at once:
* **Windows**: Double-click `templates\export_pdf.bat`.
* **macOS / Linux**: Run `./templates/export_pdf.sh` or `python3 templates/export_pdf.py`.

The script auto-detects Edge, Chrome, Brave, or Chromium across Windows, macOS, and Linux without requiring extra drivers.

---

## 📁 Repository Structure

```text
CV-Pro-By-MC-BEN/
├── index.html                   # ArtCraft-inspired homepage & template catalog
├── README.md                    # Documentation & guide
├── .gitignore                   # Safe production gitignore
├── .github/
│   └── workflows/
│       └── generate_pdfs.yml    # Automated GitHub Actions PDF build workflow
└── templates/                   # Self-contained template & engine suite
    ├── index.html               # Classic visual template selector
    ├── cv_customizer.js         # Production protected customizer & category engine
    ├── cv_customizer.css        # Customizer styles & @media print rules
    ├── dummy_profile.jpg        # Royalty-free avatar
    ├── paper_hd.jpg             # High-definition paper texture
    ├── export_pdf.py            # Cross-platform headless PDF generator
    ├── export_pdf.bat           # 1-click Windows PDF exporter
    ├── export_pdf.sh            # 1-click macOS/Linux PDF exporter
    ├── open_catalog.bat         # 1-click Windows catalog launcher
    ├── open_catalog.command     # 1-click macOS catalog launcher
    ├── template_01_minimalist.html .. template_14_diagonal_modern.html
    ├── template_01_minimalist.pdf .. template_14_diagonal_modern.pdf
    ├── thumb_template_01_minimalist.png .. thumb_template_14_diagonal_modern.png
    └── saved_cvs/
        └── .gitkeep
```

---

## 📄 License
MIT License. Free to use, adapt, and distribute for personal and professional CV generation.

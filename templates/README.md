# Professional CV Template & Customization Suite

A 100% self-contained, portable CV template system containing **14 professional CV designs** (12 modeled after sample portfolio screenshots plus 2 modernized corporate standards).

Anyone with this `templates/` folder can view, customize, edit, and export publication-ready A4 CVs offline without any external build tools or server dependencies.

---

## 🚀 Quick Start

1. **Browse All Designs**: Open [`index.html`](index.html) in any modern web browser (Edge, Chrome, Safari, Firefox) to view the visual catalog with high-resolution previews, category filters, and live search.
2. **Launch Interactive Studio**: Open [`cv_suite_pro.html`](cv_suite_pro.html) to preview all 14 templates in an interactive viewport with zoom controls and preset candidate switchers.
3. **Open Any Template Directly**: Double-click any `template_XX_*.html` file to open it in your browser with the full customization toolbar.

---

## 📁 Folder Contents

```text
templates/
├── index.html                       # Visual catalog & template selector
├── cv_suite_pro.html                # Master interactive studio with live preview switcher
├── cv_customizer.js                 # Core engine for photo tools, styling, editing & saving
├── cv_customizer.css                # Styling for customizer drawer and floating tools
├── dummy_profile.jpg                # Clean, neutral avatar silhouette (universal dummy)
├── paper_hd.jpg                     # High-definition 300 DPI texture for vector print output
├── export_pdf.py                    # Automated headless PDF exporter (1 MB – 3 MB standard)
├── saved_cvs/                       # Separate output directory for your customized CVs
│
├── template_01_minimalist.html/.pdf # 01: Minimalist Studio (Clean 2-Column)
├── template_02_executive_legal.html/.pdf # 02: Executive Legal (Centered Serif)
├── template_03_editorial_warm.html/.pdf  # 03: Warm Editorial (Beige Split)
├── template_04_blue_sidebar.html/.pdf   # 04: Blue Sidebar Modern (James Miller A)
├── template_05_navy_banner.html/.pdf    # 05: Navy Banner Header (James Miller B)
├── template_06_split_shaded.html/.pdf   # 06: Split Shaded Accent (James Miller C)
├── template_07_europass.html/.pdf       # 07: Europass Official (EU Standard)
├── template_08_vibrant_block.html/.pdf  # 08: Vibrant Block Header (Branding Block)
├── template_09_creative_studio.html/.pdf# 09: Creative Studio Bold (Charcoal Sidebar)
├── template_10_tech_teal.html/.pdf      # 10: Tech Teal Modern (Software & Cloud)
├── template_11_nordic_navy.html/.pdf    # 11: Nordic Navy Timeline (Connecting Nodes)
├── template_12_corporate_slate.html/.pdf# 12: Corporate Slate Executive (Mark Johnson Card)
├── template_13_sage_elegance.html/.pdf  # 13: Sage Green Elegance (Healthcare & Admin)
└── template_14_diagonal_modern.html/.pdf# 14: Diagonal Modern Header (CSS Polygon Clip)
```

---

## ✨ Features & Customization Capabilities

Every template includes a floating **Customization Toolbar** with a slide-out drawer:

### 1. 📷 Photo Controls & Visibility Box
- **Profile Picture Visibility Box**: Select `YES — Show Profile Picture` or `NO — Hide Profile Picture` from the dropdown, or use the quick top-bar button `[ 📷 Photo: Showing / Hidden ]`.
- **Photo Shape**: Switch between `Circle`, `Rounded Square`, `Soft Square`, `Square`, or `Pill`.
- **Photo Dimensions**: Adjust width & height sliders (80px – 180px).
- **Crop, Zoom & Positioning**: Zoom from 50% to 200% and pan horizontally / vertically (`Offset X` and `Offset Y`) to frame any portrait photo perfectly.
- **Custom Image Upload**: Click **Upload Image** to load your own photo instantly from your computer (stored in your browser session).

### 2. ✏️ Click-to-Edit HTML Text & Dynamic [+] Slots
- Click the **Edit Text** button in the top bar to activate Edit Mode:
  - **Inline Text Editing**: Click directly on any text (Name, Title, Summary, Company, Bullet points, Skills) to edit and reword.
  - **Dynamic `[＋]` Plus Buttons**:
    - **`[＋ Add Skill Slot]`**: Append new skill tags, pills, or percentage meter bars (e.g. expand from 5 skills to 10 skills).
    - **`[＋ Add Bullet Point]`**: Append extra bullet items ("subscriptions") to any job or education entry.
    - **`[＋ Add Experience Entry]`**: Append extra work experience blocks with formatted title, company, dates, and bullets.
    - **`[＋ Add Education Entry]`**: Append extra degrees or academic certificates.
    - **`[＋ Add Referee Card]`**: Append professional references with contact information.
  - **Category Management (Add & Remove Full Categories)**:
    - **`[ ＋ Add Category ]` Button**: In the top action bar and customizer drawer, click to add an entire new section (e.g. "Certifications", "Projects", "Publications", "Awards", "Volunteer Work") with formatted sub-entries and bullet points.
    - **`[ ✕ Remove Category ]` Buttons**: In Edit Mode, hover over any category header (e.g. References, Languages, Skills, Education, or any custom category) to see the red `[✕ Remove Category]` button. Clicking it removes the entire category and its contents cleanly from the CV.
    - **Drawer Category Manager**: Manage and remove all active categories from the **Save & Data** tab in the Customizer Drawer.
  - **`[ ＋ Add Text Box ]` Top Menu**: Quick dropdown button in the top action bar to insert a standalone custom text box (Title + Description) or any content block anywhere on the page.
  - **Delete `[×]` Buttons**: Hover over any item (experience block, bullet, skill, education entry, referee card, or custom text box) and click the red `[×]` button to delete it instantly.
  - **Print & View Safe**: All `[＋]` buttons, delete `[×]` buttons, and category controls are completely hidden during normal view and high-res PDF export (`display: none !important`).

### 3. 🎨 Colors, Auto-Contrast & Background Themes
- **Auto-Contrast Protection Engine**: Automatically analyzes the background luminance of sidebars and banners. When dark colors are selected (e.g., templates 08, 09, 10, 11), text dynamically adapts to crisp high-contrast white and soft light gray. When light colors are selected, text dynamically shifts to deep slate charcoal so text is **always 100% readable**.
- **Template-Native Defaults**: Each template preserves its authentic, professionally designed palette upon load.
- **Primary & Secondary Accent Colors**: Live color pickers for headings, dates, borders, and icons.
- **Sidebar & Page Backgrounds**: Customize sidebar tint and main body background with live swatches or native hex picker.
- **Paper Texture**: Toggle subtle 300 DPI high-definition paper texture with adjustable opacity.

### 4. 🔤 Typography & Font Sizes
- **8 Professional Google Fonts**: Switch between `Inter`, `Roboto`, `Open Sans`, `Lato`, `Merriweather`, `Playfair Display`, `Oswald`, and `Montserrat`.
- **Font Sizes**: Adjust Base Text (10px – 16px), Section Headings (12px – 22px), and Candidate Name (20px – 44px).
- **Line Height**: Fine-tune line spacing (1.2 – 2.0).

### 5. 👥 Universal Dummy Dataset Presets
Quickly populate any template with realistic sample data using the preset dropdown:
- **Alex Morgan**: Senior Operations & Project Lead
- **Jordan Reed**: Senior Full-Stack Software Engineer
- **Taylor Bailey**: Creative Art Director & Brand Strategist
- **Morgan Vance**: Senior Corporate Counsel & Regulatory Director

---

## 💾 Saving Without Overwriting Templates

- When you click **Save Standalone File (saved_cvs/)**, the system packages your customized CV (including your edited text, photo settings, colors, and fonts) and downloads a standalone copy (e.g. `saved_cvs/my_custom_cv.html`).
- **The original template files are never modified**, ensuring you can always create new CVs from clean originals.
- Your personal customizations are also safely remembered in your browser's local storage.

---

## 🖨️ High-Quality PDF Export (1 MB – 3 MB Standard)

All templates are strictly calibrated for single-page A4 printing (`210mm × 297mm`) with 300 DPI vector text and texture rendering.

### Method A: Browser Print (Instant on macOS & Windows)
1. In any template, click the green **Print / PDF** button in the top bar (or press `Ctrl+P` on Windows / `Cmd+P` on Mac).
2. Set Destination to **Save as PDF**.
3. Under **More Settings**:
   - Paper size: **A4**
   - Margins: **None**
   - Background graphics: **Checked** (Enabled)
4. Click **Save**.

### Method B: Headless Vector Exporter (`export_pdf.py`)
Fully cross-platform for **macOS**, **Windows**, and **Linux**. It automatically detects whichever browser is installed (Microsoft Edge, Google Chrome, Brave, or Chromium):

- **On Windows**:
  - Simply double-click `export_pdf.bat`!
  - Or in Command Prompt / PowerShell:
    ```cmd
    python export_pdf.py
    ```
- **On macOS / Linux**:
  - In Terminal:
    ```bash
    ./export_pdf.sh
    # Or:
    python3 export_pdf.py
    ```
All generated PDFs strictly adhere to the high-definition print standard of **1.44 MB – 1.57 MB**.

---

## 🖥️ Cross-Platform 1-Click Launchers

| Operating System | How to Browse Catalog | How to Export PDFs |
| :--- | :--- | :--- |
| **Windows** | Double-click `open_catalog.bat` (or open `index.html`) | Double-click `export_pdf.bat` |
| **macOS** | Double-click `open_catalog.command` (or open `index.html`) | Run `./export_pdf.sh` or `python3 export_pdf.py` |
| **Linux** | Open `index.html` in browser | Run `python3 export_pdf.py` |

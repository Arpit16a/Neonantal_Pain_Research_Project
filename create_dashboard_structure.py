
from pathlib import Path
import shutil

# Run this script from the main research project folder
ROOT = Path.cwd()
DASHBOARD = ROOT / "neopain-dashboard"

# 1. Create directories
folders = [
    "pages",
    "components",
    "data",
    "assets/figures",
]

for folder in folders:
    (DASHBOARD / folder).mkdir(parents=True, exist_ok=True)

# 2. Create starter Python files
files = {
    "app.py": "# Main Streamlit application\n",
    "pages/1_Performance.py": "# Model performance page\n",
    "pages/2_Methodology.py": "# Research methodology page\n",
    "pages/3_Subject_Demonstration.py": "# Subject-wise demonstration page\n",
    "components/__init__.py": "",
    "components/metric_cards.py": "# Metric card components\n",
    "components/charts.py": "# Chart components\n",
    "components/explanations.py": "# Research explanations\n",
    "requirements.txt": "streamlit\npandas\nnumpy\nplotly\nscikit-learn\nxgboost\n",
}

for filename, content in files.items():
    path = DASHBOARD / filename
    if not path.exists():
        path.write_text(content, encoding="utf-8")

# 3. Copy existing verified evaluation CSVs
source = ROOT / "results" / "reviewer1"

csv_files = [
    "reviewer1_summary_statistics.csv",
    "pooled_auc_summary.csv",
    "all_per_subject_metrics.csv",
]

for filename in csv_files:
    src = source / filename
    dest = DASHBOARD / "data" / filename

    if src.exists():
        shutil.copy2(src, dest)
        print(f"Copied: {filename}")
    else:
        print(f"Not found: {src}")

# 4. Copy existing research figures
figure_source = ROOT / "outputs" / "figures" / "paper_figures"
figure_destination = DASHBOARD / "assets" / "figures"

if figure_source.exists():
    for image_file in figure_source.iterdir():
        if image_file.is_file():
            shutil.copy2(image_file, figure_destination / image_file.name)

# 5. Add a note about the future prediction file
readme = DASHBOARD / "data" / "README.txt"
readme.write_text(
    "This folder contains research evaluation outputs.\n"
    "oof_predictions.csv will be generated later from the verified "
    "LOSO evaluation pipeline.\n"
    "Do not create or enter fabricated predictions.\n",
    encoding="utf-8"
)

print("\nDashboard structure created successfully!")
print(f"Location: {DASHBOARD}")

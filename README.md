# Task_04_Descriptive_Stats

This project is part of Research Task 04 and focuses on performing **Descriptive Statistical Analysis** using three different approaches: **Pure Python**, **Pandas**, and **Polars**.

The goal is to analyze datasets related to social media (Facebook posts, Facebook ads, Twitter posts) and generate meaningful summaries for further research.

---

## 📂 Project Structure

```
Task_04_Descriptive_Stats/
│
├── datasets/                 # Contains input CSV datasets (ignored by Git)
├── results/                  # Stores output summary JSON files (ignored by Git)
├── plots/                    # Stores plots generated from visualizations
│
├── Pure_Python_Stats.py      # Descriptive stats using pure Python
├── Pandas_Stats.py           # Descriptive stats using pandas
├── polars_stats.py           # Descriptive stats using polars
├── visualizations.py         # Generates visualizations from JSON summaries
├── .gitignore                # Prevents large/generated files from being pushed
└── README.md                 # Project documentation
```

---

## ⚙️ How to Run

1. Place your CSV datasets in the `datasets/` folder.
2. Run the analysis script of your choice:

```bash
python Pure_Python_Stats.py
python Pandas_Stats.py
python polars_stats.py
```

3. Run `visualizations.py` to generate plots from the output summaries.

```bash
python visualizations.py
```

---

## 📊 Outputs

- Summary files are saved in the `results/` folder in JSON format.
- Plots are saved in the `plots/` folder as PNG images.

Example output files:
- `fb_ads_summary.json`
- `fb_posts_pandas_summary.json`
- `tw_posts_polars_summary.json`

---

## 🛡️ .gitignore Explanation

The `.gitignore` file is used to **exclude large result files and datasets** from being tracked in Git. This prevents repository size issues and keeps only essential code.

### Ignored Paths:
```
datasets/
results/*.json
```

GitHub restricts uploads of files larger than 100MB, and one of the result files (`fb_ads_summary.json`) was ~2GB. So it's essential these are ignored in version control.

---

## 👩‍💻 Author

**Aakanksha Sonawane**  
M.S. Information Systems | Syracuse University

---

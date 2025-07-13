import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os




# === Setup ===
sns.set_theme(style="whitegrid")
os.makedirs("plots", exist_ok=True)

# === Load Datasets ===
base_path = "datasets"

files = {
    "fb_ads": f"{base_path}/2024_fb_ads_president_scored_anon.csv",
    "fb_posts": f"{base_path}/2024_fb_posts_president_scored_anon.csv",
    "tw_posts": f"{base_path}/2024_tw_posts_president_scored_anon.csv"
}

# === Plotting Functions ===
def plot_histogram(df, col, name):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[col].dropna(), bins=30, kde=True)
    plt.title(f"Histogram of {col} ({name})")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"plots/{name}_{col}_histogram.png")
    plt.close()

def plot_boxplot(df, x, y, name):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f"{y} by {x} ({name})")
    plt.tight_layout()
    plt.savefig(f"plots/{name}_{x}_vs_{y}_boxplot.png")
    plt.close()

def plot_top_categories(df, col, name):
    top = df[col].value_counts().head(10)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top.values, y=top.index)
    plt.title(f"Top 10 {col} values ({name})")
    plt.xlabel("Count")
    plt.ylabel(col)
    plt.tight_layout()
    plt.savefig(f"plots/{name}_{col}_top_categories.png")
    plt.close()

# === Main Loop ===
for name, path in files.items():
    print(f"📊 Visualizing {name}")
    df = pd.read_csv(path)

    # Skip large datasets or unknown types for now
    numeric_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(include="object").columns

    # Histograms for numeric columns
    for col in numeric_cols[:3]:  # limit to top 3
        plot_histogram(df, col, name)

    # Boxplot (if candidate and spend/impression type fields exist)
    if "candidate" in df.columns and "spend" in df.columns:
        plot_boxplot(df[df["spend"].notnull()], "candidate", "spend", name)

    # Top categories for categorical columns
    for col in cat_cols[:2]:  # limit to top 2
        plot_top_categories(df, col, name)

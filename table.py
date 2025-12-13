import pandas as pd

df = pd.read_csv("data/league_clean.csv")
df.head().to_html(
    "assets/league_clean_head.html",
    index=False
)

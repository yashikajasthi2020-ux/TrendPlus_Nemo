import pandas as pd
import numpy as np

df = pd.read_csv("trends_clean.csv")

print(df.info())
print(df.describe())
print(df.isnull().sum())

print(df["categories"].value_counts())

print("Average score:", df["score"].mean())

print("Highest score:")
print(df.loc[df["score"].idxmax()])

top_5 = df.nlargest(5, "score")
print(top_5)

category_avg = df.groupby("categories")["score"].mean().sort_values(ascending=False)
print(category_avg)

category_count = df["categories"].value_counts()
print(category_count)

category_avg.to_csv("category_average_scores.csv")

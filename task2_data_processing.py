import pandas as pd

df = pd.read_json("data/Data Trends 2024-04-11-5.json")

print("Rows loaded:", len(df))

df = df.drop_duplicates("post_id")
print("After duplicates:", len(df))

df = df.dropna(subset=["post_id", "title", "score"])
print("After nulls:", len(df))

df["score"] = df["score"].astype(int)
df["number_of_comments"] = df["number_of_comments"].astype(int)

df = df[df["score"] >= 5]
print("After low score:", len(df))

df["title"] = df["title"].str.strip()

df.to_csv("data/trends_clean.csv", index=False)

print("Saved rows:", len(df))
print(df["category"].value_counts())

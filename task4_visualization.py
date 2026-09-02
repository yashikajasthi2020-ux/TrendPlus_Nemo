import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("trends_clean.csv")

os.makedirs("Outputs", exist_ok=True)


top10 = df.nlargest(10, "score")

plt.figure(figsize=(10, 6))
plt.barh(top10["title"], top10["score"])
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("Outputs/chart1_Top Stories.png")
plt.show()
plt.close()


category_count = df["category"].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(category_count.index, category_count.values)
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Outputs/chart2_Category.png")
plt.show()
plt.close()


median_score = df["score"].median()
df["is_popular"] = df["score"] >= median_sco
plt.figure(figsize=(10, 6))

popular = df[df["is_popular"]]
not_popular = df[~df["is_popular"]]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Non-Popular")

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()
plt.tight_layout()
plt.savefig("Outputs/chart3_Scatter.png")
plt.show()
plt.close()


fig, axes = plt.subplots(2, 2, figsize=(16, 10))

axes[0, 0].barh(top10["title"], top10["score"])
axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")
axes[0, 0].invert_yaxis()

axes[0, 1].bar(category_count.index, category_count.values)
axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")
axes[0, 1].tick_params(axis="x", rotation=45)

axes[1, 0].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[1, 0].scatter(not_popular["score"], not_popular["num_comments"], label="Non-Popular")
axes[1, 0].set_title("Score vs Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].legend()

axes[1, 1].axis("off")

fig.suptitle("TrendPlus Dashboard")
plt.tight_layout()
plt.savefig("Outputs/dashboard.png")
plt.show()
plt.close()

print("Task 4 charts and dashboard saved successfully!")

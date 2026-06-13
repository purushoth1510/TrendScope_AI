import pandas as pd

sales = pd.read_csv("datasets/processed/processed_sales.csv")

sales["AI_Score"] = (
    sales["Sales"] * 0.7 +
    sales["Profit"] * 0.3
)
def recommendation_label(score):
    if score > 5000:
        return "Strong Buy"
    elif score > 2000:
        return "Buy"
    elif score > 500:
        return "Watch"
    else:
        return "Avoid"

sales["Recommendation"] = sales["AI_Score"].apply(
    recommendation_label
)

recommendations = (
    sales[
        [
    "Product Name",
    "Category",
    "Sales",
    "Profit",
    "AI_Score",
    "Recommendation"
]
    ]
    .sort_values("AI_Score", ascending=False)
    .head(20)
)

print(recommendations)

recommendations.to_csv(
    "reports/recommendations.csv",
    index=False
)

print("\nRecommendations saved successfully!")
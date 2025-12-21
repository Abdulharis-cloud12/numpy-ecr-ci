import pandas as pd
import numpy as np

df = pd.read_csv("sales_data.csv")

if df.empty:
    raise ValueError("CSV file is empty")

numeric_df = df.select_dtypes(include=[np.number])

summary = {
    "rows": len(df),
    "columns": len(df.columns),
    "mean": numeric_df.mean().to_dict(),
    "max": numeric_df.max().to_dict(),
    "min": numeric_df.min().to_dict()
}

print("Data Summary:")
for key, value in summary.items():
    print(f"{key}: {value}")

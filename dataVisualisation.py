import pandas as pd

DATA_PATH = "./data/oasis_cross-sectional-5708aa0a98d82080.xlsx"

# We let pandas infer types; for this dataset it usually does the right thing.
data = pd.read_excel(DATA_PATH)

print("Raw data shape:", data.shape)
print("Columns:", data.columns.tolist())
print(data.head())


import pandas as pd
import os


df = pd.read_csv("_data/aggregate.csv")
df = df.rename(columns=lambda x: x.strip())
print(list(df))

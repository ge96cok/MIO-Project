import pandas as pd
import numpy as np

df = pd.read_csv("results.csv")

df["Best of"] = df.max(axis=1)

# repeat for all algs we compare

df["Dev Alg1"] = (df["Best of"] - df["of"])/df["Best of"]*100

df["# best 1"] = np.where(df["Best of"] == df['of'], 1, 0)

print(df)
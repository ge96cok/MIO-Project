import pandas as pd
import numpy as np

df = pd.read_csv("results.csv")

#df["Best of"] = df.max(axis=1)

# repeat for all algs we compare

#df["Dev Alg1"] = (df["Best of"] - df["of"])/df["Best of"]*100

#df["# best 1"] = np.where(df["Best of"] == df['of'], 1, 0)

#print(df)

freq = [0,0.05,0.1,0.2,0.3]
for f in freq:
    df = pd.read_csv("pr_test500.csv")
    df = df[df.freq == str(f)]
    df["of"] = pd.to_numeric(df["of"])
    df["runtime"] = pd.to_numeric(df["runtime"])
    print("freq " + str(f) + ": of: " + str(df.of.mean()) + ", runtime: " + str(df.runtime.mean()))


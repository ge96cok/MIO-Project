import pandas as pd
import numpy as np

df = pd.read_csv("results25itersAGAIN.csv")
df = df._get_numeric_data()
df = df.sort_values(by=["GRASPMOD_of"])

df["Best of"] = df.max(axis=1)

# repeat for all algs we compare
algs = ["GRASP", "GRASPMOD", "PR1", "PR2", "PR3", "PR4"]
#algs = ["GRASPMOD", "PR5"]

for a in algs:
    df["Dev "+a] = (df["Best of"] - df[a+"_of"])/df["Best of"]*100
    df["# best "+a] = np.where(df["Best of"] == df[a+"_of"], 1, 0)

# split n=100 and n=500
dfs = np.split(df, [6], axis=0)

for d in dfs:
    of = []
    runtime = []
    dev = []
    best = []
    for a in algs:
        of.append(d[a+"_of"].mean())
        runtime.append(d[a+"_runtime (s)"].mean())
        dev.append(d["Dev "+a].mean())
        best.append(d["# best "+a].mean())
    data = pd.DataFrame([])
    data["algorithm"] = algs
    data["of"] = of
    data["run time (s)"] = runtime
    data["dev"] = dev
    data["rel best of"] = best

    print(data.to_latex(index=False, formatters={"name": str.upper}, float_format="{:.2f}".format))

# for frequency parameter analysis
freq = [0,0.05,0.1,0.2,0.3]
of = []
runtime = []
for f in freq:
    df = pd.read_csv("pr_test500.csv")
    df = df[df.freq == str(f)]
    df["of"] = pd.to_numeric(df["of"])
    df["runtime"] = pd.to_numeric(df["runtime"])
    of.append(round(df.of.mean(), 2))
    runtime.append(round(df.runtime.mean(), 2))

res = pd.DataFrame([])
res["frequency"] = freq
res["of"] = of
res["runtime (s)"] = runtime

#print(res.to_latex(index=False, formatters={"name": str.upper}, float_format="{:.2f}".format))

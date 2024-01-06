import pandas as pd
import numpy as np

df = pd.read_csv("results80itersAGAIN.csv")
df = df._get_numeric_data()
df = df.sort_values(by=["GRASPMOD_of"])

df["Best of"] = df.max(axis=1)

# repeat for all algs we compare
algs = ["GRASP", "GRASPMOD", "PR1", "PR2", "PR3", "PR4"]
#algs = ["GRASPMOD", "GRASP"]

for a in algs:
    df["Dev "+a] = (df["Best of"] - df[a+"_of"])/df["Best of"]*100
    df["# best "+a] = np.where(df["Best of"] == df[a+"_of"], 1, 0)

# split n=100 and n=500
dfs = np.split(df, [6], axis=0)
#dfs = np.split(df, [0], axis=0)

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
    data["algorithm"] = ["GRASP", "GRASPMOD", "PR1", "PR2", "PR3", "PR4"]
    #data["algorithm"] = ["GRASPMOD", "GRASP"]
    data["of"] = of
    data["run time (s)"] = runtime
    data["dev"] = dev
    data["rel best of"] = best

    print(data)
    #print(data.to_latex(index=False, formatters={"name": str.upper}, float_format="{:.2f}".format))

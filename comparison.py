import pandas as pd
import numpy as np

df = pd.read_csv("results300itersAGAIN.csv")
df = df._get_numeric_data()
df = df.sort_values(by=["GRASPMOD_of"])

df["Best of"] = df.max(axis=1)

# repeat for all algs we compare
algs = ["GRASP", "GRASPMOD", "PR1", "PR2", "PR3", "PR4"]

for a in algs:
    df["Dev "+a] = (df["Best of"] - df[a+"_of"])/df["Best of"]*100
    df["# best "+a] = np.where(df["Best of"] == df[a+"_of"], 1, 0)
    #df["# best "+a] = np.where((df["Best of"] == df[a+"_of"]) & (df[a+"_of"] > df["GRASP_of"]), 1, 0)
    #df["# best GRASP"] = np.where(df["Best of"] == df["GRASP_of"], 1, 0)

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
    data["algorithm"] = ["GRASP", "GRASPMOD", "PR1", "PR2", "PR3", "PR4"]
    data["of"] = of
    data["run time (s)"] = runtime
    data["dev"] = dev
    data["rel best of"] = best

    #print(data)
    print(data.to_latex(index=False, formatters={"name": str.upper}, float_format="{:.2f}".format))

#mean100 = dfs[0].loc['mean'] = dfs[0].mean()
#mean500 = dfs[1].loc['mean'] = dfs[1].mean()
#print(mean100)
#print(mean500)

#print(mean100.to_latex(index=True, formatters={"name": str.upper}, float_format="{:.2f}".format))
"""
freq = [0,0.05,0.1,0.2,0.3]
of = []
runtime = []
for f in freq:
    df = pd.read_csv("pr_test500.csv")
    df = df[df.freq == str(f)]
    df["of"] = pd.to_numeric(df["of"])
    df["runtime"] = pd.to_numeric(df["runtime"])
    #print("freq " + str(f) + ": of: " + str(round(df.of.mean(), 2)) + ", runtime: " + str(round(df.runtime.mean(),2)))
    of.append(round(df.of.mean(), 2))
    runtime.append(round(df.runtime.mean(), 2))

#df = pd.read_csv("pr_test500.csv")
#print(df)


res = pd.DataFrame([])
res["frequency"] = freq
res["of"] = of
res["runtime (s)"] = runtime

print(res.to_latex(index=False, formatters={"name": str.upper}, float_format="{:.2f}".format))
"""
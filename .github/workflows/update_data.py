import pandas as pd
import os


df = pd.read_csv("_data/hot-or-not/aggregate.csv")
df = df.rename(columns=lambda x: x.strip())
print(list(df))


for f in os.listdir("_data/hot-or-not/raw"):
    if f[:4] == "dat_":
        for l in open("_data/hot-or-not/raw/"+f,'r').readlines():
            ll = l.strip().replace("'",'').split(', ')
            #print(ll[0])
            df.loc[df.district == ll[0],ll[1]] += 1


df.to_csv("_data/hot-or-not/aggregate.csv",index=False)

js_str = "var vote_data = {"

for i,r in df.iterrows():

    js_str += ("'" + str(r["district"]) + "'" + ": [" + str(r["hot"]) + ", " + str(r["not"]) + "], ")

js_str = js_str[:-2] + '}'

with open("_data/hot-or-not/vote-data.js", 'w') as jsout:
    jsout.write(js_str)

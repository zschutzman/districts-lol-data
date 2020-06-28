import os

to_process = [f for f in os.listdir("_data/hot-or-not/raw/") if f[:3] == 'dat']


with open("_data/hot-or-not/votes.csv",'a') as fd:
    
    for fn in to_process:
        with open("_data/hot-or-not/raw/" + fn,'r') as f:
            l = f.read()
        fd.write(l)




    





d = dict()

with open("_data/hot-or-not/votes.csv",'r') as fd:
    for l in fd.readlines():
        r = (l.strip().split(', '))
        if len(r) == 2:
            if r[0] not in d.keys():
                d[r[0]] = [0,0]
            if 'hot' in r[1]:
                d[r[0]][0] += 1
            else:
                d[r[0]][1] += 1

with open("_data/hot-or-not/aggregate.csv",'w') as fd:
    fd.write("district, hot, not\n")
    for k,v in d.items():
        s = f"{k}, {v[0]}, {v[1]}\n"
        fd.write(s)
		
		
		
		
with open("_data/hot-or-not/vote-data.js",'w') as fd:
    fd.write("var vote_data = ")
    fd.write(str(d))
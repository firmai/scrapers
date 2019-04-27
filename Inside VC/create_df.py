import pandas as pd
import numpy as np

fufu = pd.read_csv("fufu_new.csv")

fufu['Bin'] = fufu['Title'].str.contains("strong").values

fufu['Loca'] = fufu['Title'].str.contains("\(.*\)").values

start = '<p dir="ltr"><strong>--'
end = '--</strong></p>'

far = fufu[fufu["Bin"] == True]

far["name"] = far["Title"].apply(lambda x: x[len(start):-len(end)])

fuff = pd.concat((fufu, far["name"]), axis=1)

fuff = fuff.fillna(method="ffill")

fuff = fuff[fuff["Bin"] == False]

fuff['Title'] = fuff['Title'].map(lambda x: x.lstrip('<p dir="ltr">-'))

fuff.iloc[3]

fuff["Title"] = fuff["Title"].apply(lambda x: x.strip())

fuff = fuff.reset_index(drop=True)

start = 'a href="'

coy_url = []
coy_name = []
coy_loc = []
location = []

for f, loc in zip(fuff["Title"], fuff["Loca"]):
    if f[:2] == "a ":
        s = f.split('/">')[0]
        s = s.split('//')[1]

        d = f.split("</a> (")[0]
        d = d.split('">')[1]


    else:
        s = None
        d = f.split(' (')[0]

    coy_name.append(d)
    coy_url.append(s)

    coy_n = []
    for w in coy_name:
        if len(w) > 25:
            w = w.split("</a>")[0]
            coy_n.append(w)
        else:
            coy_n.append(w)

fuff["name"] = coy_n
fuff["url"] = coy_url

ft = fuff[fuff["Loca"] == True]

location = []
for f, loc in zip(ft["Title"], ft["Loca"]):
    if loc == True:
        loca = f.split("(")[1]
        loca = loca.split(")")[0]
    location.append(loca)

ft["Location"] = location

fuff = pd.concat((fuff, ft["Location"]), axis=1)

tag_li = []
reffy = []
dollars = []
involved = []
type_raw = []
fuff["tell"] = fuff["Title"].apply(lambda x: len(x))
fuff = fuff[fuff["tell"] > 160].reset_index(drop=True)

fuff = fuff[fuff["Title"].str.contains("$")].reset_index(drop=True)
fuff = fuff[fuff["Title"].str.contains("M")].reset_index(drop=True)
fuff = fuff[fuff["Title"].str.contains("B")].reset_index(drop=True)
for index, f in zip(fuff.index.values, fuff["Title"]):
    try:
        try:
            try:
                b = f.split(", ")[2]
            except:
                b = "fake"
        except:
            fuff.drop(index, inplace=True)
            continue
        if len(b) > len(g):
            g = b
        tag = g.split(": ")[0]
        tag_li.append(tag)
        try:
            try:
                ref = f.split(': <a href="')[1]
                ref = ref.split('">')[0]
            except:
                ref = "None"
        except:
            fuff.drop(index, inplace=True)
            continue
        reffy.append(ref)

        dol = f.split('$')[1]
        lan = len(dol)
        dol = dol.split("</a>")[0]
        dol = "$" + dol
        dollars.append(dol)
        try:
            try:
                gol = f.split('>$')[1]
            except:
                gol = f.split(': ')[1]
        except:
            fuff.drop(index, inplace=True)
            continue
        lan = len(gol)
        inv = f[-lan:]
        try:
            try:
                inv = inv.split("</a>")[1]
            except:
                inv = inv.split(' ', 1)[1]
        except:
            fuff.drop(index, inplace=True)
            continue
        inv = inv.split("</p>")[0]
        print(inv)
        involved.append(inv)
        try:
            try:
                type_raw.append(inv.split()[0])
            except:
                type_raw.append("None")
        except:
            fuff.drop(index, inplace=True)
            continue
    except:
        fuff.drop(index, inplace=True)
        continue

fuff["type_raw"] = type_raw

fuff["involved"] = involved

fuff["value"] = dollars

fuff["tag_li"] = tag_li

fuff["reffy"] = reffy
import pandas as pd

df2 = pd.read_csv('labels.csv', delimiter=",", engine="python")
df1 = pd.read_csv('data-25.csv', delimiter=", ", engine="python")

df=df2.drop(['index'],axis=1) # Removing unnecessary Column
di=dict(df.values) # {"/m/09x0r":"Speech",....}

def replace(x):
    r=[]
    for a in x.replace('"',"").split(","):
        b=di.get(a)
        if b==None:
            r.append(a)
        else:
            r.append(b)
    return ",".join(r)

# Just replacing in same column
df1["labels"]=df1["labels"].apply(replace) # You may make new column
print(df1)


# Or same but one-liner solution is
df1["labels"]=df1["labels"].apply(lambda x:",".join([di.get(a) if di.get(a)!=None else a for a in x.split(",")]))

print(df1)

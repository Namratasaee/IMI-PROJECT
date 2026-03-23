import pandas as pd

d1 = pd.read_csv("darshan_1.csv")
d2 = pd.read_csv("darshan_2.csv")
d3 = pd.read_csv("darshan_3.csv")

n1 = pd.read_csv("namrata_1.csv")
n2 = pd.read_csv("namrata_2.csv")
n3 = pd.read_csv("namrata_3.csv")

a1 = pd.read_csv("aash_1.csv")
a2 = pd.read_csv("aash_2.csv")
a3 = pd.read_csv("aash_3.csv")

df = pd.concat([d1, d2, d3, n1, n2, n3, a1, a2, a3], axis=1)

# Target
df["Target"] = (
    (df["MolWt"] < 500) &
    (df["LogP"] < 5) &
    (df["HDonors"] <= 5) &
    (df["HAcceptors"] <= 10)
).astype(int)

df.to_csv("final_dataset_updated.csv", index=False)

print("Final dataset created")
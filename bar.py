import pandas as spd
import matplotlib.pyplot as plt
df = spd.read_csv("filtered_stars.csv")
print(df.head())
df.drop(['Unnamed: 0', 'Unnamed: 0.1'],axis=1,inplace=True)
name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()
plt.figure(figsize=(10,5))
plt.title("stars solar mass")
plt.bar(name[0:9],mass[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("stars solar radius")
plt.bar(name[0:9],radius[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("stars solar gravity")
plt.bar(name[0:9],gravity[0:9])
plt.show()
plt.figure(figsize=(10,5))
plt.title("stars solar distance")
plt.bar(name[0:9],dist[0:9])
plt.show()
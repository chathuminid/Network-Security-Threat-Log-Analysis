import pandas as pd 
import matplotlib.pyplot as plt

#load the dataset
df = pd.read_csv("RT_IOT2022.csv")

print(df.head())

#show the data types and missing values
print(df.info())

print("\nMissing Values per column:")
print(df.isnull().sum())

print("\nAttack type distribution:")
print(df['Attack_type'].value_counts())

#Attack distribution visualization
df['Attack_type'].value_counts().plot(kind='bar',figsize=(10,6))
plt.title('Attack Type Distribution')
plt.xlabel('Attack Type')
plt.ylabel('Count')
#plt.show()
plt.savefig("Attack_distribution.png")
print("Success! Created 'Attack_distribution.png'")
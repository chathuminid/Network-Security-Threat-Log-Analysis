import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

#load the dataset
df = pd.read_csv("RT_IOT2022.csv")

print(df.head())

#show the data types and missing values
print(df.info())

print("\nMissing Values per column:")
print(df.isnull().sum())

print("\nAttack type distribution:")
print(df['Attack_type'].value_counts())

#analyze about numerical data
print("\n--- Statistical Summary ---")
print(df.describe())

#Attack distribution visualization
df['Attack_type'].value_counts().plot(kind='bar',figsize=(10,6))
plt.title('Attack Type Distribution')
plt.xlabel('Attack Type')
plt.ylabel('Count')
#plt.show()
plt.savefig("Attack_distribution.png")
print("Success! Created 'Attack_distribution.png'")

if 'no' in df.columns:
    df = df.drop(columns=['no'])
    print("\nDropped the 'no' column.")

categorical_cols = df.select_dtypes(include=['object']).columns
#print("\nCategorical Columns that need encoding:")
#print(categorical_cols.tolist())

#print("\nUnique Protocols:", df['proto'].unique())
#print("Unique Services:", df['service'].unique())

#for wanning message in pandas library
categorical_cols = df.select_dtypes(include=['object', 'string']).columns

#using LabelEncoder string convert to number
encoder = LabelEncoder()

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col].astype(str))

print("\n--- After convert to Numbers")
print(df[['proto', 'service','Attack_type']].head())

#DATA splitting & Scaling
y = df['Attack_type']
X =df.drop(columns=['Attack_type'])

print("\n--- Shape of X and Y ---")
print(f"Features (X) shape:{X.shape}")
print(f"Target (y) shape: {y.shape}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\n--- Scaled Data (First 5 values of the first row) ---")
print(X_scaled[0][:5])
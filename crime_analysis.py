import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
df = pd.read_excel("crime_data.xlsx")
print("Dataset Preview:\n", df.head())

# Data Preprocessing
print("\nMissing Values:\n", df.isnull().sum())
df = df.dropna()
df["Date"] = pd.to_datetime(df["Date"])

# Descriptive Statistics
print("\nStatistics:\n", df["Crime_Count"].describe())

plt.figure()
plt.plot(df["Date"], df["Crime_Count"])
plt.title("Crime Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Crime Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


location_data = df.groupby("Location")["Crime_Count"].sum()
plt.figure()
location_data.plot(kind='bar')
plt.title("Crime Hotspots by Location")
plt.xlabel("Location")
plt.ylabel("Total Crimes")
plt.tight_layout()
plt.show()


type_data = df["Crime_Type"].value_counts()
plt.figure()
type_data.plot(kind='bar')
plt.title("Crime Type Distribution")
plt.xlabel("Crime Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


plt.figure()
plt.hist(df["Crime_Count"], bins=10)
plt.title("Crime Count Distribution")
plt.xlabel("Crime Count")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()




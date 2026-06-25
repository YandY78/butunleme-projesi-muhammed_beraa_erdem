import pandas as pd

# Veri setini oku
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Veri başarıyla yüklendi.")
print(df.head())
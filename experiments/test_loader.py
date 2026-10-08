import pandas as pd
from scipy.io import arff

# 1. Pfad zur Datei
file_path = "experiments/data/credit_g.arff"

# 2. ARFF-Datei einlesen
data, meta = arff.loadarff(file_path)
df = pd.DataFrame(data)

# 3. String-Spalten dekodieren (scipy liest Text oft als Byte-Strings b'...' ein)
for col in df.select_dtypes([object]).columns:
    df[col] = df[col].str.decode("utf-8")

# 4. Merkmale und Zielvariable trennen
target_col = "class"
X = df.drop(columns=[target_col])
y = df[target_col]

print(f"Datensatz erfolgreich geladen!")
print(f"Instanzen (Zeilen): {X.shape[0]}")
print(f"Features (Spalten): {X.shape[1]}")
print(f"Klassenverteilung:\n{y.value_counts()}")
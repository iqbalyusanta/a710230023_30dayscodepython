# Import library yang diperlukan
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Memuat dataset
iris = load_iris()
X = iris.data
y = iris.target

# Membuat model Random Forest dengan estimasi OOB diaktifkan
rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)

# Melatih model
rf.fit(X, y)

# Menghitung kesalahan OOB
oob_error = 1 - rf.oob_score_
print(f'Kesalahan OOB: {oob_error}')

# Memprediksi data pelatihan untuk menghitung akurasi
y_pred = rf.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f'Akurasi: {accuracy}')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import pandas as pd

# Charger les données
df = pd.read_csv('projets_imaginaires_100_complet.csv')

# Préparer les données
X = df.drop(columns=['Score potentiel de réussite'])
y = df['Score potentiel de réussite']

# Convertir les variables catégorielles en numériques (si nécessaire)
X = pd.get_dummies(X)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(model, 'model.pkl')

# Sauvegarder les colonnes du modèle
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')

print("Modèle et colonnes sauvegardés avec succès !")
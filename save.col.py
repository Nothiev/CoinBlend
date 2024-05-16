# Sauvegarder les colonnes du modèle
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')

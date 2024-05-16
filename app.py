from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Charger le modèle et les colonnes
model = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')

# Initialiser Flask
app = Flask(__name__)

# Point de terminaison pour les prédictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Enveloppez les données dans une liste pour indiquer une seule ligne de données
    data_df = pd.DataFrame([data])
    
    # Convertir les variables catégorielles en numériques
    data_df = pd.get_dummies(data_df)
    
    # Assurez-vous que les colonnes correspondent
    for col in model_columns:
        if col not in data_df.columns:
            data_df[col] = 0

    # Réordonner les colonnes pour correspondre au modèle
    data_df = data_df[model_columns]
    
    prediction = model.predict(data_df)
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

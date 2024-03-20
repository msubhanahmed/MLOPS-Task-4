from flask import Flask, request, jsonify
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import joblib

app = Flask(__name__)
knn = joblib.load('model/knn_model.pkl')


@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    values = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    X = np.array(values).reshape(1, -1)
    prediction = knn.predict(X)
    if prediction == 0:
        predicted_class = 'setosa'
    elif prediction == 1:
        predicted_class = 'versicolor'
    else:
        predicted_class = 'virginica'
    return jsonify({'predicted_class': predicted_class})

if __name__ == '__main__':
    app.run(debug=False)

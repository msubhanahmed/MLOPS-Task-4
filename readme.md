# 20I-0873
# Muhammad Subhan

# Flask API for Iris Flower Classification

This repository contains a Flask API for predicting the class of iris flowers using a pre-trained KNN model. Additionally, it provides instructions for Dockerizing the application for easy deployment.

## Usage

### Prerequisites

- Python 3.9 or higher
- Docker (optional)

### Installation

#### 1. Clone the repository:

   git clone https://github.com/msubhanahmed/MLOPS-Task-4.git
   cd MLOPS-Task-4

### Running the Flask Application Locally
Run the following command to start the Flask application locally:
#### Install dependencies:

pip install -r requirements.txt

#### Run the application
python app.py
The Flask application will start running on http://localhost:5000.

### Dockerization
To Dockerize the application, follow these steps:

#### Build the Docker image:

docker build -t flask-iris-app .

#### Run the Docker container:

docker run -p 5000:5000 flask-iris-app

### Testing the Endpoint
You can use curl to test the Flask endpoint. Here's an example curl command:

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}' \
  http://localhost:5000/predict

Replace http://localhost:5000/predict with the actual URL of your Flask endpoint if it's hosted on a different address.

### Notes
The KNN model used for prediction is trained on the Iris dataset, which contains measurements of various features of iris flowers.
The prediction endpoint accepts JSON data with values for sepal_length, sepal_width, petal_length, and petal_width, and returns the predicted class of the iris flower.
Feel free to explore the code and adapt it to your needs!
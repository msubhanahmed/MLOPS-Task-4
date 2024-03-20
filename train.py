from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import joblib


df = pd.read_csv('data/Iris.csv')
df.drop(columns='Id',axis=1,inplace=True)
label_encoder = LabelEncoder()
df['Species'] = label_encoder.fit_transform(df['Species'])
X = df.drop(['Species'], axis=1)
y = df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=43)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
print("Model Score: ", knn.score(X_test, y_test))
joblib.dump(knn, 'model/knn_model.pkl')
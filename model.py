import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

try:
    data = pd.read_csv('dataset/Crop_recommendation.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'dataset/Crop_recommendation.csv' not found. Checking current directory...")
    try:
        data = pd.read_csv('Crop_recommendation.csv')
        print("Dataset loaded successfully from current directory.")
    except FileNotFoundError:
        print("Error: Dataset not found.")
        exit(1)

#Preprocessing
X = data.iloc[:, :-1]  #features
y = data.iloc[:, -1]   #labels

# split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print("Training RandomForestClassifier...")
model = RandomForestClassifier()
model.fit(X_train, y_train)
print("Model trained.")

accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

#save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Model saved to 'model.pkl'.")

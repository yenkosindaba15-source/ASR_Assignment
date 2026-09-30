import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("../data/navigation_dataset.csv")

X = dataset[["left_sensor", "front_left_sensor", "front_right_sensor", "right_sensor"]]
y = dataset["action"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

model = MLPClassifier(hidden_layer_sizes=(10), max_iter=1000, random_state=42)
model.fit(X_train,y_train)

predictions = model.predict(X_test)

#Accuracy:
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.4f}")

#Matrix:
matrix = confusion_matrix(y_test, predictions)
display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=model.classes_)
display.plot(cmap="Blues")

plt.title("Navigation Decision Confusion Matrix")
plt.show()
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset from CSV file
data = pd.read_csv("student_data.csv")

# Separate features and labels
X_raw = data[["Attendance", "StudyHours", "InternalMarks"]]
y = data["Result"].values

# Ordinal Encoding
encoder = OrdinalEncoder(categories=[
    ["Low", "Medium", "High"],     # Attendance
    ["Low", "Medium", "High"],     # StudyHours
    ["Poor", "Average", "Good"]    # InternalMarks
])

X_encoded = encoder.fit_transform(X_raw)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Train Gaussian Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Prediction on test data
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)

# -------- RAW USER INPUT --------
attendance = input("Enter Attendance (Low/Medium/High): ")
study_hours = input("Enter Study Hours (Low/Medium/High): ")
internal_marks = input("Enter Internal Marks (Poor/Average/Good): ")

# Wrap in DataFrame with column names
test_raw = pd.DataFrame(
    [[attendance, study_hours, internal_marks]],
    columns=["Attendance", "StudyHours", "InternalMarks"]
)

# Transform
test_encoded = encoder.transform(test_raw)

# Predict
prediction = model.predict(test_encoded)

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")

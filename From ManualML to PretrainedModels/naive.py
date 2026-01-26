import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
data = {
    "text": [
        "Congratulations you won a free gift",
        "Meeting scheduled tomorrow",
        "Claim your prize now",
        "Please review the attached document",
        "Urgent account verification required",
        "Let us discuss the project",
        "Limited offer buy now",
        "Your OTP is 563829",
        "Win cash rewards instantly",
        "Can we reschedule the meeting"
    ],
    "label": [
        "Spam", "Not Spam", "Spam", "Not Spam", "Spam",
        "Not Spam", "Spam", "Not Spam", "Spam", "Not Spam"
    ]
}

df = pd.DataFrame(data)
df["label"] = df["label"].map({"Spam": 1, "Not Spam": 0})
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]
model = MultinomialNB()
model.fit(X, y)
print("\n=== Spam Detection System ===")
email = input("Enter the email text: ")
email_bow = vectorizer.transform([email])
prediction = model.predict(email_bow)
if prediction[0] == 1:
    print("Result: Spam Email")
else:
    print("Result: Not Spam Email")

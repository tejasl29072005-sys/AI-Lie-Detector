import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


texts = [
    "I completed the project on time",
    "I attended all the classes",
    "I studied for the exam",
    "I finished my work honestly",
    "I helped my team members",

    "I did not copy in the exam",
    "I never lie",
    "I always follow rules",
    "I didn't cheat",
    "I was not late",

    "I swear I didn't do it",
    "Believe me I am telling the truth",
    "Trust me I am honest",
    "I promise I didn't cheat",
    "Honestly I didn't do anything"
]

labels = [
    1,1,1,1,1,   # Truth
    1,1,1,1,1,   # Truth
    0,0,0,0,0    # Suspicious (over-defensive tone)
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

st.set_page_config(page_title="Lie Detector", layout="centered")

st.title("🕵️ AI Lie Detector (Text-Based)")
st.write("Type a sentence and see if it sounds truthful or suspicious.")

user_input = st.text_area("Enter your sentence:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        confidence = model.predict_proba(input_vector)[0].max()

        if prediction == 1:
            st.success(f"✅ This sounds Truthful ({confidence*100:.2f}% confidence)")
        else:
            st.error(f"⚠️ This sounds Suspicious ({confidence*100:.2f}% confidence)")

        # Extra Explanation
        st.subheader("🧠 Explanation")
        st.write("""
        - Statements with too many defensive words like *'trust me', 'I swear'* may sound suspicious.
        - Clear and direct sentences often sound more truthful.
        """)
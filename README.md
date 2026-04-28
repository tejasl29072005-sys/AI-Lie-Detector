AI Lie Detector (Text-Based)

A simple AI-powered web application that analyzes text input and predicts whether a statement sounds **truthful** or **suspicious** based on language patterns.

Built using  Streamlit and **Machine Learning (TF-IDF + Logistic Regression)

🚀 Features

* Real-time text analysis
* Detects tone: **Truthful ✅** or **Suspicious ⚠️**
* Displays prediction confidence
* Provides explanation for results
* Clean and simple UI using Streamlit


🧠 How It Works

* Uses **TF-IDF Vectorization** to convert text into numerical features
* Trained on a small dataset of sample sentences
* Sentences are labeled as:

  * **Truthful** → clear, direct statements
  * **Suspicious** → overly defensive statements (e.g., “trust me”, “I swear”)
* Model used: **Logistic Regression**


📂 Project Structure

├── app.py
├── README.md


⚙️ Installation

1. Clone the repository:

git clone https://github.com/your-username/ai-lie-detector.git
cd ai-lie-detector


2. Install required packages:

pip install streamlit scikit-learn


 ▶️ Run the Application

streamlit run app.py

 🧪 Example Inputs

| Input Sentence                | Output        |
| ----------------------------- | ------------- |
| I completed my project        | Truthful ✅    |
| Trust me I didn’t do anything | Suspicious ⚠️ |

⚠️ Limitations

* Uses a very small dataset
* Not trained on real-world data
* Detects **tone**, not actual truth
* May not perform well on complex sentences

🔮 Future Improvements

* Train on a larger and real-world dataset
* Use advanced NLP models (LSTM, BERT)
* Improve contextual understanding
* Add voice-based lie detection


🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn

📌 Note

This project is created for educational purposes to demonstrate basic Natural Language Processing and Machine Learning concepts.

📬 Contact

Feel free to connect and give feedback!

# 🤖 AI Intern Support Assistant

An AI-powered chatbot built using **Python**, **Streamlit**, and **Hugging Face Sentence Transformers** to provide intelligent answers to internship-related questions through semantic search.

## 📌 Features

- AI-powered semantic search
- Internship FAQ support
- Historical support ticket retrieval
- Real-time chatbot interface
- Confidence score for responses
- Modern Streamlit UI
- Suggested questions
- Chat history

## 🛠️ Technologies Used

- Python
- Streamlit
- Sentence Transformers
- Hugging Face
- Pandas
- Scikit-learn

## 📂 Project Structure

```
AI-Intern-Support-Chatbot/
│── app.py
│── chatbot.py
│── requirements.txt
│── README.md
│── data/
│   ├── faq.csv
│   └── support_tickets.csv
│── assets/
│── screenshots/
```

## 🚀 Installation

```bash
git clone <repository-url>

cd AI-Intern-Support-Chatbot

pip install -r requirements.txt

python -m streamlit run app.py
```

## 💡 How It Works

The chatbot converts user questions into vector embeddings using the Hugging Face **all-MiniLM-L6-v2** model.

It compares the user's question with the FAQ and historical support ticket datasets using **cosine similarity** and returns the most relevant answer.

## 📷 Screenshots

(Add screenshots after deployment.)

## 📄 License

This project was developed for educational and internship purposes.
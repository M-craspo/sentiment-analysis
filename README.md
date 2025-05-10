# Sentiment Analysis on Twitter Data

This project applies machine learning and deep learning models to analyze and classify the sentiment of tweets from the [Sentiment140 dataset](http://help.sentiment140.com/). The goal is to determine whether a tweet expresses a positive or negative sentiment.

## 🚀 Models Used

- **Logistic Regression + TF-IDF**
- **LSTM + Word2Vec**
- **DistilBERT (fine-tuned transformer)**

## 📊 Results

| Model              | Accuracy | F1-score |
|--------------------|----------|----------|
| Logistic Regression| 81%      | 0.80     |
| LSTM               | 83%      | 0.83     |
| **DistilBERT**     | **85%**  | **0.86** |

✅ **Best Model:** [DistilBERT on HuggingFace](https://huggingface.co/mahmoudelbahy33/distilbert-base-uncased-finetuned-sentiment-2)

## 🗂 Dataset

- **Source:** Sentiment140 (1.6 million tweets)
- **Fields:** `target`, `id`, `date`, `flag`, `user`, `text`
- **Classes:** 0 = Negative, 4 = Positive

## ⚙️ Preprocessing Steps

- Lowercasing
- Removal of URLs, mentions, hashtags, emojis, numbers, and punctuation
- Handling of contractions
- Tokenization and padding (for LSTM and BERT)

## 🛠 Tools & Frameworks

- Python, scikit-learn, TensorFlow, PyTorch
- NLTK, HuggingFace Transformers
- Google Colab, Kaggle

## 🧪 Evaluation Metrics

- Accuracy
- F1-score
- Confusion Matrix

## 📦 Deployment

The fine-tuned DistilBERT model is hosted on HuggingFace:
[🔗 Link to Model](https://huggingface.co/mahmoudelbahy33/distilbert-base-uncased-finetuned-sentiment-2)


## 📌 Future Work

- Hyperparameter tuning for better performance
- Integration into a web app for real-time inference
- Bias mitigation and dataset balancing
- Real-time Twitter stream analysis

---

📬 For questions or collaboration, feel free to reach out or contribute!

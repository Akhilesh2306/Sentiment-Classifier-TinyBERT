# 🎬 Sentiment Classification on IMDB with TinyBERT

This project demonstrates an **end-to-end sentiment classification system** on the IMDB movie reviews dataset using **TinyBERT** for efficient NLP.  
It features an interactive **Streamlit interface** for real-time predictions, a **FastAPI backend** for scalable API serving, **Docker** for containerization, and deployment on **AWS Cloud** for reliability and scalability.

---

## ✨ Features
- End-to-end pipeline from training to cloud deployment.  
- TinyBERT for fast and accurate sentiment classification.  
- Streamlit for an interactive user interface.  
- FastAPI for RESTful API serving.  
- Docker for portable and reproducible builds.  
- AWS deployment for scalability and accessibility.  

---

## 🌐 Web Application  
Try out the live demo here:  
👉 [Sentiment Classifier TinyBERT](https://sentiment-classifier-tinybert.streamlit.ap

---

## 🛠 Tech Stack
- **Model**: TinyBERT, Hugging Face Transformers  
- **Frontend**: Streamlit  
- **Backend**: FastAPI  
- **Containerization**: Docker  
- **Cloud**: AWS (S3, EC2, etc.)  
- **Language**: Python 3.13  

---

## 📊 Dataset
- Dataset: [IMDB Movie Reviews](https://ai.stanford.edu/~amaas/data/sentiment/)  
- Binary classification: Positive vs. Negative sentiment.  
- Preprocessing: Text cleaning, tokenization, and subword embeddings.  

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/Akhilesh2306/Sentiment-Classifier-TinyBERT.git
cd Sentiment-Classifier-TinyBERT

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
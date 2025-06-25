# 🧠 Incident Classifier AI

AI-powered system for automatic classification of IT support tickets using Natural Language Processing (NLP) and MLOps best practices.

---

## 🚀 Objective

Automatically classify support tickets based on their textual descriptions to help support teams streamline triage and resolution.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** — RESTful API
- **scikit-learn** & **HuggingFace Transformers** — Machine Learning / NLP
- **MongoDB** — Ticket and prediction storage
- **Redis** — Caching layer
- **Docker + Docker Compose** — Local orchestration
- **MLflow** — Experiment tracking and model versioning
- **Evidently AI** — Data drift monitoring
- **GitHub Actions** — CI/CD pipelines

---

## 📁 Project Structure

```bash
incident-classifier-ai/
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA and experiments
├── src/
│   ├── api/               # FastAPI routes
│   ├── model/             # Training and inference logic
│   ├── services/          # Business logic
│   ├── database/          # MongoDB / Redis interfaces
│   ├── monitoring/        # MLflow, Evidently integration
├── tests/                 # Unit and integration tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.10+
- Docker and Docker Compose

### Steps

1. Clone the repository:

```bash
git clone https://github.com/your-username/incident-classifier-ai.git
cd incident-classifier-ai
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Launch the API:

```bash
uvicorn src.api.main:app --reload
```

4. Access the Swagger UI at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🧬 Roadmap

- [ ] Implement BERT-based classification with HuggingFace Transformers
- [ ] Cloud deployment with CI/CD on Azure
- [ ] Human feedback loop and retraining
- [ ] Multilingual support

---

## 🤝 Contributing

Pull requests are welcome! Feel free to submit issues, suggest improvements, or contribute features.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

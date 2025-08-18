# Restaurant Sentimental Analysis (ML-based)

![Python](https://img.shields.io/badge/language-Python-blue)
![Status](https://img.shields.io/badge/status-active-success)

Click to visit:

[![MLFlow](https://img.shields.io/badge/MLflow-Experiments-blue)](https://dagshub.com/PigStep/Restourant-Sentimental-Analys-ML-based.mlflow/)
[![DagsHub](https://img.shields.io/badge/DagsHub-Repo-black)](https://dagshub.com/PigStep/Restourant-Sentimental-Analys-ML-based)

## Overview

This repository provides a machine learning-based solution for sentiment analysis of restaurant reviews. It leverages natural language processing (NLP) techniques to classify customer feedback as positive, negative, or neutral, helping restaurants better understand their customer satisfaction and improve their services.

## Features

- Sentiment analysis of textual restaurant reviews
- Data preprocessing and cleaning pipeline
- Model training and evaluation
- Visualization of sentiment results
- Easy integration with restaurant review platforms

## Technologies Used

- Python
- scikit-learn
- pandas
- numpy
- matplotlib / seaborn (for visualizations)
- MLFlow (for experiment tracking)
- Docker (for containerized deployment)

## Interaction demo

![DEMO GIF](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExejhldXJzaHFyaXM5bm15ZDY1MXYzZjk3dHIzcXZiYWZjazIwaTIxeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2eXZ8qX8AnV1wirssj/giphy.gif)

## Getting Started

### Installation

#### With Docker (easy way)

1. Pull the Docker image from dockerHub:

```bash
docker pull pigstep/resourant-sentimental-analys:v0.20
```

2. Run the container:

```bash
docker run -d -p 8000:8000 pigstep/resourant-sentimental-analys:v0.20
```

3. Access the application at `http://localhost:8000`.

#### Without docker

1. Clone the repository:

```bash
git clone https://github.com/PigStep/Restourant-Sentimental-Analys-ML-based.git
cd Restourant-Sentimental-Analys-ML-based
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the main script with uvicorn:

```bash
cd Restourant-Sentimental-Analys-ML-based/src
uvicorn main:app --reload
```

4. Access the application at `http://localhost:8000`.

## Project Structure

```
Restourant‑Sentimental‑Analys‑ML‑based/
├── .gitattributes           
├── Dockerfile               # Docker image definition
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── src/
│   ├── main.py              # FastAPI application entry point
│   ├── TextClassifier.py    # Wrapper around the trained model
│   └── mlflow_logging.py    # Functions for experiment tracking
├── experiment_notebook/
│   ├── baseline_model.ipynb   # Logistic‑Regression experiments
│   ├── SVM_model.ipynb        # SVM experiments
│   └── data_preparation.ipynb # Data download and cleaning
└── static/
    └── index.html           # Front‑end landing page served by FastAPI
```

## Quick start with API

soon

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License.

## Contact

For questions, suggestions, or feedback, feel free to open an issue or contact [PigStep](https://github.com/PigStep).

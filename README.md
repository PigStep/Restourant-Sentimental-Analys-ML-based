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

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

Clone the repository:

```bash
git clone https://github.com/PigStep/Restourant-Sentimental-Analys-ML-based.git
cd Restourant-Sentimental-Analys-ML-based
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. Prepare your dataset containing restaurant reviews (see `data/` folder for examples).
2. Run the main script to train and test the sentiment analysis model:

```bash
python main.py
```

3. View results and visualizations in the output directory.

## Project Structure

```
Restourant-Sentimental-Analys-ML-based/
│
├── data/                 # Sample datasets
├── models/               # Saved model files
├── src/                  # Source code
│   ├── preprocessing.py  # Data cleaning and preprocessing
│   ├── train.py          # Model training
│   ├── predict.py        # Sentiment prediction
│   └── utils.py          # Utility functions
├── requirements.txt      # Python dependencies
├── main.py               # Main entry point
└── README.md             # Project documentation
```

## Example

Sample usage for sentiment prediction:

```python
from src.predict import predict_sentiment

review = "The food was absolutely wonderful, from preparation to presentation, very pleasing."
sentiment = predict_sentiment(review)
print(f"Sentiment: {sentiment}")
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License.

## Contact

For questions, suggestions, or feedback, feel free to open an issue or contact [PigStep](https://github.com/PigStep).

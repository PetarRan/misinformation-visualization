# Misinformation Visualization - CANIS

Kaggle [data](https://www.kaggle.com/datasets/stevenpeutz/misinformation-fake-news-text-dataset-79k) used.

Tableau Story [Here](https://public.tableau.com/app/profile/petar.randjelovic/viz/VeracityAVisualExplorationofMisinformation/VeracityAVisualExplorationofMisinformation).

## Data Cleaning Tools

This repository contains Python scripts for cleaning and processing text data, including:

- `merge_and_categorize.py`: script to merge and categorize news articles, indicating a viable news source and fake news source.
- `extract_spacy.py`: script to extract entities (e.g. countries, organizations, norp, etc.) from news articles using SpaCy Library
- `word_count.py`: script to count the frequency of words in the news articles
- `sentiment_analysis.py`: script to perform sentiment analysis on news articles rating a polarity from **-1.0 (most negative) to 1.0(most positive)**
- `clean_corrupted.py`: script to clean corrupted news articles

## Requirements

- Python 3.x
- pandas
```
python -m pip install pandas
```
- spacy
```
python -m pip install spacy
```
- SpaCy model
```
python -m spacy download en_core_web_md
```

## Usage

To use the scripts, follow these steps:

1. Clone this repository to your local machine
2. Download the Kaggle [datasets](https://www.kaggle.com/datasets/stevenpeutz/misinformation-fake-news-text-dataset-79k) and put them in a folder `..root/data`
3. Install the necessary requirements (pandas and spacy) using pip
4. Run the `main.py` script or scripts in the following order:
```
cd data-cleaning-tools
py main.py
```
**Or**
```
cd data-cleaning-tools
py merge_and_categorize.py
py extract_country.py
py sentiment_analysis.py
cd misc-tools-and-parallelization
py word_count.py
py clean_corrupted.py
```



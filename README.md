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

### Gallery


![Veracity_ A Visual Exploration of Misinformation](https://user-images.githubusercontent.com/70757499/229386422-8b46e833-7fcd-429f-bb6d-900315fa1bb8.png)

![Veracity_ A Visual Exploration of Misinformation (1)](https://user-images.githubusercontent.com/70757499/229386421-7f5fafc3-5f9b-47fa-be68-402c79c064cb.png)

![Veracity_ A Visual Exploration of Misinformation (2)](https://user-images.githubusercontent.com/70757499/229386420-44b1dd1c-420d-4635-86df-59870e941fb4.png)

![Veracity_ A Visual Exploration of Misinformation (3)](https://user-images.githubusercontent.com/70757499/229386419-15a26da1-ee64-4372-8266-f3ec3b644447.png)

import pandas as pd
import spacy
from multiprocessing import Pool, freeze_support
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, '..', '..', 'data', 'manip', 'combined_articles.csv')

# Load the combined news dataset
combined_articles = pd.read_csv(csv_path)

# Load the SpaCy English language model
nlp = spacy.load('en_core_web_md')

# Define a function to extract the location and organization entities from text
def extract_entities(text):
    if isinstance(text, str):
        doc = nlp(text)
        country = ""
        organization = ""
        for ent in doc.ents:
            if ent.label_ == "GPE":
                if not country:
                    country = ent.text
            elif ent.label_ == "ORG":
                if not organization:
                    organization = ent.text
        return country, organization
    else:
        return "", ""

# Define a function to process data in parallel
def process_batch(batch):
    return batch.apply(lambda x: pd.Series(extract_entities(x)))

# Define the batch size
batch_size = 10000

if __name__ == '__main__':
    freeze_support()

    # Split the data into batches and process them in parallel
    with Pool() as p:
        results = p.map(process_batch, [combined_articles[i:i+batch_size] for i in range(0, len(combined_articles), batch_size)])

    # Concatenate the results
    combined_articles_subset = pd.concat(results, axis=1)

    # Rename the columns
    combined_articles_subset.columns = ['Country_{}'.format(i) if i % 2 == 0 else 'Organization_{}'.format(i) for i in range(len(combined_articles_subset.columns))]

    # Save the modified dataset to a CSV file
    combined_articles_subset.to_csv(csv_path, index=False)

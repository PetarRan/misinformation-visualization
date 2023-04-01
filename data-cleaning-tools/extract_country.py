import pandas as pd
import spacy

# Load the combined news dataset
combined_articles = pd.read_csv('../data/manip/combined_articles.csv')

# Load the SpaCy English language model
nlp = spacy.load('en_core_web_sm')

# Defining a function to extract the location and organization entities from text
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

# Apply the extract_entities function to the 'article' column and create new columns for the results
combined_articles_subset = combined_articles
#combined_articles[['Country', 'Organization']] = combined_articles['Article'].apply(lambda x: pd.Series(extract_entities(x)))
combined_articles_subset[['Country', 'Topic']] = combined_articles_subset['Article'].apply(lambda x: pd.Series(extract_entities(x)))

# Save the modified dataset to a CSV file
combined_articles_subset.to_csv('../data/manip/combined_articles_with_entities.csv', index=False)

import pandas as pd
import spacy

# Load the combined news dataset
combined_articles = pd.read_csv('../data/manip/combined_articles.csv', nrows=1000)

# Load the SpaCy English language model
nlp = spacy.load('en_core_web_sm')

# Define a function to extract entities from text
def extract_entities(text):
    if isinstance(text, str):
        doc = nlp(text)
        country = ""
        organization = ""
        person = ""
        norp = ""
        for ent in doc.ents:
            if ent.label_ == "GPE":
                if not country:
                    country = ent.text
            elif ent.label_ == "ORG":
                if not organization:
                    organization = ent.text
            elif ent.label_ == "PERSON":
                if not person:
                    person = ent.text
            elif ent.label_ == "NORP":
                if not norp:
                    norp = ent.text
        if not country:
            country = "Other"
        if not organization:
            organization = "Other"
        if not person:
            person = "Other"
        if not norp:
            norp = "Other"
        return pd.Series({'Country': country, 'Organization': organization, 'Person': person, 'NORP': norp})
    else:
        return pd.Series({'Country': "Other", 'Organization': "Other", 'Person': "Other", 'NORP': "Other"})


# Apply the extract_entities() function to the 'Article' column
combined_articles[['Country', 'Organization', 'Person', 'NORP']] = combined_articles['Article'].apply(extract_entities)

# Save the modified dataset to a CSV file
combined_articles.to_csv('../data/manip/combined_articles.csv', index=False)

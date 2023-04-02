from textblob import TextBlob
import pandas as pd

# Load the combined news dataset
combined_articles = pd.read_csv('../data/manip/combined_articles.csv', nrows=1000)

# Define a function to calculate polarity score
def calculate_polarity(text):
    blob = TextBlob(text)
    return round(blob.sentiment.polarity, 5)

# Apply the calculate_polarity() function to the 'Article' column
combined_articles['Polarity'] = combined_articles['Article'].apply(calculate_polarity)

# Save the modified dataset to a CSV file
combined_articles.to_csv('../data/manip/combined_articles.csv', index=False)

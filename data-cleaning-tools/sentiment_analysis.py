from textblob import TextBlob
import pandas as pd

# Read in the dataset
combined_articles = pd.read_csv('../data/manip/combined_articles.csv')

# Create an empty list to hold the polarity scores
polarity_scores = []

# Loop through each row in the dataset
for index, row in combined_articles.iterrows():
    # Get the text for the current row
    text = row['Article']
    
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get the polarity score (ranging from -1 to 1)
    polarity = blob.sentiment.polarity
    
    # Add the polarity score to the list
    polarity_scores.append(polarity)

# Add the polarity scores as a new column to the dataset
combined_articles['Polarity'] = polarity_scores

# Print the first few rows of the updated dataset
print(combined_articles.head())

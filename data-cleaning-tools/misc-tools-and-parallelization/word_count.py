import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, '..', '..', 'data', 'manip', 'combined_articles.csv')


# Load the combined news dataset
combined_articles = pd.read_csv(csv_path)

# Define a function to count the number of words in a string
def count_words(text):
    if isinstance(text, str):
        return len(text.split())-2 #These two characters substracted represent the quote and endquote
    else:
        return 0

# Apply the function to the 'Article' column and save the results in a new column 'WordCount'
combined_articles['WordCount'] = combined_articles['Article'].apply(count_words)

# Save the modified dataset to a CSV file
combined_articles.to_csv(csv_path, index=False)

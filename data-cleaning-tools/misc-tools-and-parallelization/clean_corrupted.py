import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, '..', '..', 'data', 'manip', 'combined_articles.csv')

# Load the combined news dataset
combined_articles = pd.read_csv(csv_path)

# Remove rows with 'WordCount' less than 10
combined_articles = combined_articles[combined_articles['WordCount'] >= 10]

# Reset the index and update the 'ID' column
combined_articles = combined_articles.reset_index(drop=True)
combined_articles['ID'] = combined_articles.index + 1

cols = list(combined_articles.columns)
cols.remove('ID')
cols.insert(0, 'ID')
combined_articles = combined_articles[cols]

# Save the modified dataset to a CSV file
combined_articles.to_csv(csv_path, index=False)

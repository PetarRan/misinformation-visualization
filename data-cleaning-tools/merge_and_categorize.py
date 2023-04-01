import pandas as pd

# Load the true news dataset
true_news = pd.read_csv('../data/DataSet_Misinfo_TRUE.csv', header=0, skiprows=[0], names=['ID', 'Article'])

# Load the fake news dataset
fake_news = pd.read_csv('../data/DataSet_Misinfo_FAKE.csv', header=0, skiprows=[0], names=['ID', 'Article'])

# Add a "Category" column to each dataset
true_news['Category'] = 'True'
fake_news['Category'] = 'Fake'

# Combine the datasets into one
combined_news = pd.concat([true_news, fake_news], ignore_index=True)

# Save the combined dataset to a CSV file
combined_news.to_csv('../data/combined_articles.csv', index=False)

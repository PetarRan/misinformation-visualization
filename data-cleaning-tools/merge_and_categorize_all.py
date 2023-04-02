import pandas as pd

# Load the true news dataset
true_news = pd.read_csv('../data/DataSet_Misinfo_TRUE.csv', header=0, skiprows=[0], names=['ID', 'Article'])
true_news['ID'] = range(1, len(true_news) + 1)

# Load the fake news dataset
fake_news = pd.read_csv('../data/DataSet_Misinfo_FAKE.csv', header=0, skiprows=[0], names=['ID', 'Article'])
fake_news['ID'] = range(len(true_news) + 1, len(true_news) + len(fake_news) + 1)

# Add a "Category" column to each dataset
true_news['Category'] = 'True'
fake_news['Category'] = 'False'

# Combine the datasets into one
combined_news = pd.concat([true_news, fake_news]).reset_index(drop=True)

# Save the combined dataset to a CSV file
combined_news.to_csv('../data/manip/combined_articles.csv', index=False)

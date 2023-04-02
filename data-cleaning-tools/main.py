import subprocess

# Example of executing two scripts sequentially
subprocess.run(['python', 'merge_and_categorize_1k.py'], check=True)
subprocess.run(['python', 'extract_spacy.py'], check=True)
subprocess.run(['python', 'sentiment_analysis.py'], check=True)
subprocess.run(['python', 'misc-tools-and-parallelization\\word_count.py'], check=True)
subprocess.run(['python', 'misc-tools-and-parallelization\\clean_corrupted.py'], check=True)

print("Data extraction and cleaning done.")

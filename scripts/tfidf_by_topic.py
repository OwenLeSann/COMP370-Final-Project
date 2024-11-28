# Script to calculate TF-IDF scores for each topic in a CSV file containing article summaries.
# The script processes the "Summary" column in the CSV file, filters out stopwords, and computes the top 10 most relevant words for each topic.
# It uses a threshold to filter out infrequent words from the analysis.

# Usage:
# python script_name.py <csv_file> <stopwords_file> <output_file> --threshold <threshold_value>


import pandas as pd
import re
import math
from collections import Counter, defaultdict
import json
import argparse

# Data Preprocessing 
def preprocess_text(summary, stopwords_file, topic):
    
    # Load stopwords from file
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stop_words = {line.strip().lower() for line in file if line.strip()}
    
    # Text preprocessing
    summary = summary.lower()
    summary = re.sub(r'[^\w\s]', '', summary)
    words = summary.split()

     # Filter out stopwords
    filtered_words = [word for word in words if word not in stop_words]
    
    # Remove "dance" specifically for "Gross Earnings" and "Cast and Crew/Characters"
    if topic in ['Gross Earnings', 'Cast and Crew/Characters']:
        filtered_words = [word for word in filtered_words if word != 'dance']
        
    return filtered_words

# Calculate TF
def tf_formula(document):
    """Compute term frequency (TF)"""
    word_frequencies = Counter(document)
    total_terms = sum(word_frequencies.values())

    tf_scores = {}
    for word, count in word_frequencies.items():
        tf = count / total_terms
        tf_scores[word] = tf

    return tf_scores

# Calculate IDF
def idf_formula(documents):
    """Compute inverse document frequency (IDF)"""
    total_documents = len(documents)
    document_frequencies = Counter(word for doc in documents for word in set(doc))

    idf_scores = {}
    for word, frequency in document_frequencies.items():
        idf = math.log(total_documents / (1 + frequency))
        idf_scores[word] = idf

    return idf_scores

# Calculate TF-IDF 
def tfidf_formula(tf, idf):
    """Compute TF-IDF scores"""
    tfidf_scores = {}
    for word, tf_val in tf.items():
        idf_val = idf.get(word, 0)
        tfidf = tf_val * idf_val
        tfidf_scores[word] = tfidf
    return tfidf_scores

# Apply a frequency threshold to remove words that appear less than the threshold
def filter_by_threshold(documents, threshold=1):
    """Filter out words that appear less than a given threshold across all documents."""
    word_freq = Counter(word for doc in documents for word in doc)
    filtered_documents = [
        [word for word in doc if word_freq[word] > threshold]
        for doc in documents
    ]
    return filtered_documents

# Main method 
def main(csv_file, stopwords_file, output_file, threshold=1):
    
    # Load annotated CSV file
    df = pd.read_csv(csv_file, encoding='utf-8')
    df['Annotation'] = df['Annotation'].str.strip()

    # Seperate articles by topics
    articles_by_topic = defaultdict(list)
    for topic, group in df.groupby('Annotation'):
        for summary in group['Summary'].dropna(): 
            words = preprocess_text(summary, stopwords_file, topic)
            articles_by_topic[topic].append(words)

    # Apply threshold filtering to remove infrequent words
    for topic in articles_by_topic:
        articles_by_topic[topic] = filter_by_threshold(articles_by_topic[topic], threshold)

    tfidf_scores = {}

    # For each topic combine the articles and create a giant list of words
    for topic, articles in articles_by_topic.items():
        all_words = []
        for article in articles:
            for word in article:
                all_words.append(word)

        # Compute tf-idf scores
        tf = tf_formula(all_words)
        idf = idf_formula(articles)
        tfidf = tfidf_formula(tf, idf)

        # Top 10 words 
        top_words = dict(Counter(tfidf).most_common(10))
        top_words_list = [word for word in top_words]
        tfidf_scores[topic] = top_words_list

    # Write the result to an output file (JSON format)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(tfidf_scores, f, indent=4)

    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Setup argparse
    parser = argparse.ArgumentParser(description="Calculate TF-IDF for each topic.")
    
    # Add arguments
    parser.add_argument("csv_file", help="CSV file containing the annotated data.")
    parser.add_argument("stopwords_file", help="Text file containing stopwords (one per line).")
    parser.add_argument("output_file", help="Output JSON file with tf-idf results per topic.")
    parser.add_argument("--threshold", type=int, default=1, help="Frequency threshold for word filtering.")
    
    # Parse arguments
    args = parser.parse_args()

    # Run the main function with the provided arguments
    main(args.csv_file, args.stopwords_file, args.output_file, args.threshold)

import nltk
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

def analyze_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            print("Файл порожній!")
            return 0, [], []

        words = nltk.word_tokenize(text)
        words = [word.lower() for word in nltk.word_tokenize(text)]
        total_words = len(words)

        stop_words = set(stopwords.words('english'))
        punctuation = set(string.punctuation)

        filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word not in punctuation]

        word_counts = Counter(words)
        most_common_words = word_counts.most_common(10)

        filtered_word_counts = Counter(filtered_words)
        most_common_filtered_words = filtered_word_counts.most_common(10)

        plt.figure(figsize=(10, 6))
        word_list, frequencies = zip(*most_common_words)
        plt.bar(word_list, frequencies, color='skyblue')
        plt.title('Top 10 Most Common Words (Original Text)', fontsize=14)
        plt.xlabel('Words', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(10, 6))
        filtered_word_list, filtered_frequencies = zip(*most_common_filtered_words)
        plt.bar(filtered_word_list, filtered_frequencies, color='lightgreen')
        plt.title('Top 10 Most Common Words (After Removing Stopwords & Punctuation)', fontsize=14)
        plt.xlabel('Words', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

        return total_words, most_common_words, most_common_filtered_words

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, [], []

file_path = 'blake-poems.txt'  
total_words, most_common_words, most_common_filtered_words = analyze_text(file_path)

if total_words > 0:
    print(f"Total number of words: {total_words}")
    print("Top 10 most common words (Original Text):")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")

    print("\nTop 10 most common words (After Removing Stopwords & Punctuation):")
    for word, freq in most_common_filtered_words:
        print(f"{word}: {freq}")

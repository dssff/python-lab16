import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def process_text(input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            print("Файл порожній!")
            return

        tokens = word_tokenize(text)
        print(f"Токенізовані слова: {tokens}")

        lemmatizer = WordNetLemmatizer()
        stemmer = PorterStemmer()
        lemmatized = [lemmatizer.lemmatize(word.lower()) for word in tokens]
        stemmed = [stemmer.stem(word) for word in lemmatized]
        print(f"Лемматизовані слова: {lemmatized}")
        print(f"Стемінг слів: {stemmed}")

        stop_words = set(stopwords.words('english'))
        no_stop_words = [word for word in stemmed if word not in stop_words]
        print(f"Після видалення стоп-слів: {no_stop_words}")

        no_punctuation = [word for word in no_stop_words if word not in string.punctuation]
        print(f"Після видалення пунктуації: {no_punctuation}")

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(" ".join(no_punctuation))



input_file = 'input_text.txt'  
output_file = 'output_text.txt'  
process_text(input_file, output_file)

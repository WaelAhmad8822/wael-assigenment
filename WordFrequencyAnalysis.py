import re
from collections import Counter
from nltk.corpus import stopwords

# Read the contents of the "random_paragraphs.txt" file
with open("paragraphs.txt", "r") as file:
    text = file.read()

# Define a function to remove stop words
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    words = re.findall(r'\b\w+\b', text.lower())  # Tokenize the text
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Remove stop words from the text
filtered_text = remove_stopwords(text)

# Count the frequency of each word in the processed text
word_freq = Counter(filtered_text)

# Display the word frequency count to the console
for word, freq in word_freq.items():
    print(f"{word} = {freq}")

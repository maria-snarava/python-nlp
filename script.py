# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# grabbing a part of speech function:
from part_of_speech import get_part_of_speech

text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

#Noise removal — stripping text of formatting (e.g., HTML tags)
cleaned = re.sub('\W+', ' ', text)
#breaking text into individual words
tokenized = word_tokenize(cleaned)

#Stemming is a blunt axe to chop off word prefixes and suffixes.
#“booing” and “booed” become “boo”, but “computer” may become “comput” and “are” would remain “are.”
stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]

#Lemmatization is a scalpel to bring words down to their root forms.
# For example, NLTK’s savvy lemmatizer knows “am” and “are” are related to “be”
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]

print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)
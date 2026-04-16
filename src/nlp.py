import nltk
from nltk.corpus import stopwords

import urllib.request
from bs4 import BeautifulSoup
import requests
from nltk import FreqDist
import matplotlib.pyplot as plt

nltk.download('stopwords')

wiki_url = "https://en.wikipedia.org/wiki/TATA"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }


response =requests.get(wiki_url,headers=headers)
html= response.text

#print(html)

soap = BeautifulSoup(html, 'html5lib')
text = soap.get_text(strip=True)

#print(text)

tokens = [t for t in text.split()]
str = stopwords.words('English')

clean_token =  tokens[:]

for t in tokens:
    if t in stopwords.words('English'):
        clean_token.remove(t)

#print(clean_token)

frequence = nltk.FreqDist(clean_token)

print(type(frequence))


for key,val in frequence.items():
    print(f"{key}"+" : "+ f"{val}")

frequence.plot(20)
#plt.show()

#---------------------1. Basic Sentence Tokenization---------------------   
from nltk.tokenize import sent_tokenize

# Download the pre-trained Punkt models
nltk.download('punkt_tab')

text = "NLTK is a great NLP toolkit. Dr. Smith, who joined in Jan. 2023, said it's easy to use in the U.S. market!"

# Tokenize into sentences
sentences = sent_tokenize(text)

print(sentences)
# Output: ['NLTK is a great NLP toolkit.', "Dr. Smith, who joined in Jan. 2023, said it's easy to use in the U.S. market!"]

#---------------------2. Custom Training on Your Own Data --------------------     
from nltk.tokenize.punkt import PunktSentenceTokenizer

# Sample training data (large plaintext in target language/domain)
train_text = "This is a sentence. This is another sentence with abbreviations like spec. and approx. in it."

# Initialize and train the tokenizer
custom_tokenizer = PunktSentenceTokenizer(train_text)

# Use it on new text
new_text = "The price is approx. $299. It was verified by a spec. analyst."
tokenized_sentences = custom_tokenizer.tokenize(new_text)

print(tokenized_sentences)

#---------------------3. Word Tokenization---------------------   
from nltk.tokenize import word_tokenize

sentence = "The CEO's announcement surprised investors on Wall St."
words = word_tokenize(sentence)

print(words)
# Output: ['The', 'CEO', "'s", 'announcement', 'surprised', 'investors', 'on', 'Wall', 'St', '.']


nltk.download('wordnet')
from nltk.corpus import wordnet as wn

# ---- Finding Synsets (Synonym Sets): A synset is a group of synonyms that share a common meaning. ----
# Get all synsets for the word "dog"
syns = wn.synsets("dog")
print(syns[0].name()) # Output: dog.n.01

# Get definition and example usage
print(syns[0].definition())
print(syns[0].examples())

# The Averaged Perceptron Tagger is the default Part-of-Speech (POS) tagger used by NLTK's pos_tag() function. It uses a machine learning algorithm to assign grammatical labels (like nouns or verbs) to words based on their context.

from nltk.tokenize import word_tokenize

# 1. Download required resources
nltk.download('punkt')  # Tokenizer
nltk.download('averaged_perceptron_tagger')  # The tagger model

# 2. Prepare text
text = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(text)

# 3. Perform POS tagging
tagged_text = nltk.pos_tag(tokens)

print(tagged_text)
# Output: [('The', 'DT'), ('quick', 'JJ'), ('brown', 'NN'), ('fox', 'NN'), ...]

#Training a Custom Model
#You can train the averaged perceptron on your own tagged sentences.

from nltk.tag.perceptron import PerceptronTagger

# Custom training data: list of sentences, where each sentence is a list of (word, tag) tuples
training_data = [
    [('Today', 'NN'), ('is', 'VBZ'), ('good', 'JJ')],
    [('It', 'PRP'), ('is', 'VBZ'), ('sunny', 'JJ')]
]

# Initialize without loading the default model
custom_tagger = PerceptronTagger(load=False)

# Train the model
custom_tagger.train(training_data)

# Test the custom tagger
print(custom_tagger.tag(['Today', 'is', 'sunny']))

# Common POS Tags
# DT: Determiner
# JJ: Adjective
# NN: Noun (singular or mass)
# VBZ: Verb (3rd person singular present)
# RB: Adverb

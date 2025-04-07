import streamlit as st
import pandas as pd
import numpy as np
import time
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
import spacy
nltk.download('averaged_perceptron_tagger')


st.title("Natural Language Processing Deployment")
# text_input Implementation
text1 = st.text_input("Enter some text:")
text=text1

button_clicked = st.button("Process Text", type="primary")
if button_clicked:
    # Text Processing
    text = text.lower()  # Lowercase
    # Remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces
    st.subheader("Processed Text :", divider="red")
    st.write(text)
# Tokenization
    nltk.download('punkt_tab')
    tokens = word_tokenize(text)
    st.subheader("Tokens of Given text ", divider="gray")
    st.write(tokens)
# stopwords
    nltk.download('stopwords')
        #from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word not in stop_words]
    st.subheader("Stopwords ", divider="green")
    st.write(filtered)
# Stemming
    #from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    stems = [stemmer.stem(word) for word in filtered]
    st.subheader("Stemming ", divider="green")
    st.write(stems)
    
# Lematization
    #nltk.download('wordnet')
    #from nltk.stem import WordNetLemmatizer

    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in filtered]
    st.subheader("Lemmatization ", divider="red")
    st.write(lemmas)
 # POS tagging
    #nltk.download('averaged_perceptron_tagger')
    pos_tags = nltk.pos_tag(filtered)
    st.subheader("POS Tagging ", divider="green")
    st.write(pos_tags)

# Name Entity Recognition
    #pip install spacy
    #python -m spacy download en_core_web_sm
    #import spacy
    nlp = spacy.load("en_core_web_sm")
    #doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    for ent in text1.ents:
        st.write(ent.text, ent.label_)
        #print(ent.text, ent.label_)
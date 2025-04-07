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


st.title("Natural Language Processing Deployment")
# text_input Implementation
text = st.text_input("Enter some text:")

button_clicked = st.button("Process Text", type="primary")
if button_clicked:
    # Text Processing
    text = text.lower()  # Lowercase
    # Remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces
    st.write(f"Processed Text : {text}")

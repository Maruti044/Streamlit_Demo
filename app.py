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
text_input_value = st.text_input("Enter some text:")
st.write(f"You entered: {text_input_value}")
#st.write("Nepal, nestled between China and India, spans a diverse landscape from the Himalayan mountains to fertile plains, covering an area slightly larger than Arkansas. Its population stands at 29.6 million, with a density of 206.61 per km², and a slight annual decline of 33,000, or 0.45%. The demographic breakdown shows a male-to-female ratio of 0.92 to 1, with median ages of 24.56 for males and 27.32 for females.")

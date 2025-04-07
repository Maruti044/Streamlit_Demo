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

import gensim
import pandas as pd
# import tkinter as tk
# from tkinter import *
import translate
from translate import Translator
import streamlit as st
import requests
from gensim.models import KeyedVectors
#web component
st.markdown("# Lengua.io")
st.markdown("_Created by Ali Zia (az2741@columbia.edu) and Chris Tengey (cdt50@georgetown.edu)_")
st.markdown('This website uses NLP/AI to help language learners find new words. You can read an article about it [here](https://medium.com/hoyalytics/lengua-io-and-an-introduction-to-word2vec-6338ed74f91a)')
st.markdown('Looking for words similar to one you already know? **Type the word in English and press Enter below.**')
chosenLanguage = st.selectbox(
    'Pick a language: ',
    ('Spanish', 'French')
)
st.markdown('##')
st.markdown('##')

searchedWord = st.text_input('Find some words related to...').lower()

st.markdown('##')
st.markdown('Results: ')

spanishTranslator= Translator(to_lang="Spanish")
englishTranslator= Translator(to_lang="english")
frenchTranslator = Translator(to_lang= "French")


# searchedW_var=tk.StringVar()

# df = pd.read_json("/Users/alizia/Downloads/reviews_Cell_Phones_and_Accessories_5.json", lines=True)
# review_text = df.reviewText.apply(gensim.utils.simple_preprocess)

# model = gensim.models.Word2Vec(
#     window = 10,
#     min_count = 2,
#     workers=6
# )

# model.build_vocab(review_text, progress_per= 100)
# model.train(review_text, total_examples=model.corpus_count, epochs=model.epochs)
# model.save("./word2vec-amazon-cell-accessories-reviews-short.model")

# enter_box = Entry(root, textvariable=searchedW_var, width = 35)
# enter_box.grid(row=6, column = 1)


#model = KeyedVectors.load("./word2vec-amazon-cell-accessories-reviews-short.model", mmap='r')
model = KeyedVectors.load("./utterances-2sp.model", mmap='r')
def search():
    searchedWordEng = englishTranslator.translate(searchedWord)
    just_first = [a for a, b in model.wv.most_similar(searchedWord, topn=25)]
    for x in just_first:
        try:
            if chosenLanguage == 'Spanish':
                similarWordsSpan = spanishTranslator.translate(x)
                print(similarWordsSpan)
                st.write(similarWordsSpan)
            elif chosenLanguage == 'French':
                similarWordsFren = frenchTranslator.translate(x)
                print(similarWordsFren)
                st.write(similarWordsFren)
        except:
            print("Error: Could not generate word")
            st.write('Could not generate word')

if searchedWord:
    search()
    st.markdown('_Report problems to ziaali455@gmail.com_')




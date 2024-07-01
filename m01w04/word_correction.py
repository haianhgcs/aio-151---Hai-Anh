import sys
import streamlit as st
sys.path.append("..")

if __name__ == "__main__":
    from util import ml_util

    st.title("Word Correction using Levenshtein Distance")
    vocabs = ml_util.load_voca(file_path='../data/vocab.txt')
    word = st.text_input('Word:')

    if (st.button("Compute")):
        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = ml_util.levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distance:')
        col2.write(sorted_distances)

import numpy as np
import math


def compute_tf(document):
    """
    Hàm tính Term Frequency (TF) cho một tài liệu.

    document: mảng NumPy chứa các từ trong tài liệu.
    """
    # Count frequency for each word and create a dictionary with word is key
    # and value is frequency of word in document
    words = document.lower().replace(".", "").split(" ")
    unique, counts = np.unique(words, return_counts=True)
    word_counts = dict(zip(unique, counts))

    # Calculate total words in document
    total_words = len(words)

    # Calculate TF for each word
    tf = {word: count / total_words for word, count in word_counts.items()}

    return tf


def compute_idf(documents):
    """
    Function to calculate Inverse Document Frequency (IDF) for set of documents.

    documents: numpy array, each array contains words in a document.
    """
    # Total of documents
    N = len(documents)

    # Create a dictionary to count number of document contain each word
    term_document_counts = {}

    for document in documents:
        # Get unique words in document
        words = document.lower().replace(".", "").split(" ")
        unique_terms = np.unique(words)
        # print(unique_terms)

        # Calculate number of document that contains word
        for term in unique_terms:
            if term in term_document_counts:
                term_document_counts[term] += 1
            else:
                term_document_counts[term] = 1

    # Calculate IDF for each word
    idf = {term: np.log(N / (1 + count))
           for term, count in term_document_counts.items()}

    return idf


def compute_tf_idf(tf, idf):
    tf_idf = {}
    for word in tf:
        if word not in idf:
            tf_idf[word] = 0
        else:
            tf_idf[word] = tf[word] * idf[word]

    return tf_idf

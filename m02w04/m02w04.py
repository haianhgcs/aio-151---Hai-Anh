import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def compute_mean(X):
    # np.mean
    return sum(X) / len(X)


def compute_median(X):
    # np.median
    size = len(X)
    X = np.sort(X)
    print(X)
    if (size % 2 == 0):
        return (X[int((size / 2) - 1)] + X[int(size / 2)]) / 2
    else:
        return X[math.floor(size/2)]


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    for x in X:
        variance += (x - mean) ** 2
    variance = variance / len(X)
    return np.sqrt(variance)


def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0

    for x, y in zip(X, Y):
        numerator += x * y
    numerator = N * numerator - (sum(X) * sum(Y))

    denominator = np.sqrt(N * sum(X**2) - sum(X) ** 2) * \
        np.sqrt(N * sum(Y**2) - sum(Y) ** 2)

    return np.round(numerator / denominator, 2)


def tfidf_search(question, context_embedded, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(
        context_embedded, query_embedded).flatten()

    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


def corr_search(question, context_embedded, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform(
        [question.lower()])

    corr_scores = np.corrcoef(query_embedded.toarray()[
                              0], context_embedded.toarray())

    corr_scores = corr_scores[0][1:]
    # Get top k cosine score and index its
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc_score)
    return results


if __name__ == "__main__":
    print("Câu hỏi 1: A")
    X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
    print("Mean: ", compute_mean(X))

    print("Câu hỏi 2: B")
    X = [1, 5, 4, 4, 9, 13]
    print("Median: ", compute_median(X))

    print("Câu hỏi 3: C")
    X = [171, 176, 155, 167, 169, 182]
    print("Median: ", compute_std(X))

    print("Câu hỏi 4: D")
    X = np.array([-2, -5, -11, 6, 4, 15, 9])
    Y = np.array([4, 25, 121, 36, 16, 225, 81])
    print("Correlation: ", compute_correlation_cofficient(X, Y))

    data = pd.read_csv("./data/advertising.csv")
    print("Câu hỏi 5: B")
    x = data["TV"]
    y = data["Radio"]
    corr_xy = compute_correlation_cofficient(x, y)
    print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")

    print("Câu hỏi 6: D")
    features = ['TV', 'Radio', 'Newspaper']
    for feature_1 in features:
        for feature_2 in features:
            correlation_value = compute_correlation_cofficient(
                data[feature_1], data[feature_2])
            print(
                f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")

    print("Câu hỏi 7: C")
    x = data['Radio']
    y = data['Newspaper']
    # result1 = np.correlation(x, y)
    # result1 = np.coefficient(x, y)
    result = np.corrcoef(x, y)
    # result1 = correlation(x, y)
    print(result)

    print("Câu hỏi 8: D")
    # np.corr(x, y)
    # data.corr(x, y)
    # data.correlation(x, y)
    print(data.corr())

    print("Câu hỏi 9: B")
    plt.figure(figsize=(10, 8))
    data_corr = data.corr()
    sns.heatmap(data.corr(), annot=True, fmt=".2f", linewidths=.5)
    # sns.heatmap(data_corr @ data, annot=True, fmt=".2f", linewidths=.5)
    plt.show()

    print("Câu hỏi 10: B")
    vi_data_df = pd.read_csv("./data/vi_text_retrieval.csv")
    context = vi_data_df['text']
    context = [str(doc).lower() for doc in context]

    tfidf_vectorizer = TfidfVectorizer()
    context_embedded = tfidf_vectorizer.fit_transform(context)
    print(round(context_embedded.toarray()[7][0], 2))
    print(context_embedded.shape)

    print("Câu hỏi 11: D")
    question = vi_data_df.iloc[0]['question']
    results11 = tfidf_search(question, context_embedded,
                             tfidf_vectorizer, top_d=5)
    print(round(results11[0]['cosine_score'], 2))

    print("Câu hỏi 12: B")
    question = vi_data_df.iloc[0]['question']
    results12 = corr_search(question, context_embedded,
                            tfidf_vectorizer, top_d=5)
    print(round(results12[1]['corr_score'], 2))

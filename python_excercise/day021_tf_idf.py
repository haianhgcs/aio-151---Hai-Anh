import sys
sys.path.append("..")

if __name__ == "__main__":
    from util import nlp_util
    """
    Viết chương trình Python để tính toán giá trị TF-IDF của các từ trong một List gồm các câu:
        ["Tôi thích học AI", "AI là trí tuệ nhân tạo", "AGI là siêu trí tuệ nhân tạo"]

    và sử dụng thư viện numpy để hỗ trợ trong việc tính toán các ma trận.
    """

    # Bước 1: Tạo tập tài liệu mẫu
    documents = ["Tôi thích học AI", "AI là trí tuệ nhân tạo",
                 "AGI là siêu trí tuệ nhân tạo"]

    # Bước 3: Tính toán IDF
    idf = nlp_util.compute_idf(documents=documents)

    index = 1
    for document in documents:
        # Bước 2: Tiền xử lý - tach từ và tính tần số
        tf = nlp_util.compute_tf(document)

        # Bước 4: Tính toán TF-IDF
        tf_idf = nlp_util.compute_tf_idf(tf, idf)

        print("Document ", index, ": ", document)
        for word in tf.keys():
            print(word, ": ", round(tf_idf[word], 4))
        index += 1

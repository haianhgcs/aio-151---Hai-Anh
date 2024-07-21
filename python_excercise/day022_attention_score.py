import numpy as np
import sys
sys.path.append("..")

if __name__ == "__main__":
    from util import transformer_util as tuti
    from util import softmax

    # Giúp kết quả giống nhau trên mọi máy khi tạo random
    np.random.seed(42)

    # Step #1: create dictionary and encode word
    vocab = {
        "Tôi": 0,
        "thích": 1,
        "học": 2,
        "AI": 3
    }

    # Count number of word in vocabulary
    vocab_size = len(vocab)

    # Declare the size of embedding vector
    embedding_dim = 4

    # Init embedding matrix randomly
    embedding_matrix = np.random.rand(vocab_size, embedding_dim)

    # Create an embedding input
    input_seq = np.array([embedding_matrix[vocab[word]]
                         for word in ["Tôi", "thích", "học", "AI"]])
    print("Chuỗi đầu vào (đã mã hóa):\n", input_seq)

    # Step #2: Initial weight matrix for Q, K, V
    W_q = np.random.rand(embedding_dim, embedding_dim)
    W_k = np.random.rand(embedding_dim, embedding_dim)
    W_v = np.random.rand(embedding_dim, embedding_dim)

    # Calculate Q, K, V
    Q = np.dot(input_seq, W_q)
    K = np.dot(input_seq, W_k)
    V = np.dot(input_seq, W_v)

    print("Ma trận Query Q: \n", Q)
    print("Ma trận Key K: \n", K)
    print("Ma trận Value V: \n", V)

    # Step #3: Tính toán Attention score
    scores = tuti.compute_attention_score(Q, K)

    # Device by square of size of K vectors
    d_k = K.shape[1]
    scores = scores / np.sqrt(d_k)
    print("Điểm số:\n", scores)

    # Step $4: Apply softmax function
    attention_weights = softmax.softmax_matrix(scores)
    print("Trọng số Attention:\n", attention_weights)

    # Step #5: Tính toán tổng có trọng số của các value
    output = attention_weights * V
    print("Đầu ra: \n", output)

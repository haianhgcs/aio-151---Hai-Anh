def levenshtein_distance(source, target):
    """
    Calculate Levenshtein distance for 2 tokens.

    Parameters:
    source (str): token1.
    target (str): token2.

    Return:
    int: Levenshtein distance of two tokens.
    """
    m = len(source)
    n = len(target)

    # Init matrix D với shape (m+1) x (n+1)
    D = [[0] * (n + 1) for _ in range(m + 1)]

    # Init first row and first column.
    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    # Calculate values in matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            D[i][j] = min(
                D[i - 1][j] + 1,        # cost for delete character from source
                D[i][j - 1] + 1,        # cost for insert character to target
                D[i - 1][j - 1] + cost  # Cost for replace character
            )

    # Value at D[m][n] is Levenshtein distance between source and target
    return D[m][n]


def load_voca(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    words = sorted(set([line.strip().lower() for line in lines]))
    return words

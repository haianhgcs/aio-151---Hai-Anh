def evaluate_f1_score(tp, fp, fn):
    """
    Evaluate the F1 score for a classification model.

    Parameters:
    tp (int): true positive count.
    fp (int): failure positive count
    fn (int): failure negative count

    Returns:
    float: Precision
    float: Recall
    float: F1 score.
    """
    INVALID_TP_MSG = "tp must be int"
    INVALID_FP_MSG = "fp must be int"
    INVALID_FN_MSG = "fn must be int"

    # Validate input, stop processing if any input is invalid
    if not isinstance(tp, int):
        raise ValueError(INVALID_TP_MSG)
    if not isinstance(fp, int):
        raise ValueError(INVALID_FP_MSG)
    if not isinstance(fn, int):
        raise ValueError(INVALID_FN_MSG)

    if tp < 0 | fp < 0 | fn < 0:
        raise ValueError("tp and fp and fn must be greater than zero")

    # Calculate precision and recall
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    # Calculate F1 score
    f1 = 2 * (precision * recall) / (precision + recall)

    return f1

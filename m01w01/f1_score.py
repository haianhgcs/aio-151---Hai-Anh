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
    # Validate input, stop processing if any input is invalid
    if not isinstance(tp, int):
        raise ValueError("tp must be int")
    if not isinstance(fp, int):
        raise ValueError("tp must be int")
    if not isinstance(fn, int):
        raise ValueError("tp must be int")
    
    if tp < 0 | fp < 0 | fn < 0:
        raise ValueError("tp and fp and fn must be greater than zero")


    # Calculate precision and recall
    precision = tp / (tp + fp) 
    recall = tp / (tp + fn) 
    
    # Calculate F1 score
    f1 = 2 * (precision * recall) / (precision + recall) 
    
    return precision, recall, f1

# Example usage:
precision, recall, f1 = evaluate_f1_score(2, 3, 5)
print(f"precision: {precision} recall: {recall} F1 Score: {f1}")

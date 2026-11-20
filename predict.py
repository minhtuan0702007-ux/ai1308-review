THRESHOLD = 0.5


def predict(scores):
    """Nhãn có điểm cao nhất trong dict {nhãn: điểm}, trả về 'unknown' nếu dưới ngưỡng."""
    if not scores:
        return "unknown"
    best_label = max(scores, key=scores.get)
    if scores[best_label] < THRESHOLD:
        return "unknown"
    return best_label
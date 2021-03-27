def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores = sorted(scores, reverse=True)
    return top_scores[:3]


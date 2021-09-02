def is_pair(words, x):
    for w in words:
        if x.startswith(w) and x[len(w) :] in words:
            return True
    return False

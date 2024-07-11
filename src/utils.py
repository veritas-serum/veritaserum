import nltk

def normalized_ed(s1: str, s2: str) -> float:
    """
    Calculate a normalized version of the Edit distance between two strings
    
    out = Levenstein(s1, s2) / max(len(s1), len(s2))

    Arguments:
        s1 (str): string 1
        s2 (str): string 2

    Return:
        float: normalized levenstein distance
    """

    dist = nltk.edit_distance(s1, s2)
    return dist / max(len(s1), len(s2))

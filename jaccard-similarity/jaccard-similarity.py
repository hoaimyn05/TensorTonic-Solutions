def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set1 = set(set_a)
    set2 = set(set_b)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    if len(union) == 0 :
        return 0.0

    return len(intersection)/len(union)
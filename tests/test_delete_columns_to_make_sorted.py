from problems.delete_columns_to_make_sorted import minDeletionSize


def test_normal_case():
    """
    a b c
    b c e
    c a e
    """
    assert(minDeletionSize(['abc', 'bce', 'cae']) == 1)

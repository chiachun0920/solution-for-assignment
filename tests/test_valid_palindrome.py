from valid_palindrome import isPalindrome


def test_normal_case():
    assert(isPalindrome('tenet') is True)
    assert(isPalindrome('TEneT') is True)


def test_case_with_white_space_and_special_character():
    assert(isPalindrome("Madam, I'm Adam") is True)


def test_case_with_under_score():
    assert(isPalindrome("a_bCba") is True)

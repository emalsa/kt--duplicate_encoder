import unittest


def duplicate_encode(word):
    word = word.lower()
    char_count = {}
    char_list = []

    # Count char, how many exists
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the word and decide which parenthesis have to be used
    for char in word:
        if char_count[char] > 1:
            char_list.append(char.replace(char, ')'))
        else:
            char_list.append(char.replace(char, '('))

    return ''.join(char_list)


class TestStringMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(duplicate_encode("PI(Im)FwaHwwPkvRc"), "))()((()(()))((((")
        self.assertEqual(duplicate_encode("recede"), "()()()")
        self.assertEqual(duplicate_encode("Success"), ")())())", "should ignore case")
        self.assertEqual(duplicate_encode("(( @"), "))((")


if __name__ == '__main__':
    unittest.main()

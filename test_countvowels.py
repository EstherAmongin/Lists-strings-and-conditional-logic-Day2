import unittest
from fizzbuzz.countvowels import vowel_count


class Testcountvowels(unittest.TestCase):
    def test_countvowels(self):
        self.assertTupleEqual(vowel_count('hellothere'), ('eo', 4))

    def test_input_is_string(self):
        with self.assertRaises(TypeError):
vowel_count([1, 2, 3, 4])
import unittest

# ... (your original query_map, hits, extend_hit, best_hit functions)

class TestSequenceAlignment(unittest.TestCase):

    def test_query_map(self):
        self.assertEqual(query_map("ABCD", 2), {'AB': [0], 'BC': [1], 'CD': [2]})
        self.assertEqual(query_map("AABB", 2), {'AA': [0, 1], 'AB': [1], 'BB': [2]})
        self.assertEqual(query_map("AAAA", 1), {'A': [0, 1, 2, 3]})
        self.assertEqual(query_map("", 2), {})
        self.assertEqual(query_map("A", 1), {'A': [0]})
        self.assertEqual(query_map("AB", 3), {}) 

    def test_hits(self):
        self.assertEqual(hits({'ABC': [0], 'BCD': [1]}, "ABCDE"), [(0, 0)])
        self.assertEqual(hits({'ABC': [0], 'BCD': [1]}, "XBCDY"), [(1, 1)])
        self.assertEqual(hits({'ABC': [0], 'BCD': [1]}, "XYZ"), [])
        self.assertEqual(hits({'AB': [0, 2]}, "ABAB"), [(0, 0), (0, 2), (2, 0), (2, 2)])
        self.assertEqual(hits({'XY': [0]}, "ABC"), [])
        self.assertEqual(hits({}, "ABCDE"), [])
        self.assertEqual(hits({'AB': [0]}, ""), [])

    def test_extend_hit(self):
        self.assertEqual(extend_hit("ABC", "ABCE", (0, 0), 2), (0, 0, 3, 3))
        self.assertEqual(extend_hit("ABCD", "ABCDE", (0, 0), 2), (0, 0, 4, 3))
        self.assertEqual(extend_hit("ABCD", "ABCDX", (0, 0), 2), (0, 0, 4, 4))
        self.assertEqual(extend_hit("ABC", "XYZ", (0, 0), 2), (0, 0, 2, 2))
        self.assertEqual(extend_hit("CBA", "ABC", (0, 2), 2), (1, 1, 3, 3))
        self.assertEqual(extend_hit("ABC", "ABCX", (0, 0), 2), (0, 0, 4, 3))
        self.assertEqual(extend_hit("", "", (0, 0), 2), (0, 0, 0, 0))

    def test_best_hit(self):
        self.assertEqual(best_hit("AATATAT", "AATATGTTATATAATAATATTT", 3), (0, 0, 7, 6))
        # Add more complex test cases here 
        # ...

if __name__ == '__main__':
    unittest.main()
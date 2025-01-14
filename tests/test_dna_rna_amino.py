import unittest

# Import the functions to be tested
from src.dna_rna_amino import contains_no_spaces, is_valid_sequence, get_sequence_type, count_bases, main

class TestBioFunctions(unittest.TestCase):
    def test_contains_no_spaces(self):
        self.assertTrue(contains_no_spaces("ATCG"))
        self.assertFalse(contains_no_spaces("AT CG"))
        self.assertFalse(contains_no_spaces(""))

    def test_is_valid_sequence(self):
        self.assertTrue(is_valid_sequence("ATCG", {"A", "T", "C", "G"}))
        self.assertFalse(is_valid_sequence("ATXG", {"A", "T", "C", "G"}))
        self.assertTrue(is_valid_sequence("AUGC", {"A", "U", "C", "G"}))
        self.assertFalse(is_valid_sequence("AUGX", {"A", "U", "C", "G"}))

    def test_get_sequence_type(self):
        self.assertEqual(get_sequence_type("ATCG"), "DNA")
        self.assertEqual(get_sequence_type("AUCG"), "RNA")
        self.assertEqual(get_sequence_type("MAVILK"), "AMINO_ACID")
        self.assertEqual(get_sequence_type("ATXG"), "INVALID")
        self.assertEqual(get_sequence_type(""), "INVALID")

    def test_count_bases(self):
        self.assertEqual(count_bases("ATCG"), {"A": 1, "T": 1, "C": 1, "G": 1})
        self.assertEqual(count_bases("AAAT"), {"A": 3, "T": 1})
        self.assertEqual(count_bases(""), {})

    def test_main(self):
        # DNA sequence
        self.assertEqual(
            main("ATCG"),
            "RNA sequence: AUCG\nA: 1\nT: 1\nC: 1\nG: 1"
        )
        # RNA sequence
        self.assertEqual(
            main("AUCG"),
            "cDNA: ATCG\nA: 1\nU: 1\nC: 1\nG: 1"
        )
        # Amino acid sequence
        self.assertEqual(
            main("MAVILK"),
            "Amino acid sequence detected.\nM: 1\nA: 1\nV: 1\nI: 1\nL: 1\nK: 1"
        )
        # Invalid sequence
        self.assertEqual(
            main("ATCGU"), "ERROR: Not a valid DNA/RNA/Amino Acid sequence"
        )
        # Sequence with spaces
        self.assertEqual(
            main("MA VILK"), "ERROR: Please, remove spaces between the sequence"
        )

if __name__ == "__main__":
    unittest.main()

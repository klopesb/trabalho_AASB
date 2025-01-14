import unittest
from src.multiple_alignment import star_alignment

class TestStarAlignment(unittest.TestCase):
    def test_empty_input(self):
        """Test handling of empty input"""
        with self.assertRaises(ValueError):
            star_alignment([])

    def test_single_sequence(self):
        """Test alignment of a single sequence"""
        seq = "HEAGAWGHEE"
        result = star_alignment([seq])
        self.assertEqual(result, [seq])

    def test_identical_sequences(self):
        """Test alignment of identical sequences"""
        seqs = ["HEAGAWGHEE", "HEAGAWGHEE", "HEAGAWGHEE"]
        result = star_alignment(seqs)
        self.assertEqual(len(result), len(seqs))
        self.assertTrue(all(seq == seqs[0] for seq in result))

    def test_simple_alignment(self):
        """Test alignment of simple sequences"""
        seqs = ["HEAGAWGHEE", "PAWHEAE"]
        result = star_alignment(seqs)
        self.assertEqual(len(result), len(seqs))
        # All sequences should have same length after alignment
        self.assertTrue(all(len(seq) == len(result[0]) for seq in result))
        # Check for presence of gap character
        self.assertTrue(any('-' in seq for seq in result))

    def test_multiple_sequences(self):
        """Test alignment of multiple sequences"""
        seqs = [
            "HEAGAWGHEE",
            "PAWHEAE",
            "HEAGAWGHEE",
            "PAWHEAE",
            "HEAGAWGHEE"
        ]
        result = star_alignment(seqs)
        self.assertEqual(len(result), len(seqs))
        # All sequences should have same length
        self.assertTrue(all(len(seq) == len(result[0]) for seq in result))

    def test_varying_lengths(self):
        """Test alignment of sequences with very different lengths"""
        seqs = ["A", "AAA", "AAAAA"]
        result = star_alignment(seqs)
        self.assertEqual(len(result), len(seqs))
        # All sequences should have same length
        self.assertTrue(all(len(seq) == len(result[0]) for seq in result))
        # Should contain gaps
        self.assertTrue(any('-' in seq for seq in result))

    def test_real_protein_sequences(self):
        """Test alignment with real protein sequence fragments"""
        seqs = [
            "MEEPQSDPSY",
            "MEEPQSDPSV",
            "MEEPQSDLSV"
        ]
        result = star_alignment(seqs)
        self.assertEqual(len(result), len(seqs))
        # All sequences should start with MEEPQSD
        self.assertTrue(all(seq.startswith("MEEPQSD") for seq in result))
        # All sequences should have same length
        self.assertTrue(all(len(seq) == len(result[0]) for seq in result))

if __name__ == '__main__':
    unittest.main()

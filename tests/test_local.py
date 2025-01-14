import unittest
from src.my_blosum import Blosum62
from src.local_alignment import local_score, subst, local_matrix, traceback, print_matrix_with_sequences
from pprint import pprint
import unittest
from io import StringIO
import sys

blosum = Blosum62()

class TestLocalAlignment(unittest.TestCase):
    def test_identical_sequences(self):
        """
        Tests alignment of two identical sequences.
        Expects the alignment score to equal the sum of substitution scores for all characters,
        and the aligned sequences to match the input sequences.
        """
        s1 = "ACTG"
        self.assertEqual(local_score(s1, s1), 24)  # Replace with the correct expected score.

        scoring_matrix = local_matrix(s1, s1)
        aligned_s1, aligned_s2 = traceback(scoring_matrix, s1, s1)
        self.assertEqual(aligned_s1, "ACTG")  # Expected aligned subsequence.
        self.assertEqual(aligned_s2, "ACTG")  # Expected aligned subsequence.


    def test_different_sequences(self):
        """
        Tests if two completely different sequences return a non-negative score.
        Results for the local alignment score for s1 = "AAAA" and s2 = "TTTT" should be greater than or equal to 0.
        """
        s1 = "AAAA"
        s2 = "TTTT"
        result = local_score(s1, s2)
        self.assertGreaterEqual(result, 0)

    def test_partial_match(self):
        """
        Tests if a partial match between two sequences returns a positive alignment score.
        Verifies that the local alignment score for s1 = "ALIGNMENT" and s2 = "IGN" is greater than 0, indicating a partial match.
        """
        s1 = "ALIGNMENT"
        s2 = "IGN"
        result = local_score(s1, s2)
        self.assertGreater(result, 0)

    def test_empty_sequence(self):
        """
        Tests alignment when one or both sequences are empty.
        Expects the alignment score to be 0 and the aligned sequences to also be empty.
        """
        self.assertEqual(local_score("", "ACT"), 0)
        self.assertEqual(local_score("ACT", ""), 0)

        scoring_matrix = local_matrix("", "ACT")
        aligned_s1, aligned_s2 = traceback(scoring_matrix, "", "ACT")
        self.assertEqual(aligned_s1, "")
        self.assertEqual(aligned_s2, "")

    def test_partial_overlap(self):
        """
        Tests overlapping subsequences returning a positive alignment score.
        Verifies that the local alignment score for s1 = "ALIGNMENT" and s2 = "MENT" is greater than 0.
        """
        s1 = "ALIGNMENT"
        s2 = "MENT"
        result = local_score(s1, s2)
        self.assertGreater(result, 0)

    def test_single_character(self):
        """
        Tests alignment of single characters with substitution scores and mismatches.
        The score should match substitution scores for identical characters and be 0 for mismatches.
        """
        self.assertEqual(local_score("A", "A"), subst("A", "A"))
        self.assertEqual(local_score("A", "T"), 0)

    def test_gap_handling(self):
        """
        Tests handling of gaps in one sequence, expecting a positive alignment score.
        Verifies that the alignment score for s1 = "A---G" and s2 = "AG" is positive, demonstrating correct gap handling.
        """
        s1 = "A---G"
        s2 = "AG"
        result = local_score(s1, s2)
        self.assertGreater(result, 0)

    def test_known_alignment(self):
        """
        Tests alignment of two known sequences (ALIGN and SLING).
        The result should match the expected score based on substitutions.
        """
        s1 = "ALIGN"
        s2 = "SLING"
        expected_score = subst("A", "S") + subst("L", "L") + subst("I", "I")
        self.assertEqual(local_score(s1, s2), expected_score)

    def test_max_score_verification(self):
        """
        Tests alignment of sequences ALIGNMENT and MENTAL, expecting a positive score.
        Verifies that aligning s1 = "ALIGNMENT" and s2 = "MENTAL" produces a positive score.
        """
        s1 = "ALIGNMENT"
        s2 = "MENTAL"
        result = local_score(s1, s2)
        self.assertGreater(result, 0)

    def test_zero_score(self):
        """
        Tests if two completely mismatched sequences return a score of 0 or greater.
        Verifies that the score for s1 = "ABC" and s2 = "XYZ" is 0 or greater, as local alignment resets mismatched regions to 0.
        """
        s1 = "ABC"
        s2 = "XYZ"
        self.assertGreaterEqual(local_score(s1, s2), 0)

    def test_repeated_characters_matrix(self):
        """
        Tests alignment of repeated characters across sequences.
        Validates gap penalties and diagonal values in the scoring matrix.
        """
        s1 = "AAAA"
        s2 = "AAA"
        matrix = local_matrix(s1, s2)

        # Validate diagonal scores
        for i in range(1, len(s2) + 1):
            self.assertEqual(matrix[i][i], i * subst("A", "A"))

        # Validate gap penalties
        for i in range(1, len(s1) + 1):
            self.assertLessEqual(matrix[i][0], 0)  # All gaps should reset to 0 in local alignment

    def test_complex_overlap(self):
        """
        Tests a case where sequences overlap partially with mismatches.
        Expects a positive score from the best matching subsequence.
        """
        s1 = "ACGT"
        s2 = "TACG"
        result = local_score(s1, s2)
        self.assertGreater(result, 0)

    def test_variable_gap_penalty(self):
        """
        Tests the algorithm with different gap penalties.
        Expects lower scores with higher gap penalties when gaps are involved in the alignment.
        """
        s1 = "ACGTACGT"
        s2 = "AC---GT"
        score_low_gap = local_score(s1, s2, g=-2)
        score_high_gap = local_score(s1, s2, g=-10)
        self.assertGreater(score_low_gap, score_high_gap)

    def test_all_gap_alignment(self):
        """
        Tests alignment where one sequence consists entirely of gaps.
        Expects the alignment score to be 0 since gaps cannot align with any characters.
        """
        s1 = "----"
        s2 = "AGCT"
        result = local_score(s1, s2)
        self.assertEqual(result, 0)
    
    def test_basic_alignment(self):
        """
        Tests basic alignment of two sequences with some matching and non-matching characters.
        Expects the correct alignment score and aligned subsequences.
        """
        s1 = "HGWAG"
        s2 = "PHSWG"
        score = local_score(s1, s2)
        self.assertEqual(score, 19)  # Replace with the correct expected score.
        
        scoring_matrix = local_matrix(s1, s2)
        aligned_s1, aligned_s2 = traceback(scoring_matrix, s1, s2)
        self.assertEqual(aligned_s1, "HGW")  # Replace with the expected aligned subsequence.
        self.assertEqual(aligned_s2, "HSW")  # Replace with the expected aligned subsequence.

    def test_print_matrix_with_sequences(self):
        """
        Tests the function that prints the scoring matrix with the sequences aligned.
        Expects the output to match the expected output when aligning "PHSWG" and "HGWAG".
        """
        s1 = "PHSWG"
        s2 = "HGWAG"
        matrix = [
            [0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0],
            [0, 0, 4, 2, 0, 0],
            [0, 0, 2, 6, 4, 2],
            [0, 0, 0, 4, 8, 6],
            [0, 0, 0, 2, 6, 9],
        ]

        # Capture the output
        expected_output = (
            "    -   P   H   S   W   G\n"
            "-   0   0   0   0   0   0\n"
            "H   0   2   0   0   0   0\n"
            "G   0   0   4   2   0   0\n"
            "W   0   0   2   6   4   2\n"
            "A   0   0   0   4   8   6\n"
            "G   0   0   0   2   6   9\n"
        )

        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function with the test matrix
        print_matrix_with_sequences(matrix, s1, s2)

        sys.stdout = sys.__stdout__

        # Assert the captured output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()

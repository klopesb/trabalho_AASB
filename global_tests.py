import unittest
from my_blosum import Blosum62
from global_alignment import global_score, subst, global_matrix, traceback, print_matrix_with_sequences
from pprint import pprint
import unittest
from io import StringIO
import sys

blosum = Blosum62()

class TestGlobalAlignment(unittest.TestCase):
    def test_identical_sequences(self):
        """
        Tests if two identical sequences return a positive alignment score
        The result should be greater than 0, indicating a perfect match between the sequences
        """
        s1 = "ALIGNMENT"
        s2 = "ALIGNMENT"
        score = global_score(s1, s2)
        self.assertGreater(score, 0)
        print("Alignment score for IDENTICAL sequences:", score)

    def test_different_sequences(self):
        """
        Tests if two completely different sequences return a negative alignment score
        The result should be less than 0, reflecting the penalties for mismatches between the sequences
        """
        s1 = "A"
        s2 = "T"
        score = global_score(s1, s2)
        print(f"Alignment score for {s1} vs {s2}: {score}")
        self.assertLessEqual(score, 0)

    def test_empty_sequence(self):
        """
        Tests if an empty sequence aligns with a non-empty sequence
        The result should be the gap penalty for the length of the non-empty sequence, calculated as len(s2) * -8
        """
        s1 = ""
        s2 = "ALIGNMENT"
        score = global_score(s1, s2)
        self.assertEqual(score, len(s2) * -8)

    def test_different_lengths(self):
        """
        Tests the case where the two sequences have different lengths
        The result should be negative due to the gap penalties for unaligned parts
        """
        s1 = "ALIGN"
        s2 = "ALIGNMENT"
        score = global_score(s1, s2)
        self.assertLess(score, 0)

    def test_single_character(self):
        """
        Tests alignment of single characters:
        1 - two identical characters
        2 - two different characters
        
        Result should be:
        1 - Identical characters should return the substitution score for those characters
        2 - Different characters should return the substitution score for those mismatched characters
        """
        self.assertEqual(global_score("A", "A"), subst("A", "A"))
        self.assertEqual(global_score("A", "T"), subst("A", "T"))

    def test_both_empty(self):
        """
        Tests if two empty sequences align
        The result should be 0, as there are no characters to align
        """
        self.assertEqual(global_score("", ""), 0)

    def test_known_score(self):
        """
        Tests the alignment of two known sequences (ALIGN and SLING) and compares the computed score with the expected score based on BLOSUM62 substitution values
        The result should match the expected score, which is the sum of the substitution scores for each aligned character between "ALIGN" and "SLING"
        """
        s1 = "ALIGN"
        s2 = "SLING"
        expected_score = (
            subst("A", "S") +
            subst("L", "L") +
            subst("I", "I") +
            subst("G", "N") +
            subst("N", "G")
        )
        self.assertEqual(global_score(s1, s2), expected_score)

    def test_scoring_matrix(self):
        """
        Tests the scoring matrix function for a known sequence pair.
        The result should check if the initial value in the matrix is 0.
        The scoring matrix should follow the gap penalties and match values correctly
        """
        s1 = "ALIGNMENT"
        s2 = "ALIGNMENT"
        matrix = global_matrix(s1, s2)
        self.assertEqual(matrix[0][0], 0)
        self.assertEqual(matrix[1][1], subst("A", "A"))
        print("Scoring matrix for IDENTICAL sequences:")
        pprint(matrix)

    def test_repeated_characters_matrix(self):
        """
        Tests the alignment of repeated characters across sequences.
        The result should show the correct gap penalties and positive diagonal values for repeated "A"s.
        """
        s1 = "AAAA"
        s2 = "AAA"
        matrix = global_matrix(s1, s2)
        self.assertEqual(matrix[4][3], subst("A", "A") * 3 + -8)
        print("Scoring matrix for repeated characters:")
        pprint(matrix)

    def test_repeated_characters_score(self):
        """
        Tests the alignment of repeated characters across sequences
        The result should be the substitution score for "A" repeated three times, plus the gap penalty for any extra characters in one of the sequences
        """
        expected_score = subst("A", "A") * 3 + -8
        self.assertEqual(global_score("AAAA", "AAA"), expected_score)

    def test_custom_gap_penalty(self):
        """
        Tests the effect of different gap penalties on the global alignment score.
        The alignment score with the low gap penalty should be greater than the score with the high gap penalty
        """
        s1 = "ALIGN"
        s2 = "AL---IGN"
        low_gap_penalty = global_score(s1, s2, g=-2)
        high_gap_penalty = global_score(s1, s2, g=-10)
        self.assertGreater(low_gap_penalty, high_gap_penalty)

    def test_no_overlap(self):
        """
        Tests the alignment of completely non-overlapping sequences.
        The result should be the sum of the substitution scores for the 4 mismatched pairs, calculated as `subst("A", "T") * 4`
        """
        s1 = "AAAA"
        s2 = "TTTT"
        score = global_score(s1, s2)
        self.assertEqual(score, subst("A", "T") * 4)

    def test_real_sequences(self):
        """
        Tests alignment of real biological sequences with a known expected score.
        The alignment score should match the calculated score based on the substitution scores of the aligned characters.
        The score should reflect matches and mismatches according to the BLOSUM62 substitution matrix.
        """
        s1 = "MEEPQSDPSVEPPLSQETFSDLWKLL"
        s2 = "MEETQSDPSVEPPLSQETFSDLWKLL"
        expected_score = (
            subst("M", "M") +  # Match
            subst("E", "E") +  # Match
            subst("E", "E") +  # Match
            subst("P", "T") +  # Mismatch
            subst("Q", "Q") +  # Match
            subst("S", "S") +  # Match
            subst("D", "D") +  # Match
            subst("P", "P") +  # Match
            subst("S", "S") +  # Match
            subst("V", "V") +  # Match
            subst("E", "E") +  # Match
            subst("P", "P") +  # Match
            subst("P", "P") +  # Match
            subst("L", "L") +  # Match
            subst("S", "S") +  # Match
            subst("Q", "Q") +  # Match
            subst("E", "E") +  # Match
            subst("T", "T") +  # Match
            subst("F", "F") +  # Match
            subst("S", "S") +  # Match
            subst("D", "D") +  # Match
            subst("L", "L") +  # Match
            subst("W", "W") +  # Match
            subst("K", "K") +  # Match
            subst("L", "L") +  # Match
            subst("L", "L")    # Match
        )
        self.assertEqual(global_score(s1, s2), expected_score)
    
    def test_basic_alignment(self):
        """
        Tests alignment of two simple sequences.
        Expects correct score and alignment.
        """
        s1 = "ACTG"
        s2 = "ACG"
        score = global_score(s1, s2)
        self.assertEqual(score, 11)
        matrix = global_matrix(s1, s2)
        aligned_s1, aligned_s2 = traceback(matrix, s1, s2)
        self.assertEqual(aligned_s1, "ACTG")
        self.assertEqual(aligned_s2, "AC-G")

    def test_empty_sequence(self):
        """
        Tests alignment when one sequence is empty.
        Expects gap penalties to apply for the entire sequence.
        """
        self.assertEqual(global_score("", "ACT"), -24)
        self.assertEqual(global_score("ACT", ""), -24)

    def test_identical_sequences(self):
        """
        Tests alignment of two identical sequences.
        Expects maximum score and perfect alignment.
        """
        s1 = "ACTG"
        self.assertEqual(global_score(s1, s1), 24)
        matrix = global_matrix(s1, s1)
        aligned_s1, aligned_s2 = traceback(matrix, s1, s1)
        self.assertEqual(aligned_s1, "ACTG")
        self.assertEqual(aligned_s2, "ACTG")
    
    def test_print_matrix_with_sequences(self):
        # Test inputs
        s1 = "PHSWG"
        s2 = "HGWAG"
        matrix = [
            [0, -8, -16, -24, -32, -40],
            [-8, -2, -10, -18, -26, -34],
            [-16, -10, -4, -8, -16, -24],
            [-24, -18, -12, -7, 11, 3],
            [-32, -25, -20, -11, 3, 11],
            [-40, -33, -27, -19, -5, 9],
        ]

        # Capture the output
        expected_output = (
            "    -   P   H   S   W   G\n"
            "-   0  -8 -16 -24 -32 -40\n"
            "H  -8  -2 -10 -18 -26 -34\n"
            "G -16 -10  -4  -8 -16 -24\n"
            "W -24 -18 -12  -7  11   3\n"
            "A -32 -25 -20 -11   3  11\n"
            "G -40 -33 -27 -19  -5   9\n"
        )

        captured_output = StringIO()
        sys.stdout = captured_output

        print_matrix_with_sequences(matrix, s1, s2)

        sys.stdout = sys.__stdout__

        # Assert the captured output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)

        
if __name__ == "__main__":
    unittest.main()
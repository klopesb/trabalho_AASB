import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.my_blosum import Blosum62
from pprint import pprint

blosum = Blosum62()

def subst(x, y):
    """
    Substitution function that returns the substitution score for characters x and y
    based on the BLOSUM62 matrix.
    """
    return blosum.subst(x, y)

def global_score(s1, s2, g=-8):
    """
    Implements the global alignment algorithm (Needleman-Wunsch) to find the best matching
    subsequence between s1 and s2.
    
    Arguments:
    - s1 (str): First sequence to align.
    - s2 (str): Second sequence to align.
    - g (int, optional): Gap penalty (by default is -8).
    
    Returns:
    - score (int): The final global alignment score.
    """
    scoring_matrix = global_matrix(s1, s2, g)
    return scoring_matrix[len(s1)][len(s2)]

def global_matrix(s1, s2, g=-8):
    """
    Implements the global alignment algorithm (Needleman-Wunsch) to compute the scoring matrix.
    
    Arguments:
    - s1 (str): First sequence to align.
    - s2 (str): Second sequence to align.
    - g (int, optional): Gap penalty (by default is -8).
    
    Returns:
    - matrix (list of lists): The final scoring matrix.
    """
    m, n = len(s1), len(s2)
    scoring_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column with gap penalties
    for i in range(1, m + 1):
        scoring_matrix[i][0] = i * g
    for j in range(1, n + 1):
        scoring_matrix[0][j] = j * g

    # Fill the scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = scoring_matrix[i - 1][j - 1] + subst(s1[i - 1], s2[j - 1])
            delete = scoring_matrix[i - 1][j] + g
            insert = scoring_matrix[i][j - 1] + g
            scoring_matrix[i][j] = max(match, delete, insert)

    return scoring_matrix

def align_sequences(scoring_matrix, s1, s2, g=-8):
    """
    Reconstructs the optimal alignment from the scoring matrix.

    Arguments:
    - scoring_matrix (list of lists): The scoring matrix computed by the Needleman-Wunsch algorithm.
    - s1 (str): First sequence.
    - s2 (str): Second sequence.
    - g (int): Gap penalty.

    Returns:
    - aligned_s1 (str): Aligned version of s1.
    - aligned_s2 (str): Aligned version of s2.
    """
    i, j = len(s1), len(s2)
    aligned_s1, aligned_s2 = [], []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and scoring_matrix[i][j] == scoring_matrix[i-1][j-1] + subst(s1[i-1], s2[j-1]):
            aligned_s1.append(s1[i-1])
            aligned_s2.append(s2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and scoring_matrix[i][j] == scoring_matrix[i-1][j] + g:
            aligned_s1.append(s1[i-1])
            aligned_s2.append("-")
            i -= 1
        else:
            aligned_s1.append("-")
            aligned_s2.append(s2[j-1])
            j -= 1

    return "".join(reversed(aligned_s1)), "".join(reversed(aligned_s2))

def print_matrix_with_sequences(scoring_matrix, s1, s2):
    """
    Prints the scoring matrix with the sequences aligned along the top and left edges.

    Arguments:
    - scoring_matrix (list of lists): The scoring matrix.
    - s1 (str): First sequence.
    - s2 (str): Second sequence.
    """
    # Add a gap symbol ("-") to sequences
    s1 = "-" + s1
    s2 = "-" + s2

    # Print the top sequence (s1) with proper alignment
    print("   ", "   ".join(s1))

    # Print the scoring matrix with the left sequence (s2)
    for i, row in enumerate(scoring_matrix):
        print(s2[i], " ".join(f"{cell:>3}" for cell in row))
        
if __name__ == "__main__":
    s1 = "HGWAG"
    s2 = "PHSWG"

    # Compute the scoring matrix and final alignment
    scoring_matrix = global_matrix(s1, s2)
    score = scoring_matrix[len(s1)][len(s2)]
    aligned_s1, aligned_s2 = align_sequences(scoring_matrix, s1, s2)

    # Print the results
    print("Global alignment score:", score)
    print("\nScoring matrix:")
    print_matrix_with_sequences(scoring_matrix, s1, s2)

    print("\nOptimal global alignment:")
    print("Sequence 1:", aligned_s1)
    print("Sequence 2:", aligned_s2)

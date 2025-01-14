from src.my_blosum import Blosum62
from pprint import pprint

blosum = Blosum62()

def subst(x, y):
    """
    Substitution function that returns the substitution score for characters x and y
    based on the BLOSUM62 matrix.
    """
    return blosum.subst(x, y)

def local_score(s1, s2, g=-8):
    """
    Implements local alignment (Smith-Waterman) to find the best matching subsequence
    between s1 and s2.
    """
    # Matrix to store scores
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_score = 0

    # Fill the scoring matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + subst(s1[i - 1], s2[j - 1])  # Substitution
            delete = dp[i - 1][j] + g                              # Gap in s2
            insert = dp[i][j - 1] + g                              # Gap in s1
            dp[i][j] = max(0, match, delete, insert)               # Reset to 0 if score is negative
            max_score = max(max_score, dp[i][j])                   # Update max score

    return max_score  # Return only the maximum score

def local_matrix(s1, s2, g=-8):
    """
    Computes the scoring matrix for local alignment (Smith-Waterman).
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the scoring matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + subst(s1[i - 1], s2[j - 1])
            delete = dp[i - 1][j] + g
            insert = dp[i][j - 1] + g
            dp[i][j] = max(0, match, delete, insert)  # Reset to 0 for local alignment

    return dp

def traceback(dp, s1, s2, g=-8):
    """
    Performs traceback to retrieve the optimal local alignment.
    """
    n, m = len(s1), len(s2)
    max_score = 0
    max_pos = (0, 0)

    # Find the position of the maximum score
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] > max_score:
                max_score = dp[i][j]
                max_pos = (i, j)

    i, j = max_pos
    aligned_s1, aligned_s2 = "", ""

    # Traceback from the maximum score
    while i > 0 and j > 0 and dp[i][j] > 0:
        if dp[i][j] == dp[i - 1][j - 1] + subst(s1[i - 1], s2[j - 1]):
            aligned_s1 = s1[i - 1] + aligned_s1
            aligned_s2 = s2[j - 1] + aligned_s2
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + g:
            aligned_s1 = s1[i - 1] + aligned_s1
            aligned_s2 = "-" + aligned_s2
            i -= 1
        else:
            aligned_s1 = "-" + aligned_s1
            aligned_s2 = s2[j - 1] + aligned_s2
            j -= 1

    return aligned_s1, aligned_s2

def print_matrix_with_sequences(matrix, s1, s2):
    """
    Prints the scoring matrix with the sequences aligned at the top and left edges.
    """
    # Add gap symbol ("-") to the sequences
    s1 = "-" + s1
    s2 = "-" + s2

    # Print the top sequence with proper alignment
    print("   ", "   ".join(s1))

    # Print each row of the matrix with the left sequence
    for i, row in enumerate(matrix):
        print(s2[i], " ".join(f"{cell:>3}" for cell in row))

if __name__ == "__main__":
    s1 = "HGWAG"
    s2 = "PHSWG"
    score = local_score(s1, s2)
    scoring_matrix = local_matrix(s1, s2)
    aligned_s1, aligned_s2 = traceback(scoring_matrix, s1, s2)

    print("Local alignment score:", score)
    print("\nScoring matrix:")
    print_matrix_with_sequences(scoring_matrix, s1, s2)
    print("\nOptimal local alignment:")
    print("Sequence 1:", aligned_s1)
    print("Sequence 2:", aligned_s2)

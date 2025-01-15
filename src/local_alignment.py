from .my_blosum import Blosum62
from pprint import pprint

blosum = Blosum62()

def subst(x, y):
    """
    Calculates the substitution score for aligning two characters `x` and `y` based on the BLOSUM62 matrix.

    Args:
    - x (str): A character from the first sequence.
    - y (str): A character from the second sequence.

    Returns:
    - int: The substitution score from the BLOSUM62 matrix.
    """
    return blosum.subst(x, y)

def local_score(s1, s2, g=-8):
    """
    Computes the maximum alignment score for local alignment (Smith-Waterman) between two sequences.

    Args:
    - s1 (str): The first sequence to align.
    - s2 (str): The second sequence to align.
    - g (int): The gap penalty, default is -8.

    Returns:
    - int: The highest alignment score found in the scoring matrix.
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_score = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + subst(s1[i - 1], s2[j - 1])      # Substitution
            delete = dp[i - 1][j] + g                                   # Gap in s2
            insert = dp[i][j - 1] + g                                   # Gap in s1
            dp[i][j] = max(0, match, delete, insert)                    # Reset to 0 if score is negative
            max_score = max(max_score, dp[i][j])                        # Update max score

    return max_score                                                     

def local_matrix(s1, s2, g=-8):
    """
    Computes the full scoring matrix for local alignment (Smith-Waterman) between two sequences.

    Args:
    - s1 (str): The first sequence to align.
    - s2 (str): The second sequence to align.
    - g (int): The gap penalty, default is -8.

    Returns:
    - list[list[int]]: The scoring matrix where each cell represents the optimal alignment score for subsequences ending at that cell.
    """
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + subst(s1[i - 1], s2[j - 1])
            delete = dp[i - 1][j] + g
            insert = dp[i][j - 1] + g
            dp[i][j] = max(0, match, delete, insert)  #Reset to 0 for local alignment

    return dp

def traceback(dp, s1, s2, g=-8):
    """
    Extracts the optimal local alignment from a scoring matrix by performing traceback from the highest scoring cell.

    Args:
    - dp (list[list[int]]): The scoring matrix computed by the Smith-Waterman algorithm.
    - s1 (str): The first sequence.
    - s2 (str): The second sequence.
    - g (int): The gap penalty, default is -8.

    Returns:
    - tuple[str, str]: The aligned subsequences of `s1` and `s2` that correspond to the optimal local alignment.
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
    Prints the scoring matrix with the two sequences aligned to the top and left of the matrix for easier visualization.

    Args:
    - matrix (list[list[int]]): The scoring matrix.
    - s1 (str): The first sequence.
    - s2 (str): The second sequence.

    Returns:
    - None: Prints the matrix directly to the console.
    """
    s1 = "-" + s1
    s2 = "-" + s2

    print("   ", "   ".join(s2))

    for i, row in enumerate(matrix):
        print(s1[i], " ".join(f"{cell:>3}" for cell in row))

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

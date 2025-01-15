# High-Level Project Plan - Local Alignment

## 1. Description

This project aims to implement sequence alignment algorithms for biological sequence comparison, focusing on local alignment using the Smith-Waterman algorithm. The algorithm will identify the best matching subsequence between two sequences, allowing for the alignment of the most similar parts of the sequences, even if the sequences have substantial differences.  
The alignment will be computed using the BLOSUM62 substitution matrix for amino acid substitutions and a linear gap penalty for insertions and deletions. The project will involve implementing the core algorithm, validating it through unit tests, and optimizing it for performance on larger sequences.

## 2. Key Features of the Project

- **Local Alignment (Smith-Waterman)**: Identifies the best matching subsequence, which is particularly useful for aligning parts of sequences that are similar.
- **Scoring System**: Uses the BLOSUM62 substitution matrix and gap penalties for accurate sequence comparison.
- **Backtracking**: Retrieves the optimal alignment subsequences from the scoring matrix.
- **Unit Testing**: Ensures the correctness of the implementation by testing edge cases and expected results.

The end result of this project will be a robust and efficient tool for performing local sequence alignments, useful for biological sequence analysis in genomics, proteomics, and bioinformatics.

---

# Low-Level Project Plan - Local Alignment

## a) Problem Understanding

### 1. Goal Definition
- The primary goal is to perform local alignment between two biological sequences. Local alignment identifies the best matching subsequence between two sequences, which is useful for detecting similarities even if the sequences have significant differences.

### 2. Substitution Matrix
- Use the BLOSUM62 matrix for substitution scores, which is widely used for protein sequence alignment. The matrix will provide scores for each pair of amino acids, and we will integrate gap penalties to account for insertions and deletions.

### 3. Gap Penalty
- Use a linear gap penalty for insertions and deletions, configurable (e.g., -8 for each gap).

---

## b) Design

### 1. Substitution Function
- Develop a function that computes the substitution score for two aligned characters based on the BLOSUM62 matrix.

### 2. Dynamic Programming Algorithm
- Implement the Smith-Waterman algorithm:
  - **Initialization**: Create a scoring matrix where each cell represents the alignment score for the corresponding subsequences of the two sequences.
  - **Matrix Filling**: Fill the matrix using the substitution scores and gap penalties.
  - **Traceback**: Trace back from the highest score to find the optimal local alignment.

### 3. Backtracking
- After filling the scoring matrix, implement the backtracking procedure to extract the optimal local alignment.

---

## c) Implementation

### 1. Scoring Matrix Calculation
- Write a function that computes the full scoring matrix using the Smith-Waterman algorithm.

### 2. Backtracking Function
- Implement a backtracking function that finds the optimal local alignment by starting at the highest score in the matrix and tracing back to where the score is zero or a gap.

### 3. Edge Case Handling
- Handle edge cases such as empty sequences or sequences with no alignment properly.

---

## d) Validation

### 1. Unit Tests
- Write unit tests to verify the correctness of the algorithm:
  - **Basic Test**: Test alignment between two small sequences (e.g., "GATTACA" vs "GATTA").
  - **Edge Cases**: Test cases for empty sequences, sequences with no matching subsequences, sequences of different lengths, etc.
  - **Expected Results**: Use known test cases and expected scores for validation.

### 2. Performance Tests
- Test the algorithm on larger sequences to evaluate its performance.
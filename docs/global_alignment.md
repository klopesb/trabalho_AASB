# High-Level Project Plan - Global Alignment

## 1. Description

This project focuses on implementing sequence alignment algorithms for biological sequence comparison, specifically using the Needleman-Wunsch algorithm for global alignment. The alignment process ensures that entire sequences are compared, including penalties for gaps and mismatches, to find the best possible alignment across their full lengths.

## 2. Key Features of the Project

- **Global Alignment**: The Needleman-Wunsch algorithm is implemented to find the optimal alignment for two sequences from start to finish.
- **Substitution Matrix**: The BLOSUM62 matrix is used to calculate biologically relevant substitution scores for amino acids.
- **Gap Penalties**: Linear gap penalties are applied to account for insertions and deletions in the alignment.
- **Dynamic Programming**: The algorithm employs a scoring matrix and traceback procedure to calculate alignment scores and reconstruct the optimal alignment.
- **Unit Testing**: A comprehensive set of tests validates the implementation, covering edge cases, expected results, and performance on larger sequences.

The project is designed to provide an accurate and efficient tool for global sequence alignment, making it a valuable resource for biological sequence analysis in genomics and proteomics.

---

# Low-Level Project Plan - Global Alignment

## a) Problem Understanding

### 1. Goal Definition
- Perform global alignment of biological sequences using a substitution matrix (BLOSUM62) and configurable gap penalties.
- The goal is to identify the best possible alignment of the entire sequences, ensuring that all characters are considered from start to finish.

### 2. Substitution Matrix
- Use the BLOSUM62 matrix to assign scores for matching or mismatched pairs of amino acids. This matrix provides biologically relevant substitution scores.

### 3. Gap Penalty
- Introduce a linear gap penalty for insertions or deletions, which is subtracted for each gap introduced during the alignment.

---

## b) Design

### 1. Substitution Function
- Develop a function to calculate substitution scores between two characters using the BLOSUM62 matrix.  
  Example: `subst("A", "G")` returns the substitution score for aligning "A" with "G".

### 2. Dynamic Programming Algorithm
- Implement the Needleman-Wunsch algorithm for global alignment. Key components:
  - **Initialization**: Initialize the scoring matrix with gap penalties for the first row and column.
  - **Matrix Filling**: Populate the scoring matrix using dynamic programming rules, considering substitution scores and gap penalties.
  - **Traceback**: Implement a traceback procedure to retrieve the optimal alignment from the scoring matrix.

### 3. Handling Edge Cases
- Account for scenarios such as empty sequences, identical sequences, or completely mismatched sequences.

---

## c) Implementation

### 1. Scoring Matrix Calculation
- Write a function to compute the scoring matrix based on the Needleman-Wunsch algorithm. This function will calculate scores for all possible alignments of the sequences.

### 2. Traceback Function
- Implement a function to trace back through the scoring matrix to reconstruct the aligned sequences.

### 3. Customizable Parameters
- Allow users to configure gap penalties and optionally use different substitution matrices (e.g., PAM matrices).

---

## d) Validation

### 1. Unit Tests
- Develop unit tests to ensure correctness. Include:
  - **Basic Tests**: Simple sequences (e.g., "ACT" vs "ACT") with known expected scores.
  - **Edge Cases**: Empty sequences, sequences with different lengths, completely mismatched sequences.
  - **Known Results**: Compare results against reference alignments from established tools like EMBOSS Needle.

### 2. Performance Tests
- Evaluate the algorithm on large sequences to assess runtime and memory usage.
- **Debugging and Verification**: Print the scoring matrix and alignment results for debugging during development.

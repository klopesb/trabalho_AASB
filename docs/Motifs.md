# High-Level Project Plan - Motifs

## 1. Description

This project implements a comprehensive tool for calculating **PWM (Position Weight Matrix)**, **PSSM (Position Specific Scoring Matrix)**, and sequence evaluation to identify the most probable subsequences within biological sequences. Additionally, it supports deterministic and stochastic motif identification based on defined thresholds or exact matches. The project aims to provide foundational bioinformatics tools for sequence analysis and motif discovery.

The algorithm processes input sequences to derive positional matrices, evaluate sequence probabilities, and extract significant motifs based on probabilistic or deterministic criteria. It is designed for modularity, making it suitable for extending functionality in advanced genomic studies.

---

## 2. Key features of the project

### PWM and PSSM Calculation:
- **PWM Calculation**: Computes a position weight matrix by normalizing sequence symbol frequencies, considering pseudocounts.
- **PSSM Calculation**: Derives a position-specific scoring matrix using log-odds against background frequencies. Includes customizable background frequency input.
- **Sequence Evaluation**: Computes the probability of a given sequence based on PWM. Identifies the most probable subsequences of specified lengths using a sliding window approach.

### Motif Identification:
- **Deterministic Motifs**: Finds exact subsequence matches across all input sequences.
- **Stochastic Motifs**: Identifies high-probability motifs based on PWM and user-defined thresholds.

### Validation and Error Handling:
- Ensures input sequences are uniform in length.
- Validates sequence content against supported alphabets (DNA or protein).
- Handles missing or incomplete background frequency data.

### Unit Testing and Debugging:
- Provides comprehensive test cases for validation, PWM/PSSM computation, and motif identification.
- Includes edge cases like empty sequences, invalid characters, and zero probabilities.

The result of this project is a versatile sequence analysis tool that combines probabilistic modeling with motif detection. It is suitable for analyzing biological data and serves as a foundation for more sophisticated genomic tools.

The project delivers a versatile and modular sequence analysis tool by generating precise PWM and PSSM outputs tailored to the input sequences, suitable for motif discovery and probabilistic analysis.

---

# Low-Level Project Plan - Motifs

## 1. PWM and PSSM:
- **PWM (Position Weight Matrix)**: Represents the normalized frequency of each symbol at each position in the input sequences. Accounts for pseudocounts to prevent zero probabilities.
- **PSSM (Position Specific Scoring Matrix)**: Converts the PWM into a scoring matrix using log-odds ratios relative to background frequencies. Scores each symbol based on its overrepresentation compared to a uniform or custom background distribution.

## 2. Motif Identification:
- **Deterministic Motifs**: Identifies exact subsequences shared across all input sequences.
- **Stochastic Motifs**: Finds motifs with probabilities exceeding a user-defined threshold, leveraging PWM probabilities.

## 3. Libraries and Dependencies:
- **Standard Python Libraries**:
  - `math`: Used for log computations and product calculations.
  - `re`: For sliding window operations and subsequence extraction.
- **Testing**:
  - `unittest`: Framework for validating functionality through test cases.

---

## a) Input
### Sequences:
- A list of sequences (`seqs`) for PWM and PSSM calculation.
- A single query sequence (`seq`) for motif and probability evaluation.

### Parameters:
- **tipo**: Specifies the sequence type ("DNA" or "PROTEIN").
- **Pseudocount (pseudocontagem)**: Adjusts symbol counts to avoid zero probabilities.
- **Background Frequencies (bg_freq)**: Optional dictionary of expected symbol frequencies.
- **Threshold (threshold)**: Used for stochastic motif filtering.

## b) Output
### Matrices:
- **PWM**: A list of dictionaries representing the normalized frequencies of symbols at each position.
- **PSSM**: A list of dictionaries representing the log-odds scores of symbols at each position.

### Probabilities:
- **Sequence probability**: Likelihood of the query sequence based on the PWM.
- **Most probable subsequences**: Substrings of the query sequence with the highest PWM-derived probability.

### Motifs:
- **Deterministic motifs**: Exact matches across sequences.
- **Stochastic motifs**: High-probability motifs exceeding the threshold.

## c) Functions
### PWM and PSSM Calculation:
- `pwm_pssm_e_sequencia_mais_provavel(seqs, seq, tipo, pseudocontagem, casas_decimais, bg_freq)`:
  - Computes PWM and PSSM.
  - Evaluates sequence probability and identifies most probable subsequences.

### Motif Finder:
- `encontrar_motivos(seqs, pwm, tipo, threshold)`:
  - Identifies deterministic or stochastic motifs based on the user-defined mode.

### Validation:
- Built-in checks for sequence uniformity, input validity, and completeness of background frequencies.

## d) Algorithm Implementation
### Input Validation:
- Ensure all sequences in `seqs` are of equal length.
- Validate characters against the specified alphabet (DNA or PROTEIN).
- Verify that `bg_freq` covers the full alphabet.

### PWM Calculation:
- Initialize a frequency table for each position in the sequences.
- Count symbol occurrences, adding pseudocounts.
- Normalize by the total sequence count and pseudocount adjustment.

### PSSM Calculation:
- Compute log-odds scores for each PWM value using background frequencies.
- Handle zero probabilities by substituting -inf.

### Sequence Probability:
- Multiply PWM probabilities for symbols in the query sequence.
- Return a probability of 0 if any symbol is absent in the PWM.

### Most Probable Subsequence:
- Extract all subsequences of the motif length from the query sequence.
- Compute their probabilities using the PWM.
- Return the subsequences with the highest probability.

### Motif Identification:
- **Deterministic**: Extract motifs of the PWM length from the first sequence. Verify their presence in all sequences.
- **Stochastic**: Filter subsequences based on their PWM-derived probabilities exceeding the threshold.

### Testing and Debugging:
- Create unit tests for validation, PWM/PSSM correctness, and motif identification.
- Test with edge cases: empty sequences, mismatched lengths, or invalid characters.

## e) Testing
### Basic Cases:
- Simple motifs: Short, identical sequences for deterministic motif validation.
- Uniform background frequencies for straightforward PWM/PSSM tests.

### Edge Cases:
- Sequences with invalid characters or mixed lengths.
- Query sequences shorter than the motif length.

### Complex Cases:
- Stochastic motifs with varying thresholds.
- Sequences with overlapping motifs or high variability.

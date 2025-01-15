# High-Level Project Plan - Basic Version of Blast

## 1. Description

This project implements a simplified sequence matching and alignment tool designed for biological sequence comparison - Basic Version of BLAST. The focus is on identifying matching substrings (words) between a query sequence and a database sequence, extending the matches to find regions of similarity, and determining the best alignment based on an extension score.
The result is a tool suitable for preliminary sequence analysis in genomics and bioinformatics applications.

## 2. Key Features of the Project

- **Word-Based Mapping**: Maps all substrings (of length w) in the query sequence to their positions for fast lookup.
- **Matching (Hits Identification)**: Compares the query substrings with the database sequence to identify matching regions (hits).
- **Hit Extension**: Extends matching substrings forward and backward to find the largest contiguous region of similarity. Uses a simple scoring system based on matches and mismatches to optimize the extension.
- **Best Hit Selection**: Scores all extended matches and selects the one with the highest score as the best alignment.
- **Unit Testing and Debugging**: Each function can be independently tested for correctness with various sequences and parameters.

While not as sophisticated as algorithms like Smith-Waterman or Needleman-Wunsch, it provides a foundation for understanding sequence alignment concepts and is useful for word-based sequence matching tasks. 

---

# Low-Level Project Plan - Basic Version of Blast

## a) Problem Understanding

### Goal Definition:
- Identify local alignments between two sequences by finding exact word matches (w-mers) and extending them to determine the longest alignment.

### Core Functions:
- **query_map**: Builds a dictionary of substrings (w-mers) from the query and their positions.
- **hits**: Matches the query dictionary to the database sequence and records hit positions.
- **extend_hit**: Extends the matched words to form the longest alignment.
- **best_hit**: Finds the alignment with the highest score based on the extended matches.

## b) Design

- **Query Mapping (query_map)**: Create a mapping of substrings of length `w` and their starting indices in the query sequence.

- **Hit Detection (hits)**: Compare substrings in the query map to the database sequence, recording the indices of matches.

- **Extension Logic (extend_hit)**: Extend matches both forward and backward to form the longest possible alignment. Compute alignment length and match count beyond the initial word length.

- **Best Match Selection (best_hit)**: Use the hits and extend_hit outputs to identify the best alignment by evaluating size and match score.

## c) Implementation

### Functions:

- **query_map**: Generate a dictionary mapping w-mers to indices in the query sequence.

- **hits**: Compare w-mers in the database sequence to those in the query map. Record hits as (query_index, db_index) tuples.

- **extend_hit**: Extend matches in both directions (forward and backward) until mismatches occur or the sequence ends. Calculate the total size of the alignment and the total number of matches.

- **best_hit**: Iterate over all hits to find the one with the largest score or alignment size.

### Output:

- **Query Map**: A dictionary of w-mers and their positions in the query sequence.
  
- **Hit List**: A list of tuples showing where the query aligns with the database.
  
- **Best Hit**: A tuple showing the starting indices in both sequences, the alignment size, and the total matches.

## d) Validation

### Unit Tests:
- Test small and simple inputs to verify correctness:

  **Example 1:**
  - Query: `"AATAT"`
  - Database: `"GATAATATG"`

  **Expected Output:**
  - Query Map: `{ "AAT": [0, 2], "ATA": [1], "TAT": [3] }`
  - Hits: `[(0, 3), (2, 4), (3, 5)]`
  - Best Hit: `(0, 3, 5, 3)`

  **Example 2:**
  - Query: `"GCC"`
  - Database: `"GCGC"`

  **Expected Output:**
  - Query Map: `{ "GCC": [0] }`
  - Hits: `[]`
  - Best Hit: `()`

### Edge Cases:
- Query or database sequence is empty.
- Word length `w` is larger than either sequence length.
- No matches between the query and database sequences.

### Performance Tests:
- Test with increasing sequence lengths to ensure the tool scales effectively.

## e) Optimization

### Efficiency:
- Ensure that `query_map` creation and `hits` lookup are efficient for longer sequences by using Python dictionaries effectively.

### Error Handling:
- Validate inputs to prevent invalid configurations (e.g., negative or zero word length).

## f) Documentation

### Code Comments:
- Clearly comment on the purpose and logic of each function.

### User Guide:
- Include a simple explanation of:
  - Input requirements (query, database sequence, and word length `w`).
  - Outputs for each function.

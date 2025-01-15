# Multiple Sequence Alignment Overview

## High Level Overview

The Star Alignment algorithm is a progressive multiple sequence alignment method that uses a center sequence as a reference to align all other sequences.


### Key Steps

1. **Center Selection**
   - Choose the longest sequence as the center sequence
   - This sequence will serve as the reference for all pairwise alignments

2. **Pairwise Alignments**
   - Align each remaining sequence to the center sequence
   - Use global alignment for each pair
   - Store the alignments in a mapping structure

3. **Alignment Coordination**
   - Ensure all sequences have the same length by adding gaps where necessary
   - Maintain alignment consistency across all sequences

4. **Result Generation**
   - Return aligned sequences in their original order
   - All sequences will have equal length
   - Gaps (-) indicate insertion/deletion events

### Advantages and Limitations

**Advantages:**
- Simple to implement and understand
- Computationally efficient
- Works well for closely related sequences

**Limitations:**
- Quality depends heavily on center sequence choice
- May not find the optimal alignment for divergent sequences
- Less accurate than more sophisticated methods like ClustalW

## Low Level Implementation Details

### Core Functions and Data Structures

#### star_alignment(sequences)

##### Input Processing
```python
if not sequences:
    raise ValueError("No sequences provided")
center = max(sequences, key=len)
alignment_map = {center: center}
```

##### Main Algorithm Components

1. **Pairwise Alignment Phase**
   - Uses global alignment matrix calculation:
   ```python
   matrix = global_matrix(center, seq)
   aligned_center, aligned_seq = align_sequences(matrix, center, seq)
   ```

2. **Length Normalization**
   - Tracks maximum alignment length
   - Adds padding where necessary:
   ```python
   if len(aligned_center) > max_length:
       padding = '-' * (len(aligned_center) - max_length)
       # Pad existing alignments
   ```

3. **Result Assembly**
   - Maintains original sequence order
   - Returns list of aligned sequences

### Dependencies

- Relies on global alignment functions:
  - global_matrix()
  - align_sequences()

### Complexity Analysis
- **Time Complexity**: O(N * L^2) where:
  - N = number of sequences
  - L = length of longest sequence
- **Space Complexity**: O(N * L) for storing aligned sequences

### Example Illustration

Consider three DNA sequences to be aligned:
```
Seq1: ATCG
Seq2: ATTCG
Seq3: TCG
```

Star alignment process using Seq2 (longest) as center:

1. Initial center selection (Seq2):
```
ATTCG
```

2. Align Seq1 to center:
```
ATTCG (center)
AT-CG (Seq1)
```

3. Align Seq3 to center:
```
ATTCG (center)
AT-CG (Seq1)
-TTCG (Seq3)
```

Final alignment:
```
AT-CG
ATTCG
-TTCG
```

This example shows how gaps (-) are inserted to maintain alignment length and preserve sequence relationships.

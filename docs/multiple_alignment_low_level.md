# Multiple Sequence Alignment - Low Level Implementation Details

## Core Functions and Data Structures

### star_alignment(sequences)

#### Input Processing
```python
if not sequences:
    raise ValueError("No sequences provided")
center = max(sequences, key=len)
alignment_map = {center: center}
```

#### Main Algorithm Components

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

### Time Complexity
- O(N * L^2) where:
  - N = number of sequences
  - L = length of longest sequence

### Space Complexity
- O(N * L) for storing aligned sequences

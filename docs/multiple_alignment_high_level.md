# Multiple Sequence Alignment - High Level Overview

## Star Alignment Algorithm

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

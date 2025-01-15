# Phylogenetic Tree Construction - High Level Overview

## UPGMA Tree Building Algorithm

The Unweighted Pair Group Method with Arithmetic Mean (UPGMA) is used to construct phylogenetic trees from sequence data.

### Key Steps

1. **Sequence Processing**
   - Take multiple aligned sequences as input
   - Optional naming of sequences

2. **Distance Calculation**
   - Compute pairwise distances between sequences
   - Use identity-based distance metric

3. **Tree Construction**
   - Build hierarchical clustering using UPGMA
   - Create nodes and branches based on distances
   - Connect related sequences into a tree structure

4. **Visualization**
   - Output tree in various formats:
     - ASCII visualization
     - Newick format
     - Tree structure object

### Advantages and Limitations

**Advantages:**
- Simple and intuitive approach
- Fast computation
- Good for closely related sequences

**Limitations:**
- Assumes constant evolution rate
- May not accurately represent complex evolutionary relationships
- Sensitive to input sequence order

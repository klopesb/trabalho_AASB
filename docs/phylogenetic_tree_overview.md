# Phylogenetic Tree Construction Overview

## High Level Overview

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

## Low Level Implementation Details

### Core Functions and Data Structures

#### create_phylogenetic_tree(sequences, sequence_names)

##### Input Processing
```python
if not sequences:
    raise ValueError("No sequences provided")
sequence_names = [f"Seq_{i+1}" for i in range(len(sequences))]
records = [SeqRecord(Seq(seq), id=name) for seq, name in zip(sequences, sequence_names)]
```

##### Main Algorithm Components

1. **Sequence Record Creation**
   - Convert sequences to BioPython SeqRecord objects
   - Create MultipleSeqAlignment object

2. **Distance Matrix Calculation**
   ```python
   calculator = DistanceCalculator('identity')
   dm = calculator.get_distance(alignment)
   ```

3. **Tree Construction**
   ```python
   constructor = DistanceTreeConstructor(calculator, 'upgma')
   tree = constructor.build_tree(alignment)
   ```

### Supporting Functions

1. **tree_to_newick(tree)**
   - Converts tree to Newick format string
   - Uses StringIO for string conversion

2. **display_ascii_tree(tree)**
   - Creates ASCII visualization
   - Uses BioPython's draw_ascii function

### Dependencies
- BioPython library:
  - Bio.Phylo
  - Bio.Phylo.TreeConstruction
  - Bio.Align
  - Bio.Seq
  - Bio.SeqRecord

### Complexity Analysis
- **Time**: O(N^2) for distance matrix calculation
- **Space**: O(N^2) for storing distance matrix
  where N = number of sequences

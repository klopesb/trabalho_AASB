# Bioinformatics Sequence Analysis Tools

A collection of Python tools for biological sequence analysis, including:

- DNA/RNA sequence validation and conversion
- Global sequence alignment (Needleman-Wunsch algorithm)
- Local sequence alignment (Smith-Waterman algorithm)
- Multiple sequence alignment (Star alignment method)
- Phylogenetic tree construction (UPGMA method)

## Features

- Pairwise sequence alignment with BLOSUM62 scoring
- Multiple sequence alignment capabilities
- Phylogenetic tree visualization (ASCII output)
- Built-in BLOSUM62 substitution matrix

## Requirements

- Python 3.x
- Biopython (for phylogenetic tree functionality)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/trabalho_AASB.git
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Example Usage

Each module includes example cases that demonstrate basic functionality:

```python
# Run global alignment example with sequences "HGWAG" and "PHSWG"
python -m src.global_alignment

# Run local alignment example with sequences "HGWAG" and "PHSWG"
python -m src.local_alignment

# Run multiple sequence alignment example with sequences:
# "MEEPQSDPSY", "MEEPQSDPSV", "MEEPQSDLSV"
python -m src.multiple_alignment

# Run phylogenetic tree construction example with the above sequences
python -m src.phylogenetic_tree

# Run DNA/RNA conversion and analysis example
python -m src.dna_rna_amino

# Run protein sequence analysis example
python -m src.get_proteins
```

For actual use in your code, import the modules and use their functions:

```python
from src.global_alignment import global_score, global_matrix, align_sequences
from src.local_alignment import local_score, local_matrix, traceback
from src.multiple_alignment import star_alignment
from src.phylogenetic_tree import create_phylogenetic_tree, display_ascii_tree, tree_to_newick

# Example: Perform global alignment
s1, s2 = "HGWAG", "PHSWG"
score = global_score(s1, s2)
matrix = global_matrix(s1, s2)
aligned_s1, aligned_s2 = align_sequences(matrix, s1, s2)
print(f"Score: {score}")
print(f"Aligned 1: {aligned_s1}")
print(f"Aligned 2: {aligned_s2}")

# Example: Create and visualize a phylogenetic tree
sequences = ["MEEPQSDPSY", "MEEPQSDPSV", "MEEPQSDLSV"]
names = ["Human", "Mouse", "Rat"]
tree = create_phylogenetic_tree(sequences, sequence_names=names)
display_ascii_tree(tree)  # Show tree in console
newick = tree_to_newick(tree)  # Get Newick format string
print(f"Newick format: {newick}")

# Example: DNA/RNA sequence analysis
from src.dna_rna_amino import main, get_sequence_type, count_bases

# Analyze a sequence
dna_seq = "ATCG"
result = main(dna_seq)
print(result)  # Shows RNA conversion and base counts

# Get sequence type
seq_type = get_sequence_type("AUCG")
print(f"Sequence type: {seq_type}")  # Shows "RNA"

# Count bases in sequence
base_counts = count_bases("ATCGATCG")
print(f"Base counts: {base_counts}")  # Shows frequency of each base

# Example: Protein sequence analysis
from src.get_proteins import get_all_proteins, compute_reverse_complement

# Get all possible proteins from a DNA sequence
dna = "ATGCATGCTAAGTATTAG"
proteins = get_all_proteins(dna)
print(f"Found proteins: {proteins}")

# Get reverse complement of DNA
rev_comp = compute_reverse_complement(dna)
print(f"Reverse complement: {rev_comp}")
```

## Running Tests

The project includes comprehensive unit tests in the `tests` folder. To run the tests:

```bash
# Run all tests
python -m unittest discover -s tests

# Run specific test files
python -m unittest tests.test_global
python -m unittest tests.test_local
python -m unittest tests.test_multiple_alignment
python -m unittest tests.test_phylogenetic_tree
python -m unittest tests.test_dna_rna_amino
python -m unittest tests.test_get_proteins
```

## License

This project is open source and available under the MIT License.

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

### Sequence Alignment
```python
# For global alignment
python src/global_alignment.py

# For local alignment
python src/local_alignment.py

# For multiple sequence alignment
python src/multiple_alignment.py
```

### Phylogenetic Tree Construction
```python
python src/phylogenetic_tree.py
```

## License

This project is open source and available under the MIT License.

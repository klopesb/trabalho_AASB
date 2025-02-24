from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from io import StringIO

def create_phylogenetic_tree(sequences, sequence_names=None):
    """
    Creates a phylogenetic tree from a list of sequences using UPGMA method.
    
    Args:
        sequences: List of aligned sequences
        sequence_names: List of names for the sequences (optional)
        
    Returns:
        tree: Phylogenetic tree object
    """
    if not sequences:
        raise ValueError("No sequences provided")
        
    if sequence_names is None:
        sequence_names = [f"Seq_{i+1}" for i in range(len(sequences))]
    
    if len(sequences) != len(sequence_names):
        raise ValueError("Number of sequences and names must match")
        
    # Create SeqRecord objects
    records = []
    for seq, name in zip(sequences, sequence_names):
        records.append(SeqRecord(Seq(seq), id=name))
    
    # Create multiple sequence alignment
    alignment = MultipleSeqAlignment(records)
    
    # Calculate distance matrix
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(alignment)
    
    # Construct tree using UPGMA
    constructor = DistanceTreeConstructor(calculator, 'upgma')
    tree = constructor.build_tree(alignment)
    
    return tree

def tree_to_newick(tree):
    """
    Converts a tree object to Newick format string.
    
    Args:
        tree: Phylogenetic tree object
        
    Returns:
        str: Tree in Newick format
    """
    tree_io = StringIO()
    Phylo.write(tree, tree_io, 'newick')
    return tree_io.getvalue()

def display_ascii_tree(tree):
    """
    Displays the phylogenetic tree in ASCII format in the console.
    
    Args:
        tree: Phylogenetic tree object
    """
    Phylo.draw_ascii(tree)

if __name__ == "__main__":
    # Example sequences (already aligned)
    sequences = [
        "MEEPQSDPSY",
        "MEEPQSDPSV",
        "MEEPQSDLSV"
    ]
    sequence_names = ["Human", "Mouse", "Rat"]
    
    # Create and visualize the tree
    tree = create_phylogenetic_tree(sequences, sequence_names)
    
    print("Tree in ASCII format:")
    display_ascii_tree(tree)
    
    print("\nTree in Newick format:")
    print(tree_to_newick(tree))

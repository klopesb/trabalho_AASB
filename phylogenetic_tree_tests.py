import unittest
from phylogenetic_tree import create_phylogenetic_tree, tree_to_newick
import os

class TestPhylogeneticTree(unittest.TestCase):
    def setUp(self):
        self.sequences = [
            "HEAGAWGHEE",
            "HEAGAWGHEE",
            "HEAGAWGHAE",
            "HEAGAWGHEE",
            "HEAGAWGHAE"
        ]
        self.names = ["Seq1", "Seq2", "Seq3", "Seq4", "Seq5"]
        
    def test_empty_input(self):
        """Test handling of empty input"""
        with self.assertRaises(ValueError):
            create_phylogenetic_tree([])
            
    def test_sequence_name_mismatch(self):
        """Test handling of mismatched sequence and name counts"""
        with self.assertRaises(ValueError):
            create_phylogenetic_tree(self.sequences, sequence_names=self.names[:-1])
            
    def test_tree_creation(self):
        """Test basic tree creation"""
        tree = create_phylogenetic_tree(self.sequences)
        self.assertIsNotNone(tree)
        
    def test_tree_with_names(self):
        """Test tree creation with custom sequence names"""
        tree = create_phylogenetic_tree(self.sequences, sequence_names=self.names)
        newick = tree_to_newick(tree)
        # Verify all names are present in the Newick string
        for name in self.names:
            self.assertIn(name, newick)
            
    def test_tree_visualization(self):
        """Test tree visualization output"""
        output_file = "test_tree.png"
        try:
            tree = create_phylogenetic_tree(self.sequences, output_file=output_file)
            self.assertTrue(os.path.exists(output_file))
        finally:
            # Clean up
            if os.path.exists(output_file):
                os.remove(output_file)

if __name__ == '__main__':
    unittest.main()

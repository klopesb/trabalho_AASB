import unittest
from src.phylogenetic_tree import create_phylogenetic_tree, tree_to_newick
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
        # Capture stdout to verify ASCII tree output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        
        tree = create_phylogenetic_tree(self.sequences)
        display_ascii_tree(tree)
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Verify that something was output (exact format may vary)
        self.assertGreater(len(captured_output.getvalue()), 0)

if __name__ == '__main__':
    unittest.main()

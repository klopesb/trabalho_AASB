import unittest
from src.get_proteins import (
    get_complementary_character,
    compute_reverse_complement,
    extract_codons,
    translate_codons_to_protein,
    extract_proteins,
    get_six_orfs,
    get_all_proteins
)

class TestDNAProcessing(unittest.TestCase):

    def test_get_complementary_character(self):
        self.assertEqual(get_complementary_character("A"), "T")
        self.assertEqual(get_complementary_character("T"), "A")
        self.assertEqual(get_complementary_character("C"), "G")
        self.assertEqual(get_complementary_character("G"), "C")
        self.assertEqual(get_complementary_character("X"), "")  # Invalid base

    def test_compute_reverse_complement(self):
        self.assertEqual(compute_reverse_complement("ATGC"), "GCAT")
        self.assertEqual(compute_reverse_complement("AATTCCGG"), "CCGGAATT")

    def test_extract_codons(self):
        self.assertEqual(extract_codons("ATGCGA"), ["ATG", "CGA"])
        self.assertEqual(extract_codons("ATGCG"), ["ATG"])  # Skips incomplete codon
        self.assertEqual(extract_codons(""), [])

    def test_translate_codons_to_protein(self):
        mock_table = {
            "ATG": "M",
            "CGA": "R",
            "TAA": "_",
        }
        self.assertEqual(translate_codons_to_protein(["ATG", "CGA"], mock_table), "MR")
        self.assertEqual(translate_codons_to_protein(["TAA"], mock_table), "_")

    def test_extract_proteins(self):
        self.assertEqual(extract_proteins("MRL_MF_"), ["MRL_", "MF_"])
        self.assertEqual(extract_proteins("MRL"), [])  # No stop codon
        self.assertEqual(extract_proteins(""), [])

    def test_get_six_orfs(self):
        dna = "ATGCGAATGC"
        expected = [['ATG', 'CGA', 'ATG'],
 ['TGC', 'GAA', 'TGC'],
 ['GCG', 'AAT'],
 ['GCA', 'TTC', 'GCA'],
 ['CAT', 'TCG', 'CAT'],
 ['ATT', 'CGC']]
        self.assertEqual(get_six_orfs(dna), expected)

    def test_get_all_proteins(self):
        dna = "ATGCGATAAATGCGA"
        expected = ["MR_"]
        self.assertEqual(get_all_proteins(dna), expected)

if __name__ == "__main__":
    unittest.main()


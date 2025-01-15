
# High-Level Plan for Implementing the Code

## 1. **Define Constants and Import Dependencies**
   - Define global constants such as `CODON_LENGTH`, `START_CODON`, `STOP_CODON`, and `DNA_COMPLEMENTS`.
   - Import required modules:
     - `List` from `typing` for type annotations.
     - `table` from `table_amino` for codon-to-amino acid mapping.

---

## 2. **Core Functions Implementation**

### 2.1 Complementary Base and Reverse Complement
   - **`get_complementary_character(base: str) -> str`**  
     - Return the complementary DNA base using the `DNA_COMPLEMENTS` mapping.
   - **`compute_reverse_complement(dna: str) -> str`**  
     - Compute the reverse complement of a DNA sequence by reversing it and substituting each base with its complement.

### 2.2 Codon Extraction
   - **`extract_codons(dna: str) -> List[str]`**  
     - Divide the DNA sequence into codons of length `CODON_LENGTH`.

### 2.3 Translation of Codons to Protein
   - **`translate_codons_to_protein(codon_list: List[str], codon_to_amino_table=None) -> str`**  
     - Translate a list of codons into a protein sequence using a codon-to-amino acid mapping table.

### 2.4 Protein Extraction
   - **`extract_proteins(amino_acid_sequence: str) -> List[str]`**  
     - Extract proteins using start ('M') and stop ('_') codons from the amino acid sequence.

---

## 3. **Adding Features**

### 3.1 Stop Codon Processing
   - **`process_stop_codon(proteins, current_protein, active)`**  
     - Handle appending proteins upon encountering a stop codon and reset state for new sequences.

### 3.2 Open Reading Frames (ORFs)
   - **`get_six_orfs(dna: str) -> List[List[str]]`**  
     - Generate six possible ORFs from a DNA sequence:
       1. Three forward-reading ORFs.
       2. Three reverse complement-reading ORFs.

### 3.3 Unique Protein Extraction
   - **`get_all_proteins(dna: str) -> List[str]`**  
     - Extract unique proteins from all six ORFs, sort them by length (descending) and lexicographically.

---

## 4. **Testing the Implementation**

### 4.1 Sample DNA Input
   - Use a sample DNA sequence, e.g., `sample_dna = "ATGCATGCTAAGTATTAG"`.

### 4.2 Test Cases
   - **Reverse Complement:**  
     Test `compute_reverse_complement` with `sample_dna`.
   - **Codon Extraction:**  
     Test `extract_codons` with `sample_dna`.
   - **Protein Translation:**  
     Test `translate_codons_to_protein` using the extracted codons and the amino acid table.
   - **Protein Extraction:**  
     Test `extract_proteins` with the translated protein sequence.
   - **ORFs Generation:**  
     Test `get_six_orfs` with `sample_dna`.
   - **All Proteins Extraction:**  
     Test `get_all_proteins` to ensure unique proteins are extracted and sorted correctly.

---

## 5. **Integrate Error Handling**
   - Use the `if __name__ == '__main__':` block to:
     - Execute each processing step.
     - Print the intermediate results for debugging and validation.
     - Add edge-case handling:
       - Empty or invalid DNA sequences.
       - DNA sequences without start or stop codons.
   - Expand test coverage to validate all edge cases.

---

# Low-Level Plan for Implementing the Code

## 1. **Setup Constants and Imports**
   - Import necessary modules:
     ```python
     from typing import List
     from table_amino import table
     ```
   - Define constants:
     ```python
     CODON_LENGTH = 3
     START_CODON = 'M'
     STOP_CODON = '_'
     DNA_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}
     ```

---

## 2. **Implement Base Complement and Reverse Complement**

### 2.1 Complementary Base Function
   - Implement `get_complementary_character(base: str) -> str`:
     - Check if `base` exists in `DNA_COMPLEMENTS`.
     - Return its complement or an empty string if not found.

   ```python
   def get_complementary_character(base: str) -> str:
       return DNA_COMPLEMENTS.get(base, "")
   ```

### 2.2 Reverse Complement Function
   - Implement `compute_reverse_complement(dna: str) -> str`:
     - Reverse the `dna` sequence.
     - Use `get_complementary_character` for each base.
     - Join the results into a string.

   ```python
   def compute_reverse_complement(dna: str) -> str:
       return ''.join(get_complementary_character(base) for base in reversed(dna))
   ```

---

## 3. **Implement Codon Extraction**

### 3.1 Extract Codons Function
   - Implement `extract_codons(dna: str) -> List[str]`:
     - Loop through `dna` in steps of `CODON_LENGTH`.
     - Skip substrings shorter than `CODON_LENGTH`.

   ```python
   def extract_codons(dna: str) -> List[str]:
       return [
           dna[pos:pos + CODON_LENGTH]
           for pos in range(0, len(dna), CODON_LENGTH)
           if len(dna[pos:pos + CODON_LENGTH]) == CODON_LENGTH
       ]
   ```

---

## 4. **Translate Codons to Proteins**

### 4.1 Translation Function
   - Implement `translate_codons_to_protein(codon_list: List[str], codon_to_amino_table=None) -> str`:
     - Use `table` if no custom `codon_to_amino_table` is provided.
     - Translate each codon using the table and concatenate results.

   ```python
   def translate_codons_to_protein(codon_list, codon_to_amino_table=None):
       if codon_to_amino_table is None:
           codon_to_amino_table = table
       return ''.join(codon_to_amino_table[codon] for codon in codon_list)
   ```

---

## 5. **Handle Stop Codon and Extract Proteins**

### 5.1 Stop Codon Handler
   - Implement `process_stop_codon(proteins, current_protein, active)`:
     - If `active`, append `current_protein + STOP_CODON` to `proteins`.
     - Reset `current_protein` and set `active` to `False`.

   ```python
   def process_stop_codon(proteins, current_protein, active):
       if active:
           proteins.append(current_protein + STOP_CODON)
       return '', False
   ```

### 5.2 Protein Extraction
   - Implement `extract_proteins(amino_acid_sequence: str) -> List[str]`:
     - Initialize `inside_protein`, `proteins`, and `current_protein`.
     - Loop through the amino acid sequence:
       - Start a new protein on `START_CODON`.
       - Append to `current_protein` if `inside_protein`.
       - Process stop codons using `process_stop_codon`.

   ```python
   def extract_proteins(amino_acid_sequence: str) -> List[str]:
       inside_protein = False
       proteins = []
       current_protein = ''
       for amino_acid in amino_acid_sequence:
           if amino_acid == START_CODON:
               inside_protein = True
               current_protein += START_CODON
           elif amino_acid == STOP_CODON:
               current_protein, inside_protein = process_stop_codon(proteins, current_protein, inside_protein)
           elif inside_protein:
               current_protein += amino_acid
       return proteins
   ```

---

## 6. **Generate ORFs**

### 6.1 ORF Extraction
   - Implement `get_six_orfs(dna: str) -> List[List[str]]`:
     - Define helper function `get_three_orfs(sequence: str)`.
     - Use `extract_codons` for three offsets (0, 1, 2).
     - Compute reverse complement and repeat the process.

   ```python
   def get_six_orfs(dna: str) -> List[List[str]]:
       def get_three_orfs(sequence: str) -> List[List[str]]:
           return [extract_codons(sequence[offset:]) for offset in range(3)]

       rev_comp = compute_reverse_complement(dna)
       return get_three_orfs(dna) + get_three_orfs(rev_comp)
   ```

---

## 7. **Extract All Proteins**

### 7.1 Unique Protein Extraction
   - Implement `get_all_proteins(dna: str) -> List[str]`:
     - Translate ORFs to protein sequences.
     - Extract proteins from each sequence.
     - Use a set to store unique proteins.
     - Sort proteins by descending length and lexicographically.

   ```python
   def get_all_proteins(dna: str) -> List[str]:
       orfs = [translate_codons_to_protein(orf) for orf in get_six_orfs(dna)]
       protein_orfs = [extract_proteins(orf) for orf in orfs]
       unique_proteins = {protein for proteins in protein_orfs for protein in proteins}
       return sorted(unique_proteins, key=lambda protein: (-len(protein), protein))
   ```

---

## 8. **Test the Implementation**

### 8.1 Main Testing Block
   - Use `if __name__ == '__main__':` for testing:
     - Define `sample_dna = "ATGCATGCTAAGTATTAG"`.
     - Test each function sequentially:
       - Reverse complement
       - Codon extraction
       - Codon translation
       - Protein extraction
       - ORFs generation
       - Unique protein extraction
     - Print results for validation.

   ```python
   if __name__ == '__main__':
       sample_dna = "ATGCATGCTAAGTATTAG"

       # Test reverse complement
       rev_complement = compute_reverse_complement(sample_dna)
       print("Reverse Complement:", rev_complement)

       # Test codon extraction
       codons = extract_codons(sample_dna)
       print("Codons from DNA:", codons)

       # Test translation
       protein_sequence = translate_codons_to_protein(codons, table)
       print("Protein from Codons:", protein_sequence)

       # Test protein extraction
       proteins = extract_proteins(protein_sequence)
       print("Proteins Extracted:", proteins)

       # Test ORF generation
       orfs = get_six_orfs(sample_dna)
       print("ORFs:", orfs)

       # Test unique protein extraction
       all_proteins = get_all_proteins(sample_dna)
       print("All Unique Proteins:", all_proteins)
   ```

---
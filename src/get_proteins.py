# Constants for DNA processing
from typing import List
from .table_amino import table

CODON_LENGTH = 3  # Codon length for extraction.
START_CODON = 'M'  # Start codon.
STOP_CODON = '_'  # Stop codon.
DNA_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}  # Base complement mapping.


def get_complementary_character(base: str) -> str:
    """
    Retrieves the complementary DNA character for a given base character. The
    function uses a predefined mapping to return the complement. If the
    provided base is not recognized in the mapping, an empty string is returned.

    :param base: A string representing a DNA base character for which the
                 complementary character is needed.
    :return: A string representing the complementary DNA base character, or an
             empty string if the input base is not found in the mapping.
    """
    return DNA_COMPLEMENTS.get(base, "")


def compute_reverse_complement(dna: str) -> str:
    """
    Compute the reverse complement of a DNA sequence.

    This function takes a DNA sequence as input and generates its reverse
    complement. The reverse complement is defined as the sequence obtained
    after reversing the original DNA sequence and substituting each base with
    its complementary base according to the base-pairing rules. The complementary
    bases in DNA are: A-T and C-G.

    :param dna: A string representing the input DNA sequence. Expected to only
        contain characters 'A', 'T', 'C', and 'G'.
    :return: A string containing the reverse complement of the input DNA sequence.
    """
    return ''.join(get_complementary_character(base) for base in reversed(dna))

def extract_codons(dna: str) -> list[str]:
    """
    Extracts codons from a given DNA string.

    This function processes a DNA sequence and extracts substrings of length equal
    to the codon length. It skips incomplete substrings that are shorter than the
    codon length.

    :param dna: A string representing the DNA sequence.
    :type dna: str
    :return: A list of codons, where each codon is a substring of `dna` with a
        length equal to the defined codon length.
    :rtype: list[str]
    """
    return [
        dna[pos:pos + CODON_LENGTH]
        for pos in range(0, len(dna), CODON_LENGTH)
        if len(dna[pos:pos + CODON_LENGTH]) == CODON_LENGTH
    ]


def translate_codons_to_protein(codon_list, codon_to_amino_table=None):
    """
    Translate a list of codons into a protein sequence.

    This function takes a list of codon strings and converts each codon into
    its corresponding amino acid according to the `CODON_TO_AMINO_TABLE`.
    The function then combines all the amino acids into a single string
    representing the resulting protein sequence.

    :param codon_to_amino_table:
    :param codon_list: A list of codons, where each codon is represented as
        a string of three nucleotides. All codons must be valid and
        recognized by the `CODON_TO_AMINO_TABLE`.
    :type codon_list: list[str]

    :return: A string representing the translated protein sequence. Each
        codon in the input is translated to its corresponding single-letter
        amino acid code, and all the amino acids are concatenated.
    :rtype: str
    """
    if codon_to_amino_table is None:
        codon_to_amino_table = table
    return ''.join(codon_to_amino_table[codon] for codon in codon_list)


def process_stop_codon(proteins, current_protein, active):
    """
    Processes the current protein and appends upon encountering a stop codon.
    Ensures proper resetting for subsequent sequences.
    """
    if active:
        proteins.append(current_protein + STOP_CODON)
    return '', False


def extract_proteins(amino_acid_sequence: str) -> List[str]:
    """
    Extracts proteins from a sequence of amino acids using start ('M') and stop ('_') codons.
    Handles multiple proteins in the sequence, starting new ones when encountering 'M'
    and ending at '_'.

    :param sequence: A string of amino acids (translated from codons).
    :return: A list of protein strings extracted from the sequence.
    """
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

def get_six_orfs(dna: str) -> List[List[str]]:
    """
    Derives all six possible open reading frames (ORFs) from a given DNA sequence,
    encompassing the three ORFs from the sequence in its original orientation
    and three additional ORFs from its reverse complement. Each ORF is represented
    as a list of codons extracted starting at different reading frames.

    :param dna: The input DNA sequence from which to extract ORFs. The sequence
        should be provided as a string of valid nucleotides ('A', 'T', 'C', 'G').
    :return: A list of six lists where each sublist corresponds to an ORF (as a
        series of codons), covering both the forward and reverse complement
        orientations of the DNA sequence.
    """

    def get_three_orfs(sequence: str) -> List[List[str]]:
        return [extract_codons(sequence[offset:]) for offset in range(3)]

    rev_comp = compute_reverse_complement(dna)
    return get_three_orfs(dna) + get_three_orfs(rev_comp)


def get_all_proteins(dna: str) -> List[str]:
    """
    Extracts and returns a sorted list of unique proteins encoded in all six reading frames of a DNA sequence.
    The proteins are translated from open reading frames (ORFs). The results are sorted first by descending
    length of the protein and then lexicographically for proteins of the same length.

    :param dna: A DNA sequence provided as a string composed of characters A, T, G, and C.
    :type dna: str

    :return: A sorted list of unique protein strings, ordered by descending length, then lexicographically.
    :rtype: list[str]
    """

    orfs = [translate_codons_to_protein(orf) for orf in get_six_orfs(dna)]
    protein_orfs = [extract_proteins(orf) for orf in orfs]
    unique_proteins = {protein for proteins in protein_orfs for protein in proteins}
    return sorted(unique_proteins, key=lambda protein: (-len(protein), protein))

# Main testing block
if __name__ == '__main__':
    # Sample DNA sequence for testing
    sample_dna = "ATGCATGCTAAGTATTAG"

    # Step 1: Reverse complement
    rev_complement = compute_reverse_complement(sample_dna)
    print("Reverse Complement:", rev_complement)

    # Step 2: Extract codons
    codons = extract_codons(sample_dna)
    print("Codons from DNA:", codons)

    # Step 3: Translate codons to protein using table from table_amino
    protein_sequence = translate_codons_to_protein(codons, table)
    print("Protein from Codons:", protein_sequence)

    # Step 4: Extract proteins
    proteins = extract_proteins(protein_sequence)
    print("Proteins Extracted:", proteins)

    # Step 5: Get six ORFs
    orfs = get_six_orfs(sample_dna)
    print("ORFs:", orfs)

    # Step 6: Get all proteins from all ORFs
    all_proteins = get_all_proteins(sample_dna)
    print("All Unique Proteins:", all_proteins)

# Constants
DNA_BASES = {"A", "T", "C", "G"}
RNA_BASES = {"A", "U", "C", "G"}
AMINO_ACIDS = {
    "A", "R", "N", "D", "C", "E", "Q", "G", "H", "I",
    "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"
}


# Helper functions
def contains_no_spaces(sequence):
    """
    Checks if the provided sequence contains no spaces.

    This function evaluates whether a given sequence lacks any space
    characters. It is useful for validating sequences where the absence
    of white spaces is required.

    :param sequence: The sequence to be checked for spaces.
    :type sequence: str
    :return: True if the sequence contains no space characters, False otherwise.
    :rtype: bool
    """
    if not sequence:  # Check for empty sequence
        return False
    return " " not in sequence


def is_valid_sequence(sequence, valid_bases):
    """
    Validate if a given sequence contains only valid bases from a specified set of bases.

    This function iterates over each base in the input sequence and determines whether
    the base exists in the set of valid bases provided. If all bases in the sequence
    are found within the set of valid bases, it returns True; otherwise, it returns False.

    :param sequence: The sequence of bases to validate
    :type sequence: str
    :param valid_bases: A set or collection of valid bases used for validation
    :type valid_bases: Iterable[str]
    :return: A boolean value indicating whether all bases in the sequence
             are valid based on the provided valid bases
    :rtype: bool
    """
    return all(base in valid_bases for base in sequence)


def get_sequence_type(sequence):
    """
    Determine the type of a given biological sequence.

    This function evaluates the sequence provided and checks whether it corresponds
    to DNA, RNA, amino acid, or an invalid sequence. It validates the sequence against
    predefined sets of bases or amino acids.

    :param sequence: A string representing a biological sequence.
    :type sequence: str

    :return: The type of the sequence as a string, which can be one of
             "DNA", "RNA", "AMINO_ACID", or "INVALID".
    :rtype: str
    """
    if not sequence:  # Handle empty sequence
        return "INVALID"
    if is_valid_sequence(sequence, DNA_BASES):
        return "DNA"
    elif is_valid_sequence(sequence, RNA_BASES):
        return "RNA"
    elif is_valid_sequence(sequence, AMINO_ACIDS):
        return "AMINO_ACID"
    return "INVALID"

def count_bases(sequence):
    """
    Counts the occurrences of each unique base in a given sequence and returns a dictionary
    mapping each base to its count.

    This function takes an input sequence, iterates over its unique elements,
    and calculates the frequency of each base using the built-in count method.
    The result is a dictionary where keys are unique bases, and values are their
    corresponding counts in the sequence.

    :param sequence: The input sequence for which to count the occurrences of each unique base.
                     Must be an iterable containing comparable elements.

    :return: A dictionary containing unique bases as keys and their respective counts as values.
    :rtype: dict
    """
    return {base: sequence.count(base) for base in sorted(set(sequence))}


def main(sequence):
    """
    Processes a biological sequence and determines its type, converts it accordingly, and provides base counts.

    This function processes an input sequence, ensuring it is in upper-case format, and validating that
    there are no spaces present in the sequence. Depending on the type of sequence (DNA, RNA, or
    Amino Acid), it provides conversions and detailed base counts.

    :param sequence: The input biological sequence as a string. Expected to be DNA, RNA,
        or Amino Acid format.
    :type sequence: str
    :return: A formatted string containing the sequence conversion or detection results
        and the detailed counts of bases in the sequence. Returns an error message
        if the sequence is invalid or contains spaces.
    :rtype: str
    """
    # Ensure the sequence is upper-case
    sequence = sequence.upper()

    # Validate sequence
    if not contains_no_spaces(sequence):
        return "ERROR: Please, remove spaces between the sequence"

    # Determine sequence type
    seq_type = get_sequence_type(sequence)

    result = []
    if seq_type == "DNA":
        result.append("RNA sequence: " + sequence.replace("T", "U"))
    elif seq_type == "RNA":
        result.append("cDNA: " + sequence.replace("U", "T"))
    elif seq_type == "AMINO_ACID":
        result.append("Amino acid sequence detected.")
    else:
        return "ERROR: Not a valid DNA/RNA/Amino Acid sequence"

    # Count the amino acids (or bases for DNA/RNA) in the order they appear in the sequence
    base_counts = {base: sequence.count(base) for base in sequence}  # Count only those present in the sequence

    # Display base counts in the order of their first occurrence
    seen = set()  # To avoid duplicate counts
    for base in sequence:
        if base not in seen:
            seen.add(base)
            result.append(f"{base}: {base_counts[base]}")

    return "\n".join(result)

# Testing block
if __name__ == "__main__":
    # Test cases
    sequences = [
        "ATCG",  # Example DNA
        "AUCG",  # Example RNA
        "MAVILK",  # Example Amino Acid sequence
        "ATCGU",  # Invalid sequence (mix of DNA and RNA)
        "MA VILK",  # Amino Acid sequence with a space (invalid)
    ]

    for seq in sequences:
        print(f"Testing sequence: {seq}")
        print(main(seq))
        print("-" * 40)# Main testing block


from global_alignment import global_matrix, traceback

def star_alignment(sequences):
    """
    Implements the Star Multiple Sequence Alignment algorithm.
    
    Args:
        sequences: List of sequences to align
        
    Returns:
        list: List of aligned sequences
    """
    if not sequences:
        raise ValueError("No sequences provided")
    
    # Choose center sequence (longest one)
    center = max(sequences, key=len)
    
    if len(sequences) == 1:
        return sequences

    # Get pairwise alignments with center
    alignments = []
    for seq in sequences:
        if seq != center:
            matrix = global_matrix(center, seq)
            aligned_center, aligned_seq = traceback(matrix, center, seq)
            alignments.append((aligned_center, aligned_seq))
    
    if not alignments:  # All sequences are identical
        return sequences
        
    # Find the maximum length among all alignments
    max_len = max(len(aligned[0]) for aligned in alignments)
    
    # Initialize the result with the center sequence
    result = [center + '-' * (max_len - len(center))]
    
    # Process each sequence
    processed = {center}  # Keep track of processed sequences
    
    # Add aligned sequences
    for _, aligned_seq in alignments:
        orig_seq = ''.join(c for c in aligned_seq if c != '-')  # Get original sequence
        if orig_seq not in processed:
            result.append(aligned_seq + '-' * (max_len - len(aligned_seq)))
            processed.add(orig_seq)
    
    # Add any remaining identical sequences
    for seq in sequences:
        if seq not in processed:
            result.append(seq + '-' * (max_len - len(seq)))
            processed.add(seq)
    
    return result

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

    # Create alignment mapping
    alignment_map = {}
    
    # Get pairwise alignments with center
    for seq in sequences:
        if seq == center:
            alignment_map[seq] = center
        else:
            matrix = global_matrix(center, seq)
            aligned_center, aligned_seq = traceback(matrix, center, seq)
            alignment_map[seq] = aligned_seq
            # Update max length if this alignment is longer
            if len(aligned_center) > len(alignment_map[center]):
                # Pad existing alignments
                for k in alignment_map:
                    alignment_map[k] = alignment_map[k] + '-' * (len(aligned_center) - len(alignment_map[k]))
            elif len(aligned_center) < len(alignment_map[center]):
                # Pad this alignment
                alignment_map[seq] = aligned_seq + '-' * (len(alignment_map[center]) - len(aligned_seq))
    
    # Return aligned sequences in original order
    result = []
    for seq in sequences:
        result.append(alignment_map[seq])
    
    return result

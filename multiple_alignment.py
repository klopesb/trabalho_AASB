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

    # Create alignment mapping and initialize with center sequence
    alignment_map = {center: center}
    max_length = len(center)
    
    # Get pairwise alignments with center
    for seq in sequences:
        if seq != center:
            matrix = global_matrix(center, seq)
            aligned_center, aligned_seq = traceback(matrix, center, seq)
            alignment_map[seq] = aligned_seq
            
            # Update max length and pad if necessary
            if len(aligned_center) > max_length:
                # Pad existing alignments
                padding = '-' * (len(aligned_center) - max_length)
                for k in alignment_map:
                    alignment_map[k] = alignment_map[k] + padding
                max_length = len(aligned_center)
            elif len(aligned_center) < max_length:
                # Pad this alignment
                alignment_map[seq] = aligned_seq + '-' * (max_length - len(aligned_seq))
    
    # Return aligned sequences in original order
    result = []
    for seq in sequences:
        result.append(alignment_map[seq])
    
    return result

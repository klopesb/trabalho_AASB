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
    
    # Get pairwise alignments with center
    alignments = []
    for seq in sequences:
        if seq == center:
            alignments.append((center, center))
        else:
            matrix = global_matrix(center, seq)
            aligned_center, aligned_seq = traceback(matrix, center, seq)
            alignments.append((aligned_center, aligned_seq))
    
    # Initialize with first alignment
    final_center = alignments[0][0]
    final_alignments = [alignments[0][1]]
    
    # Add gaps to make all alignments same length
    max_len = len(final_center)
    for aligned_center, aligned_seq in alignments[1:]:
        # Add gaps to current sequence if needed
        if len(aligned_seq) < max_len:
            aligned_seq = aligned_seq + '-' * (max_len - len(aligned_seq))
        # Add gaps to previous sequences if needed
        elif len(aligned_seq) > max_len:
            final_center = final_center + '-' * (len(aligned_seq) - max_len)
            final_alignments = [seq + '-' * (len(aligned_seq) - max_len) 
                              for seq in final_alignments]
            max_len = len(aligned_seq)
        final_alignments.append(aligned_seq)
    
    # Add center sequence to result
    return [final_center] + final_alignments

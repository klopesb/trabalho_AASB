def query_map(query, w):
  """
  Creates a dictionary of words and their starting indices in the query.

  Args:
    query: The input query sequence.
    w: The length of the words (substrings).

  Returns:
    A dictionary where keys are substrings of length `w` from the `query` 
    and values are lists of their starting indices in the `query`.
  """
  map_dict = {}
  for i in range(len(query) - w + 1):
    subseq = query[i:i + w] 
    if subseq not in map_dict:
      map_dict[subseq] = [] 
    map_dict[subseq].append(i) 
  return map_dict

def hits(query_dict, db_sequence):
  """
  Finds all occurrences of query words in the db_sequence.

  Args:
    query_dict: A dictionary created by `query_map`.
    db_sequence: The database sequence to search against.

  Returns:
    A list of tuples, where each tuple represents a hit and contains:
      - Starting index of the hit in the query.
      - Starting index of the hit in the db_sequence.
  """
  hit_list = []
  for i in range(len(db_sequence) - w + 1):
    subseq = db_sequence[i:i + w]
    if subseq in query_dict:
      for query_index in query_dict[subseq]:
        hit_list.append((query_index, i))
  return hit_list

def extend_hit(query, db_sequence, hit, w):
  """
  Extends a hit in both directions to find the longest local alignment.

  Args:
    query: The input query sequence.
    db_sequence: The database sequence to search against.
    hit: A tuple containing the starting indices of a hit 
         (in query and db_sequence, respectively).
    w: The length of the initial word used for the hit.

  Returns:
    A tuple containing:
      - Starting index of the extended match in the query.
      - Starting index of the extended match in the db_sequence.
      - Total size of the extended match.
      - Number of matching characters beyond the initial window.
  """
  stq, sts = hit[0], hit[1]  # stq: Starting index of the hit in the query
  # sts: Starting index of the hit in the db_sequence
  matfw = 0  # Number of forward matches 
  k = 0
  bestk = 0  # Best extension length in the forward direction
  while 2*matfw >= k and stq+w+k < len(query) and sts+w+k < len(query):
    if query[stq+w+k] == db_sequence[sts+w+k]:
      matfw+=1
      bestk = k+1
    k += 1
  size = w + bestk

  k = 0
  matbw = 0  # Number of backward matches
  bestk = 0  # Best extension length in the backward direction
  while 2*matbw >= k and stq > k and sts > k:
    if db_sequence[stq-k-1] == db_sequence[sts-k-1]:
      matbw+=1
      bestk = k+1
    k+=1
  size += bestk
  return (stq-bestk, sts-bestk, size, w+matfw+matbw)


def best_hit(query, db_sequence, w):
  """
  Finds the best hit (longest match with the highest number of matching characters) 
  between the query and db_sequence.

  Args:
    query: The input query sequence.
    db_sequence: The database sequence to search against.
    w: The length of the words (substrings).

  Returns:
    A tuple containing:
      - Starting index of the best hit in the query.
      - Starting index of the best hit in the db_sequence.
      - Total size of the best hit.
      - Number of matching characters beyond the initial window.
  """
  hit_list = hits(query_map(query, w), db_sequence) 
  bestScore = -1.0
  bestExtension = ()
  for hit in hit_list:
    ext = extend_hit(query, db_sequence, hit, w)
    score = ext[3] 
    if score > bestScore or (score == bestScore and ext[2] < bestExtension[2]):
      bestScore = score
      bestExtension = ext
  return bestExtension

# Example usage:
query = "AATATAT"
db_sequence = "AATATGTTATATAATAATATTT"
w = 3

print("Query Map:", query_map(query, w))
print("Hits:", hits(query_map(query, w), db_sequence))
best = best_hit(query, db_sequence, w)
print("Best Hit:", best)

def main():
  #make a list of DNA
  DNA = ["A","T","C","G"]

  #make a list of RNA
  RNA = ["A","U","C","G"]

  #Add input to the user
  sequence = input("FASTA:").upper()

  #Check for empty spaces between the DNA sequence

  def is_empty():
    if " " in sequence:
      return False
    return True

#Check for correct DNA sequence

  def is_DNA():
    for base in sequence:
      if base not in DNA:
        return False
    return True
#Check for correct RNA sequence

  def is_RNA():
    for base in sequence:
      if base not in RNA:
        return False
    return True

#Call all functions
  check_empty = is_empty()
  check_DNA = is_DNA()
  check_RNA = is_RNA()


#Display a result if the conditions are true
#Check if empty_space returns True, else return Fals
  if check_empty:
    #If is_empty returns True:
    if check_DNA:
      print("RNA sequence: ", sequence.replace("T","U"))

      print(f"A: {sequence.count('A')}")
      print(f"T: {sequence.count('T')}")
      print(f"C: {sequence.count('C')}")
      print(f"G: {sequence.count('G')}")

    elif check_RNA:
      print("cDNA: ", sequence.replace("U","T"))


      print(f"A: {sequence.count('A')}")
      print(f"U: {sequence.count('U')}")
      print(f"C: {sequence.count('C')}")
      print(f"G: {sequence.count('G')}")

    else:
      print("ERROR: Not a DNA/RNA")

  else:
    print("ERROR: Please, remove spaces between the sequence")


main()
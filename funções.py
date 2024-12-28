#Create a main function
    #The main funtion has to transform a  DNA (ATCG) to RNA (AUCG)
        #DNA > RNA 
        # A = (T) > U 
        # C = G 
    #Make an input so the user can put the DNA chain
    #Make a Dict to assign each base pair
    #iterate over the input with a for loop
    #Replace the DNA "T" to RNA "U"
#this main function should display the count of each base (A, C, G, T) in the original DNA sequence.

#make a list of DNA 
DNA = ["A","T","C","G"]

#make a list of RNA 
#RNA = ["A","U","C","G"]

#Add input to the user 
dna_chain = input("DNA FASTA:").upper()

def main(dna_chain):

#    for base_pair in dna_chain:
  #print("RNA sequence: ", dna_chain.replace("T","U"))

  if empty_space(dna_chain) is False:

    print("Error: The sequence contains empty spaces")

  else:
    print("RNA sequence: ", dna_chain.replace("T","U"))

#Count each one of the base pairs 

  print(f"A: {dna_chain.count('A')}")
  print(f"T: {dna_chain.count('T')}")
  print(f"C: {dna_chain.count('C')}")
  print(f"G: {dna_chain.count('G')}")

#Check for empty spaces between the DNA sequence 

  def empty_space(dna_chain):
    if " " in dna_chain:
      return False
    else:
      return True

main(dna_chain)
    

#Create another sub functions:
    #To check parameter is not empty (not empty sequences)
    #To check if the input is a DNA 
        #Both subfunction must return TRUE or FALSE
        #Main () only display a result if the return is TRUE for both, otherwise should display ERROR 

#Create a function to make a cDNA 
    #This should revert the RNA (AUCG) back to DNA (ATCG)
        #mRNA > cDNA
        # A = (U) > T 
        # C = G 




main(dna_chain)

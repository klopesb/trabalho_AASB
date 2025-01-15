# Low-Level Plan for Implementing the Code

## 1. **Define Constants**
   - Create sets to store valid bases for DNA, RNA, and Amino Acids.

   **Steps:**
   - Write the following lines of code:
     ```python
     DNA_BASES = {"A", "T", "C", "G"}
     RNA_BASES = {"A", "U", "C", "G"}
     AMINO_ACIDS = {"A", "R", "N", "D", "C", "E", "Q", "G", "H", "I",
                    "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"}
     ```

---

## 2. **Implement Helper Functions**

### 2.1 `contains_no_spaces`
   - Check if the sequence contains any spaces.

   **Steps:**
   - Write a function that:
     - Validates if the input is empty (`return False` for empty input).
     - Checks for spaces using `" " not in sequence`.

### 2.2 `is_valid_sequence`
   - Verify if a sequence contains only valid bases.

   **Steps:**
   - Write a function that:
     - Takes `sequence` and `valid_bases` as inputs.
     - Uses `all(base in valid_bases for base in sequence)` to validate.

### 2.3 `get_sequence_type`
   - Identify if a sequence is DNA, RNA, Amino Acid, or Invalid.

   **Steps:**
   - Write a function that:
     - Checks if the sequence is empty and returns `"INVALID"`.
     - Calls `is_valid_sequence` for DNA, RNA, and Amino Acids in order.
     - Returns the corresponding type (`"DNA"`, `"RNA"`, `"AMINO_ACID"`, or `"INVALID"`).

### 2.4 `count_bases`
   - Count occurrences of each base in the sequence.

   **Steps:**
   - Write a function that:
     - Uses `set(sequence)` to get unique bases.
     - Iterates over unique bases and counts occurrences with `sequence.count(base)`.
     - Returns a dictionary of base counts.

---

## 3. **Create the `main` Function**

### 3.1 Process Input Sequence
   - Convert the sequence to uppercase.

   **Steps:**
   - Add `sequence = sequence.upper()` at the start.

### 3.2 Validate Sequence
   - Check for spaces and invalid characters.

   **Steps:**
   - Call `contains_no_spaces`.
   - Return `"ERROR: Please, remove spaces between the sequence"` if validation fails.

### 3.3 Identify Sequence Type
   - Determine if the sequence is DNA, RNA, or Amino Acid.

   **Steps:**
   - Call `get_sequence_type`.
   - Handle each type accordingly:
     - DNA: Convert `T` to `U` and return as RNA.
     - RNA: Convert `U` to `T` and return as cDNA.
     - Amino Acid: Add a message indicating the sequence is valid.

### 3.4 Count Bases or Amino Acids
   - Count the frequency of each element in the sequence.

   **Steps:**
   - Use a dictionary comprehension:
     ```python
     base_counts = {base: sequence.count(base) for base in sequence}
     ```
   - Iterate through the sequence to ensure counts are displayed in order of first appearance.

### 3.5 Construct Result
   - Build the output string.

   **Steps:**
   - Append messages and base counts to a list.
   - Join the list using `"\n".join(result)`.

---

## 4. **Develop Testing Block**

### 4.1 Define Test Sequences
   - Create a list of test sequences.

   **Steps:**
   - Include valid and invalid examples:
     ```python
     sequences = [
         "ATCG",      # DNA
         "AUCG",      # RNA
         "MAVILK",    # Amino Acid
         "ATCGU",     # Invalid (mix of DNA and RNA)
         "MA VILK"    # Invalid (space in Amino Acid sequence)
     ]
     ```

### 4.2 Call `main` for Each Sequence
   - Iterate over the test sequences and process them.

   **Steps:**
   - Write a loop:
     ```python
     for seq in sequences:
         print(f"Testing sequence: {seq}")
         print(main(seq))
         print("-" * 40)
     ```

---

## 5. **Handle Errors and Edge Cases**

### 5.1 Empty Sequence
   - Return `"INVALID"` for empty input in `get_sequence_type`.

   **Steps:**
   - Add this check at the beginning of the function:
     ```python
     if not sequence:
         return "INVALID"
     ```

### 5.2 Mixed Bases
   - Return an error message for sequences with mixed DNA and RNA bases.

   **Steps:**
   - Add an else clause in `main` to handle invalid sequences:
     ```python
     return "ERROR: Not a valid DNA/RNA/Amino Acid sequence"
     ```

---

## 6. **Optimize and Refactor**
   - Reduce code redundancy and improve readability.

   **Steps:**
   - Refactor the base counting logic to avoid duplicate processing.
   - Combine validation checks where possible.

---

## 7. **Add Comments and Documentation**
   - Explain each function and critical code section.

   **Steps:**
   - Write docstrings for all functions describing their purpose, inputs, and outputs.
   - Add inline comments for complex or non-obvious logic.


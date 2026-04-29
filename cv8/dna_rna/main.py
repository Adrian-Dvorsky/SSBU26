from Bio import SeqIO
from Bio.Seq import Seq
from random import randint, choice

# Task 1: Load sequence from a file in the inputs directory
def load_sequence(filepath):
    """
    Pseudocode:
    - Use SeqIO to read the file in GenBank format.
    - Print the sequence ID.
    - Check if the sequence is defined or non-empty:
        - If valid, print the sequence.
        - Otherwise, print a message and assign an empty sequence.
    - Return the sequence record.
    """

    record = SeqIO.read(filepath, format="genbank")
    print("Sequence ID:", record.id)
    print("Sequence:", record.description)
# Task 2: Create complementary strand
def create_complementary_strand(dna_sequence):
    """
    Pseudocode:
    - Create a translation table for DNA base complements (A <-> T, G <-> C).
    - Translate the input DNA sequence using the complement table.
    - Print the complementary strand.
    - Return the complementary strand.
    """

    complement_table = str.maketrans('ATCG', 'TAGC')
    dna_sequence_translate = str.translate(dna_sequence, complement_table)
    print("DNA sequence:", dna_sequence_translate)
    return dna_sequence_translate

# Task 3: Create gene mutation
def mutate(dna):
    """
    Pseudocode:
    - Convert the DNA sequence into a list of characters.
    - Perform 1000 random mutations:
        - Select a random index in the DNA sequence.
        - Replace the base at the selected index with a random different base.
    - Join the mutated list back into a string.
    - Print the mutated DNA sequence.
    - Return the mutated DNA sequence.
    """
    characters = list(dna)
    base = ['A', 'C', 'G', 'T']
    for i in range(1000):
        index = randint(0, len(characters) - 1)
        base_random = choice(base)
        list[index] = base(base_random)
    muted_dna = ''.join(characters)
    print("Mutated DNA:", muted_dna)
    return muted_dna
# Task 4: Calculate GC content
def calculate_gc_content(dna_sequence):
    """
    Pseudocode:
    - Count the occurrences of 'G' and 'C' in the DNA sequence.
    - Calculate the GC content as a percentage of the total sequence length.
    - Print the GC content percentage.
    - Return the GC content percentage.
    """
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    percentage = round((g_count / c_count) * 100, 2)
    return percentage

# Example usage
if __name__ == "__main__":
    # Task 1: Load sequence from the inputs directory
    sequence_record = load_sequence("../inputs/NC_005816.gb")

    # Task 2: Create complementary strand
    create_complementary_strand("TACCGGAT")

    # Task 3: Mutate a sequence loaded from the inputs directory
    fasta_sequence = SeqIO.read("inputs/AE017046.1.fasta", "fasta").seq
    mutated_sequence = mutate(str(fasta_sequence))

    # Task 4: Calculate GC content
    calculate_gc_content(str(fasta_sequence))
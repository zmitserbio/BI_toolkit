def check_input(seqs: list, operation: str):
    """
    Check input for some of the most common errors
    arguments:
    - seqs (list): a list of sequences
    - operation (str): operation name
    return
    - no return
    """
    from modules.dna_rna_constants import dna_rna_alphabet
    for seq in seqs:
        if type(seq) != str:
            raise ValueError('Invalid input: all sequences must be of type str!')
        t_present = False
        u_present = False
        for i in seq:
            if i not in dna_rna_alphabet:
                raise ValueError('Invalid input: sequences must contain only letters "A", "T", "C", "G" in either upper or lower case!')
            if i == 'T' or i == 't':
                t_present = True
            if i == 'U' or i == 'u':
                u_present = True
        if t_present and u_present:
            raise ValueError('Invalid input: sequences must not include both thymine and uracil!')
        if operation == 'transcribe' and u_present:
            raise ValueError('Invalid input: cannot transcribe RNA sequence(s).')


def transcribe(seqs: list) -> list:
    """
    Produce a list of transcripts
    arguments:
    - seqs (list): a list of sequences
    return
    - transcripts (list): a list of transcripts
    """
    from modules.dna_rna_constants import compl_dna
    transcripts = []
    for seq in seqs:
        transcript = []
        for i in seq:
            transcript.append(compl_dna[i])
        transcripts.append(''.join(transcript))
    return transcripts


def reverse(seqs: list) -> list:
    """
    Produce a list of reverse sequences
    arguments:
    - seqs (list): a list of sequences
    return
    - reverse_seqs (list): a list of reverse sequences
    """
    reverse_seqs = []
    for seq in seqs:
        reverse_seqs.append(seq[::-1])
    return reverse_seqs


def complement(seqs: list) -> list:
    """
    Produce a list of complementary sequences
    arguments:
    - seqs (list): a list of sequences
    return
    - complement_seqs (list): a list of complementary sequences
    """
    from modules.dna_rna_constants import compl_dna, compl_rna
    complement_seqs = []
    for seq in seqs:
        if 'U' in seq or 'u' in seq:
            complement_seq = []
            for j in seq:
                complement_seq.append(compl_rna[j])
        else:
            complement_seq = []
            for j in seq:
                complement_seq.append(compl_dna[j])
        complement_seqs.append(''.join(complement_seq))
    return complement_seqs


def reverse_complement(seqs: list) -> list:
    """
    Produce a list of reverse complementary sequences
    arguments:
    - seqs (list): a list of sequences
    return
    - (list): a list of reverse complementary sequences
    """
    return complement(reverse(seqs))

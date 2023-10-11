def check_fastq(seqs: dict):
    """
    Check fastq dictionary
    arguments:
    - seqs (dict): a fastq dictionary
    return:
    - no return
    """
    from modules.fastq_constants import fastq_dna_code
    if type(seqs) != dict:
        raise ValueError('Invalid input: a dict object was expected!')
    for seq_name in seqs:
        if type(seqs[seq_name][0]) != str:
            raise ValueError('Invalid input: sequences must be of type str!')
        if len(seqs[seq_name][0]) == 0:
            raise ValueError('Invalid input: sequences must be at least one nucleotide long!')
        for i in seqs[seq_name][0]:
            if i not in fastq_dna_code:
                raise ValueError('Invalid input: sequences must contain only letters "A", "T", "G", "C" in upper case!')
        if seq_name[0] != '@':
            raise ValueError('Invalid input: sequence names are incorrect!')


def check_fastq(seqs: dict):
    """
    Check fastq dictionary
    arguments:
    - seqs (dict): a fastq dictionary
    return:
    - no return
    """
    from modules.fastq_constants import fastq_dna_code
    if type(seqs) != dict:
        raise ValueError('Invalid input: a dict object was expected!')
    for seq_name in seqs:
        if type(seqs[seq_name][0]) != str:
            raise ValueError('Invalid input: sequences must be of type str!')
        if len(seqs[seq_name][0]) == 0:
            raise ValueError('Invalid input: sequences must be at least one nucleotide long!')
        for i in seqs[seq_name][0]:
            if i not in fastq_dna_code:
                raise ValueError('Invalid input: sequences must contain only letters "A", "T", "G", "C" in upper case!')
        if seq_name[0] != '@':
            raise ValueError('Invalid input: sequence names are incorrect!')


def check_gc(seq: str, gc_bounds: tuple or int) -> bool:
    """
    Check how GC content of a sequence corresponds to the range provided
    arguments:
    - seq (str): a sequence
    - gc_bounds (tuple or int): the range in which GC content must vary
    return:
    - (bool): whether GC content of a sequence is in the range provided
    """
    gc_sum = 0
    for nucleotide in seq:
        if nucleotide == 'G' or nucleotide == 'C':
            gc_sum += 1
    return gc_bounds[0] <= gc_sum/len(seq)*100 <= gc_bounds[1]


def check_length(seq: str, length_bounds: tuple or int) -> bool:
    """
    Check how length of a sequence corresponds to the range provided
    arguments:
    - seq (str): a sequence
    - length_bounds (tuple or int): the range in which length must vary
    return:
    - (bool): whether length of a sequence is in the range provided
    """
    return length_bounds[0] <= len(seq) <= length_bounds[1]


def check_quality(quality: str, quality_threshold: int):
    """
    Check how average quality of a sequence corresponds to the lower limit provided
    arguments:
    - quality (str): a sequence describing the quality for each nucleotide in sequence
    - quality_threshold (int): the lower limit for average quality
    return:
    - (bool): whether average quality of a sequence is equal or higher than the lower limit provided
    """
    quality_sum = 0
    for i in quality:
        quality_sum += ord(i) - 33
    return quality_sum/len(quality) >= quality_threshold

def calculate_similarity(sequences: list, precision: int = 3, percentages: bool = False) -> dict:
    """
    Calculate similarity in aminoacids between reference sequence and other sequences
    arguments:
    - sequences (list): reference sequence and other sequences for comparison
    - precision (int): a number of decimals to round the number to
    - percentages (bool): whether percentages are returned instead of fractions
    return:
    - similarities (dict): dictionary with compared sequences as keys and percentages/fractions as their values
    """
    similarities = {}
    for i in range(1, len(sequences)):
        similarity = []
        for j in range(0, len(sequences[i])):
            similarity.append(sequences[0][j] == sequences[i][j])
        if percentages:
            similarities[sequences[i]] = round(sum(similarity) * 100 / len(sequences[i]), precision)
        else:
            similarities[sequences[i]] = round(sum(similarity) / len(sequences[i]), precision)
    return similarities


def count_length(protein: str) -> list:
    """
    Сounting the length of an amino acid sequence/protein in the number of amino acids
    :param protein:  sequence of protein
    :return: number of amino acids in an amino acid sequence/protein
    """
    return len(protein)


def info_amino_acid_percentage(seq: str) -> dict:
    """
    Count percentage of each amino acid in sequence
    arguments:
        - seq (str): sequence for counting
    return:
        - info_dict (dict): dictionary with counted percentage
    """
    length = count_length(seq)
    info_dict = {}
    for aa in seq:
        if aa not in info_dict:
            info_dict[aa] = 1
        else:
            info_dict[aa] += 1
    info_dict.update((key, round(value / length * 100, 2)) for key, value in info_dict.items())
    info_dict = {key: value for key, value in sorted(info_dict.items(), key = lambda item: item[1], reverse = True)}
    return info_dict


def find_pattern(sequences: list, pattern: str) -> dict:
    """
    Find all non-overlaping instances of a given pattern in sequences
    arguments:
    - sequences (list): sequences to find the pattern in
    - pattern (str): pattern in question
    return
    - finds(dict): dictionary with sequences as keys and lists of indexes of patterns and the number of patterns as values
    """
    finds = {}
    for j in range(0, len(sequences)):
        find = []
        i=0
        while i < len(sequences[j]):
            pattern_index = sequences[j].find(pattern, i)
            if pattern_index != -1:
                find.append(pattern_index)
                i=pattern_index+len(pattern)
            else:
                break
        finds[sequences[j]] = [len(find)] + find
    return finds


def convert_to_gene(protein: str) -> str:
    """
    Transforming of an amino acid sequence/protein to DNA sequence
    :param protein: amino acid sequence of protein
    :return: sequence of protein in the DNA sequence form
    """
    from modules.protein_constants import retranslation_dict
    return ''.join([retranslation_dict[aa] for aa in protein])


def recode_3letter_to_1letter(seqs: list, sep = '') -> list:
    """
    Transform into a three-letter amino acids entry.
    arguments:
        - seqs (list): list of sequences for transforming to three-letter entire
        - sep (str): separator between aminoacids, default = ''
    return:
        - three_letter_result (list): transformed sequences with separators
    """
    from modules.protein_constants import threel
    three_letter_result = []
    for seq in seqs:
        threel_form = ''
        for aa in seq:
            threel_form += threel[aa] + sep
        if sep:
            threel_form = threel_form[:-1]
        three_letter_result.append(threel_form)
    return three_letter_result


def check_protein(seq: str):
    """
    Checking whether a sequence is a protein sequence
    arguments:
    - seq (str): a sequence
    return:
    - no return
    """
    from modules.protein_constants import aminoacids
    for i in seq:
        if i not in aminoacids:
            raise ValueError('Incorrect input: protein sequences containing 20 common aminoacids in one-letter format were expected. Please try again')


def string_check(sequences: list):
    """
    Checking whether a sequence is a protein sequence and is of type str
    arguments:
    - sequences (list): checked sequences
    return:
    - no return
    """
    for seq in sequences:
        if type(seq) != str:
            raise ValueError('Incorrect input type: protein sequences of type str were expected. Please try again')
        check_protein(seq)


def check_input(inputs, options: str):
    """
    Input verification for all options
    arguments:
    - options (str): option name
    return:
    - no return
    """
    if options == 'length' or options == 'percentage' or options == 'DNA_code':
        string_check(inputs)
    elif options == '3Letter_name':
        string_check(inputs[:-1])
    elif options == 'similarity':
        string_check(inputs[:-2])
        for i in range(0, len(inputs[:-2])):
            if len(inputs[i]) != len(inputs[0]):
                raise ValueError('Incorrect input: same length protein sequences were expected. Please try again')
        if type(inputs[-2]) != int or inputs[-2] < 0:
            raise ValueError('Incorrect input type: positive integer value was expected as the second-to-last argument. Please try again')
        if type(inputs[-1]) != bool:
            raise ValueError('Incorrect input type: bool value was expected as the last argument. Please try again')
    elif options == 'pattern':
        string_check(inputs)
        for i in range(1, len(inputs)):
            if len(inputs[0]) > len(inputs[i]):
                raise ValueError('Incorrect input: pattern length shorter or equal to protein sequence length was expected. Please try again')

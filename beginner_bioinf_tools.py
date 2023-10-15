def check_fastq_file(path: str):
    """
    Check whether the path and file provided are valid for further processing
    arguments:
    - path (str): path to .fastq file
    return:
    - no return
    """
    import os
    if '.fastq' in os.path.basename(path):
        if os.path.isfile(path):
            with open(path) as fastq:
                line_count = 0
                total_line_count = 0
                for line in fastq:
                    line_count += 1
                    total_line_count += 1
                    if line_count == 1:
                        if not line.startswith('@'):
                            raise ValueError('Incorrect file content! Suggestion: check the lines near line number ' + str(total_line_count) + ' in the provided file.')
                    if line_count != 1 and line_count != 4 and line.startswith('@'):
                        raise ValueError('Incorrect file content! Suggestion: check the lines near line number ' + str(total_line_count) + ' in the provided file.')
                    if line_count == 4:
                        line_count = 0
                if line_count != 0:
                    raise ValueError('Incorrect file content! Suggestion: check the end of the file')
        else:
            raise ValueError(path + ' is not a correct path to a file!')
    else:
        raise ValueError('Invalid input: path to a .fastq file was expected!')


def run_dna_rna_tools(inputs: tuple) -> list or str:
    """
    Produce a list of either transcripts, reverse sequences, complementary sequences or reverse complementary sequences
    arguments:
    - inputs (tuple): an orbitrary amount of strings where the last one is the name of desired operation, and other strings are sequences
    return
    - complement_seqs (list): a list of complementary sequences
    """
    from modules.dna_rna_tools import check_input, transcribe, reverse, complement, reverse_complement
    if len(inputs) < 2:
        raise ValueError('Invalid input: the function requires at least one sequence and an operation name!')
    *seqs, operation = inputs
    check_input(seqs, operation)
    if operation == 'transcribe':
        result = transcribe(seqs)
    elif operation == 'reverse':
        result = reverse(seqs)
    elif operation == 'complement':
        result = complement(seqs)
    elif operation == 'reverse_complement':
        result = reverse_complement(seqs)
    else:
        raise ValueError('Invalid input: unknown operation! Check the last argument.')
    if len(result) == 1:
        result = ''.join(result)
    return result


def run_protein_tools(inputs: tuple, options: str = None) -> list or dict:
    """
    Produce a list or dictionary according to the option specified
    arguments:
    - inputs (tuple): a tuple of inputs
    - options (str): option name
    """
    from modules.protein_tools import calculate_similarity, count_length, info_amino_acid_percentage, find_pattern, convert_to_gene, recode_3letter_to_1letter, check_protein, string_check, check_input
    check_input(inputs, options)
    operations = {
        'similarity': calculate_similarity,
        'length': count_length,
        'percentage': info_amino_acid_percentage,
        'pattern': find_pattern,
        '3letter_name': recode_3letter_to_1letter,
        'dna_code': convert_to_gene
    }

    if options == 'similarity':
        result = operations[options](inputs[:-2], inputs[-2], inputs[-1])
        return (result)
    elif options == 'pattern':
        result = operations[options](inputs[1:len(inputs)], inputs[0])
        return (result)
    elif options == '3letter_name':
        result = operations[options](inputs[:-1], inputs[-1])
        return (result)
    elif options == 'length' or options == 'percentage' or options == 'dna_code':
        result = []
        for inpt in inputs:
            res = operations[options](inpt)
            result.append(res)
        return (result)
    else:
        raise ValueError('Incorrect options input, please try again')


def run_fastq_filtration(seqs: dict, gc_bounds: tuple = (0, 100), length_bounds: tuple = (0, 2**32), quality_threshold: int = 0):
    """
    Filtrate a fastq dictionary according to parameters specifies
    arguments:
    - seqs (dict): fastq dictionary
    - gc_bounds (tuple): range of GC content
    - length_bounds (tuple): range of sequence length
    - quality_threshold (int): lower limit of average in-sequence quality
    return:
    - seqs_filtered (dict): filtered fastq dictionary
    """
    from modules.fastq_filtration_tools import check_fastq, check_gc, check_length, check_quality
    check_fastq(seqs)
    seqs_filtered = {}
    if type(gc_bounds) == int:
        gc_bounds = tuple([0, gc_bounds])
    if type(length_bounds) == int:
        length_bounds = tuple([0, length_bounds])
    for seq_name in seqs:
        gc_check = False
        length_check = False
        quality_check = False
        gc_check = check_gc(seqs[seq_name][0], gc_bounds)
        length_check = check_length(seqs[seq_name][0], length_bounds)
        quality_check = check_quality(seqs[seq_name][1], quality_threshold)
        if gc_check and length_check and quality_check:
            seqs_filtered[seq_name] = seqs[seq_name]
    return seqs_filtered


def run_beginner_bioinf_tools(*input_data: str or dict, toolbox: str = None, **kwargs: str) -> str or list or dict:
    """
    Performs various operations on nucleic acid, protein and fastq sequences
    arguments:
    - input_data (str or dict): data to be processed
    - toolbox (str): determines which of the three toolkits is used
    return:
    - (str or list or dict): processed data
    """
    if toolbox == 'dna_rna':
        return run_dna_rna_tools(input_data)
    elif toolbox == 'proteins':
        return run_protein_tools(input_data, kwargs['options'])
    elif toolbox == 'fastq':
        return run_fastq_filtration(input_data[0], gc_bounds = kwargs['gc_bounds'], length_bounds = kwargs['length_bounds'], quality_threshold = kwargs['quality_threshold'])
    else:
        raise ValueError('Invalid input: there is no toolbox corresponding to value ' + str(toolbox) + '!')

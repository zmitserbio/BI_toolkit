def convert_multiple_fasta_to_oneline(input_fasta: str, output_fasta: str = 'convert_multiple_fasta_to_oneline-output'):
    """
    Read .fasta file where swquences are written on multiple lines,
    and create a .fasta file where each sequence is contained in one string
    arguments:
    - input_fasta (str): path to input file
    - output_fasta (str): name of output .fasta file
    return:
    - no return
    """
    import os
    with open(input_fasta) as fasta:
        fasta_dict = {}
        current_name = fasta.readline().strip()
        fasta_dict[current_name] = []
        for line in fasta:
            if line.startswith('>'):
                fasta_dict[current_name] = ''.join(fasta_dict[current_name])
                current_name = line.strip()
                fasta_dict[current_name] = []
            else:
                fasta_dict[current_name].append(line.strip())
        fasta_dict[current_name] = ''.join(fasta_dict[current_name])
    with open(str(output_fasta) + '.fasta', mode='w') as fasta:
        for name in fasta_dict:
            fasta.write(name + '\n')
            fasta.write(fasta_dict[name] + '\n')


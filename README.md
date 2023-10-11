# beginner_bioinf_tools.py
> This document provides description of `beginner_bioinf_tools` program, which contains `run_beginner_bioinf_tools` function.

This function uses three toolkits to perform a variety of tasks with nucleic acid, protein and fastq sequences. It accepts an arbitrary number of nucleic acid or protein sequences, or a dictionary (dict) of fastq sequences. Keyword arguments specify which toolkit should be used (**toolbox**), as well as various options within each toolkit: 

`run_beginner_bioinf_tools(*input_data, toolbox=None, **kwargs)`

**toolbox** accepts the following values (str):
- 'dna_rna': uses `dna_rna_tools` toolkit
- 'proteins': uses `protein_tools` toolkit
- 'fastq': uses `fastq_filtration` toolkit

Below further requirements for each toolkit are specified. Even though the program performs input checks and provides helpful error messages, the following information should be read carefully prior to program use.
## dna_rna_tools toolkit
> This toolkit, with `run_dna_rna_tools` as its main function, allows to perform basic operations with strings representing DNA or RNA sequences.

⚠️ all operations in this toolkit are case-sensetive!

### Input:

All operations in this toolkit process an orbitrary number of nucleic acid sequences (str) containing 'A', 'T'/'U', 'C', 'G' in either case. This toolkit does not require any additional keyword arguments. Instead, the last positional argument provided should be a name (str) of a desired operation. It accepts the following names:
- 'transcribe': transcribes DNA sequences; utilises `transcribe` function from *modules/dna_rna_tools.py*; **DNA input only!**
- 'reverse': reverses nucleic acid sequences; utilises `reverse` function from *modules/dna_rna_tools.py*; DNA and RNA input
- 'complement': produces complementary sequences; utilises `complement` function from *modules/dna_rna_tools.py*; DNA and RNA input
- 'reverse_complement': produces reverse complementary sequences; utilises `reverse_complement` function from *modules/dna_rna_tools.py*; DNA and RNA input

### Output:

- if there is only one sequence, a str object is returned
- if there are multiple sequences, a list object is returned

Below examples of usage are provided for each opeartion:

**'transcribe'**
```python
run_beginner_bioinf_tools('ATG', 'transcribe', toolbox = 'dna_rna') # 'TAC'
run_beginner_bioinf_tools('ATG', 'GCaTta', 'transcribe', toolbox = 'dna_rna') # ['TAC', 'CGtAat']
```
**'reverse'**
```python
run_beginner_bioinf_tools('uAg', 'reverse', toolbox = 'dna_rna') # 'gAu'
run_beginner_bioinf_tools('ATG', 'GCaTta', 'reverse', toolbox = 'dna_rna') # ['GTA', 'atTaCG']
```
**'complement'**
```python
run_beginner_bioinf_tools('uAg', 'complement', toolbox = 'dna_rna') # 'aUc'
run_beginner_bioinf_tools('uAg', 'ATCCT', 'complement', toolbox = 'dna_rna') # ['aUc', 'TAGGA']
```
**'reverse_complement'**
```python
run_beginner_bioinf_tools('uAg', 'reverse_complement', toolbox='dna_rna') # 'cUa'
run_beginner_bioinf_tools('uAg', 'ATCCT', 'reverse_complement', toolbox='dna_rna') # ['cUa', 'AGGAT']
```

> Since reverse transcription is used much less frequently than normal transcription, and to prevent accidental "contamination" with RNA sequences, in 'transcribe' supports only DNA sequences. For reverse transcription a separate operation should be used.

## protein_tools toolkit


# beginner_bioinf_tools.py
> This document provides description of `beginner_bioinf_tools` program, which contains `run_beginner_bioinf_tools` function.

This function uses three toolkits to perform a variety of tasks with nucleic acid, protein and fastq sequences. It accepts an arbitrary number of nucleic acid or protein sequences, or a dictionary ('dict') of fastq sequences. Keyword arguments specify which toolkit should be used (**toolbox**), as well as various options within each toolkit: 

`run_beginner_bioinf_tools(*input_data, toolbox=None, **kwargs)`

**toolbox** accepts the following values ('str'):
- 'dna_rna': uses `dna_rna_tools` toolkit
- 'proteins': uses `protein_tools` toolkit
- 'fastq': uses `fastq_filtration` toolkit

Below further requirements for each toolkit are specified. Even though the program performs input checks and provides helpful error messages, the following information should be read carefully prior to program use.

## 'dna_rna' - dna_rna_tools toolkit
> This toolkit, with `run_dna_rna_tools` as its main function, allows to perform basic operations with strings representing DNA or RNA sequences.

⚠️ all operations in this toolkit are case-sensetive!

### Input:

All operations in this toolkit process an arbitrary number of nucleic acid sequences ('str') containing 'A', 'T'/'U', 'C', 'G' in either case. This toolkit does not require any additional keyword arguments. Instead, the last positional argument provided should be the name ('str') of a desired operation. It accepts the following names:
- 'transcribe': transcribes DNA sequences; utilises `transcribe` function from *modules/dna_rna_tools.py*; **DNA input only!**
- 'reverse': reverses nucleic acid sequences; utilises `reverse` function from *modules/dna_rna_tools.py*; DNA and RNA input
- 'complement': produces complementary sequences; utilises `complement` function from *modules/dna_rna_tools.py*; DNA and RNA input
- 'reverse_complement': produces reverse complementary sequences; utilises `reverse_complement` function from *modules/dna_rna_tools.py*; DNA and RNA input

### Output:

- if there is only one sequence, a 'str' object is returned
- if there are multiple sequences, a 'list' object is returned

Below examples of usage are provided for each operation:

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
run_beginner_bioinf_tools('uAg', 'reverse_complement', toolbox = 'dna_rna') # 'cUa'
run_beginner_bioinf_tools('uAg', 'ATCCT', 'reverse_complement', toolbox = 'dna_rna') # ['cUa', 'AGGAT']
```

> Since reverse transcription is used much less frequently than normal transcription, and to prevent accidental "contamination" with RNA sequences, 'transcribe' supports only DNA sequences. For reverse transcription a separate operation should be used (currently not implemented).

## 'proteins' - protein_tools toolkit
> This toolkit, with `run_protein_tools` as its main function, allows to perform several operations with strings representing amino acid sequences.

⚠️ all operations in this toolkit are case-sensetive!

This toolkit requires one keyword argument: `options`. This argument accepts the following values ('str'):
- 'similarity': counts how similar sequences are to a reference; utilises `calculate_similarity` function from *modules/protein_tools.py*; **requires sequences of equal length!**
- 'length': measures the length of each sequence; utilises `count_length` function from *modules/protein_tools.py*;
- 'percentage': calculates the percentage of each amino acid in each sequence; utilises `info_amino_acid_percentage` function from *modules/protein_tools.py*;
- 'pattern': finds all non-overlapping instances of a pattern and counts their total number in each sequence; utilises `find_pattern` function from *modules/protein_tools.py*;
- '3letter_name': translates each sequence into three-letter code; utilises `recode_3letter_to_1letter` function from *modules/protein_tools.py*;
- 'dna_code': produces gene sequences that can potentially ecode each protein sequence; utilises `convert_to_gene` function from *modules/protein_tools.py*;
Below further information on each of these options is provided:

### 'similarity'
> 'similarity' option entails comparison between the first amino acid sequence (reference) and the following ones.

**Input:** 

- _an arbitrary number_ of sequences, where the first sequence is a reference to which the following sequences are compared; each argument should be of type 'str'. **All sequences must be of equal length!**
- _second-to-last_ positional argument is the number of decimals to round the number to; equals 3 if not specified; type 'int'
- _last_ positional argument determines whether percentages are returned instead of fractions; equals False if not specified; type 'bool'

**Output:** 

a 'dict' object where:
- *keys* are compared-to sequences (type 'str')
- *values* are either fractions or percentages (type 'float').

**Usage example:**

```python
run_beginner_bioinf_tools('LalKekKe', 'AwYLalKe', 'lalkekFM', 2, False, toolbox = 'proteins', options = 'similarity') # {'AwYLalKe': 0.25, 'lalkekFM': 0.5}
run_beginner_bioinf_tools('LalKekKe', 'AwYLalKe', 'lalkekFM', 1, True, toolbox = 'proteins', options = 'similarity') # {'AwYLalKe': 25.0, 'lalkekFM': 50.0}
```
> Equal length requirement results from the fact that sequences of non-equal length cannot be compared unambiguously. For instance, what is the percentage of similarity between KEK and KEKE: 100%, when we compare them 'head-to-head', or 0%, when we compare 'tail-to-tail'? What about LALKEKFM and ALKEKF? This option expects sequences to already be alligned. If that is not the case for your data, we suggest using other programs. Alternatively, 'find_pattern' can potentially be modified to find 'imprecise' matches, which in turn can be built upon to create a proper allignment tool. However, such task goes far beyond the scope of this program's intended capabilities.

### 'length'
> 'length' option calculates the length of protein sequence(s) (equal to the number of amino acids in them).

**Input:**

- _an arbitrary number_ of sequences, type 'str' 

**Output:**

a 'list' object with the length ('int') of each sequence

**Usage example:**

```python
run_beginner_bioinf_tools('LalKekK', 'AwYLalKe', 'l', toolbox = 'proteins', options = 'length') # [7, 8, 1]
```

### 'percentage'
> 'percentage' option calculates the percentages of all 20 proteinogenic amino acid residues in each sequence

**Input:**

- _an arbitrary number_ of sequences, type 'str'

**Output:**

a 'list' object containing dictionaries ('dict') with the percentages of the corresponding amino acids in each sequence; the dictionary is ordered from the largest percentage of content to the smallest

⚠️ The dictionaries contain only amino acid residues whose percentage in the sequence is not equal to 0

⚠️ Results are rounded to 2 digits. In some cases, **the overall sum of percentages** for a sequence **may not be exactly 100%** due to rounding.

**Usage example:**

```python
run_beginner_bioinf_tools('INQQTS', toolbox = 'proteins', options = 'percentage') # [{'Q': 33.33, 'I': 16.67, 'N': 16.67, 'T': 16.67, 'S': 16.67}]
run_beginner_bioinf_tools('IIQQTS', 'NHNECHNDNFF', 'EQETTCTAVQ', toolbox = 'proteins', options = 'percentage')
# [{'I': 33.33, 'Q': 33.33, 'T': 16.67, 'S': 16.67},
# {'N': 36.36, 'H': 18.18, 'F': 18.18, 'E': 9.09, 'C': 9.09, 'D': 9.09},
# {'T': 30.0, 'E': 20.0, 'Q': 20.0, 'C': 10.0, 'A': 10.0, 'V': 10.0}]
```

### 'pattern'
> 'pattern' option finds all non-overlaping cases of a given pattern in amino acid sequence(s) provided.

**Input:**

- _an arbitrary number_ of sequences, where the first sequence is a pattern, which is searched for in the following sequences; each argument should be of type 'str'

**Output:**

a 'dict' object where:
- *keys* are amino acid sequences (type 'str') 
- _values_ are 'list' objects where the first element is a number of pattern instances in a given sequence, and the following elements are indexes of these occurances

**Usage example:**
  
```python
run_beginner_bioinf_tools('Lal', 'AwYLalKekQPSMFLaKeKFCLal', 'PFERDHISTKSLallaKelalkekFM', 'laLal', 'Lal',  toolbox = 'proteins', options = 'pattern')
# {'AwYLalKekQPSMFLaKeKFCLal': [2, 3, 21],
# 'PFERDHISTKSLallaKelalkekFM': [1, 11],
# 'laLal': [1, 2],
# 'Lal': [1, 0]}
run_beginner_bioinf_tools('lal', 'AwYLalKekQPSMFLaKeKFCLal', 'PFERDHISTKSLallaKelalkekFM', 'lalal', 'Lal',  toolbox = 'proteins', options = 'pattern')
# {'AwYLalKekQPSMFLaKeKFCLal': [2, 3, 21],
# 'PFERDHISTKSLallaKelalkekFM': [1, 11],
# 'lal': [0],
# 'Lal': [1, 0]}
```

### '3letter_name'
> '3Letter_name' option transforms one-letter amino acid sequences to three-letter amino acid sequences, separated by a specified separator

**Input:**

- _an arbitrary number_ of sequences, followed by a string that should separate amino acids; each argument should be of type 'str' 

**Output:**

a 'list' of three-letter sequences ('str'). Each amino acid is separated by the specified separator

**Usage example:**
  
```python
run_beginner_bioinf_tools('haHAha', ' ',  toolbox = 'proteins', options = '3letter_name') # ['his ala HIS ALA his ala']
run_beginner_bioinf_tools('L', 'laLal', 'QwErTy', '-',  toolbox = 'proteins', options = '3letter_name') # ['LEU', 'leu-ala-LEU-ala-leu', 'GLN-trp-GLU-arg-THR-tyr']
```

### 'dna_code'
> 'dna_code' option produces DNA sequences that can theoretically encode the protein sequences provided 

**Input:**

- _an arbitrary number_ of sequences, type 'str'

**Output:**

a 'list' object with type 'str' elements - nucleotide sequences that correspond to their respective amino acid sequences.

**Usage example:**

```python
run_beginner_bioinf_tools('smallPRATEIN', toolbox = 'proteins', options = 'dna_code') # ['tcgatggcattattaCCCCGAGCAACCGAGATTAAT']
run_beginner_bioinf_tools('haHAha', 'LAlKek', 'EQSaMplE', toolbox = 'proteins', options = 'dna_code') # ['catgcaCATGCAcatgca', 'TTAGCAttaAAAgagaaa', 'GAGGAATCGgcaATGcccttaGAG']
```
> Note that the codons were chosen at the discretion of the tool authors.

## 'fastq' - fastq_filtration toolkit
> This toolkit, with `run_fastq_filtration` as its main function, allows to filtrate fastq sequences according to several criteria.

⚠️ For this toolkit to function properly, it is very important that data is provided in the format described below!

### Input:
 This toolkit accepts **one** positional argument - 'dict' object containing fastq sequences, where:
- *keys* are sequence names (in fastq format!) 
- _values_ are 'tuple' objects where the first element is a sequence, and the second element is a sequence of 'quality measurements' for that sequence (see [here](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm))

⚠️ This toolkit is designed to recieve one such 'dict' object as input; any additional positional arguments will be ignored!

Filtration criteria can be specified via three keyword arguments:
- 'gc_bounds': 'tuple' object providing range of GC content desired; equals (0,100) if not specified; if one 'int' object is provided, takes it as the upper limit
- 'length_bounds': 'tuple' object providing range of sequence length desired; equals (0,2^32) if not specified; if one 'int' object is provided, takes it as the upper limit
- 'quality_threshold': 'int' object providing the lower limit of average in-sequence quality; equals 0 if not specified
### Output:
 This toolkit returns a 'dict' object of the same format as required input, containing only those sequences that fit the criteria provided
### Usage example:
```python
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079804:1:SRR292678:1:1101:149302:149302': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079804:1:SRR292678:1:1101:170868:170868': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
    }
```
```python
run_beginner_bioinf_tools(EXAMPLE_FASTQ, toolbox = 'fastq', gc_bounds = (50,95), length_bounds = 80, quality_threshold = 27)
# {'@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG',
#  'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
# '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC',
#  'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE')}
```

## Useful links:
For either checking this code, or building upon it, we recommend the following resources:
- [generate random protein sequence](https://www.bioinformatics.org/sms2/random_protein.html?)
- [generate random nucleic acid sequence with specified length, GC content, ect.](http://www.molbiol.ru/eng/scripts/01_16.html)
- [quality score encoding](https://support.illumina.com/help/BaseSpace_OLH_009008/Content/Source/Informatics/BS/QualityScoreEncoding_swBS.htm)
- [ASCII table](https://www.asciitable.com/)

## Contacts and acknowledgements:
[Dmitry Matach](https://github.com/zmitserbio): author;

[Gleb Bobkov](https://github.com/GlebBobkov): contributor; 'length' and 'dna_code' options in protein_tools toolkit;

[Olga Bagrova](https://github.com/Olga-Bagrova): contributor; 'percentage' and '3letter_name' options in protein_tools toolkit.   

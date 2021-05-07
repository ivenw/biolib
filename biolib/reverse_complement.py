def reverse_complement(dna_string) :

	'''Given: A DNA string, case agnostic.
	Return: The reverse complement the DNA string.'''

    DNA = (
        'A', 'C', 'G', 'T',
        'a', 'c', 'g', 't',
    )

    # reverse complement map
    KEY_MAP = {
        'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
        'a': 't', 't': 'a', 'c': 'g', 'g': 'c'
    }

	if type(dna_string) != str :
		return('Input not str')

	if (any(map(lambda i : i not in DNA, dna_string))) :
		return('Input not a DNA sequence')

    reversed = ''.join([KEY_MAP[i] for i in reversed(dna_string)])

    return reversed

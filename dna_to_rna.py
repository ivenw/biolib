def dna_to_rna (dna_string, case='upper') :

    '''Given: A DNA string dna_string and options for 'upper' or 'lower' case output
    Return: The transcribed RNA string of dna_string.'''

    if type(dna_string) != str :
        return ('Input not str')

    if case == 'upper' :
        dna_string = dna_string.upper() # homogenize string to uppercase
        rna_string = dna_string.replace('T', 'U')

    if case == 'lower' :
        dna_string = dna_string.lower() # homogenize string to lowercase
        rna_string = dna_string.replace('t', 'u')

    return rna_string

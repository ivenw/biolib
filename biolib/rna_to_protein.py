def rna_to_protein(rna_str, codon_table = 'codon_table.txt') :

    '''Converts RNA string to protein sequence in one letter code.
    Given: str with RNA sequence and optional codon_table txt file.
    returns str with translated sequence'''

    # import codon table file and generate continuos string
    with open(codon_table, 'r') as f :
        f_str = f.read()
        f_str = f_str.replace(' ', '').replace('\n', '')

    # generate with codon:amino acid key:value pair
    codon_dict = { f_str[i:i+3]: f_str[i+3] for i in range(0, len(f_str) - 3, 4) }

    rna_str = rna_str.upper() # homogenize RNA str to uppercase
    
    # looping over the rna str and generating translated string
    chunk_list = [ rna_str[i:i+3] for i in range(0, len(rna_str) - 2, 3) ]
    translated = ''.join( [codon_dict[i] for i in chunk_list if codon_dict[i] != 'X'] )

    return translated

# test
if __name__ == '__main__' :
    rna_to_protein('UCAAUG')

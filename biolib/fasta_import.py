def fasta_import(file) :

    '''Given a fasta file, returns all entries as a dict with fasta header as
    key and DNA string as value'''

    with open(file, 'r') as f : # open file and generate string of contents
        f_str = f.read()

    entries = f_str.split('>')	#generate list of entries
    del entries[0]	#remove leading empty entry

    out_dict = {}	#init dict for output

    for e in entries :
        entry_list = e.splitlines()
        key = entry_list[0] #extract the future key value
        item = ''
        for part in entry_list[1:] :	#concat all parts of the DNA string
            item += part

        out_dict[key] = item

    return out_dict

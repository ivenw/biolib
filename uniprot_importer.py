from urllib.request import urlopen

def import_uniprot(uniprot_id) :

	'''Given: Uniprot ID str
    Returns: str of protein sequence'''

	with urlopen('https://www.uniprot.org/uniprot/' + uniprot_id + '.fasta') as response :
		html_content = response.read()

	encoding = response.headers.get_content_charset('utf-8')
	html_text = html_content.decode(encoding)

	html_text = html_text.split('\n', 1)[1].replace('\n', '')

	return html_text

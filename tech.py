import requests


def make_labels_for_ncbi_from_hmmer():
    # File download.fa has to be in the folder
    def fasta_lables(strings):
        labels = []
        for string in strings:
            if string.startswith('>'):
                labels.append(string[1:])
        return labels

    input_file = open('download.fa', 'r')
    lines = input_file.read().splitlines()
    labels = fasta_lables(lines)
    input_file.close()

    output_file = open('labels_for_ncbi.txt', 'w')
    for label in labels:
        string = str(label) + '\n'
        output_file.write(string)
    output_file.close()


def find_positions():
    ncbi_labels = open('ncbi_labels.txt')

    pos_file = open('positions.txt', 'w')
    for label in ncbi_labels:
        final_position = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=gp&retmode=text&id={}'.format(label))
        position = final_position.text
        pos_file.write(position)


# download.fa - is a file from hmmer
make_labels_for_ncbi_from_hmmer()
# After this function in the folder will be labels_for_ncbi.txt file
# This file should go to
# https://www.uniprot.org/uploadlists/
# ncbi_labels.txt - is the output file from ncbi converter
ncbi_labels = open('ncbi_labels.txt')
find_positions()
# positions.txt - is the final file

def extract_positions_from_input(file):
    '''
    Reading fasta format
    :param fp: multiples string on different lines
    :return: sequences as list
    '''
    positions = []
    result = ""
    for line in file:
        if "CDS" in line:
            positions.append('\n')
            positions.append('\n')
            result = line  # Initiation of a new seq
        elif 'ORIGIN' in line:
            positions.append(result)
        else:
            result += line

    positions.append(result)  # Appending list with last seq

    return positions

with open('positions.txt') as positions:
    lines = positions.readlines()
    pos = extract_positions_from_input(lines)
    places = open('places.txt', 'w')
    for p in pos:
        places.write(p)
positions.close()


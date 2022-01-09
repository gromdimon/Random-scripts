def read_fasta_with_labels(fp):
    '''
    Reading fasta format
    :param fp: multiples string on different lines
    :return: sequences referd to labels
    '''
    name = None
    seq = []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))  # interim genes
            name = line  # first name
            seq = []  # first seq
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))  # yields last gene

    genes = {}  #  Reading fasta file
    with open('test.txt') as fp:
        for name, seq in read_fasta(fp):
            genes[name] = seq
    return genes

def extract_sequence_from_input(file):
    '''
    Reading fasta format
    :param fp: multiples string on different lines
    :return: sequences as list
    '''
    sequences = []
    result = ""
    for line in file:
        if ">" in line:
            sequences.append(result)  # Appending sequence list with final seq
            result = ""  # Initiation of a new seq
        else:
            if "\n" in line:
                result += line[:len(line) - 1]  # Lengthening of sequence
            else:
                result += line
    sequences.append(result)  # Appending list with last seq
    sequences.remove('')
    return sequences

with open('test.txt') as file:
    lines = file.readlines()
    liness = [line.rstrip() for line in lines]

def counting_gc(genes):
    GC = {}
    for sample in genes:
        sample_length = len(genes[sample])
        GC_count = genes[sample].count('G') + genes[sample].count('C')  # Count G and C in sample
        percent = GC_count / sample_length
        GC[sample] = percent   # Appending GC frame
    return GC

def permutation(alphabet, number, acc = '', res = []):
    if number == 0:
        res.append(acc)
    else:  # Cycle to the last letter
        for letter in alphabet:
            alpha_combs(alphabet, number - 1, acc + letter, res)
    return res

def shared_spliced_motif(shortest, longest):
    lengths = [[0 for j in range(len(longest) + 1)] for i in range(len(shortest) + 1)]  # This builds list of 0
    # creates array of len(s) containing arrays of len(t) filled with 0
    for id_s, value_s in enumerate(shortest):
        for id_l, value_l in enumerate(longest):
            if value_s == value_l:
                lengths[id_s + 1][id_l + 1] = lengths[id_s][id_l] + 1
            else:
                lengths[id_s + 1][id_l + 1] = max(lengths[id_s + 1][id_l], lengths[id_s][id_l + 1])
    spliced_motif = ''
    value_s, value_l = len(shortest), len(longest)
    while value_s * value_l != 0:
        if lengths[value_s][value_l] == lengths[value_s - 1][value_l]:
            value_s -= 1
        elif lengths[value_s][value_l] == lengths[value_s][value_l - 1]:
            value_l -= 1
        else:
            spliced_motif = shortest[value_s - 1] + spliced_motif
            value_s -= 1
            value_l -= 1
    return spliced_motif

def shared_spliced_motif_tablet(seq1, seq2):
    current = [''] * (len(seq2) + 1)
    for i in seq1:
        last, current = current, ['']
        for j, n in enumerate(seq2):
            current.append(last[j] + i if i == n else max(last[j + 1], current[-1], key=len))
    return (current[-1])

def spliced_motif(dna, substring):
    answer = [0]
    for i in range(len(substring)):
        for j in range(len(dna)):
            if substring[i] == dna[j] and j > answer[-1] - 1:
                answer.append(j + 1)
                break
    return answer[1:]

def superstring(strings):
    ''' Create Superstring
    :param strings: list of DNA strings
    :return: superstring via maximal overlap
    '''
    max_k = len(strings[0])
    min_k = max_k // 2 + 1
    super_string = strings.pop(0)
    while strings:
        for candidate in strings:
            for l in range(min_k, max_k):
                if candidate[-l:] == super_string[:l]:
                    super_string = candidate + super_string[l:]
                    strings.remove(candidate)
                    break
                elif candidate[:l] == super_string[-l:]:
                    super_string = super_string + candidate[l:]
                    strings.remove(candidate)
                    break

    return super_string

def calculate_increasing_subseq(sequence):
    ''' Calculate a longest increasing subsequence
    :param sequence: sequence to search the lis in
    :return: a lis
    '''
    L = [[sequence[0]]]
    for i in range(1, len(sequence)):
        L.append([])
        for j in range(i):
            if (sequence[j] < sequence[i]) and (len(L[i]) < len(L[j]) + 1):
                L[i] = L[j][:]
        L[i].append(sequence[i])
    lis = []
    max_len = 0
    for l in L:
        if len(l) > max_len:
            max_len = len(l)
            lis = l
    return lis

def possible_proteins(string):
    ''' Find Possible Proteins from ORFs
    :param string: DNA string
    :return: possible protein strings
    '''
    start_pos_list = []
    for i in range(len(string) - 2):
        if string[i:i + 3] == "ATG":
            start_pos_list.append(i)
    protein_list = set()
    for start_pos in start_pos_list:
        protein = ""
        for i in range(start_pos, len(string) - 2, 3):
            triplet = string[i:i + 3].replace("T", "U")
            aa = CODON_TBL[triplet]
            if aa == "STOP":
                protein_list.add(protein)
                break
            protein += aa
    return protein_list

CODON_TBL = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"
}

def is_substr(find, data):
    if len(find) < 1 and len(data) < 1:  # If we have no substr or data
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

def longest_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:  # If we have no data or sample is too short
        for start_letter in range(len(data[0])):
            for lnth_substr in range(len(data[0]) - int(start_letter) + 1):
                if lnth_substr > len(substr) and is_substr(data[0][start_letter:start_letter + lnth_substr], data):
                    substr = data[0][start_letter: start_letter + lnth_substr]
    return substr

def longest_common_subsequence(v, w):
    current = [''] * (len(v) + 1)
    for i in w:
        last, current = current, ['']
        for j, n in enumerate(v):
            current.append(last[j] + i if i == n else max(last[j + 1], current[-1], key=len))
    return (current[-1])

def shortest_common_supersequence(v, w):
    lcsq_string = longest_common_subsequence(v, w)

    scs_string = ""
    i = 0
    j = 0
    for char in lcsq_string:
        if i < len(v):
            while v[i] != char:
                scs_string += v[i]
                i += 1
            i += 1
        if j < len(w):
            while w[j] != char:
                scs_string += w[j]
                j += 1
            j += 1
        scs_string += char

    if i < len(v):
        scs_string += v[i:]
    if j < len(w):
        scs_string += w[j:]

    return scs_string

def ti_tv_ratio(string1, string2):
    ''' Calculate Ti/Tv ratio
    :param string1: string 1
    :param string2: query string
    :return: Ti/Tv ratio (float)
    '''
    num_ti = 0
    num_tv = 0

    for sym1, sym2 in zip(string1, string2):
        if sym1 != sym2:
            if sym2 == TI_DICT[sym1]:
                num_ti += 1
            else:
                num_tv += 1

    return num_ti / num_tv

def failure_array(string):
    """ Calculate the Knuth-Morris-Pratt failure array
    :param string: the input string
    :return: failure array (list)
    """
    n = len(string)
    arr = [0] * n
    for i in range(1, n):
        j = arr[i - 1]
        while j > 0 and string[i] != string[j]:
            j = arr[j - 1]
        if string[i] == string[j]:
            j += 1
        arr[i] = j
    return arr
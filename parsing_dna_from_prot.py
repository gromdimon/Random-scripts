import requests


class dna_finding_feature():


    def make_labels_for_ncbi_from_hmmer():
        '''
        Эта программа использует последовательности протеинов из hmmer
        и выдает список всех индексов для дальнейшей загрузки в конвертер.
        :input: download.fa
        :return: labels_for_ncbi.txt
        '''
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
        '''
        Эта программа использует готовые индексы организмов для NCBI,
        и сохраняет резултаты поиска (место в геноме).
        :input: ncbi_labels.txt
        :return: positions.txt
        '''
        ncbi_labels = open('real_ncbi_labels.txt')

        pos_file = open('positions.txt', 'w')
        for label in ncbi_labels:
            final_position = requests.get(
                'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=gp&retmode=text&id={}'.format(
                    label))
            position = final_position.text
            pos_file.write(position)
        ncbi_labels.close()
        pos_file.close()


    def find_places():

        def extract_positions_from_input(file):
            '''
            Эта программа, используя информацию из ncbi,
            находит четкие места в геноме
            :param : positions.txt
            :return: places.txt
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


# Сперва мы получаем файл из hmmer, содержащий последовательности белков.
# Этот файл download.fa мы помещаем в папку, где находится и этот скрипт.
#dna_finding_feature.make_labels_for_ncbi_from_hmmer()   # Применяем эту функцию, получаем labels_for_ncbi.txt
# Далее мы загружаем этот файл в конвертер по сслыке --
# https://www.uniprot.org/uploadlists/
# Результат сохраняем в виде Target list
# Переименовываем файл в ncbi_labels.txt и помещаем в папку скрипта
dna_finding_feature.find_positions()  # Применяем функцию - получаем информацию по запросу в файле positions.txt
dna_finding_feature.find_places()  # Применяем функцию - получаем позиции для дальнейшего использования
class FASTQFile:
    """stores information about the contents of the fastq file"""

    def __init__(self, file, fastq_records):
        self.file = file
        self.fastq_records = fastq_records

    # def sort_reads(self):
    #
    #
    # def write_to_file(self):

    pass


class Read:
    """describe reads of the fastq file"""

    def __init__(self, read_id, read_sequence, comment, quality):
        self.read_id = read_id.strip()
        self.read_sequence = read_sequence.strip()
        self.comment = comment.strip()
        self.quality = quality.strip()

    def gc(self):
        gc = (self.read_sequence.count("C") + self.read_sequence.count("G")) / len(self.read_sequence) * 100
        return round(gc, 2)

    def mean_quality(self):
        total_quality = 0

        for sym in self.quality:
            total_quality += ord(sym) - 33

        mean_quality = total_quality / len(self.read_sequence)

        return round(mean_quality, 2)

    def __len__(self):
        return len(self.read_sequence)

    pass


def read_fastq(fastq_file_name):
    """It reads fastq file and returns an object of type FASTQFile"""
    with open(fastq_file_name, 'r') as file:
        fastq_records = list()
        while True:
            try:
                read_id = file.readline()
                if read_id == '':
                    break
                read_sequence = file.readline()
                comment = file.readline()
                quality = file.readline()

                fastq_records.append(Read(read_id, read_sequence, comment, quality))
            except:
                break

    for i in range(len(fastq_records)):
        globals()['fastq_read_' + str(i + 1)] = fastq_records[i]

    file = fastq_file_name.split('/')
    file = '/'.join(file[:-1])
    return FASTQFile(file, fastq_records)


FASTQFile_1 = read_fastq('C:/Users/smirn/projects/Python_BI_2022/homework_10/read_fastq.py')

print(FASTQFile_1.fastq_records[0])
print(FASTQFile_1.fastq_records[0].read_sequence)
#
# line_1 = '@SRX079804:1:SRR292678:1:1101:21885:21885 1:N:0:1 BH:ok'
# line_2 = 'ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA'
# line_3 = '+SRX079804:1:SRR292678:1:1101:21885:21885 1:N:0:1 BH:ok'
# line_4 = 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'
#
# Read(line_1, line_2, line_3, line_4)
#
# print(Read(line_1, line_2, line_3, line_4))
# print(fastq_read_1.read_sequence)
# print(len(fastq_read_1.read_sequence))
# print(fastq_read_1.gc())
# print(fastq_read_1.mean_quality())



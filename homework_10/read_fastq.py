class FASTQFile:
    """Stores information about the contents of the fastq file"""
    def __init__(self, file, name, fastq_records):
        self.file = file
        self.name = name
        self.fastq_records = fastq_records

    def sort_reads(self):
        """Sort reeds in fastq_records attribute by average quality, by reed length, GC-composition, reed ID"""
        self.fastq_records.sort(key=lambda read: (read.mean_quality(), len(read), read.gc(), read.read_id))

    def write_to_file(self):
        """Save all reads in the FASTQ file from the list fastq_records"""
        with open(self.file+'/'+self.name+'_new.fastq', 'w') as file:
            for read in self.fastq_records:
                file.write('@' + read.read_id + '\n')
                file.write(read.read_sequence + '\n')
                file.write(read.comment + '\n')
                file.write(read.quality + '\n')

    pass


class Read:
    """describe reads of the fastq file"""
    def __init__(self, read_id, read_sequence, comment, quality):
        self.read_id = read_id.strip("@\n")
        self.read_sequence = read_sequence.strip()
        self.comment = comment.strip()
        self.quality = quality.strip()

    def gc(self):
        """show GC content"""
        gc = (self.read_sequence.count("C") + self.read_sequence.count("G")) \
             / len(self.read_sequence) * 100

        return gc

    def mean_quality(self):
        """show mean quality"""
        total_quality = 0

        for sym in self.quality:
            total_quality += ord(sym) - 33

        mean_quality = total_quality / len(self.read_sequence)

        return mean_quality

    def __len__(self):
        return len(self.read_sequence)

    pass


def read_fastq(fastq_file_name):
    """It reads fastq file and returns an object of type FASTQFile"""
    with open(fastq_file_name, 'r') as file:
        i = 0
        fastq_records = list()
        while True:
            try:
                read_id = file.readline()
                if read_id == '':
                    break
                read_sequence = file.readline()
                comment = file.readline()
                quality = file.readline()

                i+=1
                globals()['fastq_read_' + str(i)] = Read(read_id, read_sequence, comment, quality)
                fastq_records.append(Read(read_id, read_sequence, comment, quality))

            except:
                break

    path = fastq_file_name.split('/')
    name = path[-1].removesuffix('.fastq')
    file = '/'.join(path[:-1])

    return FASTQFile(file, name, fastq_records)

# #For testing
# FASTQFile_1 = read_fastq('C:/Users/smirn/projects/Python_BI_2022/homework_10/test.fastq')
# FASTQFile_1.sort_reads()
# FASTQFile_1.write_to_file()
#
# print(len(fastq_read_1))
# print(fastq_read_1.gc())
# print(fastq_read_1.mean_quality())

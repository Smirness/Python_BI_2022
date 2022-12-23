# Python_BI_2022
## Description of function
The function `read_fastq()` creates objects that are obtained from the FASTQ file.
After the function is called, two types of objects are created.

## Description of classes
### **FASTQFile**
An object of class **FASTQFile** contains information about the path, name of fastq file and list of objects **Read**.

Attributes:  
* **file** - path to fastq file;
* **name** - name of fastq file;
* **fastq_records** - list of objects.

Methods:
* **sort_reads()** - Sort reeds in fastq_records attribute by average quality, by reed length, GC-composition, reed ID.
* **write_to_file()** - Save all reads in the FASTQ file from the list fastq_records.

### **Read**
Each object is a single read, which contains:
* id - header/identifier line 
* sequence - the base calls, 
* comment - separator, 
* quality - The base call quality scores (working with phred33).

The number of reads in the file is equal to the number of generated objects.

## Examples
````python
FASTQFile_1 = read_fastq('./test.fastq') # Run the function with fastq file
FASTQFile_1.sort_reads()     # Sort a list of reads 
FASTQFile_1.write_to_file()  # A new file will be created after sorting
````

````python
print(len(fastq_read_1)) # Show the length of the first read
print(fastq_read_1.gc()) # Show the GC content in the first read
print(fastq_read_1.mean_quality()) # Show the mean quality of the first read
````

## Sources used
for sorting:
* https://favtutor.com/blogs/sort-list-of-objects-python
* https://stackoverflow.com/questions/65355028/how-do-we-sort-a-list-of-objects-based-on-multiple-parameters-in-python

for reading fastq file (Used tha function - fastq_reader)
*https://github.com/ad3002/trseeker/blob/575089c2edf8ef93c3d7bdf652404823e4c4e14a/seqio/sra_file.py#L20

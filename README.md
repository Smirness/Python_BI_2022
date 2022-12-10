# Python_BI_2022
# homework_9 "os and sys"

There is folder with several UNIX commands, realised in Python.
These command are:
* wc.py [-l, -w, -c] 
* ls.py [-a]
* sort.py
* mkdir.py [-p]
* rm.py [-r]
* cat.py
* tail.py [-n]
* uniq.py

## Program feature description
### wc.py [-l, -w, -c]
It is used to find out number of lines, word count, byte specified in the files\
Usage: wc.py [OPTION]... [FILE]...

| [OPTION] | Description              |
|----------|--------------------------|
| -l       | print the newline counts |
| -w       | print the word counts    |
| -c       | print the byte counts    |
| no flags | running with all flags   |

### ls.py [-a]
List information about the FILEs (the current directory by default)\
Usage: ls.py [OPTION]... [FILE]...

| [OPTION] | Description                         |
|----------|-------------------------------------|
| -a       | do not ignore entries starting with |
| no flags | the current directory               |

### sort.py
SORT command is used to sort a file, arranging the records in a particular order\
Usage: sort.py [FILE]...

### mkdir.py [-p]
It creates each directory specifed on the command line in the order given\
Usage: mkdir.py [OPTION]... [FILE]...

| [OPTION] | Description                                             |
|----------|---------------------------------------------------------|
| -p       | no error if existing, make parent directories as needed |

### rm.py [-r]
Removes each specified file. By default, it does not remove directories\
Usage: rm.py [OPTION]... [FILE]...

| [OPTION] | Description                                       |
|----------|---------------------------------------------------|
| -r       | remove directories and their contents recursively |

### cat.py
Reads one or more files and prints their contents to standard output\
Usage: cat.py [FILE]...

### tail.py [-n]
Command for quickly accessing the last few lines of a given text file\
Usage: tail.py [OPTION]... [FILE]...

| [OPTION] | Description                                        |
|----------|----------------------------------------------------|
| -n       | output the last NUM lines, instead of the last 10; |

### uniq.py
Discard all but one of successive identical lines from INPUT (or standard input)
Usage: uniq.py [FILE]...

### Installation
There is a file - **install.sh**. It's update your $PATH and allow to run command without specifying the path.

```bash
source ./install.sh
```
After installation you will see "Installed".

### Runnig
If you didn't run ./install.sh. You can run commands only with specifying the path. \
**Example:** If your current location is **scripts_smirnov_vv** directory:
```
./wc.py ../test_files/test_wc.txt
```
output: \
11 38 219 test_files/test_wc.txt

## Examples 
Move to **test_files**\ and run:
### wc.py [-l, -w, -c]
```
wc.py test_wc.txt
```
**output:**\
11 38 219 test_files/test_wc.txt

### ls.py [-a]
```bash
ls.py -a ../../
```
**output:**\
.git  .idea  homework_9  README.md

### sort.py
```bash
sort.py ./test_sort.txt
```
**output:**\
Arrival\
Cloud Atlas\
Donnie Darko\
I Origins\
Interstellar\
Mr. Nobody\
Primer\
The Man from Earth\

### mkdir.py [-r]  and rm.py [-r]
```bash
touch test_file
rm.py test_file
```

```bash
mkdir.py test_dir
rm.py -r test_dir
```
### cat.py
```bash
cat.py ./test_wc.txt
```
**output:**\
Electric Dreams (2017 TV series)
1.  The Hood Maker
2.  Impossible Planet
3.  The Commuter
4.  Crazy Diamond
5.  Real Life
6.  Human Is
7.  The Father Thing
8.  Autofac
9.  Safe and Sound
10. Kill All Others

### tail.py [-n]
```bash
tail.py -n 3 ./test_wc.txt
```
**output:**
8.  Autofac
9.  Safe and Sound
10. Kill All Others

### uniq.py
```bash
cat.py ./test_uniq.txt
```
**output:**\
Interstellar\
Interstellar\
Arrival\
Arrival\
Arrival\
The Martian\
Interstellar\
Arrival

```bash
uniq.py ./test_uniq.txt
```
**output:**\
Interstellar\
Arrival\
The Martian\
Interstellar\
Arrival

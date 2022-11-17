import re

with open("results/ftps.txt", "w") as res:
    with open("data/references", 'r') as file:
        pattern_ftp = r"ftp\.sra\.[\w\d\.\/]*\b"
        for line in file:
            ftp = re.findall(pattern_ftp, line)
            for subftp in ftp:
                # print(subftp)
                res.write(subftp+'\n')

# The main filter function
def main(input_fastq, output_file_prefix, i=0, j=4,
         gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0, save_filtered=False):
    """
    Filter reeds by GC composition, length, quality.
    :param: input_fastq, output_file_prefix, i=0, j=4,
            gc_bounds=(0, 100), length_bounds=(0, 2 ** 32),
            quality_threshold=0, save_filtered=False
    :return: None
    """
    # numbers of lines in input_fastq
    num_lines_file_in = num_lines(input_fastq)

    # unification of parameters
    min_gc_bounds, max_gc_bounds, min_length_bounds, max_length_bounds = fix_set(gc_bounds, length_bounds)

    # lines extraction for filtering
    with open(input_fastq, "r") as file_in:
        lines = file_in.readlines()[i:j]
        line_1 = lines[1]
        line_3 = lines[3]

        # filtering
        status_gc = filtr_gc(line_1, min_gc_bounds, max_gc_bounds)
        status_len = filtr_len(line_1, min_length_bounds, max_length_bounds)
        status_q = filtr_qual(line_3, quality_threshold)

    name_output_file = name_file(input_fastq)

    # saving
    saving(status_gc, status_len, status_q, save_filtered,
           output_file_prefix, name_output_file,
           lines)

    # recursive call to read all lines in input_fastq
    if j <= (num_lines_file_in - 1):
        main(input_fastq, output_file_prefix, i + 4, j + 4, gc_bounds, length_bounds, quality_threshold, save_filtered)

    return


def num_lines(input_fastq):
    """
    Count number in input_fastq file
    :param: input_fastq
    :return: num_lines_file_in
    """
    with open(input_fastq) as file_in:
        num_lines_file_in = len(file_in.readlines())
    return num_lines_file_in


def name_file(input_fastq):
    """
    Create name for output files
    :param: input_fastq
    :return: name_output_file
    """
    input_fastq = list(input_fastq)
    name_output_file = "".join(input_fastq[:-6])

    return name_output_file


def fix_set(gc_bounds, length_bounds):
    """
    Filter reeds by GC composition, length, quality
    :param: gc_bounds, length_bounds
    :return: min_gc_bounds, max_gc_bounds, min_length_bounds, max_length_bounds
    """

    if isinstance(gc_bounds, int) is True:
        min_gc_bounds, max_gc_bounds = 0, gc_bounds
    else:
        min_gc_bounds, max_gc_bounds = gc_bounds

    if isinstance(length_bounds, int) is True:
        min_length_bounds, max_length_bounds = 0, length_bounds
    else:
        min_length_bounds, max_length_bounds = length_bounds

    return min_gc_bounds, max_gc_bounds, min_length_bounds, max_length_bounds


def filtr_gc(line_1, min_gc_bounds, max_gc_bounds):
    """
    Filter reeds by GC composition.
    :param: line_1, min_gc_bounds, max_gc_bounds
    :return: status (True/False)
    """
    status = False

    cg = (line_1.count("C") + line_1.count("G")) / (len(line_1) - 1) * 100

    if min_gc_bounds <= cg <= max_gc_bounds:
        status = True

    return status


def filtr_len(line_1, min_length_bounds, max_length_bounds):
    """
    Filter reeds by length
    :param: line_1, min_length_bounds, max_length_bounds
    :return: status (True/False)
    """
    status = False

    if min_length_bounds <= (len(line_1) - 1) <= max_length_bounds:
        status = True

    return status


def filtr_qual(line_3, quality_threshold):
    """
    Filter reeds by quality
    :param: line_3, quality_threshold
    :return: status (True/False)
    """
    acsii_table = {
        "33": "0", "34": "1", "35": "2", "36": "3", "37": "4", "38": "5", "39": "6", "40": "7", "41": "8", "42": "9",
        "43": "10", "44": "11", "45": "12", "46": "13", "47": "14", "48": "15", "49": "16", "50": "17", "51": "18",
        "52": "19",
        "53": "20", "54": "21", "55": "22", "56": "23", "57": "24", "58": "25", "59": "26", "60": "27", "61": "28",
        "62": "29",
        "63": "30", "64": "31", "65": "32", "66": "33", "67": "34", "68": "35", "69": "36", "70": "37", "71": "38",
        "72": "39", "73": "40"
    }

    status = False
    line_ascii = []
    sum_q_score = 0
    aver_q_score = 0

    for sym in line_3:
        ascii_code = ord(sym)
        line_ascii.append(ascii_code)
    line_ascii = line_ascii[:-1]

    for ascii_code in line_ascii:
        q_score = acsii_table[str(ascii_code)]
        sum_q_score += int(q_score)
        aver_q_score = sum_q_score / len(line_ascii)

    if aver_q_score >= quality_threshold:
        status = True

    return status


def saving(status_gc, status_len, status_q, save_filtered,
           output_file_prefix, name_output_file,
           lines):
    """
    Saving filtered lines in one or two files (optional).
    :param: status_gc, status_len, status_q, save_filtered,
            output_file_prefix, name_output_file,
            lines
    :return: None
    """
    if status_gc is True and status_len is True and status_q is True:
        with open(output_file_prefix + name_output_file + "_passed.fastq", "a") as file_passed:
            for line in lines:
                file_passed.write(line)
    else:
        if save_filtered is True:
            with open(output_file_prefix + name_output_file + "_failed.fastq", "a") as file_failed:
                for line in lines:
                    file_failed.write(line)
        return

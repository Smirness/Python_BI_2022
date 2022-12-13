import os
import sys


# The main filter function
def main(input_fastq, output_file_prefix, i=0,
         gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=0, save_filtered=False):
    """
    Filter reeds by GC composition, length, quality.
    :param: input_fastq, output_file_prefix, i=0, j=4,
            gc_bounds=(0, 100), length_bounds=(0, 2 ** 32),
            quality_threshold=0, save_filtered=False
    :return: None
    """
    # check if file empty
    if os.stat(input_fastq).st_size == 0:
        print('File is empty')
        sys.exit(0)

    j = i + 4
    # numbers of lines in input_fastq
    num_lines_file_in = num_lines(input_fastq)

    # unification of parameters
    min_gc_bounds, max_gc_bounds = fix_set(gc_bounds)
    min_length_bounds, max_length_bounds = fix_set(length_bounds)

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
        main(input_fastq, output_file_prefix, i + 4, gc_bounds, length_bounds, quality_threshold, save_filtered)

    return


def num_lines(input_fastq):
    """
    Count number in input_fastq file
    :param: input_fastq
    :return: num_lines_file_in
    """
    with open(input_fastq) as file_in:
        for i, line in enumerate(file_in):
            pass
    return i + 1


def name_file(input_fastq):
    """
    Create name for output files
    :param: input_fastq
    :return: name_output_file
    """
    name_output_file = input_fastq.removesuffix(".fastq")

    return name_output_file


def fix_set(bounds):
    """
    Filter reeds by GC composition, length, quality
    :param: gc_bounds, length_bounds
    :return: min_gc_bounds, max_gc_bounds, min_length_bounds, max_length_bounds
    """

    if isinstance(bounds, int) or isinstance(bounds, float):
        min_bound, max_bound = 0, bounds
    else:
        min_bound, max_bound = bounds

    return min_bound, max_bound


def filtr_gc(line_1, min_gc_bounds, max_gc_bounds):
    """
    Filter reeds by GC composition.
    :param: line_1, min_gc_bounds, max_gc_bounds
    :return: status (True/False)
    """

    cg = (line_1.count("C") + line_1.count("G")) / (len(line_1) - 1) * 100

    return min_gc_bounds <= cg <= max_gc_bounds


def filtr_len(line_1, min_length_bounds, max_length_bounds):
    """
    Filter reeds by length
    :param: line_1, min_length_bounds, max_length_bounds
    :return: status (True/False)
    """

    return min_length_bounds <= (len(line_1) - 1) <= max_length_bounds


def filtr_qual(line_3, quality_threshold):
    """
    Filter reeds by quality
    :param: line_3, quality_threshold
    :return: status (True/False)
    """

    line3 = line_3.strip()
    total_quality = 0

    for sym in line3:
        total_quality += ord(sym) - 33
    average_quality = total_quality / len(line3)

    return average_quality >= quality_threshold


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

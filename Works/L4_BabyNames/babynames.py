"""
File: babynames.py
Name: Jack Chen
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name in name_data:
        year_d = name_data[name]
        if year in year_d:
            if int(rank) < int(year_d[year]):
                year_d[year] = rank
            else:
                pass
        else:
            year_d[year] = rank
    else:
        year_d = {year: rank}
        name_data[name] = year_d  # 不能使用name_data = {name: year_d} 因name_data非第一筆資料


def add_file(name_data, filenames):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    for i in range(len(filenames)):  # Loop according to the amount of files
        year = ''
        with open(filenames[i], 'r') as f:
            for line in f:
                info = line.split(',')
                if len(info) < 2:  # The year in the first line is the only line with length less than 2.
                    year = info[0].strip()  # To acquire the year for the given chart
                else:  # Add data for the two names in every line
                    add_data_for_name(name_data, year, info[0].strip(), info[1].strip())
                    add_data_for_name(name_data, year, info[0].strip(), info[2].strip())


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    add_file(name_data, filenames)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    names = []
    for key, value in name_data.items():  # Dict loop
        key_case_sen = case_sensitive(key)  # Apply Case Sensitive
        target_case_sen = case_sensitive(target)
        if target_case_sen in key_case_sen:  # if input names is in dict, add it in the names list.
            names.append(key)
    return names


def case_sensitive(data):
    ans = ''
    for ch in data:
        if ch.isalpha():
            ans += ch.lower()
    return ans


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

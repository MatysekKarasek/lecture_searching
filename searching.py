import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)

def linear_search(sekvence,cislo):
    results ={"positions": [], "count": 0}

    for i in range(len(sekvence)):
        if sekvence[i] == cislo:
            results["positions"].append(i)
            results["count"] += 1
        else:
            continue
    return results

def pattern_search(sequence, pattern):
#  "dna_sequence": "ATGACGGAATATAAGC.."
    idx = 0
    position = set()
    pattern_index = 0
    n = len(sequence)
    m = len(pattern)
    while idx < m:
        if sequence[idx + pattern_index] != pattern[pattern_index]:
            break
        pattern_index = pattern_index + 1
    if pattern_index == m:
        position.add(idx + m //2)
        idx += 1
    return position





def main():

    sekvence = json.load("dna_sequence")
    pattern = "ATA"
    data1 = read_data("sequential.json","unordered_numbers")
    print(data1)





if __name__ == '__main__':
    main()
    cislo = 0




















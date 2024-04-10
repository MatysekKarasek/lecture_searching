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
    slovnik = []
    count = 0
    for i in sekvence:
        if i == cislo:
            slovnik.append(sekvence[i])
            count += 1
        else:
            continue
    return (slovnik, count)

def main():
    data1 = read_data("sequential.json","unordered_numbers")
    print(data1)

if __name__ == '__main__':
    main()
    cislo = 10
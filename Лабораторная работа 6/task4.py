import json

INPUT_FILE = "output.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as f:
        itog = []
        dictreader = f.readline().rstrip(new_line).split(delimiter)
        for line in f:
            dictionary = {}
            for pos, value in enumerate(line.rstrip(new_line).split(delimiter)):
                dictionary[dictreader[pos]] = value
            itog.append(dictionary)
    return itog
# TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

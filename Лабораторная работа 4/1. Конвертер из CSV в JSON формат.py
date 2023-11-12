import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, "r") as inp_f:
        reader = csv.DictReader(inp_f)
        inp = []
        for i in reader:
            inp.append(i)

    with open (OUTPUT_FILENAME, "w") as out_f:
        json.dump(inp, out_f, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
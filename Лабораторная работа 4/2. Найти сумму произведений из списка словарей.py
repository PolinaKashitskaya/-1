import json

INPUT_FILENAME = "input.json"
def task() -> float:
    with open(INPUT_FILENAME, "r") as f:
        list_of_inp_dicts = json.load(f)
        summa = sum(i["score"] * i["weight"] for i in list_of_inp_dicts)
    return round(summa, 3)

print(task())
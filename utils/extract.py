import re


def fetch_amount_from_string(string: str):
    expression = r"[0-9]+\.[0-9]+"
    return re.findall(expression, string)


def pageRange(string: str):
    expression = r"Page (\d+) of (\d+)"
    r = re.search(expression, string)
    return [str(r.group(1)), str(r.group(2))]


# if __name__ == "__main__":
#     print(fetch_amount_from_string("$22.45"))
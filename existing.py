import re
import os
import csv
from .utils import is_pair

parent = os.path.normpath(os.path.join(__file__, ".."))


def main():
    with open(os.path.join(parent, "words.txt"), "r", encoding="utf8") as stream:
        words = list(i[0] for i in csv.reader(stream, delimiter="\n"))

    with open(os.path.join(parent, "domains.txt"), "r", encoding="utf8") as stream, open(
        os.path.join(parent, "existing.txt"), "w", encoding="utf8"
    ) as out:
        reader = map(
            lambda x: x[0] if len(x) > 0 else "", csv.reader(stream, delimiter="\n")
        )
        com = re.compile(r"^[a-zA-Z]*.com$")

        for domain in reader:
            if com.search(domain) and is_pair(words, domain[:-4]):
                out.write(domain + "\n")


if __name__ == '__main__':
    main()
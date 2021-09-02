import re
import os
import csv

parent = os.path.normpath(os.path.join(__file__, ".."))
words = os.path.join(parent, "words.txt")

reader = lambda stream: map(
    lambda x: x[0] if len(x) > 0 else "", csv.reader(stream, delimiter="\n")
)

def main():
    with open(os.path.join(parent, "existing.txt"), "r", encoding="utf8") as stream:
        existing = set(i[0] for i in csv.reader(stream, delimiter="\n"))

    with open(os.path.join(parent, "generated.txt"), "w", encoding="utf8") as out:
        with open(words, "r", encoding="utf8") as stream1:
            for i, x in enumerate(reader(stream1)):
                print(f'Loop n = {i + 1}')

                with open(words, "r", encoding="utf8") as stream2:
                    for y in reader(stream2):
                        domain = x + y + ".com"
                        if domain not in existing:
                            out.write(domain + "\n")


if __name__ == '__main__':
    main()

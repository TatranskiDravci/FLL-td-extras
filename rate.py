#!/usr/bin/env python3

from sys import argv

def main():
    T = 0
    A = 0
    v = []
    with open(argv[1], "r") as data:
        avgr = 0
        count = 1
        for line in data:
            if "call to" in line:
                v.append(avgr / count)
                avgr = 0
                count = 1
                continue
            try:
                inline = line.split(" ")
                t = float(inline[0].strip())
                a = int(inline[1].strip())

                avgr += abs((a - A) / (t - T))
                count += 1

                A = a
                T = t
            except:
                continue

    print("CALL:\t|\tRATE:")
    i = 0
    for r in v:
        i += 1
        print(str(i)+"\t|\t"+str(r))

if __name__ == "__main__":
    main()

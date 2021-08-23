#!/usr/bin/env python3

from sys import argv
import numpy as np
import matplotlib.pyplot as plt

def main():
    extracted = []
    with open(argv[1], "r") as data:
        callnum = -1
        count = 0
        for line in data:
            if "call to" in line:
                callnum += 1
                count = 0
                continue
            if callnum == int(argv[2]):
                count += 1
                inline = line.split(" ")
                for i in range(len(inline)):
                    inline[i] = float(inline[i].strip())
                inline.insert(0, count)
                extracted.append(inline)

    npext = np.array(extracted)
    plt.plot(npext[:,int(argv[3])], npext[:,int(argv[4])])
    plt.show()


if __name__ == "__main__":
    main()

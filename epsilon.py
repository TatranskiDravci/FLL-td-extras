import sys

def main(args=[]):
    T = 0
    A = 0
    e = []
    with open(args[0], "r") as data:
        epsilon = 0
        for line in data:
            if "call to" in line:
                e.append(epsilon)
                epsilon = 0
                continue
            try:
                inline = line.split(" ")
                t = float(inline[0].strip())
                a = int(inline[1].strip())
                epsilon = epsilon + (((t - T) * (A + a)) / 2)
            except:
                continue

    print("CALL:\t|\tEPSILON:")
    i = 0
    for ep in e:
        i += 1
        print(str(i)+"\t|\t"+str(ep))

if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    main(args)

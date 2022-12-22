import sys

def main():
    totals = []
    curr = 0

    for line in sys.stdin:
        if line != '\n':
            curr += int(line)
        else:
            totals.append(curr)
            curr = 0

    print(sum(sorted(totals)[-3:]))

if __name__ == '__main__':
    main()
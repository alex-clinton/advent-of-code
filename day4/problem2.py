import sys

def main():
    count = 0

    for line in sys.stdin:
        range1, range2 = line.split(',')
        x1, y1 = map(int, range1.split('-'))
        x2, y2 = map(int, range2.split('-'))

        if (x1 <= x2 and y2 <= y1) or (x2 <= x1 and y1 <= y2):
            count += 1
        elif (x1 <= x2 <= y1) or (x1 <= y2 <= y1):
            count += 1

    print(count)

if __name__ == '__main__':
    main()
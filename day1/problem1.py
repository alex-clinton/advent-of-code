import sys

def main():
    largest = 0
    curr = 0

    for line in sys.stdin:
        curr = (curr+int(line)) if line != '\n' else 0
        largest = max(largest, curr)

    print(largest)

if __name__ == '__main__':
    main()
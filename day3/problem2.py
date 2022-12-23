import sys
from string import ascii_lowercase, ascii_uppercase

def main():
    priority = {}

    for index, char in enumerate(ascii_lowercase):
        priority[char] = index+1

    for index, char in enumerate(ascii_uppercase):
        priority[char] = index+27

    total = 0

    for line_count, line in enumerate(sys.stdin):
        line_chars = line.strip()

        if line_count%3 == 0:
            first_seen = set()
            second_seen = set()
            for char in line_chars:
                first_seen.add(char)

        elif line_count%3 == 1:
            for char in line_chars:
                second_seen.add(char)
                
        else:
            for char in line_chars:
                if char in first_seen and char in second_seen:
                    total += priority[char]
                    break
    
    print(total)

if __name__ == '__main__':
    main()
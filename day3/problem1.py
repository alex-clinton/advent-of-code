import sys
from string import ascii_lowercase, ascii_uppercase

def main():
    priority = {}

    for index, char in enumerate(ascii_lowercase):
        priority[char] = index+1

    for index, char in enumerate(ascii_uppercase):
        priority[char] = index+27

    total = 0

    for line in sys.stdin:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]

        seen = set()
        for char in first_half:
            seen.add(char)
        
        for char in second_half:
            if char in seen:
                total += priority[char]
                break
    
    print(total)

if __name__ == '__main__':
    main()
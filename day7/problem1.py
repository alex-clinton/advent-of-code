import sys
import os

def main():
    sizes = {}
    curr_path = '/'

    for line in sys.stdin:
        # Step out of current directory
        if 'cd ..' in line:
            curr_path, _ = os.path.split(curr_path)
        # Step into new directory
        elif ' cd ' in line:
            curr_path = os.path.join(curr_path, line.split()[2])
            sizes[curr_path] = 0
        # Add to directories that the current file is within
        elif (size := line.split()[0]).isnumeric():
            for path in filter(lambda x: x in curr_path, sizes.keys()):
                sizes[path] += int(size)

    print(sum(int(size) for size in sizes.values() if int(size) <= 100000))

if __name__ == '__main__':
    main()
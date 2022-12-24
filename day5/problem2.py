import sys

def read_line(line, stacks):
    line_chars = line.strip('\n')

    # Switch mode after empty line
    if line_chars.strip() == '':
        for stack in stacks:
            stack.reverse()
        return False

    elif '[' in line_chars:
        for i in range(9):
            if (char := line_chars[1+i*4]) != ' ':
                stacks[i].append(char)
    return True

def main():
    crate_input = True
    stacks = [[] for i in range(9)]

    for line in sys.stdin:
        # Read in crate input to arrays
        if crate_input:
            crate_input = read_line(line, stacks)
        # Move crates based on queries
        else:
            instruction = line.split()
            count, from_stack, to_stack = map(int, instruction[1::2])

            stacks[to_stack-1] = stacks[to_stack-1] + stacks[from_stack-1][-count:]
            stacks[from_stack-1] = stacks[from_stack-1][:-count]

    print(''.join(stack[-1] for stack in stacks))

if __name__ == '__main__':
    main()
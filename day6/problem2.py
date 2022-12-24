import sys

def main():
    signal = sys.stdin.readline()
    potential_packet = [signal[i] for i in range(14)]

    for i in range(14, len(signal)):
        if len(set(potential_packet)) == 14:
            print(i)
            break
        potential_packet.pop(0)
        potential_packet.append(signal[i])

if __name__ == '__main__':
    main()
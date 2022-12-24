import sys

def main():
    signal = sys.stdin.readline()
    potential_packet = [signal[0], signal[1], signal[2], signal[3]]

    for i in range(4, len(signal)):
        if len(set(potential_packet)) == 4:
            print(i)
            break
        potential_packet.pop(0)
        potential_packet.append(signal[i])

if __name__ == '__main__':
    main()
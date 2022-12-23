import sys

def main():
    win = {'A':2,'B':3,'C':1}
    lose = {'A':3,'B':1,'C':2}
    tie = {'A':1,'B':2,'C':3}

    points_key = {'X':0,'Y':3,'Z':6}
    total_points = 0

    for line in sys.stdin:
        m, n = line.split()
        points = points_key[n]

        if n == 'X':
            points += lose[m]
        elif n == 'Y':
            points += tie[m]
        else:
            points += win[m]

        total_points += points

    print(total_points)
        
if __name__ == '__main__':
    main()
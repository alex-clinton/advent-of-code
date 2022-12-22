import sys

def main():
    winning = {('A','Y'),('B','Z'),('C','X')}
    losing = {('A','Z'),('B','X'),('C','Y')}

    points_key = {'X':1,'Y':2,'Z':3}
    total_points = 0

    for line in sys.stdin:
        pair = tuple(line.split())
        points = points_key[pair[1]]

        if pair in winning:
            points += 6
        elif pair in losing:
            points += 0
        else:
            points += 3

        total_points += points

    print(total_points)
        
if __name__ == '__main__':
    main()
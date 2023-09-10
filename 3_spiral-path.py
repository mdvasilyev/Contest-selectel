# '''
# The task is to calculate the number of distracted
# programmers in matrix like office. The path is spiral 
# '''

def main():
    n, m = map(int, input().split())                    # rectangle dimensions
    y, x = map(int, input().split())                    # final point
    counter = 1                                         # number of distracted people?
    i, j = 1, 1
    upborder = 1
    lowborder = n
    leftborder = 1
    rightborder = m
    while (i != x) or (j != y):                         # the spiral path itself
        if j == upborder and i != rightborder:
            counter += 1
            i += 1
        elif i == rightborder and j != lowborder:
            counter += 1
            j += 1
        elif j == lowborder and i != leftborder:
            counter += 1
            i -= 1
        elif i == leftborder and j != upborder:
            counter += 1
            j -= 1
        if i == leftborder and j == upborder + 1:       # change borders of rectangle
            upborder += 1
            lowborder -= 1
            leftborder += 1
            rightborder -= 1
    print(counter)
    return

if __name__ == "__main__":
    main() 
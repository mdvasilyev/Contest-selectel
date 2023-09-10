# '''
# The task is to print the sequence of disks being popped from the shelf
# '''

import sys

def main():
    n = int(input())
    reader = (map(int, line.split()) for line in sys.stdin)
    shelf = []
    popped = []
    for i in range(n):
        command = list(next(reader))
        oper = command[0]
        match oper:
            case 1:                             # insert disk to the left
                shelf.insert(0, command[1])
            case 2:                             # insert disk to the right
                shelf.append(command[1])
            case 3:                             # pop disk from the left
                popped.append(shelf.pop(0))
            case 4:                             # pop disk from the right
                popped.append(shelf.pop(-1))
    print(*popped)
    return

if __name__ == "__main__":
    main()
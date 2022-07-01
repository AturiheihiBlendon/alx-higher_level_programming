#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    add = 0
    for i in range(len(sys.argv) - 1):
        add += int(sys.argv[i])
        print('{:d}'.format(add))

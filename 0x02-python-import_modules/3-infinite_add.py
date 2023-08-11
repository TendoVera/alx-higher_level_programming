#!/usr/bin/python3
if __name__ == "__main__":
    import sys

sum = 0
for adding in range(len(sys.argv) - 1):
        sum += int(sys.argv[adding + 1])
        print("{:d}".format(sum))

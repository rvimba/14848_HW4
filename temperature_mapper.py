import sys

def quality_check(q):
    return ((q == 0) or (q == 1) or (q == 4) or (q == 5) or (q == 9))

for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    q = int(line[92])
    if (quality_check(q) and (temperature != 9999)):
        print('%s\t%d' % (line[15:23], int(line[87:92])))

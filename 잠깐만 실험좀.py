List_A = []
s_line = []

f = open("hihi.txt", 'r')
while True:
    line = f.readline()
    s_line.append(line)
    if '#' in line:
        List_A.append(s_line)
        s_line = []
    if not line: break
f.close()

print(List_A)
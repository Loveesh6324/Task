
s = input('enter 4 digit values with comma seprated')
s1 = s.split(',')
s2 = []
for i in s1:
    conv = int(i, 2)
    s2.append(int(conv))

a = []
for i in s2:
    if(i % 5 == 0):
        a.append(format(i, 'b'))

print(','.join(str(x) for x in a))
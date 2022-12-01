f = open('day01.txt', 'r')
txt = f.readlines()
data = []
counter = 0
suma = []
suma.append(0)
for line in txt:
    if line == '\n':
        counter +=1
        suma.append(0)
    else:
        data.append(int(line))
        suma[counter] += int(line)

print('part 1: %s' % max(suma)) 

suma.sort()
print('part 2: %s' % sum(suma[counter-2: counter+1])) 
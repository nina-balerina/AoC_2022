f = open('day01.txt', 'r')
txt = f.readlines()
counter = 0
suma = []
suma.append(0)
for line in txt:
    if line == '\n':
        counter +=1
        suma.append(0)
    else:
        suma[counter] += int(line)

print('part 1:', max(suma)) 

suma.sort()
print('part 2:', sum(suma[counter-2: counter+1])) 
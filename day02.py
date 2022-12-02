f = open('day02.txt')
data = f.readlines()

shape_score = {'X': 1, 'Y': 2, 'Z': 3}
won = ['AY', 'BZ', 'CX']
draw = ['AX', 'BY', 'CZ']

score = 0
for line in data:
    game = line.strip().replace(' ', '')
    if game in won:
        score += 6
    if game in draw:
        score += 3
    score += shape_score[game[1]] 
    
print('part 1:', score)



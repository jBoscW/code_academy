

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters += [' ']

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
points += [0]

# ltp = {i:j for i, j in zip(letters, points)}

#lower cases
lower_cases = [i.lower() for i in letters]
letters_final = letters + lower_cases
points = points + points

ltp = {i:j for i, j in zip(letters_final, points)}
print(ltp)



def score(word):
  total = 0
  for i in word: 
    # total += ltp.get(i)
    if i in ltp: total += ltp[i]
  return total

print(ltp)
print(score('BROWNIE'))
######
ptw = {'player1': ['BLUE', 'TENNIS', 'Exit'], 'wordNerd': ['EARTH', 'eyes', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

def count_points():
    ptp = {}
    for player, wordz in ptw.items(): 
        points = 0
        for i in wordz: 
            points += score(i)
        ptp[player] = points
    print(ptp)

def play_word(player, word): 
  if player in ptw:
    ptw[player].append(word)
  count_points()
  

play_word('player1', 'wowza')
play_word('wordNiga', 'wow')
play_word('wordNerd', 'hmm idk tho')
play_word('Lexi Con', 'nigger')







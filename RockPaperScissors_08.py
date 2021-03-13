r = 'r'; p = 'p'; s = 's'; q = 'q'
p1score=0;p2score=0

print('Welcome to endless rock, paper, scissors!')
print('Acceptable Commands:')
print('=====================')
print('rock')
print('paper')
print('scissors')
print('quit')
print('=====================')
    
while True:
    try:
        p1 = input('Player One, pick your character ---- ')
        p2 = input('Player Two, pick your character ---- ')
        p1 = str(p1); p2 = str(p2)
        p1 = p1[0].lower().strip(); p2 = p2[0].lower().strip()
        if p1 == r and p2 == s or p1 == p and p2 == r or p1 == s and p2 == p:
            p1score += 1
            print('Player One Wins!')
        elif p2 == r and p1 == s or p2 == p and p1 == r or p2 == s and p1 == p:
            p2score += 1
            print('Player Two Wins!')
        elif p1 == q or p2 == q:
            print('Thanks for playing!')
            print('==== Final Score =====')
            print('Player One:', p1score, '|| Player Two:', p2score)
            if p1score > p2score: print('Player One Wins The GAME!')
            elif p2score > p1score: print('Player Two Wins The GAME!')
            elif p1score == p2score: print("It's a Tie!")
            break
        else: 
            print('Redo!')
            continue
    except:
        print('Something Went wrong')
    
    print('==== Score =====')
    print('Player Two:', p1score, '|| Player Two', p2score)


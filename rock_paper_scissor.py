import random
moves = ['stone', 'paper', 'scissors']
print(f"choose your move among these using numbers {moves}")
def getComputerMove():
    randomMum = random.randint(0, 2)
    return moves[randomNum]

def getUserMove():
    userMove = int(input("enter your choice"))
    return moves[userMove]
    
while True:
    def decideWinner():
        user = userMove()
        computer = getComputerMove()
        
        if (user == computer):
            print("Tie!!")
        elif (user == 'stone' and computer == 'scessiors') or (user == 'paper' and computer == 'stone') or (user == 'scessiors' and computer == 'stone'):
                 print("you have won the game!!")
        else: print("sorry!!, you lost the game")
    decideWinner()
    

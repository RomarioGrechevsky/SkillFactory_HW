import random
moves_and_wins = {
    "камень" : "ножницы",
    "камень" : "ящерица",
    "ящерица" : "спок",
    "спок" : "ножницы",
    "ножницы" : "ящерица",
    "ящерица" : "бумага",
    "бумага" : "спок",
    "спок" : "камень",
    "ножницы" : "бумага",
    "бумага" : "камень",
}
moves = ["камень", "ножницы", "бумага", "ящерица", "спок"]
player_wins = 0
computer_wins = 0
while player_wins < 5 and computer_wins < 5 : 
    player_move = input ("камень, ножницы, бумага, ящерица или спок? ")
    if player_move not in moves :
        print("ошибка")
        quit()
    else:
        computer_move = random.choice(moves)
        print ("компьютер выбрал", computer_move)
        if moves_and_wins[player_move] == computer_move:
            print ("победа")
            player_wins += 1
        elif player_move == computer_move:
            print ("ничья")
        else :
            print ("проигрыш")
            computer_wins += 1
        print('Счет - игрок:', player_wins, 'компьютер:', computer_wins)
if player_wins > computer_wins :
    print ("Партия выиграна!")
else :
    print ("Попробуйте еще раз")

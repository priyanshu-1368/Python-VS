import random
life = 3
list = ["Rock", "Paper", "Scissor"]
print("Welcome to Rock, Paper, Scissor Game!")
print("Rock")
print("Paper")
print("Scissor")

while True:
    bot = list[int(random.random()*3)]
    user = input("Enter your choice: ")
    life -= 1

    if (user == bot):
        print("It's a tie!", user, "You have", life, "lives left.")
    elif (user == "Rock" and bot == "Scissor") or (user == "Paper" and bot == "Rock") or (user == "Scissor" and bot == "Paper"):
        print("You win!", user, "beats", bot, "You have", life, "lives left.")
    elif (user not in list):
        print("Invalid input. Please choose Rock, Paper, or Scissor, You have", life, "lives left..")
    elif life == 0:
            print("Game over! You have no lives left.")
            break
    else:
        print("You lose!", bot, "beats", user, "You have", life, "lives left.")
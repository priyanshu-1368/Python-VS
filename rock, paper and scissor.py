import random
lives = 3
choices = ["Rock", "Paper", "Scissor"]
print("Welcome to Rock, Paper, Scissor Game!")
print("Rock")
print("Paper")
print("Scissor")

while True:
    bot = choices[int(random.random()*3)]
    user = input("Enter your choice: ")

    if (user == bot):
        print("It's a tie!", user, "You have", lives, "lives left.")
    elif (user == "Rock" and bot == "Scissor") or (user == "Paper" and bot == "Rock") or (user == "Scissor" and bot == "Paper"):
        print("You win!", user, "beats", bot, "You have", lives, "lives left.")
    elif (user not in choices):
        print("Invalid input. Please choose Rock, Paper, or Scissor, You have", lives, "lives left...")
    elif lives == 0:
            print("Game over! You have no lives left.")
            break
    else:
        lives -= 1
        print("You lose!", bot, "beats", user, "You have", lives, "lives left.")
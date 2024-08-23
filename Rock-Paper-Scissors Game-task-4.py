import tkinter as tk
import random

#Create the main window 
root = tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("400x400")

# Define the labels first
user_choice_label = tk.Label(root, text="Your Choice: ", font=('Helvetica', 14))
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=('Helvetica', 14))
computer_choice_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=('Helvetica', 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text="User: 0  Computer: 0", font=('Helvetica', 14))
score_label.pack(pady=10)


#Here i am defining the game functions
#variables for score tracking
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "it's a tie!"
    elif(user_choice =='rock' and computer_choice == 'scissors') or \
        (user_choice =='paper' and computer_choice == 'rock') or \
        (user_choice =='scissors' and computer_choice == 'paper'):
        
        result = "You win!"
        user_score+=1
    else:
        result = "You lose!"
        computer_score += 1


    #update the labels with the results
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer' s Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"User: {user_score} Computer: {computer_score}")

def reset_game():
    global user_score,computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your Choice:")
    computer_choice_label.config(text="Computer's Choice:")
    result_label.config(text="Result: ")
    score_label.config(text="User: 0 Computer:0")

#here I am creating the GUI widgets
# Buttons for user to make a choice
rock_button = tk.Button(root, text="Rock", command=lambda: play('rock'), width=15, height=2)
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play('paper'), width=15, height=2)
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play('scissors'), width=15, height=2)
scissors_button.pack(pady=5)

# Reset Button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, width=15, height=2)
reset_button.pack(pady=20)

#Run the main loop 
root.mainloop()









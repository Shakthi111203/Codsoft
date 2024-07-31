import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f0f0") 

        self.user_score, self.computer_score = 0, 0

        tk.Label(self.root, text="Rock, Paper, Scissors", font=('Arial', 20, 'bold', 'underline'), bg="#f0f0f0").pack(pady=10)
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        for choice in ["Rock", "Paper", "Scissors"]:
            btn = tk.Button(button_frame, text=choice, font=('Arial', 14, ), command=lambda ch=choice: self.play(ch), bd=5, padx=10, pady=8, bg="#f0f0f0", fg="black")
            btn.pack(side=tk.LEFT, padx=10)
        
        self.user_choice_label = tk.Label(self.root, text="Your choice: ", font=('Arial', 14), bg="#f0f0f0")
        self.user_choice_label.pack()
        
        self.computer_choice_label = tk.Label(self.root, text="Computer's choice: ", font=('Arial', 14), bg="#f0f0f0")
        self.computer_choice_label.pack()
        
        self.result_label = tk.Label(self.root, text="", font=('Arial', 16, 'bold', 'underline'), bg="#f0f0f0")
        self.result_label.pack()
        
        self.score_label = tk.Label(self.root, text="Score: You 0 - Computer 0", font=('Arial', 14), bg="light blue")
        self.score_label.pack()

        tk.Button(self.root, text="Play Again", font=('Arial', 14), command=self.reset_game, bg="#4caf50", fg="white", bd=10, padx=20, pady=3).pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.user_choice_label.config(text=f"Your choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
        
        if user_choice == computer_choice:
            result = "It's a tie!"
            result_color = "blue"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            result = "You win!"
            result_color = "green"
            self.user_score += 1
        else:
            result = "You lose!"
            result_color = "Red"
            self.computer_score += 1
        
        self.result_label.config(text=result, fg= result_color)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")

    def reset_game(self):
        self.user_score = self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="Score: You 0 - Computer 0")

if __name__ == "__main__":
    root = tk.Tk()
    RockPaperScissors(root)
    root.mainloop()

import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")
        self.window.geometry("400x300")
        
        self.target_number = random.randint(0, 100)
        self.attempts_left = 10
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.window, text="Number Guessing Game", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(self.window, text="Guess a number between 0 and 100\nYou have 10 attempts!", font=("Arial", 10))
        instructions.pack(pady=5)
        
        # Attempts counter
        self.attempts_label = tk.Label(self.window, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12))
        self.attempts_label.pack(pady=5)
        
        # Input frame
        input_frame = tk.Frame(self.window)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Your guess:", font=("Arial", 10)).pack(side=tk.LEFT)
        self.guess_entry = tk.Entry(input_frame, font=("Arial", 10), width=10)
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind('<Return>', lambda event: self.make_guess())
        
        # Guess button
        self.guess_button = tk.Button(self.window, text="Guess!", command=self.make_guess, font=("Arial", 10))
        self.guess_button.pack(pady=5)
        
        # Feedback label
        self.feedback_label = tk.Label(self.window, text="", font=("Arial", 12), fg="blue")
        self.feedback_label.pack(pady=10)
        
        # New game button
        self.new_game_button = tk.Button(self.window, text="New Game", command=self.new_game, font=("Arial", 10))
        self.new_game_button.pack(pady=5)
        
    def make_guess(self):
        try:
            guess = int(self.guess_entry.get())
            
            if guess < 0 or guess > 100:
                self.feedback_label.config(text="Please enter a number between 0 and 100!", fg="red")
                return
                
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
            
            if guess == self.target_number:
                self.feedback_label.config(text=f"🎉 Congratulations! You guessed it right!\nThe number was {self.target_number}", fg="green")
                self.guess_button.config(state="disabled")
                self.guess_entry.config(state="disabled")
            elif guess < self.target_number:
                self.feedback_label.config(text="📈 Your guess is too small! Try a bigger number.", fg="orange")
            else:
                self.feedback_label.config(text="📉 Your guess is too big! Try a smaller number.", fg="orange")
            
            if self.attempts_left == 0 and guess != self.target_number:
                self.feedback_label.config(text=f"💀 Game Over! The number was {self.target_number}", fg="red")
                self.guess_button.config(state="disabled")
                self.guess_entry.config(state="disabled")
                
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")
            
    def new_game(self):
        self.target_number = random.randint(0, 100)
        self.attempts_left = 10
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state="normal")
        self.guess_entry.config(state="normal")
        
    def run(self):
        self.window.mainloop()

# Run the game
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()

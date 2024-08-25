import tkinter as tk
import random

class GuessNumberGame:
  def __init__(self, root, max_number):
    self.root = root
    # Fixed the window position and size
    # 400 is for width of window
    # 200 is for height of window
    # 100+100 is mean (100, 100) starts from the left and top corner
    self.min = 1
    self.max = max_number
    self.max_number = max_number
    self.secret_number = random.randint(self.min, self.max_number)
    self.attempts = 10

    self.setup_window("Guess The Number Game", "400x200+100+100")
    self.create_widgets()

  def setup_window(self, title, geometry):
    self.root.title(title)
    self.root.geometry(geometry)

  def create_widgets(self):
    # Label
    self.label = tk.Label(self.root, text = f"Guess a number between {self.min} and {self.max_number}")
    self.label.pack()

    # Input box
    self.entry = tk.Entry(self.root)
    self.entry.pack()

    self.result_label = tk.Label(self.root, text = "")
    self.result_label.pack()
    
    self.range_label = tk.Label(self.root, text = "")
    self.range_label.pack()
    
    self.attempt_label = tk.Label(self.root, text = "")
    self.attempt_label.pack()

    # Trigger key Enter to check_guess function
    self.entry.bind("<Return>", self.check_guess)
    # Button
    self.guess_button = tk.Button(self.root, text = "Submit Guess", command = self.check_guess)
    self.guess_button.pack()

    self.play_again_button = tk.Button(self.root, text = "Play Again", command = self.reset_game)
    self.play_again_button.pack()
    self.play_again_button.config(state = tk.DISABLED)

    self.quit_button = tk.Button(self.root, text = "Quit", command = self.root.quit)
    self.quit_button.pack()

  def check_guess(self, event = None):
    try:
      guess = int(self.entry.get())
    except ValueError:
      self.result_label.config(text = "Please enter a valid number!")
      return
    if guess > self.max or guess < self.min:
      self.result_label.config(text = "The number is out of range")
    elif guess < self.secret_number:
      self.min = guess
      self.result_label.config(text = "The number is smaller")
    elif guess > self.secret_number:
      self.max = guess
      self.result_label.config(text = "The number is bigger")
    else:
      self.result_label.config(text = f"Congrats! The number was {self.secret_number}.")
      self.end_game()
      return
    
    self.entry.delete(0, tk.END)
    self.range_label.config(text = f"The range is {self.min} - {self.max}")
    self.attempts -= 1
    self.attempt_label.config(text = f"You have {self.attempts} time(s) left.")
    if self.attempts == 0:
      self.result_label.config(text = f"Out of attempts! The number was {self.secret_number}.")
      self.end_game()

  def end_game(self):
    self.guess_button.config(state = tk.DISABLED)
    self.play_again_button.config(state = tk.NORMAL)

  def reset_game(self):
    # Close the current window and open a new SetLevel window
    self.root.destroy()
    set_level_window = tk.Tk()
    SetLevel(set_level_window)
    set_level_window.mainloop()
    # self.min = 1
    # self.max = self.max_number
    # self.attempts = 10
    # self.secret_number = random.randint(self.min, self.max_number)
    # self.result_label.config(text = f"")
    # self.range_label.config(text = f"")
    # self.attempt_label.config(text = f"")
    # self.entry.delete(0, tk.END)
    # self.guess_button.config(state = tk.NORMAL)
    # self.play_again_button.config(state = tk.DISABLED)
    # self.quit_button.config(state = tk.NORMAL)
    
class SetLevel:
  def __init__(self, root):
    self.root = root
    self.setup_window("Guess The Number Game", "400x200+100+100")
    self.create_widgets()

  def setup_window(self, title, geometry):
    self.root.title(title)
    self.root.geometry(geometry)

  def create_widgets(self):
    tk.Label(self.root, text = "Welcome to Guess The Number!").pack(pady = 5)
    tk.Label(self.root, text = "Choose the mode you want to play").pack(pady = 5)
    tk.Button(self.root, text = "Easy (1-50)", command = lambda: self.start_game(50)).pack(pady = 5)
    tk.Button(self.root, text = "Medium (1-100)", command = lambda: self.start_game(100)).pack(pady = 5)
    tk.Button(self.root, text = "Hard (1-200)", command = lambda: self.start_game(200)).pack(pady = 5)

  def start_game(self, max_number):
    # Close the current window
    self.root.destroy()
    # Open a new window
    game_window = tk.Tk()
    GuessNumberGame(game_window, max_number)
    game_window.mainloop()

if __name__ == "__main__":
  root = tk.Tk()
  SetLevel(root)
  root.mainloop()
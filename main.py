import datetime

date_time = datetime.datetime(2021, 9, 27,
hour=12, minute=36, second=24, microsecond=585)
print(f"object datetime – {date_time}")
print(f"type – {type(date_time)}")


import tkinter as tk
from tkinter import messagebox

# Initial game state variables
bomb = 100
score = 0
press_return = True

# Initialize the main window
root = tk.Tk()
root.title("Game")
root.geometry("600x600+500+400")
# Ensure bomb.ico and the GIF images are in the correct path or comment out the icon line
# root.iconbitmap("bomb.ico")

# Set up labels
label = tk.Label(root, text='Press [enter] to start the game', font=('Comic Sans MS', 12))
label.pack()
fuse_label = tk.Label(root, text=f'Fuse: {str(bomb)}', font=('Comic Sans MS', 14))
fuse_label.pack()
score_label = tk.Label(root, text=f'Score: {str(score)}', font=('Comic Sans MS', 14))
score_label.pack()

# Load images (make sure these image files are in the correct path)
# Comment these out if images are not available
img_1 = tk.PhotoImage(file="1.gif")
img_2 = tk.PhotoImage(file="2.gif")
img_3 = tk.PhotoImage(file="3.gif")
img_4 = tk.PhotoImage(file="4.gif")
bomb_label = tk.Label(image=img_1)
bomb_label.pack()

# Function definitions
def update_display():
    bomb_label.config(image=img_4 if bomb < 25 else img_3 if bomb < 50 else img_2 if bomb < 75 else img_1)

def is_alive():
    return bomb > 0

def update_bomb():
    global bomb
    bomb -= 10  # Decrease the bomb value
    fuse_label.config(text=f'Fuse: {str(bomb)}')  # Update the label

def update_score():
    global score
    score += 10  # Increase the score
    score_label.config(text=f'Score: {str(score)}')  # Update the label

def game_over():
    global press_return
    press_return = True  # Reset for a new game
    messagebox.showinfo("Game Over", "BOOM! The bomb exploded!")
    reset_game()

def reset_game():
    global bomb, score
    bomb = 100
    fuse_label.config(text=f'Fuse: {str(bomb)}')
    score = 0
    score_label.config(text=f'Score: {str(score)}')
    update_display()

def start(event):
    global press_return
    if press_return:
        press_return = False
        reset_game()
        label.config(text="Defuse the bomb by clicking the button!")
        update_display()

def click():
    global bomb, score
    if not press_return:
        update_bomb()
        update_score()
        if not is_alive():
            game_over()
        else:
            update_display()

# Button and event binding
click_button = tk.Button(root, text='Click me', bg='black', fg='white', width=15, font=('ComicSans MS', 14), command=click)
click_button.pack()
root.bind('<Return>', start)

# Run the main app loop
root.mainloop()

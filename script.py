import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Planet names (rows)
planets = ["Космос", "Спорт", "Биология", "Путешествия", "Технологии", "Кино", "Компьютерные игры"]

# Points on buttons
numbers = ['10','20','30','40','50','60']

score = 0


def generate_question(level):
    if level <= 2:  # Easy (+, -)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-"])
    elif level <= 5:  # Multiply
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        op = "*"
    else:  # Divide
        b = random.randint(2, 12)
        a = b * random.randint(2, 12)
        op = "/"

    question = f"{a} {op} {b}"
    answer = eval(question)

    return question, answer


def on_click(row, col, button):
    global score

    question, answer = generate_question(row)
    user = simpledialog.askfloat("Question", f"{question} = ?")

    if user is None:
        return

    if round(user, 2) == round(answer, 2):
        score += 1
        score_label.config(text=f"Score: {score}")
    else:
        messagebox.showinfo("Wrong", f"Correct answer was {answer}")

    # Lock the button so it can't be opened again
    button.config(state="disabled")


# Create main window
root = tk.Tk()
root.title("Planet Maths Grid")

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=7)

# Create grid
for r in range(len(planets)):
    tk.Label(root, text=planets[r], width=20, font=('Arial', 16)).grid(row=r + 1, column=0)

    for c in range(6):
        btn = tk.Button(root, width=8, height=2, text=numbers[c], font=('Arial', 16))
        btn.grid(row=r + 1, column=c + 1)

        btn.config(command=lambda r=r, c=c, b=btn: on_click(r, c, b))

root.mainloop()

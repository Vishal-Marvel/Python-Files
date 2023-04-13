from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("280x360")
root.resizable(height=False, width=False)

count = 0
ai_move=False
winner=False

def ai():
    while True:
        ch = random.choice(buts)
        if ch["text"] == " ":
            b_click(ch)
            break

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()


    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS! X Wins!!")
        disable_all_buttons()

# O wins!!

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "OOPS! O Wins!!")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Its a Tie!\nNo one wins!")
        disable_all_buttons()

def b_click(b):
    global clicked, count, ai_move
    if b["text"] == " " and not ai_move:
        b["text"] = "X"
        count += 1
        checkifwon()
        ai_move=True
        if not winner:ai()
        
    elif b["text"] == " "  and ai_move:
        b["text"] = "O"
        count += 1
        checkifwon()
        ai_move=False
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick another one")


def reset():
    global buts, b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count
    count = 0
    global ai_move, winner
    ai_move=False
    winner=False

    b1 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(frame, text=" ", font=20, height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    buts = [b1, b2, b3, b4, b5, b6 ,b7, b8, b9]


label = Label(root, text="AI - TIC TAC TOE!!", font=20)
label.pack(pady=10)
frame = Frame(root, bg="#85c1ff", bd=7)
frame.pack(fill=BOTH, padx=20, pady=5)

my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()
from tkinter import *
import random

root = Tk()
bg = "green"
fg = "yellow"
acbg = "red"
btnbg = "sky blue"
root.config(background=bg)
score_me = 0
score_comp = 0

win_frame = Frame(root, bg="yellow")

def check(b):
	global btnbg, acbg, score_me, score_comp
	rock2['bg'] = btnbg	
	paper2["bg"] = btnbg	
	scissors2["bg"] = btnbg
	
	num = random.randint(1, 4)
	if num == 1:
		rock2["bg"] = acbg
	if num == 2:
		paper2["bg"] = acbg
	if num == 3:
		scissors2["bg"] = acbg
	
	if b["text"] == "\nRock\n":
		if num == 1:
			score_me += 1
			score_comp += 1
			me['text'] = f"""Me
Score: {score_me}"""
			comp["text"] = f"""Computer
Score: {score_comp}"""

		if num == 3:
			score_me += 1
			me['text'] = f"""Me
Score: {score_me}"""

		if num == 2:
			score_comp += 1
			comp["text"] = f"""Computer
Score: {score_comp}"""	

	if b["text"] == "\nPaper\n":
		if num == 2:
			score_me += 1
			score_comp += 1
			me['text'] = f"""Me
Score: {score_me}"""
			comp["text"] = f"""Computer
Score: {score_comp}"""

		if num == 1:
			score_me += 1
			me['text'] = f"""Me
Score: {score_me}"""

		if num == 3:
			score_comp += 1
			comp["text"] = f"""Computer
Score: {score_comp}"""

	if b["text"] == "\nScissors\n":
		if num == 3:
			score_me += 1
			score_comp += 1
			me['text'] = f"""Me
Score: {score_me}"""
			comp["text"] = f"""Computer
Score: {score_comp}"""

		if num == 2:
			score_me += 1
			me['text'] = f"""Me
Score: {score_me}"""

		if num == 1:
			score_comp += 1
			comp["text"] = f"""Computer
Score: {score_comp}"""

	if score_me == 10 or score_comp == 10:
		win_screen()
		
def win_screen():
	global score_me, score_comp
	left_frame.destroy()
	right_frame.destroy()
	
	win_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
	
	if score_me > score_comp:
		win_text = f"""Congratulations!
You Won!!
Your Score: {score_me}
Computer's Score: {score_comp}"""
	
	if score_me < score_comp:
		win_text = f"""You Lost!
Better Luck Next Time ;)
Your Score: {score_me}
Computer's Score: {score_comp}"""

	if score_me == score_comp:
		win_text = f"""It's A Tie!!
Your Score: {score_me}
Computer's Score: {score_comp}"""
		
	win_label = Label(win_frame, text=win_text, bg="yellow", fg="red", font=("Comic Sans MS", 14))
	win_label.pack()
	
top_frame = Frame(root, bg = bg)
top_frame.pack()

left_frame = Frame(root, bg=bg)
left_frame.pack(side=LEFT)

empty_space = Label(left_frame, text="""

""", bg=bg)
empty_space1 = Label(left_frame, text="""

""", bg=bg)
empty_space2 = Label(left_frame, text="""

""", bg=bg)
empty_space3 = Label(left_frame, text="""

""", bg=bg)

heading = Label(top_frame, text="""
Rock, Paper, Scissors""", bg=bg, fg=fg, font=("Comic Sans MS", 16, "underline"))
heading.pack()

me = Label(left_frame, text=f"""Me
Score: {score_me}""", bg=bg, fg=fg, font=("Comic Sans MS", 16))
me.grid(row=0, column=0)

empty_space.grid(row=2, column=0)

rock1 = Button(left_frame, text="""
Rock
""", padx=100, pady=30, activebackground=acbg, bg=btnbg)
rock1["command"] = lambda b=rock1: check(b)
rock1.grid(row=3, column=0)

empty_space1.grid(row=4, column=0)

paper1 = Button(left_frame, text="""
Paper
""", padx=90, pady=30, activebackground=acbg, bg=btnbg)
paper1["command"] = lambda b=paper1: check(b)
paper1.grid(row=5, column=0)

empty_space2.grid(row=6, column=0)

scissors1 = Button(left_frame, text="""
Scissors
""", padx=75, pady=30, activebackground=acbg, bg=btnbg)
scissors1["command"] = lambda b=scissors1: check(b)
scissors1.grid(row=7, column=0)



right_frame = Frame(root, bg=bg)
right_frame.pack(side=RIGHT)

empty_space4 = Label(right_frame, text="""

""", bg=bg)
empty_space5 = Label(right_frame, text="""

""", bg=bg)
empty_space6 = Label(right_frame, text="""

""", bg=bg)
empty_space7 = Label(right_frame, text="""

""", bg=bg)

comp = Label(right_frame, text=f"""Computer
Score: {score_comp}""", bg=bg, fg=fg, font=("Comic Sans MS", 16))
comp.grid(row=0, column=0)

empty_space4.grid(row=1, column=0)

rock2 = Button(right_frame, text="""
Rock
""", padx=100, pady=30, activebackground=acbg, bg=btnbg, state=DISABLED)
rock2.grid(row=2, column=0)

empty_space5.grid(row=3, column=0)

paper2 = Button(right_frame, text="""
Paper 
""", padx=90, pady=30, activebackground=acbg, bg=btnbg, state=DISABLED)
paper2.grid(row=4, column=0)

empty_space6.grid(row=5, column=0)

scissors2 = Button(right_frame, text="""
Scissors
""", padx=75, pady=30, activebackground=acbg, bg=btnbg, state=DISABLED)
scissors2.grid(row=6, column=0)

root.mainloop()

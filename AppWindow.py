import tkinter as tk
from tkinter import ttk
import random

# root is instance of tk
# frame is window
# grid controls where placed
# label, button fall are children of frame, frame is parameter
# interface updates through loops

# setup
root = tk.Tk()
root.title("prepper")
#homescreen setup
home = ttk.Frame(root, padding=200)
home.grid()
#discipline/prep setup
prep = ttk.Frame(root, padding=200)
prep.grid()

#helper clear function
def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()

    # prep question screen
    # takes question object
def basic(*args):
    # clean window
    clear_frame(prep)
    # q_type = question.type() #string
    # q_string = question.question() #string
    q_string = "question?"
    q_type = "open ended"
    answer_bank = ["wrong", "wrong2", "wrong3"]
    root.update()
    
    
    # show/establish window updated
    prep.grid()
    # get question to show
    # present input box or multiple choice
    answer = ""
    if (q_type == "open ended"):
        print("open")
        ttk.Entry(prep, width=100, textvariable=answer).grid(column=1,row=2)
    
    else:
        print("multiple")
        answers = []
        answers.add("correct")  # placeholder for question
        for x in range(3):
            random.randrange(answer_bank.size())
    ttk.Label(prep, text=q_string).grid(column=1,row=1)
    ttk.Button(prep, text="Finished").grid(column=1, row=3)        
    # if quit button pressed
    
    # if next question pressed
        
        
# update prep selection page
def to_prep(*args):
    root.update()
    home.grid_remove()
    
    discipline_title = ttk.Label(prep, text="Which discipline?").grid(column=1, row=1)
    ttk.Button(prep, text="basic", command=basic).grid(column=1, row=2)
    root.mainloop()
    

# main page
title = ttk.Label(home, text="Interview Prepper").grid(column=1, row=1)
begin = ttk.Button(home, text="Begin Prep", command=to_prep).grid(column=1, row=2)

root.mainloop()

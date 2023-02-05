import tkinter as tk
from tkinter import ttk
import random
from Violet23.questionO import question
import Violet23.scanner as scanner

# root is instance of tk
# frame is window
# grid controls where placed
# label, button fall are children of frame, frame is parameter
# interface updates through loops

# setup
root = tk.Tk()
root.title("prepper")
root.update()
list = scanner.getList(list)
# frame setup
frame = ttk.Frame(root, padding=200)
frame.grid()
# value storing
answer = tk.StringVar()
num_completed = 0


# helper clear function
def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


# takes question object
def intermediate():
    # clear window
    clear_frame(frame)
    
    # setup
    global num_completed
    num_completed = num_completed + 1
    q_answer = question.getAnswer()
    
    #labels
    ttk.Label(frame, text="your answer: " + str(answer.get())).grid(column=1, row=2)
    ttk.Label(frame, text=q_answer).grid(column=1, row=1)
    ttk.Label(frame, text="")
    #buttons
    ttk.Button(frame, text="Next", command=basic).grid(column=1, row=3)
    ttk.Button(frame, text="quit", command=quit_practice).grid(column=1, row=4)

    
# quit practice window
def quit_practice():
    # clear window
    clear_frame(frame)
    # labels
    ttk.Label(frame, text="You completed: " + str(num_completed)).grid(column=1, row=1)
    # buttons
    ttk.Button(frame, text="quit to main menu", command=main_title).grid(column=1, row=2)


    # prep question screen
    # takes question object
def basic():
    # clean window
    clear_frame(frame)
    
    i = random.randrange(list.__len__())
    global question
    question = list[i]
    q_type = question.getQType() #string
    q_string = question.getQuestion() #string
    
    

    root.update()
    
    # show/establish window updated
    frame.grid()
    
    # check which type
    if (q_type == 2): #free response
        answer_box = ttk.Entry(frame, width=50, textvariable=answer)
        answer_box.delete(0, 999)
        answer_box.grid(column=2, row=2)
    elif (q_type == 1): #multiple choice
        print("multiple")
        answers = []
        answers.add("correct")  # placeholder for question
        for x in range(3):
            random.randrange(answer_bank.size())
            
    ttk.Label(frame, text=q_string).grid(column=2, row=1)#print question
    ttk.Button(frame, text="Finished", command=intermediate).grid(column=2, row=3)        
    ttk.Button(frame, text="quit", command=quit_practice).grid(column=1, row=1)
    
        
# update prep selection page
def to_prep():
    clear_frame(frame)
    ttk.Label(frame, text="Which discipline?").grid(column=1, row=1)
    ttk.Button(frame, text="basic", command=basic).grid(column=1, row=2)
    root.mainloop()
    

# main page
def main_title():
    clear_frame(frame)
    frame.grid()
    global num_completed
    num_completed = 0
    label = ttk.Label(frame, text="Interview Prepper")
    label.grid(column=1, row=1)
    ttk.Button(frame, text="Begin Prep", command=to_prep).grid(column=1, row=2)
    

main_title()
root.mainloop()

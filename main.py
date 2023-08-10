#importing modules
from tkinter import *
from random import randint

#every program must have this root
root  = Tk() 
root.title("Guess The Number")
root.geometry("700x450")
root.configure(bg="#1e1e1e")

#generating the number
num = randint(0,100)


#functions
def onSubmit():

    if num == int(init_guess.get()):
        success_prompt = Label(root, text="You Won!")
        success_prompt.pack()
    elif num < int(init_guess.get()):
        small_prompt = Label(root, text="The Number is smaller!")
        small_prompt.pack()
    elif num> int(init_guess.get()):
        large_prompt = Label(root, text="The Number is bigger!")
        large_prompt.pack()
    else:
        warning = Label("Error!")
        warning.pack()


#creating the display
init_prompt = Label(root, text="Enter a number", bg="#1e1e1e", fg="#fff")
init_guess = Entry(root)
submit = Button(root, text="Submit", command=onSubmit)

#packing everything in the window
init_prompt.pack()
init_guess.pack()
submit.pack()

#showing in using the mainloop method
root.mainloop()

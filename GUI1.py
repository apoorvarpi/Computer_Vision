from tkinter import *
from new_window import *
from combination_save import *

r1 = []
r2 = []

def caliberate(limit):
    for i in range(1,limit):
        str1 = "C"+str(r1[0])
        str2 = "C"+str(r2[0])
        transform(str1,str2)

def ok():
    x = var.get()
    new_win(x)
    #Saving relations
    print(" Enter relations example 1-2: ")
    for i in range(1,x):
        y = str(i)
        string = "Enter relation "+y+": "
        t = input(string)
        members = t.split('-')
        a = members[0]
        b = members[1]
        r1.append(int(a))
        r2.append(int(b))
    app.quit()
    #Actual Calliberation function call
    caliberate(x)

if __name__ == '__main__':
    app = Tk()
    app.title("Camera Calliberation")
    app.geometry("500x500")
    app.resizable(0, 0)
    var1 = StringVar(app)
    var1.set("Select the number of cameras")
    label = Label( app, textvariable=var1, relief=FLAT )
    label.pack(side=LEFT)
    var = IntVar(app)
    var.set(1)
    option = OptionMenu(app, var, 2,3,4,5,6)
    option.pack(side=LEFT)
    button = Button(app, text="OK", command=ok)
    button.pack(side=LEFT)
    mainloop()

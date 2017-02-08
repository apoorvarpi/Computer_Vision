from tkinter import *
from new_window import *

def display(x):
    y = str(x)
    im_name = "input/C"+y+""

def ok():
    x = var.get()
    print( "value is ", x)
    new_win(x)
    #for i in range(0,x):
    #    display(i)
    app.quit()

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

    option = OptionMenu(app, var, 1,2,3,4,5,6)
    option.pack(side=LEFT)

    button = Button(app, text="OK", command=ok)
    button.pack(side=LEFT)

    mainloop()

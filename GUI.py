from tkinter import *
from new_window import *
app = Tk()

app.title('Outer GUI')
app.geometry("500x500")
app.resizable(0, 0)

var1= StringVar(app)
var1.set("Select the number of cameras")

label = Label( app, textvariable=var1, relief=FLAT )
label.pack(side=LEFT)

var = IntVar(app)
var.set(1)

option = OptionMenu(app, var, 1, 2,3,4,5,6)
option.pack(side=LEFT)



# test stuff

def ok():
    print ("value is", var.get())
    new_win(var.get())
    app.quit()

button = Button(app, text="OK", command=ok)
button.pack(side=LEFT)

mainloop()

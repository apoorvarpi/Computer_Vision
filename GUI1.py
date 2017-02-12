from tkinter import *
from new_window import *
from combination_save import *
from path_finding import *
import numpy as np

r1 = []
r2 = []

def caliberate(limit):
    for i in range(0,limit-1):
        str1 = "C"+str(r1[i])
        str2 = "C"+str(r2[i])
        transform(str1,"calib.jpg",str2,"calib.jpg")
        cv2.waitKey(0)

def ok():
    app.quit()
    x = var.get()
    new_win(x)
    #Saving relations
    w, h = x, x;
    mat = [[0 for x in range(w)] for y in range(h)]
    print(" Enter relations example 1-2: ")
    for i in range(1,x):
        y = str(i)
        string = "Enter relation "+y+": "
        t = input(string)
        members = t.split('-')
        a = members[0]
        b = members[1]
        mat[int(a)-1][int(b)-1] = 1
        mat[int(b)-1][int(a)-1] = 1
        r1.append(int(a))
        r2.append(int(b))
    #Actual Calliberation function call
    file_name = "./Matrices/adjacency_matrix"
    np.save(file_name,mat)
    caliberate(x)
    final_matrices(x)

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

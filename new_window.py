from Tkinter import *
from PIL import Image, ImageTk

def new_win(var):
    for i in range(0,var):
     top=Toplevel()
     top.title("camera "+X)
     top.geometry("800x800")
     top.resizable(0, 0)
 
     imagee = Image.open("birds")
     photo = ImageTk.PhotoImage(imagee)
     frm1=Frame(top,width=532,height=800)
     frm1.pack(fill=None, expand=False)
     lb=Label(frm1, image=photo,width=532,height=800)
     lb.image = photo
     lb.pack(expand=False)
     top.mainloop()
     




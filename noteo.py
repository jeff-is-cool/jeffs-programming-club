from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showerror

filename = None

def newFile():
    global filename
    filename = "New Text"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w') 
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="unable to save file ):")

def openFile():
    f = askopenfile(mode='r')
    t=f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)



root = Tk()
root.title("Noteo")

root.geometry("400x400")
root.maxsize(2000, 2000)
root.minsize(400, 400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="new", command=newFile)
filemenu.add_command(label="open", command=openFile)
filemenu.add_command(label="save", command=saveFile)
filemenu.add_command(label="save as ...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="quit", command=root.quit)
menubar.add_cascade(label="file", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
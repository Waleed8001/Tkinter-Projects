from tkinter import*
import tkinter.messagebox as tmsg
from customtkinter import* 

root = Tk()
root.geometry("310x360")
root.minsize(320, 360)
root.maxsize(320, 360)
root.config(bg="gray16")
root.title("Calculator by Waleed")
root.iconbitmap("cal-ico.ico")

labelstr = StringVar()
labelstr.set("0")
# entryvalue = Entry(root, textvariable=labelstr, font=("Times New Roman", 28))
entryvalue = CTkEntry(root, textvariable=labelstr, font=("Times New Roman", 35), width=280, height=60, fg_color="DarkOliveGreen3", corner_radius=10, text_color="Black", border_width=0)
entryvalue.pack(pady=(20, 7))


def b1click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
        
    myevent = b1.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()
    
def b2click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    
    myevent = b2.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b3click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    
    myevent = b3.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b4click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b4.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b5click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b5.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b6click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b6.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b7click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b7.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b8click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b8.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def b9click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b9.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()
    
def b0click():
    if labelstr.get() == "0":
        labelstr.set("")
        entryvalue.update()
    
    root.focus()
    myevent = b0.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def clear():    
    root.focus()
    labelstr.set("")
    entryvalue.update()

def addnum():
    root.focus()
    myevent = add.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()


def subtractnum():
    root.focus()
    myevent = subtract.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def mulnum():    
    root.focus()
    myevent = mul.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()
    

def divnum():    
    root.focus()
    myevent = div.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()
    
def equalnum():
    if len(labelstr.get()) == 0:
            labelstr.set("")
            entryvalue.update()
            
    try:            
        if (labelstr.get()).isdigit():
            value = int(labelstr.get())
        
        else:
            value = eval(labelstr.get())
            
            # print(len(str(value)))
            if "." in str(value):
                if len(str(value)) > 9:
                    value = round(value, 9)
                
                else:
                    value = value
                    
            
        
    except Exception as e:
        value = "Error"
        
    labelstr.set(value)
    entryvalue.update()

def dotnum():
    root.focus()
    myevent = dot.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()

def remnum():
    root.focus()
    myevent = reminder.cget("text")
    labelstr.set(labelstr.get() + myevent)
    entryvalue.update()
    
def backbtn():
    root.focus()
    if len(labelstr.get()) != 0:
        value = labelstr.get()
        
        labelstr.set(value[0:len(value)-1])
        entryvalue.update()

f1 = Frame(root, bg="gray16")
f1.pack(pady=(20, 0), padx=(20, 0), anchor="nw")

b1 = CTkButton(f1, text="1", command=b1click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b1.pack(side=LEFT, padx=(0, 10))
b2 = CTkButton(f1, text="2", command=b2click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b2.pack(side=LEFT, padx=(0, 10))
b3 = CTkButton(f1, text="3", command=b3click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b3.pack(side=LEFT, padx=(0, 10))
clear_button = CTkButton(f1, text="C", command=clear, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
clear_button.pack(side=LEFT, padx=(0, 10))
back = CTkButton(f1, text="⬅️", command=backbtn, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
back.pack(side=LEFT, padx=(0, 0))

f2 = Frame(root, bg="gray16")
f2.pack(pady=(20, 0), padx=(20, 0), anchor="nw")

b4 = CTkButton(f2, text="4", command=b4click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b4.pack(side=LEFT, padx=(0, 10))
b5 = CTkButton(f2, text="5", command=b5click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b5.pack(side=LEFT, padx=(0, 10))
b6 = CTkButton(f2, text="6", command=b6click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b6.pack(side=LEFT, padx=(0, 10))
add = CTkButton(f2, text="+", command=addnum, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
add.pack(side=LEFT, padx=(0, 10))
subtract = CTkButton(f2, text="-", command=subtractnum, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
subtract.pack(side=LEFT, padx=(0, 10))

f3 = Frame(root, bg="gray16")
f3.pack(pady=(20, 0), padx=(20, 0), anchor="nw")

b7 = CTkButton(f3, text="7", command=b7click, width=50, font=("Times New Roman", 30), fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b7.pack(side=LEFT, padx=(0, 10))
b8 = CTkButton(f3, text="8", command=b8click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b8.pack(side=LEFT, padx=(0, 10))
b9 = CTkButton(f3, text="9", command=b9click, width=50, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b9.pack(side=LEFT, padx=(0, 10))
mul = CTkButton(f3, text="*", command=mulnum, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
mul.pack(side=LEFT, padx=(0, 10))
div = CTkButton(f3, text="/", command=divnum, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
div.pack(side=LEFT, padx=(0, 0))

f4 = Frame(root, bg="gray16")
f4.pack(pady=(20, 0), padx=(20, 0), anchor="nw")

equal = CTkButton(f4, text="=", command=equalnum, width=110, font=("Times New Roman", 30), fg_color="orange red", text_color="White", border_width=0, corner_radius=1)
equal.pack(side=LEFT, padx=(0, 10))
b0 = CTkButton(f4, text="0", command=b0click, width=50, font=("Times New Roman", 30), fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
b0.pack(side=LEFT, padx=(0, 10))
dot = CTkButton(f4, text=".", command=dotnum, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
dot.pack(side=LEFT, padx=(0, 10))
reminder = CTkButton(f4, text="%", command=remnum, width=45, font=("Times New Roman", 30),  fg_color="gray40", text_color="White", border_width=0, corner_radius=1)
reminder.pack(side=LEFT, padx=(0, 0))


root.mainloop()



# b.bind("<Button-1>", click)

# f1 = Frame(root, bg=)










# root = Tk()
# root.geometry("400x350")
# root.title("Calculator by Waleed")

# def add():
#     mylabel.config(text=num1.get()+num2.get())
    
# num1 = IntVar()
# num2 = IntVar()

# num1_value = Entry(root, textvariable=num1, font=("Times New Roman ", 31)).pack()
# num2_value = Entry(root, textvariable=num2, font=("Times New Roman ", 31)).pack(pady=(0, 15))

# Button(root, text="add", command=add, font=("Times New Roman ", 15)).pack(pady=(0, 15))
# mylabel = Label(root, text=0, font=("Times New Roman ", 15))
# mylabel.pack()

# root.mainloop()

# class MyCalculator(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x350")
#         self.title("Calculator by Waleed")
        
#         self.num1 = StringVar()
#         self.num1.set("0")
#         self.num2 = StringVar()
#         self.num2.set("0")
    
#         self.enter_value_1 = Entry(self, textvariable=self.num1)
#         self.enter_value_1.pack()
        
#         enter_value_2 = Entry(self, textvariable=self.num2)
#         enter_value_2.pack()
#         print(self.num1.get())
        
#         self.add = int(self.num1.get()) + int(self.num2.get())
        
#         Button(text="=", command=self.calculate).pack()
    
#     def calculate(self):
#         print(self.add)
#         Label(text=self.add).pack()
        
        
# if __name__ == "__main__":
#     cal = MyCalculator()
#     cal.mainloop()
    
from tkinter import*

root = Tk()
root.geometry("500x400")

strip_label = Label(root, text="ready", font=("Times New Roman", 10), relief=SUNKEN, bg="red", fg="white")
strip_label.pack(side=BOTTOM, anchor=CENTER, fill=X)

root.mainloop()
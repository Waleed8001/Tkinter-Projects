from tkinter import*

root = Tk()
root.geometry("700x400")

frame_1 = Frame(root, borderwidth=0)

news_str = ""
with open(r"D:\Tkinter Projects\Program-4\News\News1.txt", "r") as f:
    print(f.read())
    
    file_label = Label(frame_1, text=f.read(), font=("Times New Roman", 10), bg="white")
    file_label.pack(side=LEFT, anchor="e")

frame_1.pack()

root.mainloop()
from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.geometry("733x434")
root.minsize(733, 434)
root.maxsize(733, 434)
root.resizable(False,False)

root.configure(bg="white")

# GIve space on title for taking him center
root.title(70 * " " + "Welcome to Pycharm - Community Edition")

image = Image.open(r"D:\Tkinter Projects\Programs\pycharm_pic.png").resize((90, 90), resample=3)

image_open = ImageTk.PhotoImage(image=image)

image_label = Label(root, image=image_open, borderwidth=0)
image_label.pack(pady=10)

pycharm_label = Label(root, text="PyCharm", background="white", font=("Candara Light", 35))
pycharm_label.pack()

pycharm_label = Label(root, text="Version 2018.3.3", background="white", font="Arial 13")
pycharm_label.pack()

new_frame = Frame(root, background="white")


Create_new_project = Label(new_frame, text="☀️ Create new project", background="white", font="Arial 12")
Create_new_project.pack(padx=(0, 50), pady=(20, 0), anchor="w")

open_label = Label(new_frame, text="📂      Open", background="white", font="Arial 12",)
open_label.pack(padx=0, pady=(0, 0), anchor="w")

Version_Control = Label(new_frame, text="🔽      Check out from Version Control", background="white", font="Arial 12")
Version_Control.pack(padx=0,  pady=(0, 0), anchor="w")

new_frame.pack()

bottom_frame = Frame(root, bg="White")

configure_label = Label(bottom_frame, text="⚙️ Configure", background="white", font="Arial 11",)
configure_label.pack(side=LEFT, padx=0, pady=(0, 0))

help_label = Label(bottom_frame, text="Get Help", background="white", font="Arial 11")
help_label.pack(side=LEFT, padx=(10,0),  pady=(0, 0))

bottom_frame.pack(side="bottom", anchor="se")



root.mainloop()


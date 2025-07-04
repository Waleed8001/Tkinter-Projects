import os
from tkinter import*
from PIL import Image, ImageTk
import time 

root = Tk()
root.geometry("800x500")

labeling = ["posting", "S1", "S2", "S3", "cisco packet tracer", "Sea Pic"]
i = 0
folder_pic = r"D:\Tkinter Projects\Program-2"
j = 0

for images in os.listdir(folder_pic):
    if images.endswith(".png") or images.endswith(".jpg"):
        pic_label = Label(root, text = labeling[i])
        pic_label.grid(row=0, column=j)
        i = i + 1
        
        all_image = Image.open(folder_pic + "\\" + images).resize((150, 150), resample=3)
        
        photo = ImageTk.PhotoImage(all_image)
        photo_label = Label(root, image=photo)
        photo_label.image = photo
        photo_label.grid(row=1, column=j, padx=10)
        
        j = j + 1
# for images in os.listdir(folder_pic):
#     if images.endswith(".png") or images.endswith(".jpg"):
#         pic_label = Label(root, text = labeling[i])
#         pic_label.pack()
#         i = i + 1
        
#         all_image = Image.open(folder_pic + "\\" + images).resize((150, 150), resample=3)
        
#         photo = ImageTk.PhotoImage(all_image)
#         photo_label = Label(root, image=photo)
#         photo_label.image = photo
#         photo_label.pack()
        # print(images)
        
print(4)

root.mainloop()
    
# all_image = Image.open(folder_pic + "\\" + os.listdir(folder_pic)[1]).resize((150, 150), resample=3)
        
# photo = ImageTk.PhotoImage(all_image)
# photo_label = Label(image=photo)
# photo_label.pack()
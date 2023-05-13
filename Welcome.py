import tkinter  as tk
import os
from PIL import ImageTk, Image


class welcome:
    def __init__(self, master,next_frame):
        self.master = master
        master.pack()
        self.next_frame = next_frame
        self.canvas = tk.Canvas(master, bg="black", width=1000, height=800)
        self.welcomeFile = "robocub2-resize.jpg"
        self.menu_button_file = "menu_button.png"
        self.folder = "Assets"

        self.cwd = os.getcwd()

        self.path_to_welcome_file = os.path.join(self.cwd,self.folder,self.welcomeFile)
        self.path_to_menu_button_file = os.path.join(self.cwd,self.folder,self.menu_button_file)

        self.welcomeIm = Image.open(self.path_to_welcome_file).resize((1000,800),Image.LANCZOS)
        self.welcomeImObject = ImageTk.PhotoImage(self.welcomeIm)

        self.menu_buttonIM = Image.open(self.path_to_menu_button_file).resize((200,75),Image.LANCZOS)
        self.menu_buttonIMobject = ImageTk.PhotoImage(self.menu_buttonIM)


        self.welcomebg=self.canvas.create_image(0, 0, image=self.welcomeImObject, anchor="nw")
        self.menu_buttonbg = self.canvas.create_image(400, 500, image=self.menu_buttonIMobject, anchor="nw")
        self.canvas.tag_bind(self.menu_buttonbg,"<Button-1>",self.go_to_menu)
        self.canvas.pack()

    def go_to_menu(self,event):
        self.master.pack_forget()
        self.next_frame.pack(fill="both",expand=True)





















'''    canvas = tk.Canvas(Frame_welcome, bg="black", width=1000, height=800)


    welcomeFile = "robocub2-resize.jpg"
    menu_button_file = "menu_button.png"
   

    path_to_welcome_file = os.path.join(cwd,folder,welcomeFile)
    path_to_menu_button_file = os.path.join(cwd,folder,menu_button_file)

    welcomeIm = Image.open(path_to_welcome_file)
    welcomeIm = welcomeIm.resize((1000,800),Image.LANCZOS)
    welcomeImObject = ImageTk.PhotoImage(welcomeIm)

    menu_buttonIM = Image.open(path_to_menu_button_file)
    menu_buttonIM = menu_buttonIM.resize((200,75),Image.LANCZOS)
    menu_buttonIMobject = ImageTk.PhotoImage(menu_buttonIM)


    welcomebg=canvas.create_image(0, 0, image=welcomeImObject, anchor="nw")
    menu_buttonbg = canvas.create_image(400, 500, image=menu_buttonIMobject, anchor="nw")
    canvas.tag_bind(menu_buttonbg,"<Button-1>", go_to_menu)
    canvas.pack()'''
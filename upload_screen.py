import tkinter as tk
import tkinter.ttk as tkk
import os
from PIL import ImageTk, Image
import shutil
from tkinter.filedialog import askdirectory
import time

class UploadScreen:
    def __init__(self, master, main_screen):
        self.master = master
        self.main_screen = main_screen
        master.grid()
        master.protocol("WM_DELETE_WINDOW", self.close_screen)
        master.withdraw()

        self.welcomeFile = "welcome screen_resized.jpg"
        self.folder = "Assets"

        self.cwd = os.getcwd()

        self.path_to_welcome_file = os.path.join(self.cwd, self.folder, self.welcomeFile)

        self.image = ImageTk.PhotoImage(Image.open(self.path_to_welcome_file).resize((1200, 800), Image.LANCZOS))

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.label = tk.Label(master, image=self.image)
        self.label.grid(row=0, rowspan=10, column=0, columnspan=10)

        self.text_label = tk.Label(master, text="How to upload more games", font=("Arial", 30), fg="white", bg="Teal")
        self.text_label.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        self.Text = tk.Text(master, height=5, width=50, fg="white", bg="teal", font=30)
        self.Text.grid(row=0, column=0, sticky="", padx=10, pady=10)
        self.Text.insert(tk.END, "Add a new folder of log files to the match folder\nin the match folder add the new folder of log files to a folder \ncalled Match* "
                         "\nreplace the star with match number\n")
        self.back_button = tk.Button(master, text="Back", font=20, padx=20, pady=8, command=self.close_screen)
        self.back_button.grid(row=1, column=1, sticky="s", padx=10, pady=80)
        self.upload = tk.Button(master, text='Upload Files', font=20, padx=20, pady=8, command=self.move)
        self.upload.grid(row=1, column=0, sticky="n", padx=10, pady=80)

    def open_popup(self, source):
        top = tk.Toplevel(self.master)
        top.geometry("300x150")
        top.title("Game Name")

        name = tk.Entry(top, font=('Mistral 15 bold'))
        name.grid(row=0, column=0, sticky="n", padx=10)

        def on_enter():
            entered_name = name.get()
            if entered_name == "":
                message = tk.Label(top, text="please enter file name")
                message.grid(row=1, column=0, sticky="s")
            else:
                # this is to update the config file for the matches folder with the name of the new file
                cwd = os.getcwd()
                file_path = os.path.join(cwd,"matches","config.txt")  # Update with the actual file path
                with open(file_path, "a") as file:
                    file.write(entered_name + "\n")
                file.close()
                # this is to generate the config file for the new file
                txt = os.path.join(source, "config.txt")
                file = open(txt, "w")
                file.write(entered_name)
                file.close()
                top.destroy()

        enter_button = tk.Button(top, text="Enter", font=('Mistral 15 bold'), command=on_enter)
        enter_button.grid(row=0, column=1, sticky="n")

        top.wait_window(top)

    def get_folder_name(self):
        cur = os.getcwd()
        directory = os.path.join(cur,"matches")
        subdirectories = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
        if subdirectories:
            last_folder = sorted(subdirectories)[-1]
            last_folder = os.path.join(directory, last_folder)
        else:
            last_folder= None
        
        if last_folder:
            last = last_folder.split("\\")
            return "match"+str(int(last[-1][-1]) + 1)
        else:
            print(f"No subfolders found in {directory}")

    

    def move(self):
        source_directory = askdirectory()
        if source_directory:
            current_directory = os.getcwd()
            destination_directory = os.path.join(current_directory, "matches")
            directory_name = os.path.basename(source_directory)
            destination_path = os.path.join(destination_directory, directory_name)
            new_folder_name = self.get_folder_name()
            destination_path = os.path.join(destination_directory, new_folder_name)

            self.open_popup(source_directory)

            try:
                shutil.move(source_directory, destination_path)
                pb1 = tkk.Progressbar(
                    self.master,
                    orient=tk.HORIZONTAL,
                    length=300,
                    mode='determinate'
                )

                pb1.grid(row=0, columnspan=3, sticky="s", pady=20)
                for i in range(5):
                    self.master.update_idletasks()
                    pb1['value'] += 20
                    time.sleep(0.1)
                pb1.destroy()
            except shutil.Error as e:
                print("Error occurred while moving the directory.")
                print(f"Source Directory: {source_directory}")
                print(f"Destination Directory: {destination_path}")
                print(f"Error Details: {e}")
            else:
                print("No directory selected.")

    def close_screen(self):
        self.master.withdraw()
        self.main_screen.deiconify()


# Example usage:


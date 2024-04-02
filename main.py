from tkinter import *
from tkinter import filedialog
import requests, zipfile, io
import os
from dotenv import dotenv_values

my_secrets = dotenv_values(".env")
dir = ""

def browseFiles():
    global dir
    dirname = filedialog.askdirectory(initialdir = "/")
    dir = dirname
    label_file_explorer.configure(text="Selected Folder: "+dirname)


def downloadZip():
    try:
        files = os.listdir(dir)
        for file in files:
            file_path = os.path.join(dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")

    try:
        label_status.configure(text="Downloading zip from Mirror...", fg="orange")
        r = requests.get("https://mirror.thewoodenbox.uk/modpack.zip")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        label_status.configure(text="Extracting...", fg="orange")
        z.extractall(dir)
        label_status.configure(text="Sucessfully applied the update!", fg="green")
    except:
        label_status.configure(text="Something went wrong...", fg="red")

# Create the root window
window = Tk()
window.maxsize(500, 300)
window.minsize(500, 300)
  
# Set window title
window.title('Modpack Updater - v1.0')
  
# Set window size
window.geometry("500x300")
  
#Set window background color
window.config(background = "grey")
  
# Create a File Explorer label
label_file_explorer = Label(window, text = "Select mods folder...", width = 100, height = 4, fg = "white", bg= "grey")
label_file_explorer.place(relx = 1, x =160, y = 5, anchor = NE)

label_status = Label(window, text = "Operation status will show here.", width = 100, height = 4, fg = "white", bg= "grey")
label_status.place(relx = 0.5, rely = 0.9, anchor = CENTER)

button_explore = Button(window, text = "Browse Files", command = browseFiles) 
button_explore.place(relx = 0.5, rely = 0.3, anchor = CENTER)

button_explore = Button(window, text = "Apply new modpack version", command = downloadZip) 
button_explore.place(relx = 0.5, rely = 0.5, anchor = CENTER)
  
# Let the window wait for any events
window.mainloop()
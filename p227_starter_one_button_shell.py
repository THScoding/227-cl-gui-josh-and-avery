# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded
# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

from fileinput import filename
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, padx= 530, pady=10,  bg="blue") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("times new roman", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="orange")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="green") # change frame color
frame.pack()

save_var = tk.BooleanVar()
Checkbox = tk.Checkbutton(frame, text="Save results as a file?", variable=save_var)
Checkbox.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=30, width=190)
command_textbox.pack()

#listbox
listbox = tk.Listbox(frame, height = 6, width = 50)
items = ["Ping", "Tracert","Nslookup","IPconfig", "Netstat","Nmap"]
for item in items:
    listbox.insert(tk.END, item)

# code from google
def getfromlistbox():
    try:
        sel = listbox.curselection()
        if not sel:
            return ""
        return listbox.get(sel[0]).lower()
    except Exception:
        return ""

#code from google
def move_listbox_grid_left():
    listbox.pack_forget()
    listbox.pack(side=tk.LEFT, padx=20)

def move_listbox_grid_right():
    listbox.pack_forget()
    listbox.pack(side=tk.RIGHT, padx=20)

move_button = tk.Button(root, text="Move List Left", command=move_listbox_grid_left,
    fg = "red")
move_button.pack(side=tk.LEFT, padx=5, pady=10)

move_button = tk.Button(root, text="Move List Right", command=move_listbox_grid_right,
    fg = "blue")
move_button.pack(side=tk.RIGHT, padx=5, pady=10)

def do_command():
    global command_textbox, listbox
    
    command = getfromlistbox()

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
     # url_val = "127.0.0.1"    
        url_val = "::1"
    if command == "ipconfig" or command == "netstat" or command == "nmap":
        url_val = " "

    with subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            command_textbox.insert(tk.END,line)
            command_textbox.update()
    # automatically save the textbox contents if the checkbox is checked
    if save_var.get():
        try:
            mSave()
        except Exception as e:
            command_textbox.insert(tk.END, f"\nError saving file: {e}\n")
            command_textbox.update()

# Save function.
def mSave():
        filename = asksaveasfilename(defaultextension='.txt', filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
        if not filename:
                return
        text_to_save = command_textbox.get("1.0", tk.END)
        try:
                with open(filename, mode='w', encoding='utf-8') as file:
                        file.write(text_to_save)
        except Exception as e:
                command_textbox.insert(tk.END, f"\nError saving file: {e}\n")
                command_textbox.update()
# Modifies the one button parameters.
oneringdothemall_btn = tk.Button(frame, text="Check selected function", 
    compound="center",
    font=("times new roman", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "red",
    bg="yellow")
oneringdothemall_btn.config(command=do_command)
oneringdothemall_btn.pack() 

listbox.pack()
 
   
root.mainloop()
# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded
# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

# Makes the command button pass it's name to a function using lambda

  # Modifies the ping button parameters.
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "mediumpurple3",
    bg="black", activebackground="gray")
ping_btn.pack() 

tracert_btn = tk.Button(frame, text="Map your data packet's route", command=lambda:do_command("tracert"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "mediumpurple3",
    bg="black", activebackground="gray")
tracert_btn.pack()

nslookup_btn = tk.Button(frame, text = "Name server look up", command=lambda:do_command("nslookup"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "mediumpurple3",
    bg="black", activebackground="gray")
nslookup_btn.pack()

ipconfig_btn = tk.Button(frame, text = "Check to see IP address", command=lambda:do_command("ipconfig"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "mediumpurple3",
    bg="black", activebackground="gray")
ipconfig_btn.pack()

netstat_btn = tk.Button(frame, text = "See the path of data transmission", command= lambda:do_command("netstat"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "mediumpurple3",
    bg="black", activebackground="gray")
netstat_btn.pack()

nmap_btn = tk.Button(frame, text="Find open ports and services", command=lambda:do_command("nmap"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    fg = "mediumpurple3",
    bg="black", activebackground="gray")
nmap_btn.pack()

def do_command(command):
    global command_textbox, listbox
    
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

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()
'''
listbox = tk.Listbox(frame, height = 5, width = 50)
items = ["Ping", "Tracert","Nslookup","IPconfig", "Netstat","Nmap"]
for item in items:
    listbox.insert(tk.END, item)

listbox.pack()
'''
   
root.mainloop()
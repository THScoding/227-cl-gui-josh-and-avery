# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command_ping():
    subprocess.call("ping localhost")

def do_command_ipconfig():
    subprocess.call("ipconfig")

def do_command_Netstat():
    subprocess.call("netstat")

def do_command_tracert():
    subprocess.call("tracert localhost")

def do_command_nslookup():
    subprocess.call("nslookup localhost")

def do_command_nmap():
    subprocess.call("nmap localhost")

root = tk.Tk()
frame = tk.Frame(root)
frame.configure(width =300, height=200)
frame.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="ping", command=do_command_ping)
ping_btn.pack()

ipconfig_btn = tk.Button(frame, text="ipconfig", command=do_command_ipconfig)
ipconfig_btn.pack()

netstat_btn = tk.Button(frame, text="netstat", command=do_command_Netstat)
netstat_btn.pack()

tracert_btn = tk.Button(frame, text="tracert", command=do_command_tracert)
tracert_btn.pack()

nslookup_btn = tk.Button(frame, text="nslookup", command=do_command_nslookup)
nslookup_btn.pack()

nmap_btn = tk.Button(frame, text="nmap", command=do_command_nmap)
nmap_btn.pack()

listbox = tk.Listbox(frame)
listbox.insert(1, ping_btn)
listbox.insert(2, ipconfig_btn)
listbox.insert(3, netstat_btn)
listbox.insert(4, tracert_btn)
listbox.insert(5, nslookup_btn)
listbox.insert(6, nmap_btn)
listbox.pack()
root.mainloop()

import nmap
import tkinter as tk
from tkinter import messagebox

def scan():
    target = entry.get()
    nm = nmap.PortScanner()

    try:
        result = nm.scan(target, arguments='-p 1-1024')
        messagebox.showinfo("Scan Results", result)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Nmap GUI")

label = tk.Label(root, text="Enter target IP/hostname:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

scan_button = tk.Button(root, text="Scan", command=scan)
scan_button.pack(pady=10)

root.mainloop()

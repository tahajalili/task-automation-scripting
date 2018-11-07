#!/usr/bin/env python3

import tkinter as tk
import pyautogui as pt

def counter_label(labelx, labely):
  def count():
    global  counterx
    global countery
    counterx, countery = pt.position()
    labelx.config(text='X position: '+str(counterx))
    labely.config(text='Y position: '+str(countery))
    label.after(100, count)
  count()
 
 
root = tk.Tk()
root.title("  Taha Mouse Position   ")
label = tk.Label(root, fg="green")
label1 = tk.Label(root, fg="red")
label.pack()
label1.pack()
counter_label(label,label1)
button = tk.Button(root, text='Stop', width=30, command=root.destroy)
button.pack()
root.mainloop()
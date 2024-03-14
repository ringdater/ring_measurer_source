# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:53:54 2023

@author: david
"""
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from menubar import MenuBar

from PIL import Image, ImageTk
from tkinter import filedialog
import os



class MainWindow(ttk.Frame):
    def __init__(self, mainframe):
        ttk.Frame.__init__(self, master=mainframe)
        self.master.title('Ring Measurer AI')
        self.master.geometry('800x600')  # size of the main window
        self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        self.master.columnconfigure(0, weight=1)
        
        self.menu = MenuBar(self.master)
        
        classframe = ctk.CTkFrame(self.master)
        classframe.grid(row = 0, column = 0, pady = 0, sticky = "NSEW")
        
        classframe.rowconfigure(0, weight = 1)       
        
        title_label = ctk.CTkLabel(classframe, text = "Help")
        title_label.grid(row = 0, column = 0, sticky = "NW", pady = 5, padx = 5, columnspan = 1)  
        
        # btn = ctk.CTkButton(classframe, text = "Help", command = lambda: open_new_win(self.master, classframe))
        # btn.grid(row = 1, column = 0, sticky = "NW", pady = 5, padx = 5, columnspan = 1)  
        
        filename = filedialog.askopenfilename(initialdir = os.getcwd() + "/images",
                                            title = "Select a File",
                                            filetypes = (("tif",
                                                          "*.tif*"),
                                                          ("jpeg",
                                                          "*.jpg*"),                                                           
                                                          ("png",
                                                          "*.png*"),))
        
        MAX_sizE = (100,100)       
        img = Image.open(filename)
        img.thumbnail(MAX_sizE)
        img = ImageTk.PhotoImage(img)
        
        label1 = tk.Label(image = img)
        label1.image = img

        # Position image
        label1.grid(row = 1, column = 0)
        

        
        
if __name__ == "__main__":
   # ST.init()
    app = MainWindow(tk.Tk())
    app.mainloop()  
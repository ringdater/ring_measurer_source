# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:07:01 2023

@author: david
"""
import tkinter as tk
import customtkinter as ctk

from menubar import MenuBar

class img_win():
    def __init__(self, parent, win_num):
        self.window = tk.Toplevel(parent)
        self.wun_num = str(win_num)     
        
        self.window.title("Measurements")
        self.window.geometry('800x600')  # size of the main window
        self.window.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        self.window.columnconfigure(0, weight=1)
        
        self.menu = MenuBar(self.window)
        
        self.classframe = ctk.CTkFrame(self.window, width = 500, height = 500)
        self.classframe.grid(row = 0, column = 0, pady = 0, sticky = "NSEW")
        
        self.classframe.rowconfigure(0, weight = 1)       
        
        self.title_label = ctk.CTkLabel(self.classframe, text = str("this is window") + self.wun_num)
        self.title_label.grid(row = 0, column = 0, sticky = "NW", pady = 5, padx = 5, columnspan = 1)  

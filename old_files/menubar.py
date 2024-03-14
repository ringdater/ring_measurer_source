# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:19:32 2023

@author: david
"""
import tkinter as tk

class MenuBar:
    def __init__(self, parent):
        self.parent = parent
        self.menu = tk.Menu(self.parent)
        
        self.parent.config(menu=self.menu)

        self.fileMenu = tk.Menu(self.menu)
        self.fileMenu.add_command(label="Item")
        self.fileMenu.add_command(label="Exit", command=self.exitProgram)
        self.menu.add_cascade(label="File", menu=self.fileMenu)
        
    def exitProgram(self):
        self.parent.destroy()

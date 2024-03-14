# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:33:33 2023

@author: david
"""

import tkinter as tk
import customtkinter
import global_variables as ST

class restart_frame:
    def __init__(self, parent, master):
        self.visible = False
        self.parent = parent
        self.classframe = customtkinter.CTkFrame(self.parent)
        self.master = master
        
    def show(self):
        print("showing")
        self.visible = True
        
        self.classframe.grid(row= 0, column = 0)       
        
        tmp_label = customtkinter.CTkLabel(self.classframe, text = "Close the current image and return to the starting point menu? \n" +
                                           "Unsaved measurements will be lost")                       
        tmp_label.grid(row = 0, column = 0, columnspan = 2,  padx= 5, pady = 5) 
        tmp_label.configure(font=('Helvetica bold', ST.FT_SZ))
        
        confirm_btn = customtkinter.CTkButton(self.classframe, 
                                             text = "Return to startting point",
                                             command = self.confirm_restart,
                                             corner_radius=5,
                                             height=100)
        confirm_btn .grid(row = 1, column = 0, pady = 5, padx = 5, sticky=tk.EW) 
        confirm_btn.configure(font=('Helvetica bold', ST.FT_SZ))
        
        cancel_btn = customtkinter.CTkButton(self.classframe, 
                                             text = "Cancel",
                                             command = self.hide,
                                             corner_radius=5,
                                             height=100)
        cancel_btn .grid(row = 1, column = 1, pady = 5, padx = 5, sticky=tk.EW) 
        cancel_btn.configure(font=('Helvetica bold', ST.FT_SZ))        

    def hide(self):
        self.classframe.grid_forget()

    def confirm_restart(self):
        #self.master.destroy()
        #ST.init() 
        ST.starting_menu.parent = self.parent        
        ST.starting_menu.toggle()
        
        #ST.CALIBRATION = CALIBRATE()
        #self.__init__(tk.Tk())
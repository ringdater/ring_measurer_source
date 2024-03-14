# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:40:46 2023

@author: dr454
"""
import customtkinter as ctk
import tkinter as tk
from global_functions import toggle_series, toggle_mode, save_AI_data

class AI_window:
    def __init__(self, parent, win_num):
        self.parent = parent
        self.winnum = win_num 
        self.visible = False
        
        self.AI_results_frame = ctk.CTkFrame(self.parent, width = 150)
        #######################################################################
        
        self.AI_results_label = ctk.CTkLabel(self.AI_results_frame, text = "AI Options")
        self.AI_results_label.grid(row = 0, column = 0, pady = 5)

        self.Mode_select = ctk.CTkComboBox(master=self.AI_results_frame,
                                     values= ["delete", "insert"],
                                     command=self.AI_mode_select)
        
        self.Mode_select.grid(row = 1, column = 0, pady = 5, padx = 5, sticky=tk.EW)
        self.Mode_select.set("delete")

        self.gen_measurements = ctk.CTkButton(self.AI_results_frame, text = "Generate measurements",
                                              command = self.generate_AI_data,
                                              width=50)
        
        self.gen_measurements.grid(row = 2, column = 0, columnspan = 2, pady = 5, padx = 2, sticky=tk.EW) 



        self.save_data = ctk.CTkButton(self.AI_results_frame, text = "Save AI data",
                                              command = save_AI_data,
                                              width=50)
        
        self.save_data.grid(row = 3, column = 0, columnspan = 2, pady = 5, padx = 2, sticky=tk.EW) 



        self.close_window = ctk.CTkButton(self.AI_results_frame, text = "close",
                                              command = self.toggle,
                                              width=50)
        
        self.close_window.grid(row = 4, column = 0, columnspan = 2, pady = 5, padx = 2, sticky=tk.EW) 
        # toggle_mode("AI")
        # toggle_series("AI")
        
    def show(self):
        self.AI_results_frame.grid(row = 0, column = 0, pady = 125, padx = 0, sticky = tk.NW)         

    def hide(self):
        self.AI_results_frame.grid_forget()
    
    def toggle(self):
        #if the frame is not visible, then show it.
        if self.visible == False:
            self.show()
        # if the frame is currently visible, hide it.
        elif self.visible == True:
            self.hide()
        #     toggle_mode("measure", self.win_num)
        #     WA.wins[self.win_num].canvas.IDT.toolbar.active_mode_label.configure(text = str("Measure"))
        self.visible = not self.visible  
    
    def AI_mode_select(self):
        pass
    
    def generate_AI_data(self):
        pass
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:38:15 2023

@author: david
"""
import tkinter as tk
import customtkinter
from tkinter import colorchooser

import global_variables as ST

class settings_window:
    def __init__(self, parent):
        self.visible = False
        
        self.vertical_offset = 75
        
        self.settings_frame = customtkinter.CTkScrollableFrame(parent, width = 400, height = 300)
        #self.settings_frame.grid(row = 0, column = 0, pady = self.vertical_offset, padx = 5)
        self.settings_frame.columnconfigure(0, minsize = 150)
        
        series_col_label = customtkinter.CTkLabel(self.settings_frame, text = "Measurement colours")
        series_col_label.grid(row = 1, column = 0, pady = 5, columnspan = 2)
              
        self.ser1_col_entry = customtkinter.CTkEntry(self.settings_frame)
        self.ser1_col_entry.grid(row = 2, column = 1, pady = 5)
        self.ser1_col_entry.insert(0, ST.ser_1_col) 
        
        ser1_col_btn = customtkinter.CTkButton(master=self.settings_frame, text="Series 1 colour", 
                                               command= lambda: [self.ser1_col_entry.delete(0, tk.END), self.ser1_col_entry.insert(0, self.choose_color(ST.ser_1_col))])
        ser1_col_btn.grid(row = 2, column = 0, pady = 5)
     
        self.ser2_col_entry = customtkinter.CTkEntry(self.settings_frame)
        self.ser2_col_entry.grid(row = 3, column = 1, pady = 5)
        self.ser2_col_entry.insert(0, ST.ser_2_col)
        
        ser2_col_btn = customtkinter.CTkButton(master=self.settings_frame, text="Series 2 colour", 
                                               command= lambda: [self.ser2_col_entry.delete(0, tk.END), 
                                                                 self.ser2_col_entry.insert(0, self.choose_color(ST.ser_2_col))])
        ser2_col_btn.grid(row = 3, column = 0, pady = 5)
        
        self.ser3_col_entry = customtkinter.CTkEntry(self.settings_frame)
        self.ser3_col_entry.grid(row = 4, column = 1, pady = 5)
        self.ser3_col_entry.insert(0, ST.ser_3_col) 
        
        ser3_col_btn = customtkinter.CTkButton(master=self.settings_frame, text="Series 3 colour", 
                                               command= lambda: [self.ser3_col_entry.delete(0, tk.END), 
                                                                 self.ser3_col_entry.insert(0, self.choose_color(ST.ser_3_col))])
        ser3_col_btn.grid(row = 4, column = 0, pady = 5)
        
        self.insert_col_entry = customtkinter.CTkEntry(self.settings_frame)
        self.insert_col_entry.grid(row = 5, column = 1, pady = 5)
        self.insert_col_entry.insert(0, ST.insert_col)
        
        insert_col_btn = customtkinter.CTkButton(master=self.settings_frame, text="Insert measurements colour", 
                                               command= lambda: [self.insert_col_entry.delete(0, tk.END), 
                                                                 self.insert_col_entry.insert(0, self.choose_color(ST.insert_col))])
        insert_col_btn.grid(row = 5, column = 0, pady = 5)
        
        self.active_col_entry = customtkinter.CTkEntry(self.settings_frame)
        self.active_col_entry.grid(row = 6, column = 1, pady = 5)
        self.active_col_entry.insert(0, ST.active_col)
        
        active_col_btn = customtkinter.CTkButton(master=self.settings_frame, text="Active measurement colour", 
                                               command= lambda: [self.active_col_entry.delete(0, tk.END), 
                                                                 self.active_col_entry.insert(0, self.choose_color(ST.active_col))])
        active_col_btn.grid(row = 6, column = 0, pady = 5)
               
        line_thick_label = customtkinter.CTkLabel(self.settings_frame, text = "Line width")
        line_thick_label.grid(row = 7, column = 0, pady = 5) 
        
        self.line_thick_value = customtkinter.CTkSlider(self.settings_frame, from_=1, to=15)
        self.line_thick_value.grid(row = 7, column = 1, pady = 5) 
        self.line_thick_value.set(ST.L_WIDTH)
        
        line_end_cap_label = customtkinter.CTkLabel(self.settings_frame, text = "Line end cap size")
        line_end_cap_label.grid(row = 8, column = 0, pady = 5) 
        
        self.line_end_cap_value = customtkinter.CTkSlider(self.settings_frame, from_=1, to=100)
        self.line_end_cap_value.grid(row = 8, column = 1, pady = 5) 
        self.line_end_cap_value.set(ST.line_cap_len)
        
        line_cap_thick_label = customtkinter.CTkLabel(self.settings_frame, text = "Line end cap tickness")
        line_cap_thick_label.grid(row = 9, column = 0, pady = 5) 
        
        self.line_cap_thick_value = customtkinter.CTkSlider(self.settings_frame, from_=1, to=100)
        self.line_cap_thick_value.grid(row = 9, column = 1, pady = 5) 
        self.line_cap_thick_value.set(ST.line_cap_thickness)      
                
        show_label_label = customtkinter.CTkLabel(self.settings_frame, text = "Show/Hide measurement labels")
        show_label_label.grid(row = 10, column = 0, pady = 5)
        
        label_btn = customtkinter.CTkButton(self.settings_frame, text = "Toggle labels",
                                                command = self.show_labels,
                                                width = 100)
        label_btn.grid(row = 10, column = 1, padx = 5, sticky=tk.EW) 
                
        x_off_label = customtkinter.CTkLabel(self.settings_frame, text = "Labels X position")
        x_off_label.grid(row = 11, column = 0, pady = 5) 
        
        self.lab_x_off_value = customtkinter.CTkSlider(self.settings_frame, from_=-50, to=50)
        self.lab_x_off_value.grid(row = 11, column = 1, pady = 5) 
        self.lab_x_off_value.set(ST.lab_x_off)
        
        y_off_label = customtkinter.CTkLabel(self.settings_frame, text = "Labels Y position")
        y_off_label.grid(row = 12, column = 0, pady = 5) 
        
        self.lab_y_off_value = customtkinter.CTkSlider(self.settings_frame, from_=-50, to=50)
        self.lab_y_off_value.grid(row = 12, column = 1, pady = 5) 
        self.lab_y_off_value.set(ST.lab_y_off)
        
        proximity_label = customtkinter.CTkLabel(self.settings_frame, text = "Proximity")
        proximity_label.grid(row = 13, column = 0, pady = 5) 
        
        self.proximity_value = customtkinter.CTkSlider(self.settings_frame, from_=1, to=40)
        self.proximity_value.grid(row = 13, column = 1, pady = 5) 
        self.proximity_value.set(ST.PROXIMITY)
                      
        insert_submit = customtkinter.CTkButton(self.settings_frame, text = "Apply",
                                                command = self.apply_settings,
                                                width = 100)
        insert_submit.grid(row = 19, column = 0, padx = 5, sticky=tk.EW) 
        
        calib_submit = customtkinter.CTkButton(self.settings_frame, text = "Close", 
                                               command = self.toggle,
                                               width = 100)
        calib_submit.grid(row = 19, column = 1, padx = 5, sticky=tk.EW)  
        
    def choose_color(self, prev_colour): 
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color")
        
        if color_code[1] != None:
            return color_code[1]
        else: return prev_colour
    
    def show_labels(self):
        pass    
    
    def apply_settings(self):
        pass
    
    def show(self):
        self.settings_frame.grid(row = 0, column = 0, sticky = "NW")

    def hide(self):
        self.settings_frame.grid_forget()
                         
    def toggle(self):
        #if the frame is not visible, then show it.
        if self.visible == False:
            self.show()
        # iof the frame is currently visible, hide it.
        elif self.visible == True:
            self.hide()
        self.visible = not self.visible
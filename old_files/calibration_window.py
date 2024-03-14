# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:10:25 2023

@author: david
"""

import tkinter as tk
import customtkinter

#import global_variables as ST
#from global_functions import toggle_mode

class calibration_window:
    def __init__(self, parent):
        
        self.visible = False
                        
        self.calib_frame = customtkinter.CTkFrame(parent, width = 200, height = 200)
        #self.calib_frame.grid(row = 0, column = 0, pady = 115)
        
        self.calib_label = tk.Label(self.calib_frame, text = "Use the mouse (left click) to measure \nthe scale bar ")
        self.calib_label.grid(row = 0, column = 0, pady = 5)
        
        self.calib_label = tk.Label(self.calib_frame, text = "Enter distance measured (um)")
        self.calib_label.grid(row = 1, column = 0, pady = 5)        
                
        self.calib_dist = tk.Entry(self.calib_frame)
        self.calib_dist.grid(row = 2, column = 0, pady = 5)  
        
        self.calib_submit = tk.Button(self.calib_frame, text = "Submit", command = lambda: self.set_calibration(self.calib_dist.get()))
        self.calib_submit.grid(row = 3, column = 0, pady = 0) 
        
        self.calib_close = tk.Button(self.calib_frame, text = "Close", command = self.toggle)
        self.calib_close.grid(row = 3, column = 1, pady = 0)  
        
        if ST.CALIBRATED == True:
            cal_set_label = tk.Label(self.calib_frame, text = "Calibration set: " + str(round(ST.CALIBRATION.sf, 3)))
            cal_set_label.grid(row = 4, column = 0, pady = 5)
            
            
    def show(self):
        self.calib_frame.grid(row = 0, column = 0, pady = 115, sticky = "NW")

    def hide(self):
        self.calib_frame.grid_forget()
                         
    def toggle(self):
        #if the frame is not visible, then show it.
        if self.visible == False:
            self.show()
        # if the frame is currently visible, hide it.
        elif self.visible == True:
            self.hide()
            toggle_mode("measure")
        self.visible = not self.visible   
        
    def set_calibration(self, value):          
        if ST.CALIBRATED == False:
            ST.object_list[len(ST.object_list)-1].abs_distance = float(value)
            
            ST.calibration_SF = 1/ (float(ST.object_list[len(ST.object_list)-1].px_distance)/ ST.object_list[len(ST.object_list)-1].abs_distance)
            ST.object_list[len(ST.object_list)-1].calibration = ST.calibration_SF
            cal_set_label = tk.Label(self.calib_frame, text = "Calibration set:" + str(round(ST.object_list[len(ST.object_list)-1].calibration, 3)))
            cal_set_label.grid(row = 4, column = 0, pady = 5)
            ST.CALIBRATED = True        
        self.calibrate_series()
            
    def calibrate_series(self):        
        for i in range(len(ST.object_list)):        
            ST.object_list[i].calibration = ST.calibration_SF
            print(ST.object_list[i].mode)
            if ST.object_list[i].mode == "measure":
                ST.object_list[i].abs_distance = ST.object_list[i].px_distance * ST.object_list[i].calibration
                ST.object_list[i].calibrated = True  
        
        
        
        
        
        
        
        
        
        
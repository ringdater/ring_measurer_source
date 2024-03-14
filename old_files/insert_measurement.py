# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:09:34 2023

@author: david
"""

import customtkinter
#import tkinter as tk

import global_variables as ST
from global_functions import toggle_mode, toggle_series, set_order, sort_object_list

class insert_measurement:
    def __init__(self, parent):
        # set if visible
        self.visible = False
        
        #######################################################################
        # create a frame to hold all contents
        self.classframe = customtkinter.CTkFrame(parent)

        self.classframe.rowconfigure(0, weight = 1)       
       
        self.M1_label = customtkinter.CTkLabel(self.classframe, text = "Left click on the increment you want to add \nnew measurements before")
        self.M1_label.grid(row = 1, column = 0, pady = 5, columnspan = 2)        
                
        self.M1_label2 = customtkinter.CTkLabel(self.classframe, text = "No measurement selected")
        self.M1_label2.grid(row = 2, column = 0, pady = 5, columnspan = 2) 
        
        confirm_Select = customtkinter.CTkButton(self.classframe, text = "Confirm selection", command = self.insert_confirm)
        confirm_Select.grid(row = 3, column = 1, pady = 0, stick="nsew") 
        
        clear_Select = customtkinter.CTkButton(self.classframe, text = "Clear selection", command = self.insert_clear)
        clear_Select.grid(row = 3, column = 0, pady = 0, stick="nsew") 
        
        insert_submit = customtkinter.CTkButton(self.classframe, text = "Insert Measurements", command = self.insert_measurements)
        insert_submit.grid(row = 4, column = 0, columnspan = 2, pady = 5, stick="nsew") 
        
        insert_close = customtkinter.CTkButton(self.classframe, text = "Close", command = self.toggle)
        insert_close.grid(row = 5, column = 1, pady = 5, stick="nsew") 
            
    def insert_confirm(self):
        ST.IN_CONFIRM == True
        ring_no = ST.object_list[ST.M1[1]].ind
        self.M1_label2.configure(text = ("Ring confirmed: " + str(ST.M1[0]) + " " + str(ring_no) + "\nNow make the measurements"))
        toggle_mode("measure")
        toggle_series("insert")        
             
    def insert_clear(self):
        ST.IN_CONFIRM == False
        self.M1_label2.configure(text = "No ring selected")
        ST.M1 = [0]
    
    def insert_measurements(self):
        series = ST.M1[0] # which series to insert the measurements into    
        ring = ST.object_list[ST.M1[1]].ind # which ring to insert them before
        n_rings = len(ST.INSERT_SERIES) # how rings to insert
        print("ring num =" + str(ring) + "num of rungs = " + str(n_rings))
        
        #### change the numbers on existing measurements after the insert
        for i in range(len(ST.object_list)):
            if ST.object_list[i].series == series and ST.object_list[i].ind >= ring:
                
                ST.object_list[i].ind = ST.object_list[i].ind + n_rings
                ST.object_list[i].label_text = ST.object_list[i].ind
                ST.canvas.canvas.itemconfigure(ST.object_list[i].label,
                                               text = ST.object_list[i].label_text)
        
        # update the labels on the insert series
        for i in range(len(ST.INSERT_SERIES)):
            print("i + ring = " + str(i + ring))
            ST.INSERT_SERIES[i].label_text = i + ring            
            ST.INSERT_SERIES[i].ind = ST.INSERT_SERIES[i].label_text            
            ST.canvas.canvas.itemconfigure(ST.INSERT_SERIES[i].label,
                                            text = ST.INSERT_SERIES[i].label_text)
            print("new label text = " + str(ST.object_list[i].label_text))
            
            # ST.canvas.canvas.itemconfigure(ST.object_list[i].label,
            #                                text = ST.object_list[i].label_text)
        
        ### change the insert measurements to the correct series
        if ST.M1[0] == "series_1":            
            for i in range(len(ST.INSERT_SERIES)):
                obj = ST.INSERT_SERIES[i].obj_index
                
                ST.canvas.canvas.itemconfig(ST.object_list[obj].object, fill = ST.ser_1_col)
                ST.object_list[obj].series = "series_1"
                ST.object_list[obj].col = ST.ser_1_col
                
        if ST.M1[0] == "series_2":            
            for i in range(len(ST.INSERT_SERIES)):
                obj = ST.INSERT_SERIES[i].obj_index
                
                ST.canvas.canvas.itemconfig(ST.object_list[obj].object, fill = ST.ser_2_col)
                ST.object_list[obj].series = "series_2"
                ST.object_list[obj].col = ST.ser_2_col
                
        if ST.M1[0] == "series_3":            
            for i in range(len(ST.INSERT_SERIES)):
                obj = ST.INSERT_SERIES[i].obj_index
                
                ST.canvas.canvas.itemconfig(ST.object_list[obj].object, fill = ST.ser_3_col)
                ST.object_list[obj].series = "series_3"
                ST.object_list[obj].col = ST.ser_3_col
        
        ST.SERIES_1 = self.update_series("series_1")
        ST.SERIES_2 = self.update_series("series_2")
        ST.SERIES_3 = self.update_series("series_3")
        #self.update_series
        
        #ST.results.update()
        
        ST.M1 = [0]
        ST.IN_CONFIRM == False
        
        ST.INSERT_SERIES = []
        toggle_mode("measure")
        toggle_series("series_1")
        sort_object_list()
        
                
    def update_series(self, series):                
        tmp_series = []
        for i in range(len(ST.object_list)):
            if ST.object_list[i].series == series:
                tmp_series.append(ST.object_list[i])              
        
        if len(tmp_series) != 0:                                  
            return set_order(tmp_series)
        else: return []
 
    def show(self):
        toggle_mode("insert")
        toggle_series("insert")            
        ST.M1 = [0]
        ST.IN_CONFIRM == False
        self.M1_label2.configure(text = "No measurement selected") 
        self.classframe.grid(row = 0, column = 0, pady = 125, sticky = "NW")

    def hide(self):
        toggle_mode("measure")
        tmp_series = ST.prev_series
        toggle_series("series_1")
        ST.prev_series = tmp_series
        self.classframe.grid_forget()
        ST.INSERT_SERIES = []
                         
    def toggle(self):
        #if the frame is not visible, then show it.
        if self.visible == False:
            self.show()
        # iof the frame is currently visible, hide it.
        elif self.visible == True:
            self.hide()
        self.visible = not self.visible
        
        
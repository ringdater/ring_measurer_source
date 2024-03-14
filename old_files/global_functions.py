# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:17:56 2023

@author: david
"""

import global_variables as ST

import customtkinter
import tkinter as tk
import math

#import master_array as WS

class canvas_object:
    def __init__(self, x1, y1, x2, y2, mode, series, ind):
        self.obj_index = None # what is the index in the object lst - use to keep track of objects between lists
        self.x1 = x1 # the x1 position on the original image - not the canvas position
        self.y1 = y1 # the y1 position on the original image - not the canvas position
        self.x2 = x2 # the x2 position on the original image - not the canvas position
        self.y2 = y2 # the y2 position on the original image - not the canvas position
        self.mode = mode # what mode was the app in when the object was created
        self.series = series # what series was being measured
        self.type = False # is this part of a measurement line
        self.ind = ind # the index in the object_list array
        self.object = None # the actual canvas object
        self.text = None # if the object is text, this is the actual text to display
        self.px_distance = None # measurement length in pixels
        self.abs_distance = None # the calibration for the image defaults to 1 pixel per um
        self.calibrated = False # has the distance had a calibration applied?       
        self.calibration = 1 # the scale factor to use to convert from pixel to absolute distance
        self.line_label = None # holds the label object
        self.year = None # use to assign years to the measurements        
        self.dated = None # has this sample been crossdated
        self.col = None # what colour is the object        
        self.label = None # the label object
        self.label_visible = False # is the label visible or not
        self.label_text = None # the text to show in the label 
        
        
# =============================================================================
#  functions       
# =============================================================================

  
def toggle_series(series, win):
    WS.DT[win].prev_ser = WS.DT[win].ACT_SER
    if series == "series_1":
        WS.DT[win].ACT_SER = "series_1"
    if series == "series_2":
        WS.DT[win].ACT_SER = "series_2"
    if series == "series_3":
        WS.DT[win].ACT_SER = "series_3"
    if series == "insert":
        WS.DT[win].ACT_SER = "insert" 
    WS.DT[win].toolbar.current_series_label.configure(text =  WS.DT[win].ACT_SER)
    
def set_anno_type(anno_type, win):    
    WS.DT[win].anno_type = anno_type



    #when the mouse is moveed check if it goes over an object on the canvas
           
            
def convert_to_canvas(x, y, win):
    top_left_coords = WS.DT[win].canvas.canvas.coords(WS.DT[win].TOP_LEFT)
    cx = top_left_coords[0] + (x * WS.DT[win].canvas.imscale)
    cy = top_left_coords[1] + (y * WS.DT[win].canvas.imscale)
    return([cx, cy])

# get the coordinates on the original image
def absolute(x, y, win):
    top_left_coords = WS.DT[win].canvas.canvas.coords(WS.DT[win].TOP_LEFT)
    x1 = (x - top_left_coords[0])/WS.DT[win].canvas.imscale
    y1 = (y - top_left_coords[1])/WS.DT[win].canvas.imscale
    return([x1, y1])         
    

def delete_object(event, win):
    if hover_over(event, win) != None:
        obj = hover_over(event, win)[0] # was the delete button clicked on an object in the canvas?
    #if obj != None:
        WS.DT[win].canvas.canvas.delete(WS.DT[win].object_list[obj].object)
        WS.DT[win].canvas.canvas.delete(WS.DT[win].object_list[obj].label)# remove the object from the canvas
        remove_from_Series(obj, win)
        # remove the object from the list of objects
    
def delete_last(win):    
    if len(WS.DT[win].object_list) >  0:
        WS.DT[win].canvas.canvas.delete(WS.DT[win].object_list[len(WS.DT[win].object_list)-1].object) # remove the object from the canvas
        WS.DT[win].canvas.canvas.delete(WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label)
        #remove_from_Series()
        if WS.DT[win].object_list[len(WS.DT[win].object_list)-1].series == "series_1":
            WS.DT[win].SERIES_1.pop()
        if WS.DT[win].object_list[len(WS.DT[win].object_list)-1].series == "series_2":
            WS.DT[win].SERIES_2.pop()
        if WS.DT[win].object_list[len(WS.DT[win].object_list)-1].series == "series_3":
            WS.DT[win].SERIES_3.pop()
        WS.DT[win].object_list.pop() # remove the object from the list of objects

def remove_from_Series(obj, win):
    
    series = WS.DT[win].object_list[obj].series
    ind = WS.DT[win].object_list[obj].ind     
    WS.DT[win].object_list.pop(obj)
    
    for i in range(len(WS.DT[win].object_list)):
        if (WS.DT[win].object_list[i].series == series and 
            WS.DT[win].object_list[i].ind > ind):
            WS.DT[win].object_list[i].ind = WS.DT[win].object_list[i].ind - 1
            WS.DT[win].object_list[i].label_text = WS.DT[win].object_list[i].ind
            WS.DT[win].canvas.canvas.itemconfigure(WS.DT[win].object_list[i].label,
                                           text = WS.DT[win].object_list[i].label_text)
    del_ser = None    
    if series == "series_1":
        for i in range(len(WS.DT[win].SERIES_1)):
            if WS.DT[win].SERIES_1[i].ind == ind:
               del_ser = i                
            elif WS.DT[win].SERIES_1[i].ind > ind:
                WS.DT[win].SERIES_1[i].ind - 1
        WS.DT[win].SERIES_1.pop(del_ser)                
    if series == "series_2":
        for i in range(len(WS.DT[win].SERIES_2)):
            if WS.DT[win].SERIES_2[i].ind == ind:
                del_ser = i                
            elif WS.DT[win].SERIES_2[i].ind > ind:
                WS.DT[win].SERIES_2[i].ind - 1
        WS.DT[win].SERIES_2.pop(del_ser)        
    if series == "series_3":
        for i in range(len(WS.DT[win].SERIES_3)):
            if WS.DT[win].SERIES_3[i].ind == ind:
                del_ser = i                
            elif WS.DT[win].SERIES_3[i].ind > ind:
                WS.DT[win].SERIES_3[i].ind - 1
        WS.DT[win].SERIES_3.pop(del_ser)
        
    sort_object_list(win)
        
###############################################################################


###############################################################################

def draw_line(event, win):
    print(len(WS.DT))
    #get coords of where the mouse was clikced in the canvas
    x = WS.DT[win].canvas.canvas.canvasx(event.x)
    y = WS.DT[win].canvas.canvas.canvasy(event.y)        
    # to start a measurement temporarily store the coordinates where the mouse was clicked
    if WS.DT[win].ACTIVE == -1:
        WS.DT[win].TMP = [x,y]   
    
    # if a measurement has already been started, create  a perminent line and store the coordinates
    else:       
        p1 = absolute(WS.DT[win].TMP[0], WS.DT[win].TMP[1], win)
        p2 = absolute(x, y, win)       
        
        ind = None
        #get the index for the series
        if WS.DT[win].MODE == "measure":
            if WS.DT[win].ACT_SER == "series_1":
                ind = len(WS.DT[win].SERIES_1) 
            if WS.DT[win].ACT_SER == "series_2":
                ind = len(WS.DT[win].SERIES_2) 
            if WS.DT[win].ACT_SER == "series_3":
                ind = len(WS.DT[win].SERIES_3) 
            if WS.DT[win].ACT_SER == "insert" and len(WS.DT[win].M1) == 2:
                #ind = len(ST.INSERT_SERIES) 
                ind = WS.DT[win].object_list[WS.DT[win].M1[1]].ind + len(WS.DT[win].INSERT_SERIES)
                
                
        WS.DT[win].object_list.append(canvas_object(p1[0], p1[1],
                                            p2[0], p2[1],
                                            WS.DT[win].MODE, 
                                            WS.DT[win].ACT_SER, 
                                            ind))
        WS.DT[win].object_list[len(WS.DT[win].object_list)-1].obj_index = (len(WS.DT[win].object_list) - 1)
        WS.DT[win].object_list[len(WS.DT[win].object_list)-1].type = "line"
        WS.DT[win].object_list[len(WS.DT[win].object_list)-1].col = WS.DT[win].ACT_COLOR
        WS.DT[win].object_list[len(WS.DT[win].object_list)-1].object = WS.DT[win].canvas.canvas.create_line(WS.DT[win].TMP[0], WS.DT[win].TMP[1],
                                                                                     x, y,
                                                                                     fill=WS.DT[win].ACT_COLOR, 
                                                                                     width=WS.DT[win].L_WIDTH,
                                                                                     arrow=tk.BOTH,
                                                                                     arrowshape = WS.DT[win].line_cap)        
        px_distance = math.dist((WS.DT[win].TMP[0],WS.DT[win].TMP[1]), 
                             (x, y)) * (1/WS.DT[win].canvas.imscale) 
        
        if WS.DT[win].MODE == "measure" or WS.DT[win].MODE == "calibrate":                                                                 
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].px_distance = px_distance
        
        if WS.DT[win].CALIBRATED == True:
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].px_distance = px_distance
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].calibrated = True
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].calibration = WS.DT[win].calibration_SF
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].abs_distance = WS.DT[win].object_list[len(WS.DT[win].object_list)-1].px_distance * WS.DT[win].calibration_SF
        
        if WS.DT[win].CALIBRATED == False: 
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].abs_distance = WS.DT[win].object_list[len(WS.DT[win].object_list)-1].px_distance
            
        if WS.DT[win].MODE == "measure":
            coords = WS.DT[win].canvas.canvas.coords(WS.DT[win].object_list[len(WS.DT[win].object_list)-1].object)
            label_x = (coords[0] + coords[2]) / 2 + WS.DT[win].lab_x_off
            label_y = (coords[1] + coords[3]) / 2 + WS.DT[win].lab_y_off
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label_text = ind
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label = WS.DT[win].canvas.canvas.create_text(label_x, label_y,
                                                                                        text= WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label_text, 
                                                                                        fill="black", 
                                                                                        font=('Helvetica 15 bold'))
           
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label_visible = True # is the label visible or not
           
            add_to_series(win)
            
        if WS.DT[win].MODE == "anno" or WS.DT[win].MODE == "calibrate":
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].series = None
                
    WS.DT[win].canvas.canvas.delete(WS.DT[win].TMP_LINE)         
    WS.DT[win].ACTIVE = - WS.DT[win].ACTIVE
    

    
###############################################################################
        
def draw_point(event, win):    
    #get coords of where the mouse was clikced in the canvas
    x = WS.DT[win].canvas.canvas.canvasx(event.x)
    y = WS.DT[win].canvas.canvas.canvasy(event.y)

    size = 5
    
    p1 = absolute(x, y, win)       
    
    # to start a measurement temporarily store the coordinates where the mouse was clicked
  
    WS.DT[win].object_list.append(canvas_object(p1[0] - size, p1[1] - size, 
                                        p1[0] + size, p1[1] + size,
                                        WS.DT[win].MODE, 
                                        None, 
                                        len(WS.DT[win].object_list)))
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].obj_index = len(WS.DT[win].object_list)-1
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].type = "dot"
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].col = WS.DT[win].ACT_COLOR
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].object = WS.DT[win].canvas.canvas.create_oval(x - size, y - size, 
                                                                                x + size, y + size, 
                                                                                fill = WS.DT[win].ANNOTE_COL)
    
###############################################################################
      
def draw_text(event, win):
    #get coords of where the mouse was clikced in the canvas
    x = WS.DT[win].canvas.canvas.canvasx(event.x)
    y = WS.DT[win].canvas.canvas.canvasy(event.y)

    size = 5
        
    # to start a measurement temporarily store the coordinates where the mouse was clicked
    
    p1 = absolute(x, y, win)
    
    WS.DT[win].object_list.append(canvas_object(p1[0] - size, p1[1] - size, 
                                        p1[0] + size, p1[1] + size,
                                        WS.DT[win].MODE, 
                                        None, 
                                        len(WS.DT[win].object_list)))
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].obj_index = len(WS.DT[win].object_list)-1
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].type = "text"
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].col = WS.DT[win].ACT_COLOR
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].text = "some stabd in text"
    WS.DT[win].object_list[len(WS.DT[win].object_list)-1].object = WS.DT[win].canvas.canvas.create_text(x, y, 
                                                                                text= WS.DT[win].object_list[len(WS.DT[win].object_list)-1].text, 
                                                                                fill="black", 
                                                                                font=('Helvetica 15 bold'))
   
###############################################################################

def adjust_point(event, win):
    if WS.DT[win].ACTIVE == 1: return
    x = WS.DT[win].canvas.canvas.canvasx(event.x)
    y = WS.DT[win].canvas.canvas.canvasy(event.y)        
    # to start a measurement temporarily store the coordinates where the mouse was clicked
    
    tmp = hover_over(event, win)
    
    if tmp[0] != None:     
        index = tmp[0]
        point = tmp[1]
        series = tmp[2]
        
        pos = WS.DT[win].canvas.canvas.coords(WS.DT[win].object_list[index].object)        
        WS.DT[win].canvas.canvas.delete(WS.DT[win].object_list[index].object)
        
        size = 5 # size of circle
        
        if WS.DT[win].object_list[index].type == "line":    
            if point == 1:
                WS.DT[win].object_list[index].object = WS.DT[win].canvas.canvas.create_line(x, y,
                                                                            pos[2],pos[3],
                                                                            fill=WS.DT[win].ACT_COLOR, 
                                                                            width=WS.DT[win].L_WIDTH,
                                                                            arrow=tk.BOTH,
                                                                            arrowshape = WS.DT[win].line_cap)
                p1 = absolute(x, y, win)
                WS.DT[win].object_list[index].x1 = p1[0]
                WS.DT[win].object_list[index].y1 = p1[1]
                
                px_distance = math.dist((x, y), 
                                        (pos[2],pos[3])) * (1/WS.DT[win].canvas.imscale)
                WS.DT[win].object_list[index].px_distance = px_distance
                WS.DT[win].object_list[index].abs_distance = WS.DT[win].object_list[index].px_distance * WS.DT[win].object_list[index].calibration
                
            if point == 2:
                WS.DT[win].object_list[index].object = WS.DT[win].canvas.canvas.create_line(pos[0],pos[1],
                                                                            x, y,
                                                                            fill=WS.DT[win].ACT_COLOR, 
                                                                            width=WS.DT[win].L_WIDTH,
                                                                            arrow=tk.BOTH,
                                                                            arrowshape = WS.DT[win].line_cap)
                p1 = absolute(x, y, win)
                WS.DT[win].object_list[index].x2 = p1[0]
                WS.DT[win].object_list[index].y2 = p1[1]
                
                px_distance = math.dist((pos[0],pos[1]),
                                        (x, y)) * (1/WS.DT[win].canvas.imscale)
                
                WS.DT[win].object_list[index].px_distance = px_distance
                WS.DT[win].object_list[index].abs_distance = WS.DT[win].object_list[index].px_distance * WS.DT[win].object_list[index].calibration
      
            # print("seris: " + str(ST.object_list[index].series) +
            #       "\nindex: " + str(ST.object_list[index].ind))
            series_index = WS.DT[win].object_list[index].ind
            if series == "series_1":
                 WS.DT[win].SERIES_1[series_index] =  WS.DT[win].object_list[index]
            if series == "series_2":
                 WS.DT[win].SERIES_2[series_index] =  WS.DT[win].object_list[index]
            if series == "series_3":
                 WS.DT[win].SERIES_3[series_index] =  WS.DT[win].object_list[index]
            
            WS.DT[win].canvas.canvas.delete(WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label)
            coords = WS.DT[win].canvas.canvas.coords(WS.DT[win].object_list[len(WS.DT[win].object_list)-1].object)
            label_x = (coords[0] + coords[2]) / 2 + WS.DT[win].lab_x_off
            label_y = (coords[1] + coords[3]) / 2 + WS.DT[win].lab_y_off
            WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label = WS.DT[win].canvas.canvas.create_text(label_x, label_y,
                                                                                        text= WS.DT[win].object_list[len(WS.DT[win].object_list)-1].label_text, 
                                                                                        fill="black", 
                                                                                        font=('Helvetica 15 bold'))
           
        
        if WS.DT[win].object_list[index].type == "dot":
            
            WS.DT[win].object_list[index].object = WS.DT[win].canvas.canvas.create_oval(x - size, y - size, 
                                                                        x + size, y + size, 
                                                                        fill = WS.DT[win].ANNOTE_COL)
            p1 = absolute(x, y, win)
            WS.DT[win].object_list[index].x1 = p1[0] - size
            WS.DT[win].object_list[index].y1 = p1[1] - size
            WS.DT[win].object_list[index].x2 = p1[0] + size
            WS.DT[win].object_list[index].y2 = p1[1] + size
    
        if WS.DT[win].object_list[index].type == "text":
            WS.DT[win].object_list[index].object = WS.DT[win].canvas.canvas.create_text(x, y, 
                                                                        text= WS.DT[win].object_list[index].text, 
                                                                        fill=WS.DT[win].ANNOTE_COL, 
                                                                        font=('Helvetica 15 bold'))
            p1 = absolute(x, y, win)
            WS.DT[win].object_list[index].x1 = p1[0] 
            WS.DT[win].object_list[index].y1 = p1[1] 
            WS.DT[win].object_list[index].x2 = p1[0] 
            WS.DT[win].object_list[index].y2 = p1[1] 
        
###############################################################################
def load_the_data(data):
    # check if the data is the correct format
    names = list(data.columns)
    
    correct = ["x1","y1","x2", "y2", "mode","series", "ob_type", "ind", "text", 
                "px_distance", "abs_distance",	"calibration",	"calibrated",	
                "label_text",	"year",	"dated", "col"]
    
    for i in range(len(correct)):
        if names[i] != correct[i]:
            ST.error_frame.label.configure(text = "The loaded file is not \n" +
                                                    "the correct structure \n" +
                                                    "and cannot be loaded")
            ST.error_frame.toggle()
            return     
    # if it is the correct format - load the data
    for i in range(data.shape[0]):
        tmp = data.iloc[i]
        p1 = convert_to_canvas(tmp["x1"],tmp["y1"])
        p2 = convert_to_canvas(tmp["x2"],tmp["y2"])
        
        ST.object_list.append(canvas_object(p1[0], p1[1],
                                            p2[0], p2[1],
                                            tmp["mode"], 
                                            tmp["series"],
                                            tmp["ind"]        
                                            ))
        N = len(ST.object_list)-1
        
        ST.object_list[N].object = None
        ST.object_list[N].type = tmp["ob_type"]
        ST.object_list[N].text = tmp["text"]
        ST.object_list[N].px_distance = tmp["px_distance"]
        ST.object_list[N].abs_distance = tmp["abs_distance"]
        ST.object_list[N].calibrated = tmp["calibrated"]      
        ST.object_list[N].calibration =  tmp["calibration"]
        ST.object_list[N].label_text =  tmp["label_text"]
        ST.object_list[N].year =  tmp["year"]      
        ST.object_list[N].dated =  tmp["dated"]
        ST.object_list[N].col =  tmp["col"]
        
        # print("check type = " + ST.object_list[N].type)
        if ST.object_list[N].type == "line":
            ST.object_list[N].object = ST.canvas.canvas.create_line(ST.object_list[N].x1, ST.object_list[N].y1,
                                                                    ST.object_list[N].x2, ST.object_list[N].y2,
                                                                    fill = ST.object_list[N].col, 
                                                                    width = ST.L_WIDTH,
                                                                    arrow=tk.BOTH,
                                                                    arrowshape = ST.line_cap)
        if ST.object_list[N].mode == "measure":            
            ST.object_list[N].label = ST.canvas.canvas.create_text(ST.object_list[N].x1, ST.object_list[N].y1,
                                                                    text = ST.object_list[N].label_text, 
                                                                    fill = "black", 
                                                                    font = ('Helvetica 15 bold'))
            
        if ST.object_list[N].type == "dot":
            ST.object_list[N].object = ST.canvas.canvas.create_oval(ST.object_list[N].x1, ST.object_list[N].y1,
                                                                    ST.object_list[N].x2, ST.object_list[N].y2, 
                                                                    fill = ST.object_list[N].col)
        if ST.object_list[N].type == "text":    
            ST.object_list[N].object = ST.canvas.canvas.create_text(ST.object_list[N].x1, ST.object_list[N].y1,
                                                                    text = ST.object_list[N].text, 
                                                                    fill = ST.object_list[N].col, 
                                                                    font = ('Helvetica 15 bold'))

###############################################################################
    
def add_to_series(win):
    if len(WS.DT[win].object_list) == 0: return

    if WS.DT[win].object_list[len(WS.DT[win].object_list) - 1].series == "series_1":
        WS.DT[win].SERIES_1.append(WS.DT[win].object_list[len(WS.DT[win].object_list) - 1])
    
    if WS.DT[win].object_list[len(WS.DT[win].object_list) - 1].series == "series_2":
        WS.DT[win].SERIES_2.append(WS.DT[win].object_list[len(WS.DT[win].object_list) - 1])
    
    if WS.DT[win].object_list[len(WS.DT[win].object_list) - 1].series == "series_3":
        WS.DT[win].SERIES_3.append(WS.DT[win].object_list[len(WS.DT[win].object_list) - 1])
    
    if WS.DT[win].object_list[len(WS.DT[win].object_list) - 1].series == "insert":
        WS.DT[win].INSERT_SERIES.append(WS.DT[win].object_list[len(WS.DT[win].object_list) - 1])    
    
###############################################################################

def get_points(event, value, win):
    
    if value != "none":
               
        WS.DT[win].M1 = [value[2], value[0]]
        ring_no = WS.DT[win].object_list[value[0]].ind
        WS.DT[win].insert_frame.M1_label2.configure(text = "Increment selected: " + str(WS.DT[win].M1[0]) + " Ring: " +  str(ring_no))
        WS.DT[win].ACTIVE = -1    
    
# def update_index():    
#     for i in range(len(ST.object_list)):
#         ST.object_list[i].obj_index = i
    
def sort_object_list(win):
    tmp_ser_1 = []
    tmp_ser_2 = []
    tmp_ser_3 = []
    tmp_anno = []
    combined = []
    
    for i in range(len(WS.DT[win].object_list)):    
        if WS.DT[win].object_list[i].mode == "measure" and WS.DT[win].object_list[i].series == "series_1":
            tmp_ser_1.append(WS.DT[win].object_list[i])
        if WS.DT[win].object_list[i].mode == "measure" and WS.DT[win].object_list[i].series == "series_2":
            tmp_ser_2.append(WS.DT[win].object_list[i]) 
        if WS.DT[win].object_list[i].mode == "measure" and WS.DT[win].object_list[i].series == "series_3":
            tmp_ser_3.append(WS.DT[win].object_list[i])
        if WS.DT[win].object_list[i].mode == "anno":
            tmp_anno.append(WS.DT[win].object_list[i])
                       
    if len(tmp_ser_1) > 0:
        tmp_ser_1 = set_order(tmp_ser_1)         
        combined = combined + tmp_ser_1 
    if len(tmp_ser_2) > 0:
        tmp_ser_2 = set_order(tmp_ser_2)
        combined = combined + tmp_ser_2 
    if len(tmp_ser_3) > 0:
        tmp_ser_3 = set_order(tmp_ser_3)
        combined = combined + tmp_ser_3   
    if len(tmp_anno) > 0:    
        combined = combined + tmp_anno         
    
    WS.DT[win].object_list = combined
    
def set_order(tmp_series):
    if len(tmp_series) != 0:
        ordered = [None] * len(tmp_series)
        for i in range(len(ordered)):
            for j in range(len(tmp_series)):
                if tmp_series[j].ind == i:
                    ordered[i] = tmp_series[j]                    
        return ordered
    
def restart():    
    if ST.canvas != None:
        ST.restart_frame.show()
    else:
        ST.restart_frame.confirm_restart()
        

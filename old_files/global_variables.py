# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:52:34 2023

@author: david
"""
def init():
        
    global test_num
    test_num = "settings loaded to CVI"
    
    global dir_label, DIRECTORY, filename, mask_path 
    global canvas, TOP_LEFT, sample         
    dir_label = None
    DIRECTORY = None # the directory for the multi image AI process
    dir_label = None
    filename = None # image filename
    mask_path = None # path to growth axis mask for AI model
    canvas = None # the canvas object where everything will happen
    TOP_LEFT = None # object to store the position of the top left corner of the canvas
    sample = None # get the sample name - extracted from the filename

    global object_list
    object_list = [] # a list of all things put on the canvas


    global MODE, act_mod_txt_label
    MODE = "measure" # what mode is the app in?]
    act_mod_txt_label = MODE

    global ACTIVE
    ACTIVE = -1 # toggle between -1/1 if a line is being drawn

    global TMP, TMP_LINE
    TMP = None # hold the coordinates of the first part of the line being drawn before it gets stored properly
    TMP_LINE = None # A temporaruy line before it can be stored in the right place

    global FT_SZ    
    FT_SZ = 22

    global L_WIDTH, L_COL
    global ser_1_col, ser_2_col, ser_3_col
    global insert_col, AI_col, ACT_COLOR
    L_WIDTH = 5 # how wide are the lines?
    L_COL = "green" # what colour are the measurement lines?
    
    ACT_COLOR = "#ff8400"
    ser_1_col = "#ff8400"
    ser_2_col = "#00bd0d"
    ser_3_col = "#9c00ff"
    insert_col = "black"
    AI_col = "orange"

    global ANNOTE_COL, active_col, PROXIMITY
    ANNOTE_COL = "yellow" # what colour are the annotation?
    active_col = "red" # colourof active measurement line
    PROXIMITY = 15 # how close to the points do you need to be to select them
    
    global lab_x_off, lab_y_off
    lab_x_off = 0
    lab_y_off = 0
    
    #line caps
    global line_cap_len, line_cap_thickness, line_cap
    line_cap_len = 25
    line_cap_thickness = 5
    line_cap = (line_cap_thickness, 0, line_cap_len)

    # when inserting measurements select the measurements to insert between
    global IN_CONFIRM, M1_label_text, M1
    IN_CONFIRM = False # sets whether the increment has been selected
    #GETTING_POINTS = -1 #toggle between -1 and 1 when clicking the first and second point
    M1_label_text = [] # will contain the text leabel in the insert frame]
    M1 = [0] # get index of the first point
      
    global SERIES, TMP_SERIES, SERIES_1, SERIES_2, SERIES_3, INSERT_SERIES, MEAN_SERIES
    SERIES = []
    TMP_SERIES = [] # will be used when modifying a series to insert the extra lines
    SERIES_1 = [] # contains the data for each of the measurement series
    SERIES_2 = []
    SERIES_3 = []
    INSERT_SERIES = [] #the series to use to hold measurements that are to be inserted
    MEAN_SERIES = [] # arithmetic mean of series 1-3 # not currently used   
    
    global prev_series, ACT_SER
    prev_series = "series_1" # Will contain the name ofthe series previously masured
    ACT_SER = "series_1"

    global ANNOTATIONS, GROWTH_LINE
    ANNOTATIONS = [] # store all the annotations here
    GROWTH_LINE = []
    
    #FULL_SIZE = None 
    
    global CALIBRATED, CALIBRATION, sb_length, calibration_SF
    CALIBRATED = False
    CALIBRATION = None
    calibration_SF = 1
    sb_length = 0 # length of the scale bar
    
    # toggles
    global toggle_labels
    toggle_labels = 1
####################################################################
    # FRAMES #####       
    global starting_menu, insert_frame, toolbar
    global settings_frame, annotate_frame, AI_frame
    global multi_AI_frame, AI_results_frame, calib_frame
    global winframe, results, holder_frame, error_frame 
    global help_window, restart_frame 
    holder_frame = None
    error_frame = None
    starting_menu = None
    insert_frame = None # window for showing inseret new measurements options
    toolbar = None
    settings_frame = None
    annotate_frame = None
    AI_frame = None # placeholder for the AI frame 
    multi_AI_frame = None
    AI_results_frame = None
    calib_frame = None
    winframe = None
    results = None
    help_window = None
    restart_frame = None
    ### Labels
    global active_ser_label
    active_ser_label = None # this will be label that contains the active series text
    
    ### Settings menu entry boxes
    global ser1_col_entry, ser2_col_entry, ser3_col_entry
    global insert_col_entry, active_col_entry, line_thick_value
    global proximity_value, lab_x_off_value, lab_y_off_value
    global line_cap_thick_value, line_end_cap_value    
    ser1_col_entry = None
    ser2_col_entry = None
    ser3_col_entry = None
    insert_col_entry = None
    active_col_entry = None
    line_thick_value = None
    proximity_value = None
    lab_x_off_value = None
    lab_y_off_value = None
    line_cap_thick_value = None
    line_end_cap_value = None
    
    #test = None
#############################################################    
    ### Annotation stuff
    global anno_frame, Anno_text, anno_type, show_anno
    anno_frame = None
    Anno_text = None
    anno_type = "line"
    show_anno = -1

    #### AI stuff
    global selected_model, tmp_points, AI_MODE, AI_insert_pos
    selected_model = "final_model"
    tmp_points = []
    AI_MODE = "delete" 
    AI_insert_pos = None
    
    ### crossdating stuff
    global start_year
    start_year = 1
    
# Commonly used Variables and Constants in another script to avoid clutter
# License: http://creativecommons.org/licenses/by-sa/3.0/
#
# Brian Acosta
# July 5 2017
#
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import glob
import json
import tkinter as tk
from tkinter import ttk

# Font constants
LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Helvetica', 10)
SMALL_FONT = ('Helvetica', 8)

def popUpMsg(msg):
    popup = tk.Tk()
    tk.Tk.wm_title(popup, '!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    popup.mainloop()

# Function in progress, not really sure how to pass parameters for graph settings
def graph_settings(figure):
    popup = tk.Tk()
    tk.Tk.wm_title(popup, '!')
    
    label = ttk.Label(popup, text='Graph Settings Page', font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    
    popup.mainloop()
    
        
    return ('hist', 'times')

# returns a dictionary of 'run_id':('json_File_Name', 'Label Text')    
def json_dict():
    json_names = glob.glob('*.json')
    run_ids = json_names[:]
    
    for i in range(len(run_ids)):
        run_ids[i] = run_ids[i].strip('.json')
    
    labels = []
    
    for id in run_ids:
        try:
            int(id)
        except:
            run_ids.pop(id)
            json_names.pop('%s.json' %id)
            continue
        
        labels.append(run_id_to_label(id))
        
    j_dict = {}
    
    for i in range(len(json_names)):
        j_dict[run_ids[i]] = (json_names[i], labels[i])
        
    return j_dict
    
def run_id_to_label(id):
    
    year = id[0:4]
    month = num2month(int(id[4:6]))
    day = id[6:8]
    run_num = id[8:10]
    
    return '%s %s, %s, Run #%s' %(month, day, year, run_num)
    
def num2month(month):
    months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 
            'Sep.', 'Oct.', 'Nov.', 'Dec.']
    return months[month - 1]
        
    
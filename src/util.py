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


LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Helvetica', 10)
SMALL_FONT = ('Helvetica', 8)

def graph_settings(figure):
    popup = tk.Tk()
    tk.Tk.wm_title(popup, '!')
    
    label = ttk.Label(popup, text='Graph Settings Page', font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    
    return ('hist', 'times')
    
    popup.mainloop()
    
def json_dict():
    
# GUI Data explorer application for Grand Prix data management
#
# License: http://creativecommons.org/licenses/by-sa/3.0/
# The GUI Framework was derived from https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/	
# 
# Brian Acosta
# July 5 2017
from util import LARGE_FONT, SMALL_FONT, NORM_FONT, graph_settings, json_dict
import glob
import json
import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

def popUpMsg(msg):
    popup = tk.Tk()
    tk.Tk.wm_title(popup, '!')
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Okay', command=popup.destroy)
    B1.pack()
    popup.mainloop()

def save_setup(entries, entry_list):
    
    data = {}
    
    # F = Field (dictionary key), E = ttk Entry object
    for key in entries:
        inStr = entries[key].get()
        
        # make sure all fields are filled out
        if len(inStr) == 0:
            popUpMsg('Please Fill Out All Fields')
            return
        
        # add field entry to data{}
        try:
            data[key] = int(inStr)
        except ValueError:
            try:
                data[key] = float(inStr)
            except ValueError:
                data[key] = inStr
        
    data['run_id'] = data['Run Number'] + 100 * data['Day'] + 10000 * data['Month'] + 1000000 * data['Year']
    data['tags'] = []
    data['times'] = []
    
    # Write data to a json file
    if len(glob.glob('%d.json' %data['run_id'])) > 0:
        popUpMsg('Data for this setup already exists')
        return
    try:
        with open('%d.json' %data['run_id'], 'w') as json_file:
            json.dump(data, json_file)
    except:
        popUpMsg('Failed to save data')
        return
    
    popUpMsg('Success!')
    
    #TODO: Find appropriate 'CLEAR' method for Entry ttk object
    
    # for i in range(len(entry_list)):
        # entry_list[i].

########################################
### Application Parent Window
########################################   
class GrandPrixDataManager(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        #initialize a Tk instance as the main controller
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        tk.Tk.wm_title(self, 'Grand Prix Data Manager')
        
        # Container is the parent frame for all ohter frames in the program
        container = tk.Frame(self)
        
        container.pack(side='top', fill='both', expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Create a dictionary to hold all of the frames in the program
        self.frames = {}
        
        for F in (StartPage, DataEntry, GraphsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky ='nsew')
        
        self.show_frame(StartPage)
    
    # Brings the appropriate frame to the top
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

########################################
### Start Page
########################################    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        
        data_entry_button = ttk.Button(self, text='Enter Data',
                            command=lambda: controller.show_frame(DataEntry))
        data_entry_button.pack()
        
        graphs_button = ttk.Button(self, text='View Graphs',
                            command=lambda: controller.show_frame(GraphsPage))
        graphs_button.pack()
        
        quit_button = ttk.Button(self, text='Quit', command=lambda: quit())
        quit_button.pack()
        

#######################################
### Data Entry Page
######################################## 
class DataEntry(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Data Entry Wizard', font=LARGE_FONT)
        label.grid(row=0)
        
        self.string_vars = {}
        self.ent_list =[]
        
        # add labeled entry fields for data
        r = 2
        for Field in ('Day', 'Month', 'Year', 'Run Number', 'Front PSI', 'Rear PSI', 
                      'Clutch RPM', 'Carb Temp', 'Track Temp', 'Driver'):
            label = ttk.Label(self, text=Field, font=SMALL_FONT).grid(row=r, column=0)
            self.string_vars[Field] = tk.StringVar()

            entry = ttk.Entry(self, textvariable=self.string_vars[Field])
            self.ent_list.append(entry)
            entry.grid(row=r, column=1)
            r += 1
        
        # Add navigation back to StartPage
        button = ttk.Button(self, text='Home',
                            command=lambda: controller.show_frame(StartPage))
        
        button.grid(row=r+1)
        
        # Add button to save data entries
        save = ttk.Button(self, text='Save', 
                        command=lambda: save_setup(self.string_vars, self.ent_list))
        save.grid(row=r+1, column=1)



########################################
### Graph Viewing Page
########################################         
class GraphsPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Graphs Page', font=LARGE_FONT)
        label.pack()
        
        home_button = ttk.Button(self, text='Home', 
                            command=lambda: controller.show_frame(StartPage))
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        
        settings_button = ttk.Button(self, text='Graph Settings', 
                                    command=lambda: graph_settings(a))
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        settings_button.pack()
        home_button.pack()

################################################################################   
app = GrandPrixDataManager()
app.mainloop()
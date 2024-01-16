import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import os

import serial.tools.list_ports
from DB import DB
from Com import Com
import Icon


class App(ttk.Window):
    def __init__(self, theme = 'minty'):
        super().__init__(theme)
        self.title('Machine Controller')

        # Sizing and placing Window
        window_width = 700
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        left = int(screen_width/2 - window_width/2)
        top = int(screen_height/2 - window_height/2)
        
        self.geometry(f"{window_width}x{window_height}+{left}+{top-40}")

        self.resizable(False, False)

        # Commands to get the image of the icon.
        icon = Icon.getIcon()
        img = tk.PhotoImage(data=icon)
        self.tk.call('wm', 'iconphoto', self._w, img)


        # Widgets
        self.mainFrame = Main(self)


        # run
        self.mainloop()
        
        try:
            prevState = self.mainFrame.com.getData()
            self.mainFrame.com.sendData([0, 0, 0])
            user = os.getlogin()
            self.mainFrame.dBase.checkConnection()
            print(prevState)

            # Inserting statements for three tables if user closes the window.
            if(prevState[0] != 0):
                self.mainFrame.dBase.insertData("TrainerKit", user, 0)
            if(prevState[1] != 0):
                self.mainFrame.dBase.insertData("DSO", user, 0)
            if(prevState[2] != 0):
                self.mainFrame.dBase.insertData("Supply", user, 0)
        except:
            print('CONNECTION HALTED!')

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.5, rely = 0.5, relwidth=0.97, relheight=0.97, anchor='center')
        self.initialLayout()
        self.screen1()
        try:
            self.dBase = DB()
            print("Successfully connected to database.")
        except:
            print('Not Able to connect to databse!')

    def initialLayout(self):
        # Widgets
        user = User(self)

        # Layout
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
        self.columnconfigure((0, 2), weight=1, uniform='a')
        self.columnconfigure(1, weight=4, uniform='a')
        
        # ttk.Label(self, background='red').grid(row = 0, column = 0, sticky='nswe')
        # ttk.Label(self, background='red').grid(row = 0, column = 2, sticky='nswe')
        
        ttk.Separator(self, orient = 'horizontal').grid(row = 1, column = 1, sticky = 'we')
        user.grid(row = 0, column = 1, sticky='nswe')

    def getPorts(self):
        lst = []
        ports = serial.tools.list_ports.comports()

        for i, j, k in sorted(ports):
            if('USB Serial Device' in j):
                lst.append(i)       
        
        return lst
    
    def screen1(self):        # Initial screen of the Application.
        global combo
        global connectButton
        global portLabel

        lst = self.getPorts()   # Updating the ports list.
        
        selected = tk.StringVar()
        combo = ttk.Combobox(
            self, 
            textvariable = selected, 
            state = 'readonly', 
            bootstyle = 'primary'
        )
        combo['values'] = lst
        
        portLabel = ttk.Label(
            self, 
            text = 'Choose the port', 
            anchor='center', 
            font='Calibri 15'
        )

        def connect():
            combo.grid_forget()
            portLabel.grid_forget()
            self.com = Com(selected.get())
            self.screen2()

        self.connectButton = ttk.Button(
            self, 
            text="CONNECT",
            command = connect,
            bootstyle = 'outline',
            state='disabled'
        )
        
        
        portLabel.grid(row = 2, column=1, sticky='nsew')
        combo.grid(row = 3, column = 1, sticky='n')
        self.connectButton.place(relx = 0.5, rely = 0.9, anchor = 'center')


        def updateVal(event):
            combo['values'] = self.getPorts()
            return 
        
        combo.bind('<Button-1>', updateVal)
        combo.bind('<<ComboboxSelected>>', lambda event: self.connectButton.config(state = 'enabled'))
    
    def screen2(self):        # Main screen of the App.

        # Initializing Widgets        
        kit = Machine(self, 'DC Trainer Kit')
        kVal = kit.radio.value
        dso = Machine(self, 'DSO')
        dVal = dso.radio.value
        supply = Machine(self, 'DC Supply')
        sVal = supply.radio.value

        def submitFunc():
            prevState = self.com.getData()
            user = os.getlogin()
            kitV = kVal.get()
            dsoV = dVal.get()
            supplyV = sVal.get()
            self.com.sendData([kitV, dsoV, supplyV])
            self.dBase.checkConnection()
            print(prevState)
            # INSERT THE INSERTING COMMAND OF DATABASE
            if(prevState[0] != kitV):
                self.dBase.insertData("TrainerKit", user, kitV)
            if(prevState[1] != dsoV):
                self.dBase.insertData("DSO", user, dsoV)
            if(prevState[2] != supplyV):
                self.dBase.insertData("Supply", user, supplyV)
        
        self.connectButton['text'] = 'Submit'
        self.connectButton['command'] = submitFunc

        # Layout
        kit.grid(row = 2, column = 1, sticky='nswe')
        dso.grid(row = 3, column = 1, sticky='nswe')
        supply.grid(row = 4, column = 1, sticky='nswe')

class User(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        # Packing
        self.user(os.getlogin()).pack(expand=True, pady = (20, 0), ipadx = 4, ipady=4)

    def user(self, name):
        user = ttk.Label(
        self, 
        text = f'Hello {name}!', 
        font = 'Calibri 24 bold',
        bootstyle = 'inverse-',
        anchor='center'
        )
        
        return user

class Machine(ttk.Frame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.radio = Radio(self)
        self.label(name).place(x = 40, y = 0)
        self.radio.place(relx = 1, rely = 0, anchor = 'ne')

    def label(self, name):
        label = ttk.Label(
            self,
            text = name,
            font = 'Calibri 15'
        )
        return label
    
class Radio(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.value = tk.IntVar(value = 0)

        self.button('ON', 1).pack(side = 'left', expand = True, padx=(0, 15))
        self.button('OFF', 0).pack(side = 'left', expand = True, padx = (15, 40))

    def button(self, state, value):
        button = ttk.Radiobutton(
            self, 
            text = state, 
            value = value, 
            variable = self.value,
            bootstyle = 'toolbutton-success'
        )
        return button

App()
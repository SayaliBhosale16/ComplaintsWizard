import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import time
from datetime import datetime

from VAdminComplaint import *

class VAdminPassword(tk.Toplevel):
    # def __init__(self, parent, vInfo):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.master = parent

        # self.vInfo = vInfo

        ## setup stuff goes here
        self.geometry("551x550+250+35")
        self.configure(bg='#d9e6f2')
        self.title("Admin Password")

        self.fontStyle = tkFont.Font(family="Lucida Grande", size=12)
        self.fontStyleBold = tkFont.Font(family="Lucida Grande", size=12, weight='bold')

        #date time
        #datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        now = datetime.now().strftime("%d %B %Y %I:%M%p")
        self.dttm = tk.Label(self, text=now, bg='#d9e6f2', font=self.fontStyle, width=25)
        self.dttm.place(x =325, y = 2, anchor=tk.NW)

        self.fontStyleMessages = tkFont.Font(family="Lucida Grande", size=18, weight='bold')
        self.fontStyleHeader = tkFont.Font(family="Lucida Grande", size=16, weight='bold')

        #Message1 Label
        msg1Label = "Complaint Systems"
        self.lblMsg1 = tk.Label(self, text=msg1Label, bg='#d9e6f2', font=self.fontStyleMessages, width=24, anchor=tk.W, justify=tk.LEFT)
        self.lblMsg1.place(x =15, y = 2, anchor=tk.NW)

        txtRegComplaint = "Enter Password"
        self.lblRegComplaint = tk.Label(self, text=txtRegComplaint, bg='#d9e6f2', font=self.fontStyleBold, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblRegComplaint.place(x =14, y = 45, anchor=tk.NW)

        #Header Label
        # header1Label = "Entry Password"
        # lblHeader1 = tk.Label(self, text=header1Label, bg='white', fg='grey', font=self.fontStyleHeader, width=33)
        # lblHeader1.place(x =0, y = 40)

        self.strPassword = tk.StringVar() 
        txtPassword = tk.Entry(self, textvariable=self.strPassword, show='*', width=27, font=self.fontStyle, bg='#d7e8fc') 
        txtPassword.place(x =100, y = 75)
        txtPassword.focus_set()

        self.fontStyleMessages = tkFont.Font(family="Lucida Grande", size=16)

        #Message1 Label
        self.lblMsg1 = tk.Label(self, text="", font=self.fontStyleMessages, anchor=tk.W, bg='#d9e6f2')
        self.lblMsg1.place(x =20, y = 180, anchor=tk.NW)

        btnOk = tk.Button(self, text = "OK", width=15, command = self.check_password) 
        btnOk.place(x =100, y = 270)

        # btnCancel = tk.Button(self, text = "Close", width=15, command = self.close_window) 
        # btnCancel.place(x =265, y = 270)

        btnMessage = " Close "
        buttonSettings = tk.Button(self, text=btnMessage, width=14, command = self.close_window)
        buttonSettings.place(x =425, y = 500)

    def check_password(self):
        if(self.strPassword.get() == "admin"):
            self.lblMsg1.config(text = "Password Valid")
            windowAdminComplaint = VAdminComplaint(self)
        else:
            self.lblMsg1.config(text = "Incorrect Password")

    def close_window(self):
        self.destroy()

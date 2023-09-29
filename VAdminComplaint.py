import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import time
from datetime import datetime
import sqlite3

class VAdminComplaint(tk.Toplevel):
    # def __init__(self, parent, vInfo):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.master = parent

        # self.vInfo = vInfo

        ## setup stuff goes here
        self.geometry("551x550+250+35")
        self.configure(bg='#d9e6f2')
        self.title("Manage Complaint")

        self.fontStyle = tkFont.Font(family="Lucida Grande", size=12)
        self.fontStyleBold = tkFont.Font(family="Lucida Grande", size=12, weight='bold')

        #date time
        #datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        now = datetime.now().strftime("%d %B %Y %I:%M%p")
        self.dttm = tk.Label(self, text=now, bg='#d9e6f2', font=self.fontStyle, width=25)
        self.dttm.place(x =325, y = 2, anchor=tk.NW)

        self.fontStyleMessages = tkFont.Font(family="Lucida Grande", size=18, weight='bold')

        #Message1 Label
        msg1Label = "Complaint Systems"
        self.lblMsg1 = tk.Label(self, text=msg1Label, bg='#d9e6f2', font=self.fontStyleMessages, width=24, anchor=tk.W, justify=tk.LEFT)
        self.lblMsg1.place(x =15, y = 2, anchor=tk.NW)

        btnMessage = " Close "
        buttonSettings = tk.Button(self, text=btnMessage, width=14, command = self.close_window)
        buttonSettings.place(x =425, y = 500)

        btnMessage = " < "
        self.btnPrev = tk.Button(self, text=btnMessage, width=3, command = self.output_prev)
        self.btnPrev.place(x =375, y = 45)

        #Message Count Label
        self.lblCount = tk.Label(self, text="0", bg='#d9e6f2', font=self.fontStyleBold, width=38, anchor=tk.W, justify=tk.LEFT)
        self.lblCount.place(x =440, y = 45, anchor=tk.NW)

        btnMessage = " > "
        self.btnNext = tk.Button(self, text=btnMessage, width=3, command = self.output_next)
        self.btnNext.place(x =500, y = 45)

        self.lblMsgDetails1 = tk.Label(self, text="Select Department", bg='#d9e6f2', font=self.fontStyleBold, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblMsgDetails1.place(x =15, y = 45, anchor=tk.NW)

        result = []
        result.append("PWD")
        result.append("Water Supply")
        result.append("Electricity")
        result.append("Sewage")
        result.append("Other")
        self.n = tk.StringVar() 
        self.selectDept = ttk.Combobox(self, width = 14, textvariable = self.n) 
        self.selectDept.place(x =170, y = 47)
        self.selectDept['values'] = result
        print("select default")
        self.selectDept.current(0)

        self.btnSearch = tk.Button(self, text="Search", command = self.search_complaints)
        self.btnSearch.place(x =280, y = 45)

        self.UIComplaintStatus()

    def UIComplaintStatus(self):
        # txtRegComplaint = "Complaint Status"
        # self.lblRegComplaint = tk.Label(self, text=txtRegComplaint, bg='#d9e6f2', font=self.fontStyleBold, width=18, anchor=tk.W, justify=tk.LEFT)
        # self.lblRegComplaint.place(x =565, y = 45, anchor=tk.NW)

        # self.strComplaintIDForSearch = tk.StringVar() 
        # txtComplaintIDForSearch = tk.Entry(self, textvariable=self.strComplaintIDForSearch, font=self.fontStyle) 
        # txtComplaintIDForSearch.place(x =725, y = 47, width=100, height=26)
        # # txtComplaintIDForSearch.focus_set()

        # btnSearchComplaint = tk.Button(text="Search", width=14, command = self.search_complaint)
        # btnSearchComplaint.place(x =830, y = 47)

        self.lblComplaint = tk.Label(self, text="Complaint", bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaint.place(x =14, y = 75, anchor=tk.NW)

        self.lblComplaintDetails = tk.Label(self, text="", bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.NW, justify=tk.LEFT)
        self.lblComplaintDetails.place(x =159, y = 75, anchor=tk.NW, height=112, width=370)

        self.lblAddress = tk.Label(self, text="Address", bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblAddress.place(x =14, y = 205, anchor=tk.NW)

        self.lblAddressDetails = tk.Label(self, text="", bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.NW, justify=tk.LEFT)
        self.lblAddressDetails.place(x =159, y = 205, anchor=tk.NW, height=112, width=370)

        self.lblComplaintNumberDetails = tk.Message(self, text="Complaint Status", bg='#d9e6f2', font=self.fontStyle, width=300, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaintNumberDetails.place(x =14, y = 340, anchor=tk.NW)

        self.lblComplaintStatus = tk.Label(self, text="", bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaintStatus.place(x =159, y = 340, anchor=tk.NW, height=34, width=133)

        # self.chkStatusVar = tk.IntVar()
        # self.chkStatus = tk.Checkbutton(self, text = "", variable = self.chkStatusVar, \
        #          onvalue = 1, offvalue = 0, height=5, \
        #          width = 5)
        # self.chkStatus.place(x =325, y = 340, anchor=tk.NW)

        self.btnCloseComplaint = tk.Button(self, text="Close & Save", width=30, command = self.close_complaint)
        self.btnCloseComplaint.place(x =305, y = 343, anchor=tk.NW)

        self.lblDateTime = tk.Message(self, text="Date Time", bg='#d9e6f2', font=self.fontStyle, width=100, anchor=tk.W, justify=tk.LEFT)
        self.lblDateTime.place(x =14, y = 390, anchor=tk.NW)

        self.lblDateTimeValue = tk.Label(self, text="", bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.W, justify=tk.LEFT)
        self.lblDateTimeValue.place(x =159, y = 390, anchor=tk.NW, height=34, width=370)

        # self.lblDept = tk.Message(self, text="Department", bg='#d9e6f2', font=self.fontStyle, width=100, anchor=tk.W, justify=tk.LEFT)
        # self.lblDept.place(x =14, y = 440, anchor=tk.NW)

        # self.lblDeptValue = tk.Label(self, text="", bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.W, justify=tk.LEFT)
        # self.lblDeptValue.place(x =159, y = 440, anchor=tk.NW, height=34, width=370)

    def search_complaints(self):
        print("search_complaints")
        self.txtDept = self.selectDept.get()
        print(self.txtDept)

        self.rowPointer = -1

        try:
            self.lblCount.config(text = "")
            self.lblDateTimeValue.config(text = "")
            self.lblComplaintDetails.config(text = "")
            self.lblAddressDetails.config(text = "")
            self.lblComplaintStatus.config(text = "")
            self.btnCloseComplaint['state']='disabled'
            self.btnPrev['state']='disabled'
            self.btnNext['state']='disabled'

            pconn  = self.db_conn_open()

            sql_read_row = "select ID , complaint_datetime , complaint_details , citizen_contact , complaint_status, derived_polarity, derived_department "
            sql_read_row = sql_read_row + " FROM complaint_reg "
            sql_read_row = sql_read_row + " WHERE derived_department = '" + self.txtDept + "' "
            sql_read_row = sql_read_row + " ORDER BY derived_polarity, complaint_datetime DESC "
            # sql_read_row = sql_read_row + " LIMIT 2 "
            # print(sql_read_row)
            self.cursor = pconn.execute(sql_read_row)
            self.result_rows = []

            flg = False
            for row in self.cursor:
                self.rowPointer = 0

                self.result_rows.append(row)

                if flg == False:
                    self.btnPrev['state']='normal'
                    self.btnNext['state']='normal'

                if str(row[4]).lower() == 'open':
                    self.btnCloseComplaint['state']='normal'

                flg = True

                # break

            print("len(result_rows)")
            print(len(self.result_rows))
            # print(self.result_rows[0])
            # print(self.result_rows[0][0])
            # print(self.result_rows[0][1])

            if flg == False:
                self.lblComplaintDetails.config(text = "No Complaints Found")
            else:
                print ("ID = " + str(self.result_rows[self.rowPointer][0]))
                print ("complaint_datetime = " + str(self.result_rows[self.rowPointer][1]))
                print ("complaint_details = " + str(self.result_rows[self.rowPointer][2]))
                print ("citizen_contact = " + str(self.result_rows[self.rowPointer][3]))
                print ("complaint_status = " + str(self.result_rows[self.rowPointer][4]))

                self.lblCount.config(text = str(self.result_rows[self.rowPointer][0]))
                self.lblDateTimeValue.config(text = str(self.result_rows[self.rowPointer][1]))
                self.lblComplaintDetails.config(text = str(self.result_rows[self.rowPointer][2]))
                self.lblAddressDetails.config(text = str(self.result_rows[self.rowPointer][3]))
                self.lblComplaintStatus.config(text = str(self.result_rows[self.rowPointer][4]))

            self.db_conn_close(pconn)
        except Exception as e: 
            print(e)

    def close_complaint(self):
        try:

            if str(self.lblComplaintStatus.cget("text")) == "Closed":
                return

            strComplaintNumber = "0" + str(self.lblCount.cget("text"))

            pconn  = self.db_conn_open()
            
            sql_update = "UPDATE complaint_reg SET " 
            sql_update = sql_update + "complaint_status = 'Closed' " 
            sql_update = sql_update + "WHERE "
            sql_update = sql_update + "ID = '" + strComplaintNumber + "' "

            self.lblComplaintStatus.config(text = 'Closed')
            pconn.execute(sql_update)
            pconn.commit()

            self.db_conn_close(pconn)

        except Exception as e: 
            print(e)

    def output_next(self):
        print("output_next")

        print(len(self.result_rows))
        # print(self.result_rows[0])
        # print(self.result_rows[0][0])
        # print(self.result_rows[0][1])

        self.btnCloseComplaint['state']='disabled'

        if len(self.result_rows) > 0:
            if self.rowPointer < len(self.result_rows)-1:
                self.rowPointer = self.rowPointer + 1

                print ("ID = " + str(self.result_rows[self.rowPointer][0]))
                print ("complaint_datetime = " + str(self.result_rows[self.rowPointer][1]))
                print ("complaint_details = " + str(self.result_rows[self.rowPointer][2]))
                print ("citizen_contact = " + str(self.result_rows[self.rowPointer][3]))
                print ("complaint_status = " + str(self.result_rows[self.rowPointer][4]))

                if str(self.result_rows[self.rowPointer][4]).lower() == 'open':
                    self.btnCloseComplaint['state']='normal'

                self.lblCount.config(text = str(self.result_rows[self.rowPointer][0]))
                self.lblDateTimeValue.config(text = str(self.result_rows[self.rowPointer][1]))
                self.lblComplaintDetails.config(text = str(self.result_rows[self.rowPointer][2]))
                self.lblAddressDetails.config(text = str(self.result_rows[self.rowPointer][3]))
                self.lblComplaintStatus.config(text = str(self.result_rows[self.rowPointer][4]))

    def output_prev(self):
        print("output_prev")

        # print(len(self.result_rows))
        # print(self.result_rows[0])
        # print(self.result_rows[0][0])
        # print(self.result_rows[0][1])

        self.btnCloseComplaint['state']='disabled'

        if len(self.result_rows) > 0:
            if self.rowPointer > 0:
                self.rowPointer = self.rowPointer - 1

                print ("ID = " + str(self.result_rows[self.rowPointer][0]))
                print ("complaint_datetime = " + str(self.result_rows[self.rowPointer][1]))
                print ("complaint_details = " + str(self.result_rows[self.rowPointer][2]))
                print ("citizen_contact = " + str(self.result_rows[self.rowPointer][3]))
                print ("complaint_status = " + str(self.result_rows[self.rowPointer][4]))

                if str(self.result_rows[self.rowPointer][4]).lower() == 'open':
                    self.btnCloseComplaint['state']='normal'

                self.lblCount.config(text = str(self.result_rows[self.rowPointer][0]))
                self.lblDateTimeValue.config(text = str(self.result_rows[self.rowPointer][1]))
                self.lblComplaintDetails.config(text = str(self.result_rows[self.rowPointer][2]))
                self.lblAddressDetails.config(text = str(self.result_rows[self.rowPointer][3]))
                self.lblComplaintStatus.config(text = str(self.result_rows[self.rowPointer][4]))

    def close_window(self):
        self.destroy()

    def db_conn_open(self):
        conn = sqlite3.connect("data/dbdata.db")
        return conn

    def db_conn_close(self, pconn):
        pconn.close()

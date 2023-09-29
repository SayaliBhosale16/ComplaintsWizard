import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import time
from datetime import datetime

import subprocess
from threading import *
import sqlite3
import sys,csv,re
from textblob import TextBlob

from VAdminPassword import *

import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords

class App(tk.Tk):
    # def __init__(self, vInfo):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()

        # self.bind('<Motion>', self.fnGetCcordinates)

        # self.vInfo = vInfo

        ## setup stuff goes here
        self.geometry("1111x550+35+35")
        self.configure(bg='#d9e6f2')
        self.title("Citizen")
        # self.resizable(False, False)
        # self.update_idletasks()
        # self.overrideredirect(True) 

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

        txtAdmin = " ADMIN "
        btnAdmin = tk.Button(text=txtAdmin, width=14, command = self.open_admin)
        btnAdmin.place(x =985, y = 10)

        self.UIRegisterComplaint()
        self.lblSeperator = tk.Label(self, text="", bg='#000000', font=self.fontStyle, wraplength=350, anchor=tk.NW, justify=tk.LEFT)
        self.lblSeperator.place(x =547, y = 50, anchor=tk.NW, height=425, width=3)
        self.UIComplaintStatus()

        btnMessage = " Exit App "
        buttonSettings = tk.Button(text=btnMessage, width=14, command = self.close_window)
        buttonSettings.place(x =985, y = 500)

        self.fontStyleItem = tkFont.Font(family="Lucida Grande", size=12)
        self.fontStyleValue = tkFont.Font(family="Lucida Grande", size=11, weight='bold')

        self.flagSerOpen = False

        self.focus_force()
        self.deiconify()

    def UIRegisterComplaint(self):
        txtRegComplaint = "Register Complaint"
        self.lblRegComplaint = tk.Label(self, text=txtRegComplaint, bg='#d9e6f2', font=self.fontStyleBold, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblRegComplaint.place(x =14, y = 45, anchor=tk.NW)

        txtComplaint = "Complaint"
        self.lblComplaint = tk.Label(self, text=txtComplaint, bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaint.place(x =14, y = 75, anchor=tk.NW)

        btnClearComplaint = tk.Button(text="Clear", width=14, command = self.clear_complaint)
        btnClearComplaint.place(x =159, y = 47)

        # self.txtComplaint = tk.Text(self, height=7, width=50)
        # self.txtComplaint.place(x =125, y = 75)
        self.txtRegComplaintTxtBox = tk.Text(self)
        self.txtRegComplaintTxtBox.place(x =125, y = 75, height=112, width=404)

        txtAddress = "Address"
        self.lblAddress = tk.Label(self, text=txtAddress, bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblAddress.place(x =14, y = 205, anchor=tk.NW)

        self.txtRegAddressTxtBox = tk.Text(self, height=7, width=50)
        self.txtRegAddressTxtBox.place(x =125, y = 205)

        btnComplaint = " SUBMIT COMPLAINT "
        btnSaveComplaint = tk.Button(text=btnComplaint, width=18, command = self.submit_complaint)
        btnSaveComplaint.place(x =230, y = 340)

        txtAddress = "Complaint\nNumber"
        self.lblAddress = tk.Message(self, text=txtAddress, bg='#d9e6f2', font=self.fontStyle, width=100, anchor=tk.W, justify=tk.LEFT)
        self.lblAddress.place(x =14, y = 390, anchor=tk.NW)

        self.var_complaintNumber=tk.StringVar()
        self.var_complaintNumber.set("_____")
        self.lblComplaintNumber = tk.Label(self, textvariable=self.var_complaintNumber, bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaintNumber.place(x =125, y = 390, anchor=tk.NW)

        self.lblDeptReg = tk.Message(self, text="Department", bg='#d9e6f2', font=self.fontStyle, width=100, anchor=tk.W, justify=tk.LEFT)
        self.lblDeptReg.place(x =14, y = 440, anchor=tk.NW)

        self.var_deptreg=tk.StringVar()
        self.var_deptreg.set("_____")
        self.lblDeptRegVal = tk.Label(self, textvariable=self.var_deptreg, bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblDeptRegVal.place(x =125, y = 440, anchor=tk.NW)

    def UIComplaintStatus(self):
        txtRegComplaint = "Complaint Status"
        self.lblRegComplaint = tk.Label(self, text=txtRegComplaint, bg='#d9e6f2', font=self.fontStyleBold, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblRegComplaint.place(x =565, y = 45, anchor=tk.NW)

        self.strComplaintIDForSearch = tk.StringVar() 
        txtComplaintIDForSearch = tk.Entry(self, textvariable=self.strComplaintIDForSearch, font=self.fontStyle) 
        txtComplaintIDForSearch.place(x =725, y = 47, width=100, height=26)
        # txtComplaintIDForSearch.focus_set()

        btnSearchComplaint = tk.Button(text="Search", width=14, command = self.search_complaint)
        btnSearchComplaint.place(x =830, y = 47)

        txtComplaint = "Complaint"
        self.lblComplaint = tk.Label(self, text=txtComplaint, bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaint.place(x =565, y = 75, anchor=tk.NW)

        txtComplaintDetails = ""
        # self.lblComplaintDetails = tk.Message(self, text=txtComplaintDetails, bg='#d9e6f2', font=self.fontStyle, width=350, anchor=tk.W, justify=tk.LEFT)
        # self.lblComplaintDetails.place(x =725, y = 75, anchor=tk.NW)
        # self.lblComplaintDetails = tk.Message(self, text=txtComplaintDetails, bg='#91f1fa', font=self.fontStyle, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaintDetails = tk.Label(self, text=txtComplaintDetails, bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.NW, justify=tk.LEFT)
        self.lblComplaintDetails.place(x =725, y = 75, anchor=tk.NW, height=112, width=370)

        txtAddress = "Address"
        self.lblAddress = tk.Label(self, text=txtAddress, bg='#d9e6f2', font=self.fontStyle, width=18, anchor=tk.W, justify=tk.LEFT)
        self.lblAddress.place(x =565, y = 205, anchor=tk.NW)

        txtAddressDetails = ""
        # self.lblAddressDetails = tk.Message(self, text=txtAddressDetails, bg='#d9e6f2', font=self.fontStyle, width=350, anchor=tk.W, justify=tk.LEFT)
        self.lblAddressDetails = tk.Label(self, text=txtAddressDetails, bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.NW, justify=tk.LEFT)
        self.lblAddressDetails.place(x =725, y = 205, anchor=tk.NW, height=112, width=370)

        txtComplaintNumberDetails = "Complaint Status"
        self.lblComplaintNumberDetails = tk.Message(self, text=txtComplaintNumberDetails, bg='#d9e6f2', font=self.fontStyle, width=300, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaintNumberDetails.place(x =565, y = 340, anchor=tk.NW)

        txtComplaintStatus = ""
        self.lblComplaintStatus = tk.Label(self, text=txtComplaintStatus, bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.W, justify=tk.LEFT)
        self.lblComplaintStatus.place(x =725, y = 340, anchor=tk.NW, height=34, width=370)

        txtDateTime = "Date Time"
        self.lblDateTime = tk.Message(self, text=txtDateTime, bg='#d9e6f2', font=self.fontStyle, width=100, anchor=tk.W, justify=tk.LEFT)
        self.lblDateTime.place(x =565, y = 390, anchor=tk.NW)

        txtDateTimeValue = ""
        # self.lblDateTimeValue = tk.Message(self, text=txtDateTimeValue, bg='#d9e6f2', font=self.fontStyle, width=425, anchor=tk.W, justify=tk.LEFT)
        self.lblDateTimeValue = tk.Label(self, text=txtDateTimeValue, bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.W, justify=tk.LEFT)
        self.lblDateTimeValue.place(x =725, y = 390, anchor=tk.NW, height=34, width=370)

        self.lblDept = tk.Message(self, text="Department", bg='#d9e6f2', font=self.fontStyle, width=100, anchor=tk.W, justify=tk.LEFT)
        self.lblDept.place(x =565, y = 440, anchor=tk.NW)

        self.lblDeptValue = tk.Label(self, text="", bg='#91f1fa', font=self.fontStyle, wraplength=350, anchor=tk.W, justify=tk.LEFT)
        self.lblDeptValue.place(x =725, y = 440, anchor=tk.NW, height=34, width=370)

    def clear_complaint(self):
        self.txtRegComplaintTxtBox.delete('1.0', tk.END)
        self.txtRegAddressTxtBox.delete('1.0', tk.END)
        self.var_complaintNumber.set("")
        self.var_deptreg.set("")

    def find_department(self, paramComplaint):
        self.department_evaluated = "Other"

        ################################################################

        movie_data = load_files(r"txt_sentoken")
        X, y = movie_data.data, movie_data.target
        print(X[0])
        X[0]=paramComplaint
        print(X[0])

        ################################################################

        documents = []

        from nltk.stem import WordNetLemmatizer

        stemmer = WordNetLemmatizer()

        for sen in range(0, len(X)):
            # Remove all the special characters
            document = re.sub(r'\W', ' ', str(X[sen]))
            
            # remove all single characters
            document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
            
            # Remove single characters from the start
            document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
            
            # Substituting multiple spaces with single space
            document = re.sub(r'\s+', ' ', document, flags=re.I)
            
            # Removing prefixed 'b'
            document = re.sub(r'^b\s+', '', document)
            
            # Converting to Lowercase
            document = document.lower()
            
            # Lemmatization
            document = document.split()

            document = [stemmer.lemmatize(word) for word in document]
            document = ' '.join(document)
            
            documents.append(document)
        # print(documents)

        ################################################################

        from sklearn.feature_extraction.text import CountVectorizer
        vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
        X = vectorizer.fit_transform(documents).toarray()
        # print(X)

        ################################################################

        from sklearn.feature_extraction.text import TfidfTransformer
        tfidfconverter = TfidfTransformer()
        X = tfidfconverter.fit_transform(X).toarray()
        # print(X)

        ################################################################

        with open('text_classifier', 'rb') as training_model:
            model = pickle.load(training_model)

        ################################################################

        print("Saved Model")

        from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

        try:
            y_pred2 = model.predict(X)

            print(y_pred2[0])

            if y_pred2[0] == 0:
                self.department_evaluated = "Electricity"
            elif y_pred2[0] == 1:
                self.department_evaluated = "Other"
            elif y_pred2[0] == 2:
                self.department_evaluated = "PWD"
            elif y_pred2[0] == 3:
                self.department_evaluated = "Sewage"
            elif y_pred2[0] == 4:
                self.department_evaluated = "Water Supply"
            else:
                self.department_evaluated = "Other"

            self.var_deptreg.set(self.department_evaluated)

        except Exception as e: 
            self.department_evaluated = "Other"

    def submit_complaint(self):

        ##########################################################

        #     Form Validation

        varText = self.txtRegComplaintTxtBox.get("1.0", "end")
        varText = str(varText)
        print("varText")
        print(varText)
        print("varText len")
        print(len(varText))
        if len(varText) < 2:
            print(len(varText))
            self.var_complaintNumber.set("Enter Complaint Details")
            return

        varText = self.txtRegAddressTxtBox.get("1.0", "end")
        varText = str(varText)
        print("varText")
        print(varText)
        print("varText len")
        print(len(varText))
        if len(varText) < 2:
            print(len(varText))
            self.var_complaintNumber.set("Enter Address Details")
            return

        ##########################################################

        #     Sentiment for Complaint sevierity
        
        varText = self.txtRegComplaintTxtBox.get("1.0", "end")
        varText = str(varText)
        analysis = TextBlob(varText)
        polarity = analysis.sentiment.polarity  # adding up polarities to find the average later
        print("polarity")
        print(polarity)
        derived_polarity = 0

        # decide ploarity/sevierity
        if (polarity == 0):  # adding reaction of how people are reacting to find average later
            derived_polarity = 0
        elif (polarity > 0 and polarity <= 0.3):
            derived_polarity = 0.3
        elif (polarity > 0.3 and polarity <= 0.6):
            derived_polarity = 0.6
        elif (polarity > 0.6 and polarity <= 1):
            derived_polarity = 1
        elif (polarity > -0.3 and polarity <= 0):
            derived_polarity = -0.3
        elif (polarity > -0.6 and polarity <= -0.3):
            derived_polarity = -0.6
        elif (polarity > -1 and polarity <= -0.6):
            derived_polarity = -1

        print("derived_polarity")
        print(derived_polarity)

        ##########################################################

        #     Find department

        varText = varText.lower()
        self.find_department(varText)
        derived_department = self.department_evaluated
        
        # derived_department = "Other"

        # varText = varText.lower()

        # if varText.find("street") > -1 or varText.find("road") > -1:
        #     derived_department = "PWD"

        # if varText.find("water") > -1 or varText.find("rain") > -1 or varText.find("river") > -1:
        #     derived_department = "Water Supply"

        # if varText.find("light") > -1 or varText.find("electr") > -1 or varText.find("power") > -1:
        #     derived_department = "Electricity"

        # if varText.find("garbage") > -1 or varText.find("shabby") > -1 or varText.find("waste") > -1:
        #     derived_department = "Sewage"

        print("derived_department")
        print(derived_department)

        try:
            pconn  = self.db_conn_open()

            sql_insert = "INSERT INTO complaint_reg ( complaint_datetime, complaint_details, citizen_contact, complaint_status, derived_polarity, derived_department) "
            sql_insert = sql_insert + "VALUES ( "
            sql_insert = sql_insert + "'" + time.strftime("%b %d %Y %I:%M%p") + "', "
            sql_insert = sql_insert + "'" + self.txtRegComplaintTxtBox.get("1.0", "end") + "', "
            sql_insert = sql_insert + "'" + self.txtRegAddressTxtBox.get("1.0", "end") + "', "
            sql_insert = sql_insert + "'Open', "
            sql_insert = sql_insert + "'" + str(derived_polarity) + "', "
            sql_insert = sql_insert + "'" + str(derived_department) + "' "
            sql_insert = sql_insert + ") "
            pconn.execute(sql_insert)
            pconn.commit()

            sql_max_row_id = "SELECT last_insert_rowid()"
            cursor = pconn.execute(sql_max_row_id)
            for row in cursor:
                print ("last_insert_rowid() = " + str(row[0]))
                complaint_id = str(row[0])
                self.var_complaintNumber.set(complaint_id)

            self.db_conn_close(pconn)
        except Exception as e: 
            print(e)

    def search_complaint(self):
        try:
            self.lblDateTimeValue.config(text = "")
            self.lblComplaintDetails.config(text = "")
            self.lblAddressDetails.config(text = "")
            self.lblComplaintStatus.config(text = "")
            self.lblDeptValue.config(text = "")

            pconn  = self.db_conn_open()

            sql_read_row = "select ID , complaint_datetime , complaint_details , citizen_contact , complaint_status, derived_polarity, derived_department "
            sql_read_row = sql_read_row + " FROM complaint_reg "
            sql_read_row = sql_read_row + " WHERE ID = '" + self.strComplaintIDForSearch.get() + "' "
            sql_read_row = sql_read_row + " ORDER BY ID DESC "
            sql_read_row = sql_read_row + " LIMIT 1 "
            print(sql_read_row)
            cursor = pconn.execute(sql_read_row)

            flg = False
            for row in cursor:
                print ("ID = " + str(row[0]))
                print ("complaint_datetime = " + str(row[1]))
                print ("complaint_details = " + str(row[2]))
                print ("citizen_contact = " + str(row[3]))
                print ("complaint_status = " + str(row[4]))

                self.lblDateTimeValue.config(text = str(row[1]))
                self.lblComplaintDetails.config(text = str(row[2]))
                self.lblAddressDetails.config(text = str(row[3]))
                self.lblComplaintStatus.config(text = str(row[4]))
                self.lblDeptValue.config(text = str(row[6]))
                
                flg = True

                break

            if flg == False:
                self.lblComplaintDetails.config(text = "Complaint ID Not Found")

            self.db_conn_close(pconn)
        except Exception as e: 
            print(e)

    def db_conn_open(self):
        conn = sqlite3.connect("data/dbdata.db")
        return conn

    def open_admin(self):
        windowPassword = VAdminPassword(self)

    def db_conn_close(self, pconn):
        pconn.close()

    def close_window(self):
        self.destroy()

    def fnGetCcordinates(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))

# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))

if __name__ == "__main__":
    # vInfo = VInfo()
    # app = App(vInfo)
    app = App()
    # app.bind('<Motion>', motion)
    app.mainloop()


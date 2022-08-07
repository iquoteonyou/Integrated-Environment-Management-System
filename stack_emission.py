import tkinter
from tkinter import messagebox
from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkcalendar import *

flag=1
check=0
class Window:
    def __init__(self,master):
        self.master = master
        self.Main = Frame(self.master)

    #widgets
        self.l1 = Label(self.Main, text="Stack Emission")
        self.l1.grid(row=0 , column = 0, padx = 5, pady = 5,columnspan = 3)


        self.date = Label(self.Main,text ="Date")
        self.date.grid(row= 1, column = 0 ,padx = 5 , pady = 5 )
        self.cal = DateEntry(self.Main , )
        self.cal.grid(row = 1 , column = 1)



        self.l2 = Label(self.Main, text = "Area")
        self.l2.grid(row = 2 , column = 0, padx = 5, pady = 5)

        Area_text = StringVar()
        self.e1 = Entry(self.Main ,textvariable = Area_text)
        self.e1.grid(row = 2, column = 1  , padx = 5, pady = 5,columnspan = 3)

        self.l3 = Label(self.Main ,  text = "Location")
        self.l3.grid(row =  3 , column = 0, padx = 5, pady = 5)

        loc_text  = StringVar()
        self.e2 = Entry(self.Main, textvariable = loc_text)
        self.e2.grid(row = 3, column = 1 , padx = 5, pady = 5,columnspan = 3)

        self.l4 = Label(self.Main,  text = "Norm( μg/Nm3)")
        self.l4.grid(row =  4, column = 0, padx = 5, pady = 5)

        norm_text = StringVar()
        self.e3 = Entry(self.Main, textvariable= norm_text)
        self.e3.grid(row = 4 , column = 1 , padx = 5, pady = 5,columnspan = 3)

        self.l5 = Label(self.Main, text = "PM(mg/Nm3)")
        self.l5.grid(row =5 , column = 0, padx = 5, pady = 5)

        PM_text = StringVar()
        self.e4 = Entry(self.Main, textvariable = PM_text )
        self.e4.grid(row = 5, column = 1, padx = 5, pady = 5,columnspan = 3)


        self.b1 = Button(self.Main, text = "Submit",command = self.insert_record)
        self.b1.grid(row = 6 , column = 1 , padx = 5 , pady = 5, sticky = "e")
        
        
        #clear
        self.B2 = Button(self.Main, text = "Clear", command = self.clear)
        self.B2.grid(row = 6, column = 2, padx = 5, pady = 5)

        self.Main.pack(padx = 5, pady = 5)
    

    #clear    
    def clear(self):
        self.e1.delete(0, 'end')
        self.e2.delete(0, 'end')
        self.e3.delete(0, 'end')
        self.e4.delete(0, 'end')

    #insertion
    def insert_record(self):
        if self.e1.get()=="" or self.e2.get()=="" or self.e3.get()=="" or self.e4.get()=="":
            tkinter.messagebox.showinfo("Confirmation","Empty Fields!")
        else:
            self.submit()    

    def connect(self):
        try:
            self.db = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        password = "123456",
                        database = "db")
 
            self.cursor = self.db.cursor()
            tkinter.messagebox.showinfo("Connection Status","database Connected")
            self.flag=0
            print("Connection Succeeded")
        except:
            tkinter.messagebox.showinfo("Connection Status","database Not Connected")
            print("Connection Failed")


    def submit(self):
            # self.onConnect()
            self.connect()
            if self.flag==0:
                sql = """INSERT INTO stack_emission (date,Area, Location, Norm, PM)
                            VALUES (%s,%s, %s, %s, %s)"""
                values = (self.cal.get(),self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())
                
                self.cursor.execute(sql, values)
                self.db.commit()
                self.onClick()
            

    def onClick(self):
            tkinter.messagebox.showinfo("Confirmation","Successful Submission")

root = Tk()
window = Window(root)
root.mainloop()


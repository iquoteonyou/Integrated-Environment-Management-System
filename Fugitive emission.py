import tkinter
from tkinter import messagebox
from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkcalendar import Calendar, DateEntry

flag=1
check=0
class Window:
    def __init__(self,master):
        self.master = master
        self.Main = Frame(self.master)

        #widgets
        self.l1 = Label(self.Main, text = "Fugitive emission (COKE OVEN)")
        self.l1.grid(row=0 , column = 0, padx = 5, pady = 5,columnspan = 3)

        self.date = Label(self.Main,text ="Date")
        self.date.grid(row= 1, column = 0 ,padx = 5 , pady = 5 )
        self.cal = DateEntry(self.Main , )
        self.cal.grid(row = 1 , column = 1)

        self.l3 = Label(self.Main,text = "Battery No.")
        self.l3.grid(row = 3 , column = 0, padx = 5 , pady = 5 )

        batt = StringVar()
        self.e3 = Entry(self.Main ,  textvariable= batt)
        self.e3.grid(row = 3 , column = 1, padx = 5 , pady = 5 ) 

        self.l4 = Label(self.Main, text = "Pa0.43 parameters")
        self.l4.grid(row = 4 ,column = 0 , padx =5 , pady = 5 ,columnspan= 3)

        self.l5  = Label(self.Main, text= "PLD(10%)")
        self.l5.grid(row = 5 ,column = 0 , padx =5 , pady = 5)

        Pld = StringVar()
        self.e5 = Entry(self.Main , textvariable= Pld)
        self.e5.grid(row = 5 , column = 1 , padx=5 , pady = 5)

        self.l6  = Label(self.Main, text= "PLL(1%)")
        self.l6.grid(row = 5 ,column = 2 , padx =5 , pady = 5)

        Pll = StringVar()
        self.e6 = Entry(self.Main , textvariable= Pll)
        self.e6.grid(row = 5 , column = 3 , padx=5 , pady = 5)

        self.l7  = Label(self.Main, text= "PLO(4%)")
        self.l7.grid(row = 6 ,column = 0 , padx =5 , pady = 5)

        Plo = StringVar()
        self.e7 = Entry(self.Main , textvariable= Plo)
        self.e7.grid(row = 6 , column = 1 , padx=5 , pady = 5)


        self.l8 = Label(self.Main, text = "Charging Emission")
        self.l8.grid(row = 7 , column = 0 , padx = 5, pady = 5 , columnspan= 3)

        self.l9 = Label(self.Main, text="Oven No.")
        self.l9.grid(row = 8 , column = 0 , padx = 5 , pady = 5)

        oven = StringVar()
        self.e9 = Entry(self.Main, textvariable= oven)
        self.e9.grid(row = 8 , column = 1, padx = 5 , pady = 5 )

        self.l10 = Label(self.Main, text="Time (in sec.)")
        self.l10.grid(row = 8 , column = 2 , padx = 5 , pady = 5)

        Time = StringVar()
        self.e10 = Entry(self.Main, textvariable= Time)
        self.e10.grid(row = 8 , column = 3, padx = 5 , pady = 5 )


        self.l11 = Label(self.Main, text="GCM Pressure (P/S)(C/S)")
        self.l11.grid(row = 9 , column = 0 , padx = 5 , pady = 5)

        GCM = StringVar()
        self.e11 = Entry(self.Main, textvariable= GCM)
        self.e11.grid(row = 9 , column = 1, padx = 5 , pady = 5 )

        self.l12 = Label(self.Main, text="Inspected By")
        self.l12.grid(row = 10 , column = 0 , padx = 5 , pady = 5)

        Ins = StringVar()
        self.e12 = Entry(self.Main, textvariable= Ins)
        self.e12.grid(row = 10, column = 1, padx = 5 , pady = 5 )


        self.b1 = Button(self.Main , text = "Submit",command = self.insert_record)
        self.b1.grid(row = 11 ,  column = 1 , padx = 5 , pady = 5 , sticky= 'e')

        #clear
        self.B2 = Button(self.Main, text = "Clear", command = self.clear)
        self.B2.grid(row = 11, column = 2, padx = 5, pady = 5)

        self.Main.pack(padx = 5, pady = 5)
#clear    
    def clear(self):
        self.e3.delete(0, 'end')
        self.e5.delete(0, 'end')
        self.e6.delete(0, 'end')
        self.e7.delete(0, 'end')
        self.e9.delete(0, 'end')
        self.e10.delete(0, 'end')
        self.e11.delete(0, 'end')
        self.e12.delete(0, 'end')

    #insertion
    def insert_record(self):
        if self.e3.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()=="" or self.e9.get()=="" or self.e10.get()=="" or self.e11.get()=="" or self.e12.get()=="":
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
        
            self.connect()
            if self.flag==0:
                sql = """INSERT INTO fugitive_emission (date,Battery_No,PLD,PLL,PLO,Oven_No,Time,GCM_Pressure,Inspected_By)
                            VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s)"""
                values = (self.cal.get(),self.e3.get(), self.e5.get(), self.e6.get(), self.e7.get(),self.e9.get(), self.e10.get(), self.e11.get(), self.e12.get())
                
                self.cursor.execute(sql, values)
                self.db.commit()
                self.onClick()
    
    
    def onClick(self):
            tkinter.messagebox.showinfo("Confirmation","Successful Submission")

root = Tk()
window = Window(root)
root.mainloop()

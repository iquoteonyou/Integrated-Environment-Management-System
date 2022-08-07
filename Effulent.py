import tkinter
from tkinter import messagebox
from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

flag=1
check=0
options = [
            "CO",
            "BPP",
            "OF-1",
            "TPP",
            "CRM"
        ]

class Window:
    
    def __init__(self,master):
        self.master = master
        self.Main = Frame(self.master)
        
        self.date = Label(self.Main,text ="Date")
        self.date.grid(row= 1, column = 0 ,padx = 5 , pady = 5 )
        self.cal = DateEntry(self.Main , )
        self.cal.grid(row = 1 , column = 1)

        self.l1 = Label(self.Main , text = "Effulent")
        self.l1.grid(row = 0 , column = 0 , padx = 5 , pady = 5 , columnspan = 3)

        self.l2 = Label(self.Main , text = "Location")
        self.l2.grid(row = 2 , column = 0 , padx = 5 , pady = 5 )
        self.c = ttk.Combobox(self.Main, value=options, width=17)
        self.c.grid(row = 2 , column = 1)
        self.c.current(0)
        
        self.l3 = Label(self.Main , text = "Oil/Grease(10.0 mg/l)")
        self.l3.grid(row = 3 , column = 0 , padx = 5 , pady = 5 )

        oilco = StringVar()
        self.e3 = Entry(self.Main ,textvariable= oilco)
        self.e3. grid(row = 3 , column = 1 , padx = 5 , pady = 5 )

        self.l4 = Label(self.Main , text = "Phenol(1.0 mg/l)")
        self.l4.grid(row = 3 , column = 2 , padx = 5 , pady = 5 )

        pheco = StringVar()
        self.e4 = Entry(self.Main ,textvariable= pheco)
        self.e4. grid(row = 3 , column = 3 , padx = 5 , pady = 5 )

        self.l5 = Label(self.Main , text = "Cyanide(0.2 mg/l)")
        self.l5.grid(row = 4 , column = 0 , padx = 5 , pady = 5 )

        cyaco = StringVar()
        self.e5 = Entry(self.Main ,textvariable= cyaco)
        self.e5. grid(row = 4 , column = 1 , padx = 5 , pady = 5 )

        self.l6 = Label(self.Main , text = "TSS(100 mg/l)")
        self.l6.grid(row = 4 , column = 2 , padx = 5 , pady = 5 )

        TSco = StringVar()
        self.e6 = Entry(self.Main ,textvariable= TSco)
        self.e6. grid(row = 4 , column = 3 , padx = 5 , pady = 5 )

        self.l7 = Label(self.Main , text = "pH(6.0-8.5( 6.0-9.0 for Mills zone))")
        self.l7.grid(row = 5 , column = 0 , padx = 5 , pady = 5 )

        phco = StringVar()
        self.e7 = Entry(self.Main ,textvariable= phco)
        self.e7. grid(row = 5 , column = 1 , padx = 5 , pady = 5 )

        self.l8 = Label(self.Main , text = "Remarks")
        self.l8.grid(row = 5 , column = 2 , padx = 5 , pady = 5 )

        reco = StringVar()
        self.e8 = Entry(self.Main ,textvariable= reco)
        self.e8. grid(row = 5 , column = 3 , padx = 5 , pady = 5 )

        #---------------------------------------------------------#

        self.b1 = Button(self.Main,text="Submit", command=self.insert_record)
        self.b1.grid(row = 17 , column=1  , sticky='e')

        #clear
        self.B2 = Button(self.Main, text = "Clear", command = self.clear)
        self.B2.grid(row = 17, column = 2, padx = 5, pady = 5)

        self.Main.pack(padx = 5, pady = 5)

  

    def clear(self):
            self.e3.delete(0, 'end')
            self.e4.delete(0, 'end')
            self.e5.delete(0, 'end')
            self.e6.delete(0, 'end')
            self.e7.delete(0, 'end')
            self.e8.delete(0, 'end')
            

    #insertion
    def insert_record(self):
        if self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="" or self.e6.get()=="" or self.e7.get()==""or self.e8.get()=="":
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
                if self.c.get()==options[0]:
                    sql = """INSERT INTO effluent_co (date,Oil_grease, Phenol,Cyanide, TSS, PH,remarks)
                                VALUES (%s,%s, %s, %s, %s,%s, %s)"""
                elif self.c.get()==options[1]:
                    sql = """INSERT INTO effluent_bpp (date,Oil_grease, Phenol,Cyanide, TSS, PH,remarks)
                                VALUES (%s,%s, %s, %s, %s,%s, %s)"""
                elif self.c.get()==options[2]:
                    sql = """INSERT INTO effluent_of_1 (date,Oil_grease, Phenol,Cyanide, TSS, PH,remarks)
                                VALUES (%s,%s, %s, %s, %s,%s, %s)"""
                elif self.c.get()==options[3]:
                    sql = """INSERT INTO effluent_tpp (date,Oil_grease, Phenol,Cyanide, TSS, PH,remarks)
                                VALUES (%s,%s, %s, %s, %s,%s, %s)"""
                elif self.c.get()==options[4]:
                    sql = """INSERT INTO effluent_crm (date,Oil_grease, Phenol,Cyanide, TSS, PH,remarks)
                        VALUES (%s,%s, %s, %s, %s,%s, %s)"""
        
                values = (self.cal.get(),self.e3.get(), self.e4.get(),self.e5.get(), self.e6.get(),self.e7.get(), self.e8.get())
                self.cursor.execute(sql, values)
                self.db.commit()
        
                self.onClick()

    def onClick(self):
        tkinter.messagebox.showinfo("Confirmation","Successful Submission")

    
 
root = Tk()
window= Window(root)
root.mainloop()
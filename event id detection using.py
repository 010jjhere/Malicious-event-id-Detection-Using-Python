#CYBER SECURITY PROJECT
#TEAM- JAYNIL-LEADER, FIZZA, UMAIR, [PUNITH, KAPIL, NIKHIL, PRATHMESH]
from tkinter import *
from tkinter.ttk import Combobox, Scrollbar
import tkinter.ttk as ttk
from tkinter import messagebox

class EventIDSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Event ID Project")
        self.root.geometry("1300x600+0+0")

        self.email_var = StringVar()
        self.name_var = StringVar()
        self.eventid_var = StringVar()
        self.phone_var = StringVar()

        lbltitle = Label(self.root, text="Event ID System", bg="indigo", fg="pink", bd=13,
                         relief=RIDGE,
                         font=("times new roman", 30, "bold", "underline"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, bg="indigo", padx=20)
        frame.place(x=0, y=80, width=1300, height=600)

        DataFrame = LabelFrame(frame, text="Event ID info", bg="indigo", fg="pink", bd=10,
                                   relief=RIDGE,
                                   font=("times new roman", 15, "bold", "underline"), padx=20)
        DataFrame.place(x=0, y=3, width=1230, height=450)

        lblName = Label(DataFrame, font=("times new roman", 10, "bold"), text="NAME",
                        bg="indigo",fg="pink", padx=2)
        lblName.grid(row=1, column=0, sticky=W)
        txtName = Entry(DataFrame, font=("times new roman", 10, "bold"), width=20, textvariable=self.name_var)
        txtName.grid(row=1, column=1)

        lblEmail = Label(DataFrame, font=("times new roman", 10, "bold"), text="E-MAIL", bg="indigo",fg="pink", padx=2)
        lblEmail.grid(row=3, column=0, sticky=W)
        txtEmail = Entry(DataFrame, font=("times new roman", 10, "bold"), width=20, textvariable=self.email_var)
        txtEmail.grid(row=3, column=1)

        lblName = Label(DataFrame, font=("times new roman", 10, "bold"), text="EVENT ID",
                        bg="indigo",fg="pink", padx=2)
        lblName.grid(row=5, column=0, sticky=W)
        txtName = Entry(DataFrame, font=("times new roman", 10, "bold"), width=20, textvariable=self.eventid_var)
        txtName.grid(row=5, column=1)

        lblEmail = Label(DataFrame, font=("times new roman", 10, "bold"), text="PHONE", bg="indigo",fg="pink", padx=2)
        lblEmail.grid(row=7, column=0)
        txtEmail = Entry(DataFrame, font=("times new roman", 10, "bold"), width=20, textvariable=self.phone_var)
        txtEmail.grid(row=7, column=1)

        def ExitData():
            messagebox.askyesnocancel("EXIT","ARE YOU SURE YOU WANT TO EXIT")

        Framebutton = Frame(self.root, bg="indigo", bd=10, relief=RIDGE, padx=20)
        Framebutton.place(x=0, y=480, width=1300, height=61)

        btnSubmitData = Button(Framebutton, text='SUBMIT', font=("times new roman", 10, "bold"), width=27,height=2, bg="black",
                            fg="pink")
        btnSubmitData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text='ADD', font=("times new roman", 10, "bold"), width=27, height=2,
                            bg="black",
                            fg="pink")
        btnAddData.grid(row=0, column=1)

        btnDeleteData = Button(Framebutton, text='DELETE', font=("times new roman", 10, "bold"), width=27, height=2,
                            bg="black",
                            fg="pink")
        btnDeleteData.grid(row=0, column=2)

        btnResetData = Button(Framebutton, text="RESET", font=("times new roman",10,"bold"),width=27,height=2,bg="black",fg="pink")
        btnResetData.grid(row=0,column=3)

        btnExitData = Button(Framebutton, text='EXIT', font=("times new roman", 10, "bold"), width=27, height=2,
                            bg="black",
                            fg="pink",command=ExitData)
        btnExitData.grid(row=0, column=4)

        DataFrameRight = LabelFrame(frame, text="SELECT EVENT ID", fg="pink", bg="indigo", bd=10,
                                    relief=RIDGE, font=("times new roman", 15, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=600, y=5, width=546, height=350)

        listEventID = ["4624","4625","4634","4648","4719","4964","1102","4720","4722","4723","4725","4728","4732","4756","4738","4740","4767","4735","4737","4755","4772","4777",
                         "4782","4616","4657","4697","4698","4699","4700","4701","4702","4946","4947","4950","4954","5025","5031","5152","5153","5155","5157","5447"]

        def SelectEventID(event=""):
            value = str(listbox.get(listbox.curselection()))
            x = value
            if x == '4624':
                messagebox.showwarning("WARNING","SUCCESSFUL LOGIN")

            elif x == '4625':
                messagebox.showwarning("WARNING","FAILED LOGIN")

            elif x == '4634':
                messagebox.showwarning("WARNING","ACCOUNT LOGGED OFF")

            elif x == '4648':
                messagebox.showwarning("WARNING","A LOGIN ATTEMPT WAS MADE WITH EXPLICIT CREDENTIALS")

            elif x == '4719':
                messagebox.showwarning("WARNING","SYSTEM AUDIT POLICY WAS CHANGED")

            elif x == '4694':
                messagebox.showwarning("WARNING","SPECIAL GROUP HAS BEEN ASSIGNED TO A NEW LOGIN")

            elif x == '1102':
                messagebox.showwarning("WARNING","AUDIT LOGIN WAS CLEARED. THIS CAN RELATE TO POTENTIAL ATTACK")

            elif x == '4720':
                messagebox.showwarning("WARNING","A USER ACCOUNT WAS CREATED")

            elif x == '4722':
                messagebox.showwarning("WARNING","A USER ACCOUNT WAS ENABLED")

            elif x == '4723':
                messagebox.showwarning("WARNING","AN ATTEMPT WAS MADE TO CHANGE PASSWORD OF THE SYSTEM")

            elif x == '4725':
                messagebox.showwarning("WARNING","A USER ACCOUNT WAS DISABLED")

            elif x == '4728':
                messagebox.showwarning("WARNING","A USER WAS ADDED TO PRIVILEDGED GLOBAL GROUP")

            elif x == '4732':
                messagebox.showwarning("WARNING","A USER WAS ADDED TO PRIVILEDGED LOCAL GROUP")

            elif x == '4756':
                messagebox.showwarning("WARNING","A USER WAS ADDED TO PRIVILEDGED UNIVERSAL GROUP")

            elif x == '4738':
                messagebox.showwarning("WARNING","USER ACCOUNT WAS CHANGED")

            elif x == '4740':
                messagebox.showwarning("WARNING","A USER ACCOUNT WAS LOCKED OUT")

            elif x == '4767':
                messagebox.showwarning("WARNING","A USER ACCOUNT WAS UNLOCKED")

            elif x == '4735':
                messagebox.showwarning("WARNING","A PRIVILEDGED LOCAL GROUP WAS MODIFIED")

            elif x == '4737':
                messagebox.showwarning("WARNING","A PRIVILEDGED GLOBAL GROUP WAS MODIFIED")

            elif x == '4755':
                messagebox.showwarning("WARNING","A PRIVILEDGED UNIVERSAL GROUP WAS MODIFIED")

            elif x == '4772':
                messagebox.showwarning("WARNING","A KEBROS AUTHENTICATION TICKET REQUEST FAILED")

            elif x == '4777':
                messagebox.showwarning("WARNING","THE DOMAIN CONTROLLER FAILED TO VALIDATE THE CREDENTIALS OF AN ACCOUNT")

            elif x == '4782':
                messagebox.showwarning("WARNING","PASSWORD HASH AN ACCOUNT WAS ACCESSED")

            elif x == '4616':
                messagebox.showwarning("WARNING","SYSTEM TIME WAS CHANGED")

            elif x == '4657':
                messagebox.showwarning("WARNING","A REGISTRY VALUE IS CHANGED")

            elif x == '4698':
                messagebox.showwarning("WARNING","EVENTS RELATED TO WINDOWS SCHEDULED TASKS BEING CREATED,MODIFIED,DELETED,ENABLED OR DISABLED")

            elif x == '4699':
                messagebox.showwarning("WARNING","EVENTS RELATED TO WINDOWS SCHEDULED TASKS BEING CREATED,MODIFIED,DELETED,ENABLED OR DISABLED")

            elif x == '4700':
                messagebox.showwarning("WARNING","EVENTS RELATED TO WINDOWS SCHEDULED TASKS BEING CREATED,MODIFIED,DELETED,ENABLED OR DISABLED")

            elif x == '4701':
                messagebox.showwarning("WARNING","EVENTS RELATED TO WINDOWS SCHEDULED TASKS BEING CREATED,MODIFIED,DELETED,ENABLED OR DISABLED")

            elif x == '4702':
                messagebox.showwarning("WARNING","EVENTS RELATED TO WINDOWS SCHEDULED TASKS BEING CREATED,MODIFIED,DELETED,ENABLED OR DISABLED")

            elif x == '4946':
                messagebox.showwarning("WARNING","A RULE WAS ADDED TO WINDOWS FIREWALL EXCEPTION LIST")

            elif x == '4947':
                messagebox.showwarning("WARNING","A RULE WAS MODIFIED TO WINDOWS FIREWALL EXCEPTION LIST")

            elif x == '4950':
                messagebox.showwarning("WARNING","A SETTING WAS CHANGED IN WINDOWS FIREWALL")

            elif x == '4954':
                messagebox.showwarning("WARNING","A GROUP POLICY SETTINGS FOR WINDOWS FIREWALL HAS CHANGED")

            elif x == '5025':
                messagebox.showwarning("WARNING","THE WINDOWS FIREWALL SERVICE HAS BEEN STOPPED")

            elif x == '5031':
                messagebox.showwarning("WARNING","A WINDOWS FIREWALL BLOCKED AN APPLICATION FROM ACCEPTING INCOMING TRAFFIC")

            elif x == '5152':
                messagebox.showwarning("WARNING","A NETWORK POCKET WAS BLOCKED BY WINDOWS FILTERING PLATFORM ")

            elif x == '5153':
                messagebox.showwarning("WARNING","A NETWORK POCKET WAS BLOCKED BY WINDOWS FILTERING PLATFORM")

            elif x == '5155':
                messagebox.showwarning("WARNING","A WINDOWS FILTERING PLATFORM BLOCKED AN APPLICATION OR SERVICE FROM LISTENING ON A PORT")

            elif x == '5157':
                messagebox.showwarning("WARNING","A WINDOWS FILTERING PLATFORM BLOCKED A CONNECTION")

            elif x == '5447':
                messagebox.showwarning("WARNING", "A WINDOWS FILTERING PLATFORM FILTER WAS CHANGED")

        listbox = Listbox(DataFrameRight, font=("times new roman", 10, "bold"), width=20, height=16)
        listbox.bind("<<ListboxSelect>>",SelectEventID)
        listbox.grid(row=0, column=0, padx=4)
        for i in listEventID:
            listbox.insert('end', i)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        listScrollbar.config(command=listbox.yview)


if __name__ == '__main__':
    root = Tk()
    obj=EventIDSystem(root)
    root.mainloop()


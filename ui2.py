from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


def fun(args):
    print(args)

# main window frame with title


class Hospital:

    def __init__(self, root):

        ### variables ###

        self.root = root
        self.Pas_ID = StringVar()
        self.Name = StringVar()
        self.age = StringVar()
        self.number = StringVar()
        self.Tick_ID = StringVar()
        self.price = StringVar()
        self.seat_num = StringVar()
        self.flight_ID = StringVar()

    def home_page(self):

        self.root.title("Hospital Management System")
        self.root.geometry("1540x780+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System",
                         fg="purple", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        ##################### buttons frame ###########

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE, bg="cyan")
        Buttonframe.place(x=0, y=130, width=1540, height=650)

        b1 = Button(Buttonframe, text="Admin",
                    background="red", fg="white", font=("times new roman", 50, "bold"), command=lambda: [lbltitle.destroy(), Buttonframe.destroy(), self.admin_page_2()])
        b1.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 2
        b2 = Button(Buttonframe, text="Reception",
                    background="blue", fg="white", font=("times new roman", 50, "bold"), command=lambda: [lbltitle.destroy(), Buttonframe.destroy(), self.rec_page_2()])
        b2.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 3
        b3 = Button(Buttonframe, text="Exit",
                    background="green", fg="white", font=("times new roman", 50, "bold"), command=self.root.destroy)
        b3.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

    def admin_page_2(self):

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Admin System",
                         fg="purple", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        ########### Data Frame #############
        Dataframe = Frame(self.root, bd=20, relief=RIDGE, bg="cyan")
        Dataframe.place(x=0, y=130, width=1540, height=650)

        ############ Button Frame ###########

        Buttonframe = Frame(Dataframe, bd=5, relief=RAISED, bg="brown")
        Buttonframe.place(x=0, y=0, width=100, height=50)

        ########### Back Button #############

        b1 = Button(Buttonframe, text="< Back",
                    background="red", fg="white", font=("times new roman", 10, "bold"), command=lambda: [lbltitle.destroy(), Buttonframe.destroy(), self.home_page()])
        b1.pack(fill=BOTH, side=BOTTOM)

        ########### Admin Login Form #############

        usernameLabel = Label(Dataframe, text="Admin User Name", background="red", fg="white", font=(
            "times new roman", 10, "bold")).place(x=480, y=150)
        username = StringVar()
        usernameEntry = Entry(
            Dataframe, textvariable=username).place(x=600, y=150)

        passwordLabel = Label(Dataframe, text="Admin Password", background="red", fg="white", font=(
            "times new roman", 10, "bold")).place(x=480, y=180)
        password = StringVar()
        passwordEntry = Entry(
            Dataframe, textvariable=password, show='*').place(x=600, y=180)

        #login button
        loginButton = Button(Dataframe, text="Login", background="red", fg="white", font=(
            "times new roman", 10, "bold"), command=lambda: self.validateLogin(username, password)).place(x=500, y=210)

    def admin_page_3(self):

        ########### Data Frame #############
        Dataframe = Frame(self.root, bd=20, relief=RIDGE, bg="cyan")
        Dataframe.place(x=0, y=130, width=1540, height=650)

        ############ Button Frame ###########

        Buttonframe = Frame(Dataframe, bd=5, relief=RAISED, bg="brown")
        Buttonframe.place(x=0, y=0, width=100, height=50)

    def rec_page_2(self):

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Reception",
                         fg="purple", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        ########### Data Frame #############
        Dataframe = Frame(self.root, bd=20, relief=RIDGE, bg="cyan")
        Dataframe.place(x=0, y=130, width=1540, height=650)

        ############ Button Frame ###########

        Buttonframe = Frame(Dataframe, bd=5, relief=RAISED, bg="brown")
        Buttonframe.place(x=0, y=0, width=100, height=50)

        ########### Back Button #############

        b1 = Button(Buttonframe, text="< Back",
                    background="red", fg="white", font=("times new roman", 10, "bold"), command=lambda: [lbltitle.destroy(), Buttonframe.destroy(), self.home_page()])
        b1.pack(fill=BOTH, side=BOTTOM)

        ########### Admin Login Form #############

        usernameLabel = Label(Dataframe, text="Staff User Name", background="red", fg="white", font=(
            "times new roman", 10, "bold")).place(x=480, y=150)
        username = StringVar()
        usernameEntry = Entry(
            Dataframe, textvariable=username).place(x=600, y=150)

        passwordLabel = Label(Dataframe, text="Staff Password", background="red", fg="white", font=(
            "times new roman", 10, "bold")).place(x=480, y=180)
        password = StringVar()
        passwordEntry = Entry(
            Dataframe, textvariable=password, show='*').place(x=600, y=180)

        #login button
        loginButton = Button(Dataframe, text="Login", background="red", fg="white", font=(
            "times new roman", 10, "bold"), command=lambda: self.validateLogin2(username, password)).place(x=500, y=210)

    def rec_page_3(self):

        ##################### buttons frame ###########

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE, bg="cyan")
        Buttonframe.place(x=0, y=130, width=1540, height=650)

        b1 = Button(Buttonframe, text="Show All",
                    background="red", fg="white", font=("times new roman", 50, "bold"), command=lambda: [Buttonframe.destroy(), self.rec_showtable()])
        b1.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 2
        b2 = Button(Buttonframe, text="Add New Patient",
                    background="red", fg="white", font=("times new roman", 50, "bold"), command=lambda: [Buttonframe.destroy(), self.rec_addnew()])
        b2.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 3
        b3 = Button(Buttonframe, text="Find",
                    background="red", fg="white", font=("times new roman", 50, "bold"), command=lambda: [Buttonframe.destroy()])
        b3.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 4
        b4 = Button(Buttonframe, text="Log Out",
                    background="green", fg="white", font=("times new roman", 50, "bold"), command=lambda: [Buttonframe.destroy(), self.home_page()])
        b4.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

    def rec_showtable(self):

        ########### Data Frame #############

        Dataframe = Frame(self.root, bd=20, relief=RIDGE, bg="cyan")
        Dataframe.place(x=0, y=130, width=1540, height=650)

        ############ Button Frame ###########

        Buttonframe = Frame(Dataframe, bd=5, relief=RAISED, bg="brown")
        Buttonframe.place(x=0, y=0, width=100, height=50)

        ########### Back Button #############

        b1 = Button(Buttonframe, text="< Back",
                    background="red", fg="white", font=("times new roman", 10, "bold"), command=lambda: [Buttonframe.destroy(), self.rec_page_3()])
        b1.pack(fill=BOTH, side=BOTTOM)

        ########### Scroll Bar #############

        scroll_x = ttk.Scrollbar(Dataframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Dataframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Dataframe, column=("Pat_ID", "Name", "Diagnosis", "Address", "Hosp_ID",
                                           "Doc_ID", "Checkup_Date", "Gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("Pat_ID", text="Ticket No:")
        self.hospital_table.heading("Name", text="Price")
        self.hospital_table.heading("Diagnosis", text="Seat number")
        self.hospital_table.heading("Address", text="Passport Number")
        self.hospital_table.heading("Hosp_ID", text="Name")
        self.hospital_table.heading("Doc_ID", text="age")
        self.hospital_table.heading("Checkup_Date", text="phone no")
        self.hospital_table.heading("Gender", text="source")
        self.hospital_table.heading("Gender", text="destination")
        self.hospital_table.heading("Gender", text="arrival")
        self.hospital_table.heading("Gender", text="departure")
        self.hospital_table.heading("Gender", text="airline id")

        



        self.hospital_table["show"] = "headings"
        self.hospital_table.place(x=0, y=50, width=1485, height=540)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="rambo", database="fms")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT t.ticket_num,t.price,t.seat_num,p.*,f.* from ticket t,passenger p,flight f where(t.passport_number=p.passport_number and t.flight_number=f.flight_number)")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def rec_addnew(self):

        ########### Data Frame #############

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1540, height=650)

        ############ Button Frame ###########

        Buttonframe = Frame(Dataframe, bd=5, relief=RAISED, bg="brown")
        Buttonframe.grid(row=0, column=1)

        ########### Back Button #############

        b1 = Button(Buttonframe, text="< Back",
                    background="red", fg="white", font=("times new roman", 10, "bold"), command=lambda: [Buttonframe.destroy(), self.rec_page_3()])
        b1.pack(fill=BOTH, side=BOTTOM)

        ########### Add new record form ##########

        lblPatID = Label(Dataframe, text="Passenger ID", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=0, column=5)
        txtPatID = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                         textvariable=self.Pas_ID).grid(row=0, column=6, sticky=W)

        lblName = Label(Dataframe, text="Passenger Name", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=1, column=5)
        txtName = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                        textvariable=self.Name).grid(row=1, column=6, sticky=W)

        lblName = Label(Dataframe, text="age", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=2, column=5)
        txtDiagnosis = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                             textvariable=self.age).grid(row=2, column=6, sticky=W)

        lblName = Label(Dataframe, text="Mobile Num", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=3, column=5)
        txtAddress = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                           textvariable=self.number).grid(row=3, column=6, sticky=W)

        lblName = Label(Dataframe, text="Ticket ID", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=4, column=5)
        txtHosp_ID = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                           textvariable=self.Tick_ID).grid(row=4, column=6, sticky=W)

        lblName = Label(Dataframe, text="Price", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=5, column=5)
        txtDoc_ID = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                          textvariable=self.price).grid(row=5, column=6, sticky=W)

        lblName = Label(Dataframe, text="seat number", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=6, column=5)
        txtCheckup_Date = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                                textvariable=self.seat_num).grid(row=6, column=6, sticky=W)
        lblName = Label(Dataframe, text="Flight Id", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=7, column=5)
        txtCheckup_Date = Entry(Dataframe, font=("arial", 12, "bold"), width=33,
                                textvariable=self.flight_ID).grid(row=6, column=6, sticky=W)

        lblName = Label(Dataframe, text=" ", font=(
            "arial", 12, "bold"), padx=2, pady=6).grid(row=9, column=5)
        comGender = ttk.Combobox(Dataframe, font=(
            "arial", 12, "bold"), width=33)
        comGender["values"] = ("M", "F")
        comGender.grid(row=7, column=6, sticky=W)

        b2 = Button(Dataframe, text="Submit",
                    background="red", fg="white", font=("times new roman", 10, "bold"), command=lambda: [Buttonframe.destroy(), self.insert()])
        b2.grid(row=10, column=5, sticky=W)

    #### contains actual sql query for insertion operation ####

    def insert(self):
        a=5
        # if self.Name.get() == "" or self.Address.get() == "" or self.Diagnosis.get() == "" or self.Gender.get() == "" or self.Hosp_ID.get() == "" or self.Pat_ID.get() == "" or self.Checkup_Date.get() == "" or self.Doc_ID.get() == "":
        #     messagebox.showerror("Error", "One or More Fields are empty !")
        #     self.rec_addnew()
        if a==1:
            print("jsgvh")
        else:
            messagebox.showinfo("Success", "Inserted")
            conn = mysql.connector.connect(
                host="localhost", username="root", password="rambo", database="fms")
            my_cursor = conn.cursor()
            print(self.Pas_ID.get(), self.Name.get(
            ), self.age.get(), self.number.get(), self.Tick_ID.get(), self.price.get(), self.seat_num.get(
            ), self.Pas_ID.get(), self.flight_ID.get())
            my_cursor.execute("INSERT INTO PASSENGER VALUES(%s,%s,%s,%s)", (self.Pas_ID.get(), self.Name.get(
            ), self.age.get(), self.number.get()))
            # rows = my_cursor.fetchall()
            
            
            # if len(rows) != 0:
            #     self.hospital_table.delete(*self.hospital_table.get_children())
            #     for i in rows:
            #         self.hospital_table.insert("", END, values=i)
            # conn.commit()
            # self.rec_showtable()
            # conn.close()

            my_cursor.execute("INSERT INTO TICKET VALUES(%s,%s,%s,%s,%s)", (self.Tick_ID.get(), self.price.get(), self.seat_num.get(
            ), self.Pas_ID.get(), self.flight_ID.get()))
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("", END, values=i)
            conn.commit()
            self.rec_showtable()
            conn.close()

    #### validates reception staff ####

    def validateLogin2(self, username, password):

        if username.get() == "staff" and password.get() == "s":
            messagebox.showinfo("Success !", "Welcome " + username.get())
            self.rec_page_3()

        else:
            self.rec_page_2()
            messagebox.showerror(
                "Error", "The credentials are incorrect or unauthorized access")

    #### validates admin ####

    def validateLogin(self, username, password):

        if username.get() == "ps" and password.get() == "6":
            messagebox.showinfo(
                "Success !", "Admin has been authenticated successfully")
            self.admin_page_3()

        else:
            self.admin_page_2()
            messagebox.showerror("Error", "The credentials are incorrect")


########## Driver Code ##########

def main():
    root = Tk()
    ob = Hospital(root)
    ob.home_page()
    root.mainloop()


if __name__ == "__main__":
    main()

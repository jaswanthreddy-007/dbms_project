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
        self.root = root

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
                    background="red", fg="white", font=("times new roman", 50, "bold"))
        b1.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 2
        b2 = Button(Buttonframe, text="Add New Patient",
                    background="red", fg="white", font=("times new roman", 50, "bold"))
        b2.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 3
        b3 = Button(Buttonframe, text="Find",
                    background="red", fg="white", font=("times new roman", 50, "bold"))
        b3.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

        # Button 4
        b4 = Button(Buttonframe, text="Log Out",
                    background="green", fg="white", font=("times new roman", 50, "bold"))
        b4.pack(side=TOP, expand=True, fill=BOTH, pady=5, padx=5)

    def validateLogin2(self, username, password):

        if username.get() == "staff" and password.get() == "s":
            messagebox.showinfo("Success !", "Welcome " + username.get())
            self.rec_page_3()

        else:
            self.rec_page_2()
            messagebox.showerror(
                "Error", "The credentials are incorrect or unauthorized access")

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

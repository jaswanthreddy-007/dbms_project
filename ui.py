from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 

main_screen=Tk()

img = (Image.open("D:/dbms_project/699780710235c0ee61a913328abf928e.png"))
global resized
resized=img.resize((150,75),Image.ANTIALIAS)
Indian_Flag = ImageTk.PhotoImage(resized)
#EXIT DATA BASE SCREEN
def open_thankyou():
    main_screen.destroy()
    messagebox.showinfo("EXIT DATA BASE","THANK YOU FOR USING THE APPLICATION \n \n \tMade With Passion \n \n \t  By  Jaswanth Reddy")
     

#RETURN TO MAIN SCREEN(FIRST SCREEN)
def open_main(forms_screen):
    global Indian_Flag
    forms_screen.destroy()
    global main_screen
    main_screen=Tk()
    main_screen.config(bg="grey")
    main_screen.title("AIRLINE DATABASE")
    main_screen.geometry("900x700")
    # main_screen.iconbitmap("C:\Shreyas\projects\DBMS Mini Project\INDIAN ARMY LOGO.ico")
    Indian_Flag = ImageTk.PhotoImage(resized)
    Flag_label=Label(image=Indian_Flag).grid(row=0,column=0)
    Upper_bar = Label(main_screen,text="AIRLINE DATABASE",fg="orange",bg="white",width=49,height=3,padx=1,font="bold",border=True).grid(row=0,column=1)
    plain=Label(main_screen,text="",bg="grey").grid(row=1,column=0,columnspan=3)
    # quote1=Label(main_screen,text="“Our flag does not fly because the wind moves it, ",fg="blue",bg="grey",font="bold").grid(row=2,column=0,columnspan=3)
    # quote2=Label(main_screen,text="it flies with the last breath of each soldier who died protecting it.” ",fg="blue",bg="grey",font="bold").grid(row=3,column=0,columnspan=3)
    MAIN_MENU = Label(main_screen,text="MAIN MENU",fg="black",bg="grey",height=3,pady=5,font="bold",underline=12).grid(row=4,column=0,columnspan=3)
    plain=Label(main_screen,text="",bg="grey").grid(row=5,column=0,columnspan=3)
    forms_menu=Button(main_screen,text="Open AIRLINE menu",pady=10,padx=3,command=open_forms).grid(row=6,column=0,columnspan=2)
    plain=Label(main_screen,text="",bg="grey").grid(row=7,column=0,columnspan=3)
    reports_menu=Button(main_screen,text="Open reports menu",pady=10,padx=3,command=open_reports).grid(row=8,column=0,columnspan=2)
    plain=Label(main_screen,text="",bg="grey").grid(row=9,column=0,columnspan=3)
    close_menu=Button(main_screen,text="Close Database",pady=10,padx=3,command=open_thankyou).grid(row=10,column=0,columnspan=2)

def soldier_registration(forms_screen):
    global Indian_Flag
    forms_screen.destroy()
    soldier_registration_screen=Tk()
    soldier_registration_screen.config(bg="grey")
    soldier_registration_screen.title("REGISTRATION")
    soldier_registration_screen.geometry("700x625")
    # soldier_registration_screen.iconbitmap("C:\Shreyas\projects\DBMS Mini Project\INDIAN ARMY LOGO.ico")
    Indian_Flag = ImageTk.PhotoImage(resized)
    Flag_label=Label(image=Indian_Flag).grid(row=0,column=0)
    Upper_bar = Label(soldier_registration_screen,text="SOLDIER REGISTRATION",fg="white",bg="darkgreen",width=49,height=3,padx=1,font="bold",border=True).grid(row=0,column=1)







#REPORTS SCREEN(THIRD SCREEN)
def open_reports():
    global Indian_Flag
    main_screen.destroy()
    reports_screen=Tk()
    reports_screen.config(bg="grey")
    reports_screen.title("REPORTS SCREEN")
    reports_screen.geometry("700x625")
    # reports_screen.iconbitmap("C:\Shreyas\projects\DBMS Mini Project\INDIAN ARMY LOGO.ico")
    Indian_Flag = ImageTk.PhotoImage(resized)
    Flag_label=Label(image=Indian_Flag).grid(row=0,column=0)
    Upper_bar = Label(reports_screen,text="MILITARY DATABASE",fg="white",bg="darkgreen",width=49,height=3,padx=1,font="bold",border=True).grid(row=0,column=1)
    REPORTS_MENU = Label(reports_screen,text="REPORTS MENU",fg="black",bg="grey",height=3,pady=5,font="bold",underline=12).grid(row=2,column=0,columnspan=3)
    Soldier_info=Button(reports_screen,text="Display Soldier Info",pady=10,padx=3,command=lambda : option_box(reports_screen,1)).grid(row=4,column=0,columnspan=2)
    plain=Label(reports_screen,text="",bg="grey").grid(row=5,column=0,columnspan=3)
    medical_info=Button(reports_screen,text="Display Medical Info",pady=10,padx=3,command=lambda : option_box(reports_screen,2)).grid(row=6,column=0,columnspan=2)
    plain=Label(reports_screen,text="",bg="grey").grid(row=7,column=0,columnspan=3)
    Regiment_info=Button(reports_screen,text="Display Regiment Info",pady=10,padx=3,command=lambda : option_box(reports_screen,3)).grid(row=8,column=0,columnspan=2)
    plain=Label(reports_screen,text="",bg="grey").grid(row=9,column=0,columnspan=3)
    Weapon_info=Button(reports_screen,text="Display Weapon Info",pady=10,padx=3,command=lambda : option_box(reports_screen,4)).grid(row=10,column=0,columnspan=2)
    plain=Label(reports_screen,text="",bg="grey").grid(row=11,column=0,columnspan=3)
    mission_info=Button(reports_screen,text="Display Mission Info",pady=10,padx=3,command=lambda : option_box(reports_screen,5)).grid(row=12,column=0,columnspan=2)
    plain=Label(reports_screen,text="",bg="grey").grid(row=13,column=0,columnspan=3)
    medal_info=Button(reports_screen,text="Display Medal Info",pady=10,padx=3,command=lambda : option_box(reports_screen,6)).grid(row=14,column=0,columnspan=2)
    plain=Label(reports_screen,text="",bg="grey").grid(row=15,column=0,columnspan=3)
    rtn_main=Button(reports_screen,text="Return to Main Menu",bg="lightblue",border=True,fg="Black",pady=10,padx=3,command=lambda : open_main(reports_screen)).grid(row=16,column=0,columnspan=2)

#FORMS SCREEN(SECOND SCREEN)
def open_forms():
    global Indian_Flag
    main_screen.destroy()
    forms_screen=Tk()
    forms_screen.config(bg="grey")
    forms_screen.title("FORMS SCREEN")
    forms_screen.geometry("700x625")
    # forms_screen.iconbitmap("C:\Shreyas\projects\DBMS Mini Project\INDIAN ARMY LOGO.ico")
    Indian_Flag = ImageTk.PhotoImage(resized)
    Flag_label=Label(image=Indian_Flag).grid(row=0,column=0)
    Upper_bar = Label(main_screen, text="AIRLINE DATABASE", fg="orange", bg="white",
                      width=49, height=3, padx=1, font="bold", border=True).grid(row=0, column=1)
    FORMS_MENU = Label(forms_screen, text="FORMS MENU", fg="black", bg="grey", height=3,
                       pady=5, font="bold", underline=12).grid(row=2, column=0, columnspan=3)
    Soldier_regis=Button(forms_screen,text="Soldier Registration",pady=10,padx=3,command=lambda : soldier_registration(forms_screen)).grid(row=4,column=0,columnspan=2)
    plain=Label(forms_screen,text="",bg="grey").grid(row=5,column=0,columnspan=3)
    Meds_regis=Button(forms_screen,text="Medical Information Addition",pady=10,padx=3).grid(row=6,column=0,columnspan=2)
    plain=Label(forms_screen,text="",bg="grey").grid(row=7,column=0,columnspan=3)
    Regi_regis=Button(forms_screen,text="Regiment Registration",pady=10,padx=3).grid(row=8,column=0,columnspan=2)
    plain=Label(forms_screen,text="",bg="grey").grid(row=9,column=0,columnspan=3)
    Weapon_regis=Button(forms_screen,text="Weapon Information Addition",pady=10,padx=3).grid(row=10,column=0,columnspan=2)
    plain=Label(forms_screen,text="",bg="grey").grid(row=11,column=0,columnspan=3)
    mission_regis=Button(forms_screen,text="Previous Mission Addition",pady=10,padx=3).grid(row=12,column=0,columnspan=2)
    plain=Label(forms_screen,text="",bg="grey").grid(row=13,column=0,columnspan=3)
    Medal_Regis=Button(forms_screen,text="Medals Won Addition",pady=10,padx=3,border=3).grid(row=14,column=0,columnspan=2)
    plain=Label(forms_screen,text="",bg="grey").grid(row=15,column=0,columnspan=3)
    rtn_main=Button(forms_screen,text="Return to Main Menu",bg="lightblue",border=True,fg="Black",pady=10,padx=3,command=lambda : open_main(forms_screen)).grid(row=16,column=0,columnspan=2)


#MAIN SCREEN(FIRST SCREEN)
main_screen.config(bg="grey")
main_screen.title("DEFENCE DATABASE")
main_screen.geometry("700x500")
# main_screen.iconbitmap("C:\Shreyas\projects\DBMS Mini Project\INDIAN ARMY LOGO.ico")
Flag_label=Label(image=Indian_Flag).grid(row=0,column=0)
Upper_bar = Label(main_screen,text="AIRLINE DATABASE",fg="white",bg="darkgreen",width=49,height=3,padx=1,font="bold",border=True).grid(row=0,column=1)
plain=Label(main_screen,text="",bg="grey").grid(row=1,column=0,columnspan=3)
# quote1=Label(main_screen,text="“Our flag does not fly because the wind moves it, ",fg="blue",bg="grey",font="bold").grid(row=2,column=0,columnspan=3)
# quote2=Label(main_screen,text="it flies with the last breath of each soldier who died protecting it.” ",fg="blue",bg="grey",font="bold").grid(row=3,column=0,columnspan=3)
MAIN_MENU = Label(main_screen,text="MAIN MENU",fg="black",bg="grey",height=3,pady=5,font="bold",underline=12).grid(row=4,column=0,columnspan=3)
plain=Label(main_screen,text="",bg="grey").grid(row=5,column=0,columnspan=3)
forms_menu=Button(main_screen,text="Open forms menu",pady=10,padx=3,command=open_forms).grid(row=6,column=0,columnspan=2)
plain=Label(main_screen,text="",bg="grey").grid(row=7,column=0,columnspan=3)
reports_menu=Button(main_screen,text="Open reports menu",pady=10,padx=3,command=open_reports).grid(row=8,column=0,columnspan=2)
plain=Label(main_screen,text="",bg="grey").grid(row=9,column=0,columnspan=3)
close_menu=Button(main_screen,text="Close Database",pady=10,padx=3,command=open_thankyou).grid(row=10,column=0,columnspan=2)


def option_box(reports_screen,n):
    response =  messagebox.askquestion("choose data selection", "DO YOU WANT TO DISPLAY ALL ENTRIES?")
    if response=="no":
        reports_screen.destroy()
        condition_box=Tk()
        condition_box.title("ENTER ID")
        condition_box.config(bg="#439A97")
        condition_box.geometry("250x125")
        # condition_box.iconbitmap("C:\Shreyas\projects\DBMS Mini Project\INDIAN ARMY LOGO.ico")
        condition_text=Label(condition_box,text=" Enter the ID , whose info is to be displayed",bg="#439A97").grid(row=0)
        plain=Label(condition_box,text="",bg="#439A97").grid(row=1)
        Display_ID=Entry(condition_box).grid(row=2)
        plain=Label(condition_box,text="",bg="#439A97").grid(row=3)
        submit=Button(condition_box,text="SUBMIT",bg="black",fg="white").grid(row=4)
        if n==1:
            g



main_screen.mainloop()




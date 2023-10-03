from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import datetime
import pytz
import sqlite3 as sqlite

root = Tk()

root.title("STUDENT REG")
root.geometry('1350x700+0+0')
my_tree = ttk.Treeview(root)
IST = pytz.timezone('Asia/Manila')
root.resizable(False, False)



title = tk.Label(root, text="PROGRAMMING CLUB ATTENDANCE", font=('Verdana', 20, 'bold'), border=12, relief=tk.GROOVE, bg='lightgray')
title.pack(side=tk.TOP,fill=tk.X)

details = tk.LabelFrame(root, text="STUDENT DETAILS", font=('Verdana', 20, 'bold'), relief= tk.GROOVE,bd=12, bg='lightgray')
details.place(x=20,y=90,width=500,height=440)

#treeFrame = tk.Frame(root, bd=12, bg='lightgray', relief=tk.GROOVE)
#treeFrame.place(x=600,y=90,width=720,height=575)

#--------------------REGISTER FUNCTION---------------------#
# def reg():
    
def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%I:%M:%S %p")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    label_date_now.config(text = date_now)
    # label_date_now.after(500, update_clock)
    label_time_now.config(text = time_now)
    label_time_now.after(1000, update_clock)
    return formatted_now

def check_in():
        Name = stud_numEntry.get()
        Track = track.get()
        Year = year.get()
        Taken_class = taken_class.get()

        if Name=="" or Track=="SELECTED TRACK" or Year=="YEAR LEVEL" or Taken_class =="TAKEN CLASS":
            messagebox.showerror("Error","Please fill the form",parent=root)
        else:

            connection = sqlite.connect("db0.db")
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS tb1([Name] VARCHAR(225), [Track] VARCHAR(225), [Year] VARCHAR(225), [Taken Class] VARCHAR(255))""")
            cur.execute("INSERT INTO tb1 VALUES('"+Name+"', '"+Track+"','"+Year+"','"+Taken_class+"')")
            connection.commit()

            stud_numEntry.delete(0, "end")
            track.set("SELECTED TRACK")
            year.set("YEAR LEVEL")
            taken_class.set("TAKEN CLASS")



def TREE():
    for i in my_tree.get_children():
        my_tree.delete(i)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array,text="", values=(array), tags="orow")

def read():
    conn = sqlite.connect("db0.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tb1([Name] VARCHAR(225), [Track] VARCHAR(225), [Year] VARCHAR(225), [Taken Class] VARCHAR(255))""")
    cur.execute("SELECT * FROM tb1")
    aa = cur.fetchall()
    conn.commit()

    for row in aa:
        print(row)
    return aa


label_time = tk.Label(root, text="Current Date and Time", font=('Verdana', 20, 'bold'),bg='lightgray').place(x=88, y=400)

label_date_now = tk.Label(text="Current Date", font = ('Verdana 20 bold'),bg='lightgray')
label_date_now.place(x=40, y=450)

label_time_now = tk.Label(text="Current Time", font = ('Verdana 20 bold'),bg='lightgray')
label_time_now.place(x=300, y=450)



#--------------ENTRY FIELDS------------------#

stud_name = tk.Label(root, text="Student ID: ", font=('Verdana', 15),bg='lightgray').place(x=35, y=150)
stud_numEntry = Entry(root, width=25, bd=2, font=('Verdana', 13))
stud_numEntry.place(x=200, y=155, height = 25)

course = tk.Label(root, text='Track/Course:', font=('Verdana', 15),bg='lightgray')
course.place(x=35,y=197)
track = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
track.set("SELECTED TRACK")
track['values'] = ('BSCS DM', 'BSCS BA','BSIT - NS', 'BSIT BPO', 'BSIT WMAD', 'OTHERS')
track['state'] = 'readonly'
track.place(x=200, y=200, height=25)

year = tk.Label(root, text='Year:',font=('Verdana', 15),bg='lightgray' )
year.place(x=35,y=245)
year = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
year.set("YEAR LEVEL")
year['values'] = ('1st', '2nd','3rd')
year['state'] = 'readonly'
year.place(x=200, y=250, height=25)

taken_class = tk.Label(root, text='Take Class:',font=('Verdana', 15),bg='lightgray' )
taken_class.place(x=35,y=295)
taken_class = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
taken_class.set("TAKEN CLASS")
taken_class['values'] = ('Fundamentals of Programming', 'Database')
taken_class['state'] = 'readonly'
taken_class.place(x=200, y=300, height=25)


#----------------BUTTONS------------------#

reg_button = Button(text="Check In", command = lambda: [check_in(), TREE()], font=('Verdana', 15, 'bold'), width=17, height=1, bg='SpringGreen4')
reg_button.place(x=140, y=350)

#------------------FRAME-----------------#

# db_frame = tk.Frame(treeFrame,bg='lightgray',bd=11,relief=tk.GROOVE)
# db_frame.pack(fill=tk.BOTH,expand=TRUE)

#-----------------TREE VIEW-----------------#
my_tree.tag_configure('orow', background="#EEEEEE", font=('Verdana', 10))
my_tree.place(x=570, y=90, height=440)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 13, 'bold'))

my_tree['columns'] = ("Student ID", "Track/Course", "Year", "Taken Class")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Student ID", anchor=CENTER, width=180)
my_tree.column("Track/Course", anchor=CENTER, width=180)
my_tree.column("Year", anchor=CENTER, width=180)
my_tree.column("Taken Class", anchor=CENTER, width=220)

my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
my_tree.heading("Track/Course", text="Track/Course", anchor=CENTER)
my_tree.heading("Year", text="Year", anchor=CENTER)
my_tree.heading("Taken Class", text="Taken CLass", anchor=CENTER)















TREE()
update_clock()
root.mainloop()
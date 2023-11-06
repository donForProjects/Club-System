from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from datetime import datetime
import pytz
import sqlite3 as sqlite
import os
import csv

root = Tk()

root.title("Attendance System")
root.geometry('1530x700+0+0')
my_tree = ttk.Treeview(root)
IST = pytz.timezone('Asia/Manila')
root.resizable(False, False)



title = tk.Label(root, text="PROGRAMMING CLUB ATTENDANCE", font=('Verdana', 20, 'bold'), border=12, relief=tk.GROOVE, bg='lightgray')
title.pack(side=tk.TOP,fill=tk.X)

details = tk.LabelFrame(root, text="STUDENT DETAILS", font=('Verdana', 20, 'bold'), relief= tk.GROOVE,bd=12, bg='lightgray')
details.place(x=20,y=90,width=500,height=490)

#--------------------REGISTER FUNCTION---------------------#
    
def update_clock():
    raw_TS = datetime.now(IST)
    date_now = raw_TS.strftime("%d %b %Y")
    time_now = raw_TS.strftime("%I:%M:%S %p")
    formatted_now = raw_TS.strftime("%d-%m-%Y")
    label_date_now.config(text = date_now)
    label_time_now.config(text = time_now)
    label_time_now.after(1000, update_clock)
    return formatted_now



def update_count():
    for selected in my_tree.selection():
        stud_id = str(my_tree.item(selected)['values'][0])      
        count = int(my_tree.item(selected)['values'][6])

        current_date = datetime.now().strftime('%Y-%m-%d')
        path_in = 'Attendance '+ current_date+'.csv'

        if stud_id and count:
            connection = sqlite.connect("Attendance " + current_date + ".db")
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS tb1([ID] VARCHAR(225), [Name] VARCHAR(225), [Track] VARCHAR(225), [Year] VARCHAR(225), [Taken Class] VARCHAR(255), [Status] VARCHAR(255), [Count] INTEGER)""")
            cur.execute("UPDATE tb1 SET [Count] = ? WHERE [ID] = ?", (count+1, stud_id))
            connection.commit()
        else:
            return 0



def check_in():
        Stud_ID = stud_numEntry.get()
        Name = stud_nameEntry.get()
        Track = track.get()
        Year = year.get()
        Taken_class = taken_class.get()
        Status = status.get()
        Count = 1

        if Name=="" or Track=="SELECTED TRACK" or Year=="YEAR LEVEL" or Taken_class =="TAKEN CLASS" or Status == "STATUS":
            messagebox.showerror("Error","Please fill the form",parent=root)
        else:
            current_date = datetime.now().strftime('%Y-%m-%d')
            path_in = 'Attendance '+ current_date+'.csv'

            connection = sqlite.connect("Attendance " + current_date + ".db")
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS tb1([ID] VARCHAR(225), [Name] VARCHAR(225), [Track] VARCHAR(225), [Year] VARCHAR(225), [Taken Class] VARCHAR(255), [Status] VARCHAR(255), [Count] INTEGER)""")
            # cur.execute("INSERT INTO tb1 VALUES('"+Stud_ID+"', '"+Name+"', '"+Track+"','"+Year+"','"+Taken_class+"','"+Status+"', 1)")
            cur.execute("INSERT INTO tb1 ([ID], [Name], [Track], [Year], [Taken Class], [Status], [Count]) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (Stud_ID, Name, Track, Year, Taken_class, Status, Count))

            # cur.execute("INSERT INTO tb1 ([Count]) VALUES (?)",(Count))

            connection.commit()

            stud_numEntry.delete(0, "end")
            stud_nameEntry.delete(0, "end")
            track.set("SELECTED TRACK")
            year.set("YEAR LEVEL")
            taken_class.set("TAKEN CLASS")
            status.set("STATUS")

            isExist_in = os.path.exists(path_in)

            mode = 'a' if isExist_in else 'w'
            with open('Attendance '+ current_date+'.csv', mode, newline='') as csv_file:
                csv_writer_in = csv.writer(csv_file)
                csv_writer_in.writerow([Stud_ID, Name, Track, Year, Taken_class])



def count_rows_in_tree(my_tree):
    all_items = my_tree.get_children('')
    row_count = len(all_items)
    return row_count


def TREE():
    for i in my_tree.get_children():
        my_tree.delete(i)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array,text="", values=(array), tags="orow")

    row_count = count_rows_in_tree(my_tree)
    # print(f"Number of rows in the tree: {row_count}")
    stud_count = tk.Label(text=f"Attendance Count: {row_count}", font = ('Verdana', 15, 'bold'),bg='lightgray').place(x=300, y=600)


def read():
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite.connect("Attendance " + current_date + ".db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tb1([ID] VARCHAR(225), [Name] VARCHAR(225), [Track] VARCHAR(225), [Year] VARCHAR(225), [Taken Class] VARCHAR(255), [Status] VARCHAR(255), [Count] INTEGER)""")
    cur.execute("SELECT * FROM tb1")
    aa = cur.fetchall()
    conn.commit()

    return aa


label_time = tk.Label(root, text="Current Date and Time", font=('Verdana', 18, 'bold'),bg='lightgray').place(x=98, y=485)

label_date_now = tk.Label(text="Current Date", font = ('Verdana', 15, 'bold'),bg='lightgray')
label_date_now.place(x=50, y=520)

label_time_now = tk.Label(text="Current Time", font = ('Verdana' ,15, 'bold'),bg='lightgray')
label_time_now.place(x=300, y=520)



#--------------ENTRY FIELDS------------------#

stud_id = tk.Label(root, text="Student ID: ", font=('Verdana', 15),bg='lightgray').place(x=35, y=150)
stud_numEntry = Entry(root, width=25, bd=2, font=('Verdana', 13))
stud_numEntry.place(x=200, y=155, height = 25)

stud_name = tk.Label(root, text="Student Name: ", font=('Verdana', 15),bg='lightgray').place(x=35, y=200)
stud_nameEntry = Entry(root, width=25, bd=2, font=('Verdana', 13))
stud_nameEntry.place(x=200, y=205, height = 25)


course = tk.Label(root, text='Track/Course:', font=('Verdana', 15),bg='lightgray')
course.place(x=35,y=245)
track = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
track.set("SELECTED TRACK")
track['values'] = ('BSCS DM', 'BSCS BA','BSIT - NS', 'BSIT BPO', 'BSIT WMAD', 'OTHERS')
track['state'] = 'readonly'
track.place(x=200, y=250, height=25)

year = tk.Label(root, text='Year:',font=('Verdana', 15),bg='lightgray' )
year.place(x=35,y=295)
year = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
year.set("YEAR LEVEL")
year['values'] = ('1st', '2nd','3rd', '4th')
year['state'] = 'readonly'
year.place(x=200, y=300, height=25)

taken_class = tk.Label(root, text='Take Class:',font=('Verdana', 15),bg='lightgray' )
taken_class.place(x=35,y=345)
taken_class = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
taken_class.set("TAKEN CLASS")
taken_class['values'] = ('Fundamentals of Programming', 'Database')
taken_class['state'] = 'readonly'
taken_class.place(x=200, y=350, height=25)

status = tk.Label(root, text='Status:',font=('Verdana', 15),bg='lightgray' )
status.place(x=35,y=398)
status = ttk.Combobox(root, width = 17,font=('Verdana', 10, 'bold'))
status.set("STATUS")
status['values'] = ('Member', 'Non-Member')
status['state'] = 'readonly'
status.place(x=200, y=400, height=25)

# row_count = count_rows_in_tree(my_tree)
# stud_count = tk.Label(root, text = row_count).place(x=1, y=500)


#----------------BUTTONS------------------#

reg_button = Button(text="Add Student", command = lambda: [check_in(), TREE()], font=('Verdana', 15, 'bold'), width=15, height=1, bg='SpringGreen4')
reg_button.place(x=35, y=435)

reg_button = Button(text="Check In", command = lambda: [update_count(), TREE()], font=('Verdana', 15, 'bold'), width=15, height=1, bg='SpringGreen4')
reg_button.place(x=285, y=435)


#-----------------TREE VIEW-----------------#
my_tree.tag_configure('orow', background="#EEEEEE", font=('Verdana', 10))
my_tree.place(x=570, y=90, height=490)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 10, 'bold'))

my_tree['columns'] = ("Student ID", "Student Name", "Track/Course", "Year", "Taken Class", "Status", "Count")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Student ID", anchor=CENTER, width=130)
my_tree.column("Student Name", anchor=CENTER, width=130)
my_tree.column("Track/Course", anchor=CENTER, width=130)
my_tree.column("Year", anchor=CENTER, width=100)
my_tree.column("Taken Class", anchor=CENTER, width=200)
my_tree.column("Status", anchor=CENTER, width=180)
my_tree.column("Count", anchor=CENTER, width=80)


my_tree.heading("Student ID", text="Student ID", anchor=CENTER)
my_tree.heading("Student Name", text="Student Name", anchor=CENTER)
my_tree.heading("Track/Course", text="Track/Course", anchor=CENTER)
my_tree.heading("Year", text="Year", anchor=CENTER)
my_tree.heading("Taken Class", text="Taken CLass", anchor=CENTER)
my_tree.heading("Status", text="Status", anchor=CENTER)
my_tree.heading("Count", text="Count", anchor=CENTER)



TREE()
update_clock()
root.mainloop()
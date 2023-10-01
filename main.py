from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

root = Tk()

root.title("STUDENT REG")
root.geometry('1350x700+0+0')
my_tree = ttk.Treeview(root)


title = tk.Label(root, text="PROGRAMMING CLUB ATTENDANCE", font=('Verdana', 20, 'bold'), border=12, relief=tk.GROOVE, bg='lightgray')
title.pack(side=tk.TOP,fill=tk.X)

details = tk.LabelFrame(root, text="STUDENT DETAILS", font=('Verdana', 20, 'bold'), relief= tk.GROOVE,bd=12, bg='lightgray')
details.place(x=20,y=90,width=500,height=440)

#treeFrame = tk.Frame(root, bd=12, bg='lightgray', relief=tk.GROOVE)
#treeFrame.place(x=600,y=90,width=720,height=575)

#--------------ENTRY FIELDS------------------#

stud_name = tk.Label(root, text="Student Name: ", font=('Verdana', 15),bg='lightgray').place(x=35, y=150)
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


#----------------BUTTONS------------------#

reg_button = Button(text="Check In", font=('Verdana', 15, 'bold'), width=17, height=1, bg='SpringGreen4')
reg_button.place(x=130, y=350)

#------------------FRAME-----------------#

# db_frame = tk.Frame(treeFrame,bg='lightgray',bd=11,relief=tk.GROOVE)
# db_frame.pack(fill=tk.BOTH,expand=TRUE)
my_tree.tag_configure('orow', background="#EEEEEE", font=('Verdana', 10))
my_tree.place(x=600, y=90, height=440)

#-----------------TREE VIEW-----------------#
style = ttk.Style()
style.configure("Treeview.Heading", font=('Verdana', 9, 'bold'))

my_tree['columns'] = ("Name", "Track/Course", "Year")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", anchor=CENTER, width=230)
my_tree.column("Track/Course", anchor=CENTER, width=230)
my_tree.column("Year", anchor=CENTER, width=230)

my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Track/Course", text="Track/Course", anchor=CENTER)
my_tree.heading("Year", text="Year", anchor=CENTER)

















root.bind('<Return>', reg_button)
root.mainloop()
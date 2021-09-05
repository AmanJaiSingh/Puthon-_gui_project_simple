from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import json


win=Tk()

win.title("Student Database")
win.iconbitmap("C:/Users/Aman Jai Singh/python/GUI_Project/New folder/logo.ico")
win.geometry("1520x815+0+0")
win.resizable(height=0,width=0)
win.configure(background="#252156")


lable1=Label(win,text="EXPLORE",bg="#252156",fg="red",font="none 32 bold").place(x=10,y=10)
lable2=Label(win,text="YOUR",bg="#252156",fg="white",font="none 32 bold").place(x=10,y=55)
lable3=Label(win,text="POTENTIAL",bg="#252156",fg="red",font="none 32 bold").place(x=10,y=100)

lable4=Label(win,text="CHITKARA UNIVERSITY",bg="#252156",fg="white",font="none 28 bold").place(x=640,y=10)

lable5=Label(win,text="STUDENT DATABASE",bg="#252156",fg="white",font="none 28 bold").place(x=640,y=150)

lable6=Label(win,text="Department of Computer Science & Engineering",bg="#252156",fg="white",font="none 18 bold").place(x=545,y=750)
#-----------Chitkara Logo--------------

logo=ImageTk.PhotoImage(Image.open('New folder/Chitkara.jpg'))
logo_label=Label(image=logo)
logo_label.place(x=1400,y=3)
#--------------my photo-----------------------
Dp=ImageTk.PhotoImage(Image.open('New folder/Aman.jpg'))
Dp_label=Label(image=Dp,borderwidth=0)
Dp_label.place(x=10,y=300)

Label(win,text="Aman Jai Singh",font="Montserrat 20",fg="red",bg="#252156").place(x=20,y=620)
Label(win,text="3639",font="Montserrat 20",fg="red",bg="#252156").place(x=220,y=620)
Label(win,text="Batch-3 Group-155",font="Montserrat 20",fg="red",bg="#252156").place(x=20,y=660)
#---------------------------------Creating Frame--------------------------
frame=LabelFrame(win,text="",padx=10,pady=10,height=500,width=1100)
frame.place(x=325,y=200,height=500,width=1100)

#------------------------------Creating notebook in frame-----------------
nb=ttk.Notebook(frame)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
page3=ttk.Frame(nb)
page4=ttk.Frame(nb)
page5=ttk.Frame(nb)
page6=ttk.Frame(nb)

#-----------------Nameing notebook ------------------------------------

nb.add(page1,text="New Student")
nb.add(page2,text="Display")
nb.add(page3,text="Course Creation")
nb.add(page4,text="Display Course")
nb.add(page5,text="Course Allocation")
nb.add(page6,text="Student Course")

nb.pack(expand=1,fill="both")
#-------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------Screen 1-----------------------------------------------------------
#---------funcitons page 1-------------


#Making columns -------------------- copied from master class
for i in range(6):
    page1.columnconfigure(i,weight=1)

#----------ROW 1------------
Label_name=Label(page1,text="Enter your name",font="none 13").grid(row=0,column=0,sticky="e",pady=10)
entry_name=Entry(page1,width=80,borderwidth=0.5)
entry_name.grid(row=0,column=3,sticky="e")

#---------ROW 2-------------
Label_rollno=Label(page1,text="Enter your Rollno",font="none 13").grid(row=2,column=0,sticky="e",pady=10)
entry_rollno=Entry(page1,width=80,borderwidth=0.5)
entry_rollno.grid(row=2,column=3,sticky="e")

#--------ROW 3--------------
Label_gender=Label(page1,text="Choose your Gender",font="none 13").grid(row=3,column=0,sticky="e",pady=10)

gender=StringVar()
Radiobutton(page1,text="Male",value="Male",variable=gender,tristatevalue=0,font="none 13").grid(row=3,column=3,columnspan=1,padx=150,pady=10,sticky='w')
Radiobutton(page1,text="Female",value="Female",variable=gender,tristatevalue=0,font="none 13").grid(row=3,column=3,padx=100,pady=10,sticky='e')

#---------ROW 4------------

Label_Address=Label(page1,text="Address for Correspondence",font="none 13").grid(row=4,column=0,sticky="e",pady=10)
entry_address=Entry(page1,width=80,borderwidth=0.5)
entry_address.grid(row=4,column=3,sticky="e")

#--------ROW 5-------------
Label_phoneno=Label(page1,text="Phone no",font="none 13").grid(row=5,column=0,sticky="e",pady=10)
entry_Phoneno=Entry(page1,width=80,borderwidth=0.5)
entry_Phoneno.grid(row=5,column=3,sticky="e")

#-------ROW 6--------------

Label_Batchno=Label(page1,text="Your Batch",font="none 13").grid(row=6,column=0,sticky="e",pady=10)

batch_no=StringVar()
batch=ttk.Combobox(page1,state='readonly',width=18,textvariable=batch_no)

batch['values']=('2020','2019','2018','2017')
batch.grid(row=6,column=3,sticky='e',pady=10)

batch.current(0)

#--------ROW 7------------

Label_hostel=Label(page1,text="Hostel[Y/N]",font="none 13").grid(row=7,column=0,sticky="e",pady=10)

hostel=StringVar()
hostel_checkbox=Checkbutton(page1,text="Yes",variable=hostel,onvalue='yes',offvalue='no',height=2,width=12)
hostel_checkbox.grid(row=7,column=2,columnspan=2,sticky='e',pady=10)
hostel_checkbox.deselect()


def saaf():
    entry_name.delete(0,END)
    entry_rollno.delete(0,END)
    entry_address.delete(0,END)
    entry_Phoneno.delete(0,END)

def clear_data():
    messagebox.showinfo("Status","Record Cleared")
    saaf()

def submit():
    messagebox.showinfo("Save", "Record added")
    saaf()
def save_del():
    r1=entry_rollno.get()
    r2=entry_name.get()
    r3=gender.get()
    r4=entry_address.get()
    r5=entry_Phoneno.get()
    r6=batch_no.get()
    r7=hostel.get()
    r8=False
    if r7=='yes':
        r8=True
    submit()
    r={"Rollno":r1,"Name":r2,"Gender":r3,"address":r4,"Phone no":r5,"Batch": " Batch "+r6,
    "Hostel":r8
    }
    with open('Student.json') as a:
        data=json.load(a)
    data["Students"].append(r)
    serialise_data=json.dumps(data,indent=2)

    with open('Student.json','w') as a:
        json.dump(data,a,indent=1)


#------------BUUTTONS----------------

button_save=Button(page1,text="Save",width=20,height=2,command=save_del).grid(row=8,column=1,sticky="e")
button_clear=Button(page1,text="Clear",width=20,height=2,command=clear_data).grid(row=8,column=2,sticky="w")

#---------------------------Screen 2--------------------------------------------------------------
#----------USING TREEVIEW WIDGET---------
scr_2_tree=ttk.Treeview(page2)

scr_2_tree['columns']=('RollNo','Name','Gender','Address','Phoneno','Batch','Hostel')

# Formate Coulmns
scr_2_tree.column('#0',width=0,minwidth=0)
scr_2_tree.column('RollNo',width=120,minwidth=80)
scr_2_tree.column('Name',width=120,minwidth=120)
scr_2_tree.column('Gender',width=120,minwidth=80)
scr_2_tree.column('Address',width=120,minwidth=120)
scr_2_tree.column('Phoneno',width=120,minwidth=120)
scr_2_tree.column('Batch',width=120,minwidth=120)
scr_2_tree.column('Hostel',width=120,minwidth=80)

#Headings
scr_2_tree.heading('#0',text="",anchor=W)
scr_2_tree.heading('RollNo',text="RollNO",anchor=W)
scr_2_tree.heading('Name',text="Name",anchor=W)
scr_2_tree.heading('Gender',text="Gender",anchor=W)
scr_2_tree.heading('Address',text="Address",anchor=W)
scr_2_tree.heading('Phoneno',text="PhoneNo",anchor=W)
scr_2_tree.heading('Batch',text="Bacth",anchor=W)
scr_2_tree.heading('Hostel',text="Hostel",anchor=W)

#Display

def dis():
    scr_2_tree.delete(*scr_2_tree.get_children())
    with open('Student.json') as a:
        data=json.load(a)
    temp_iid=0
    for i in data['Students']:
        scr_2_tree.insert(parent='',index='end',iid=temp_iid,text='',values=(i['Rollno'],i['Name'],i['Gender'],i['address'],i['Phone no'],i['Batch'],i['Hostel']))

        temp_iid+=1

    scr_2_tree.place(x=0,y=0,width=1100)
#----------BUTTON--------------------
Button(page2,text="Display",bg="#3175d2",fg='white',command=dis).place(x=340,y=340)

#-------------------------Screen 3-----------------------------------------------------------------

for i in range(6):
    page3.columnconfigure(i,weight=1)

#--------------ROW 1---------------
lable_course_id=Label(page3,text="Course ID",font="none 13").grid(row=0,column=1,sticky="e",pady=30)
entry_course_id=Entry(page3,width=80,borderwidth=0.5)
entry_course_id.grid(row=0,column=3,sticky="e")

#-------------ROW 2----------------

lable_course_name=Label(page3,text="Course Name",font="none 13").grid(row=1,column=1,sticky="e")
entry_course_name=Entry(page3,width=80,borderwidth=0.5)
entry_course_name.grid(row=1,column=3,sticky="e")
#--------------------
def saaf2():
    entry_course_id.delete(0,END)
    entry_course_name.delete(0,END)

def clear_data2():
    messagebox.showinfo("Status","Claeard")
    saaf2()

def submit2():
    messagebox.showinfo("Save","Course added")
    saaf2()
def course_add():
    v1=entry_course_id.get()
    v2=entry_course_name.get()
    l={"CourseID":v1,"CourseName":v2}
    submit2()
    with open('Course.json') as a:
        data2=json.load(a)
    data2["Courses"].append(l)
    serialise_data=json.dumps(data2,indent=2)

    with open('Course.json','w') as a:
        json.dump(data2,a,indent=1)




#---------------BUTTONS---------------
button_save2=Button(page3,text="Save",width=20,height=2,command=course_add).grid(row=8,column=2,sticky="e",pady=30)
button_clear2=Button(page3,text="Clear",width=20,height=2,command=clear_data2).grid(row=8,column=3,sticky="e",pady=30)


#----------------Screen 4-----------------------------------------------------------------------
#---------USING TREEVIEW WIDGET--------------------
scr_4_tree=ttk.Treeview(page4)

scr_4_tree['columns']=('CourseID','CourseName')

#Formate
scr_4_tree.column('#0',width=0,minwidth=0)
scr_4_tree.column('CourseID',width=550,minwidth=550)
scr_4_tree.column('CourseID',width=550,minwidth=550)
# Create Headings
scr_4_tree.heading('#0',text="",anchor=W)
scr_4_tree.heading('CourseID',text="CourseID",anchor=W)
scr_4_tree.heading('CourseName',text="CourseName",anchor=W)

#-------------DISPLAY--------------

def dis2():
    scr_4_tree.delete(*scr_4_tree.get_children())

    with open('Course.json') as p:
        data3=json.load(p)
    
    temp_iid=0
    for i in data3['Courses']:
        scr_4_tree.insert(parent='',index='end',iid=temp_iid,text='',values=(i["CourseID"],i["CourseName"]))
        temp_iid+=1
    
    scr_4_tree.place(x=0,y=0,width=1100)

#------------BUTTON-----------------
Button(page4,text="Display",bg='black',fg='white',command=dis2).place(x=350,y=300)

#-------------------Screen 5-------------------------------------------------------------------------

for i in range(6):
    page5.columnconfigure(i,weight=1)
#-------------ROW 1------------
lable_Student_rollno=Label(page5,text="Student Rollno",font="none 13").grid(row=0,column=1,sticky="e",pady=40)
entry_student_rollno=Entry(page5,width=80,borderwidth=0.5)
entry_student_rollno.grid(row=0,column=3,sticky="e")

#------------ROW 2--------------
lable_course_Name=Label(page5,text="Course Name",font="none 13").grid(row=1,column=1,sticky="e")
Course_name=StringVar()
Course_allocate=ttk.Combobox(page5,state='readonly',width=50,textvariable=Course_name)

with open('Course.json') as k:
    data3=json.load(k)

course=[]
for i in data3['Courses']:
    course.append(i['CourseName'])

Course_allocate['value']=course

#-----------
def refresh():
    global Course_name
    global Course_allocate
    global course
    with open('Course.json') as k:
        data3=json.load(k)
    course=[]
    for i in data3['Courses']:
        course.append(i['CourseName'])
    
    Course_allocate['values']=course

Course_allocate.grid(row=1,column=3,pady=10,columnspan=2)
Course_allocate.current(4)


def saaf3():
    entry_student_rollno.delete(0,END)

def clear_data3():
    messagebox.showinfo("Status","Cleared")
    saaf3()

def submit3():
    messagebox.showinfo("Save","Course Allotted")
    saaf3()

def get_CourseID(Q):
    with open('Course.json') as j:
        data5=json.load(j)
    for i in data5['Courses']:
        if i['CourseName']==Q:
            return i['CourseID']

def course_add2():
    a1=entry_student_rollno.get()
    a2=Course_name.get()
    a3=get_CourseID(a2)
    w={"Rollno":a1,"CourseID":a3}
    submit3()
    with open('Course Allocation.json') as y:
        data6=json.load(y)
    data6['Stu_Course'].append(w)
    serialise_data=json.dumps(data6,indent=2)
    with open('Course Allocation.json','w') as y:
        json.dump(data6,y,indent=1)





#-------------------BUTTONS----------------

button_Allocate=Button(page5,text="Allocate",width=20,height=2,command=course_add2).grid(row=8,column=2,sticky="e",pady=40)
button_clear3=Button(page5,text="Clear",width=20,height=2,command=clear_data3).grid(row=8,column=3,sticky="e",pady=40)
Button(page5,text="Refresh",fg="White",bg="Darkblue",command=refresh,width=20,height=2).place(x=400,y=350)

#--------------------------------------Screen 6---------------------------------

#-------------------USING TREEVIEW WIDGET---------
scr_6_tree=ttk.Treeview(page6)

scr_6_tree['columns']=('Rollno','CourseID')

#formate Columns
scr_6_tree.column('#0',width=0,minwidth=0)
scr_6_tree.column('Rollno',width=550,minwidth=80)
scr_6_tree.column('CourseID',width=550,minwidth=120)

#Heading
scr_6_tree.heading('#0',text='',anchor=W)
scr_6_tree.heading('Rollno',text='RollNO',anchor=W)
scr_6_tree.heading('CourseID',text='CourseID',anchor=W)


def dis3():
    scr_6_tree.delete(*scr_6_tree.get_children())

    with open('Course Allocation.json') as m:
        data7=json.load(m)
        
    temp_iid=0
    for i in data7['Stu_Course']:
        scr_6_tree.insert(parent='',index='end',iid=temp_iid,values=(i['Rollno'],i['CourseID']))
        temp_iid+=1
    

    scr_6_tree.place(x=0,y=0,width=1100)

#-------------------BUTTON--------------
Button(page6,text='Display',bg='black',fg='white',command=dis3).place(x=400,y=350)




#-----------------------------code ends here------------------------------------------------------
win.mainloop()
#----------------------------Finally-The-End--------------------------------------
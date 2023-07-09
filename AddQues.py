from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
qcount=1
def QuesRegister():
    global qcount
    ques = str(bookInfo1.get())
    op1 = str(bookInfo2.get())
    op2 = str(bookInfo3.get())
    op3 = str(bookInfo4.get())
    op4 = str(bookInfo5.get())
    cor_op = int(bookInfo6.get())

    
    insertques = "insert into QuesTable values(%s,%s,%s,%s,%s,%s,%s)"
    values = qcount,ques, op1,op2, op3,op4,cor_op
    try:
        cur.execute(insertques,values)
        con.commit()
        qcount+=1
        messagebox.showinfo('Success',"Questions added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")


    root.destroy()
    
def addQues():

    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,bookInfo6,Canvas1,con,cur,bookTable,root

    root = Tk()
    root.title("Add Questions")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = ""  # insert mysql password here
    mydatabase = ""  # insert database used

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="saddle brown")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Questions", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.45)
        
    #
    lb1 = Label(labelFrame,text="QUESTION : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.1, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.1)
        
    #
    lb2 = Label(labelFrame,text="Option 1 : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.1)
        
    #
    lb3 = Label(labelFrame,text="Option 2 : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.1)
        
    #
    lb4 = Label(labelFrame,text="Option 3 : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.55, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.1)

    #
    lb5 = Label(labelFrame, text="Option 4 : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)

    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.1)

    #
    lb6 = Label(labelFrame, text="Correct Opt:\n(1/2/3/4)", bg='black', fg='white')
    lb6.place(relx=0.05, rely=0.85, relheight=0.18)

    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3, rely=0.85, relwidth=0.62, relheight=0.1)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=QuesRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
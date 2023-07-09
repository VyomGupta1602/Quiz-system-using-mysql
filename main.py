from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from AddQues import *
from Showques import *


mypass = ""  #insert mysql password here
mydatabase="" #insert the database here

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
cur.execute("show tables")
r=('QuesTable',)
if r not in cur :
    cur.execute("create table QuesTable( Sno int,Ques varchar(100) primary key, Opt1 varchar(22), Opt2 varchar(22),Opt3 varchar(22),Opt4 varchar(22), Correct_Opt int(1))")

cur.execute("show tables")

root = Tk()
root.title("Quizzer")
root.minsize(width=400,height=400)
root.geometry("600x500")

same=True
n=0.25

def quit():
    root.destroy()
    import file
def rest():
    cur = con.cursor()
    cur.execute("delete from QuesTable")
    con.commit()
def des():
    root.destroy()


background_image =Image.open("bgi.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Quizzer", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Questions",bg='black', fg='Black', command=addQues)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Show Questions",bg='black', fg='Black', command=View)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="Start",bg='black', fg='Black', command=quit)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Reset",bg='black', fg='Black', command =rest)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="QUIT",bg='black', fg='Black', command = des)

btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()


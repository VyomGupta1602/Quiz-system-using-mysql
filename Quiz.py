
from tkinter import *


import pymysql
q=[]
options = []
a = []
mypass = ""  #insert mysql password here
mydatabase=""  #insert database used

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
cur.execute("SELECT * from QuesTable order by Sno")

myresult = cur.fetchall()

for x in myresult:
  q.append(x[1])
  t=[x[2],x[3],x[4],x[5]]
  options.append(t)
  a.append(x[6])

counter=1
resultlist=[]
k=""
def quiz():
    class Quiz:
        def __init__(self, master):
            self.opt_selected = IntVar()
            self.qn = 0
            self.correct = 0
            self.ques = self.create_q(master, self.qn)
            self.opts = self.create_options(master, 4)
            self.display_q(self.qn)
            self.button = Button(master, text="Quit", command=root.destroy)
            self.button.pack(side=BOTTOM)
            self.button = Button(master, text="Next", command=self.next_btn)
            self.button.pack(side=BOTTOM)

        def create_q(self, master, qn):
            w = Label(master, text=q[qn])
            w.pack(side=TOP)
            return w

        def create_options(self, master, n):
            b_val = 0
            b = []
            while b_val < n:
                btn = Radiobutton(master, text="", variable=self.opt_selected, value=b_val+1)
                b.append(btn)
                btn.pack(side=TOP, anchor="w")
                b_val = b_val + 1
            return b

        def display_q(self, qn):
            b_val = 0
            self.opt_selected.set(0)
            self.ques['text'] = q[qn]
            for op in options[qn]:
                self.opts[b_val]['text'] = op
                b_val = b_val + 1

        def check_q(self, qn):
            global counter
            if self.opt_selected.get() == a[qn]:
                return True
            return False

        def print_results(self):
            global resultlist
            global k

            k = "Score: " + str(self.correct) + "/" + str(len(q))

            def resultwin():
                global resultlist
                global k
                class MyWindow:
                    def __init__(self, win):
                        global resultlist
                        global k

                        u = 0

                        def mainmenu():
                            root.destroy()
                            window.destroy()
                            import file2


                        for x in range(0,len(resultlist),2):
                            o = resultlist[x]
                            l = resultlist[x+1]

                            self.lbl1 = Label(win, text=o, fg="black")
                            self.lbl1.place(x=50, y=(50+u))
                            self.lbl2 = Label(win, text=l, fg="black")
                            self.lbl2.place(x=50, y=(70 + u))
                            u += 50
                        self.lbl3 = Label(win, text=k, fg="black")
                        self.lbl3.place(x=50, y=(100 + u))
                        self.btn1 = Button(win, text="Return",fg='black', command=mainmenu)
                        self.btn1.place(x=50 , y=(150 + u))
                window = Tk()
                mywin = MyWindow(window)
                window.title('Result')
                window.geometry("500x320+10+10")

                window.mainloop()

            resultwin()

        def next_btn(self):
            global counter
            global resultlist
            if self.check_q(self.qn):
                y = a[counter - 1]
                p=options[counter - 1][y-1]
                res="Q"+str(counter)+": "+str(q[counter-1])+"  >>> Correct"
                res2 = "Correct Answer: " + str(p)
                resultlist.append(res)
                resultlist.append(res2)
                self.correct += 1
                counter+=1
            else:
                y=int(a[counter-1])
                p=options[counter-1][y-1]
                res="Q"+str(counter)+": "+str(q[counter-1])+"  >>> Wrong"
                res2="Correct Answer: "+str(p)
                resultlist.append(res)
                resultlist.append(res2)
                counter+=1

            self.qn = self.qn + 1
            if self.qn >= len(q):
                self.print_results()
            else:
                self.display_q(self.qn)


    root = Tk()
    root.title('Quiz')
    root.geometry("500x300")
    app = Quiz(root)
    root.mainloop()

quiz()
counter=0
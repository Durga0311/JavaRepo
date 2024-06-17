import cv2, sys, numpy
import os
from datetime import date
import mysql.connector
import tkinter
from tkinter import messagebox
def enroll():
    db=1
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="student")
        c=mydb.cursor()
    except:
        messagebox.showwarning("WARNING","Database connection failed")
        db=0
    if db!=0:
        r=tkinter.Tk()
        r.title(string="REGISTRATION")
        r.geometry("400x400")
        r.configure(bg="black")
        t1=tkinter.Text(r,height=3,width=30)
        t2=tkinter.Text(r,height=3,width=30)
        t3=tkinter.Text(r,height=3,width=30)
        t4=tkinter.Text(r,height=3,width=30)
        l1=tkinter.Label(r,text="enter your roll number:",bg="lightgreen")
        l2=tkinter.Label(r,text="enter your name:",bg="lightgreen")
        l3=tkinter.Label(r,text="enter your branch:",bg="lightgreen")
        l4=tkinter.Label(r,text="enter your gender:",bg="lightgreen")
        l1.grid(row=0,column=0)
        t1.grid(row=0,column=1)
        l2.grid(row=1,column=0)
        t2.grid(row=1,column=1)
        l3.grid(row=2,column=0)
        t3.grid(row=2,column=1)
        l4.grid(row=3,column=0)
        t4.grid(row=3,column=1)
        def click():
            rno=t1.get(1.0,"end-1c")
            na=t2.get(1.0,"end-1c")
            if t3.get(1.0,"end-1c")!="":
                branch=t3.get(1.0,"end-1c")
            else:
                age=0
            gender=t4.get(1.0,"end-1c")
            if len(rno)==0:
                messagebox.showwarning("WARNING","please enter your registration number")
            elif len(rno)<10:
                messagebox.showwarning("WARNING","please enter a valid registration number")
            elif len(na)==0:
                messagebox.showwarning("WARNING","please enter your name")
            elif len(branch)==0:
                messagebox.showwarning("WARNING","please enter valid age")
            elif gender=="":
                messagebox.showwarning("WARNING","please enter your gender")
            elif (gender.lower()!="male")and(gender.lower()!="female"):
                messagebox.showwarning("WARNING","please enter a valid gender")
            else:
                s="insert into attendance(NAME,ROLL_NO,BRANCH,GENDER) values(%s,%s,%s,%s)"
                values=(na,rno,branch,gender)
                c.execute(s,values)
                pd="datasets"
                directory=str(rno)
                path=os.path.join(pd,directory)
                haar_file = 'haarcascade_frontalface_default.xml'	
                if not os.path.isdir(path):
                    os.mkdir(path)
                (width, height) = (130, 100)
                face_cascade = cv2.CascadeClassifier(haar_file)
                webcam = cv2.VideoCapture(0)
                count = 1
                while count < 30:
                    (_, im) = webcam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        face = gray[y:y + h, x:x + w]
                        face_resize = cv2.resize(face, (width, height))
                        cv2.imwrite('% s/% s.png' % (path, count), face_resize)
                    count += 1
                    cv2.imshow('OpenCV', im)
                    key = cv2.waitKey(10)
                    if key == 27:
                        break
                webcam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("CONFIRMATION","registration is completed")
                r.destroy()
                mydb.commit()
        ba=tkinter.Button(r,text="SUBMIT",bg="blue",command=click)
        ba.grid(row=4)
        r.mainloop()
def attendance():
    db=1
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="student")
        cur=mydb.cursor()
    except:
        messagebox.showwarning("WARNING","database connection failed")
        db=0
    if db!=0:
        file1 = open("myfile.txt", "r")
        a=file1.read()
        file1.close()
        x=str(date.today())
        d=x[-2:]+'_'+x[-5:-3]
        if x not in a:
            s="alter table attendance add "+d+" varchar(10)"
            d=[d]
            d=tuple(d)
            cur.execute(s)
            mydb.commit()
            file1 = open("myfile.txt", "a")
            file1.write(x+'\n')
            file1.close()
        size = 4
        c=0
        haar_file = 'haarcascade_frontalface_default.xml'
        datasets = 'datasets'
        messagebox.showinfo('TAKING ATTENDANCE','Recognizing Face Please Be in sufficient Lights...')
        (images, labels, names, id) = ([], [], {}, 0)
        sub=[]
        n=0
        for (subdirs, dirs, files) in os.walk(datasets):
             for subdir in dirs:
                  sub.append(subdir)
                  n=n+1
                  names[id]=subdir
                  id=id+1
        id=0
        flag=0
        if len(sub)==0:
             exit()
        for i in range(n):
             c=0
             p=0
             images=[]
             labels=[]
             subjectpath = os.path.join(datasets,sub[i])
             for filename in os.listdir(subjectpath):
                  path = subjectpath + '/' + filename
                  label = id
                  images.append(cv2.imread(path, 0))
                  labels.append(int(label))
             id += 1
             (width, height) = (130, 100)
             (images, labels) = [numpy.array(lis) for lis in [images, labels]]
             model = cv2.face.LBPHFaceRecognizer_create()
             model.train(images, labels)
             face_cascade = cv2.CascadeClassifier(haar_file)
             webcam = cv2.VideoCapture(0)
             while True:
                  (_, im) = webcam.read()
                  gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                  for (x, y, w, h) in faces:
                       cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                       face = gray[y:y + h, x:x + w]
                       face_resize = cv2.resize(face, (width, height))
                       prediction = model.predict(face_resize)
                       cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
                       if prediction[1]<80:
                            c=c+1
                       else:
                           p=p+1

                  cv2.imshow('OpenCV', im)
                  key = cv2.waitKey(10)
                  if key == 27:
                       break
                  if c==20:
                       flag=1
                       k=str(sub[i])
                       print(k)
                       s="update attendance set "+d+"='yes' where ROLL_NO='"+k+"'"
                       cur.execute(s)
                       mydb.commit()
                       m=i
                       break
                  if p==20:
                      break
             if flag==1:
                  break
        if flag==1:
            l=[sub[m]]
            value=tuple(l)
            s="select * from attendance where ROLL_no=%s"
            cur.execute(s,value)
            h=cur.fetchall()
            if h:
                webcam.release()
                cv2.destroyAllWindows()
                for i in h:
                     text="NAME:"+i[0].upper()+"\nREG.NO:"+i[1].upper()+"\nBRANCH:"+str(i[2])+"\nGENDER:"+i[3].upper()
                     messagebox.showinfo("DETAILS",text)
        else:
            cv2.destroyAllWindows()
            messagebox.showwarning("ALERT","you are not registered")
my=tkinter.Tk()
my.title(string="STUDENT ATTANDENCE SYSTEM")
my.geometry('400x400')
my.configure(bg="skyblue")
b1=tkinter.Button(my,text="REGISTER",width=25,bg="green",command=enroll)
b2=tkinter.Button(my,text="ATTENDANCE",width=25,bg="red",command=attendance)
b1.place(x=150,y=200)
b2.place(x=150,y=250)
my.mainloop()
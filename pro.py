
import image_slicer
import cv2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from cryptography.fernet import Fernet

global key
global cipher_suite

key = b'fNSIxUWutwwBpY9wRbCoAoZtv5NRM1_2G-ILXxLOWVc='
cipher_suite = Fernet(key)


def mainfn():
    global seq
    seq=[]
    window = Tk()
    window.geometry('200x200')
    Btn1 = Button(text="Login", command=login, height=1, width=15).grid(row = 1, column = 5)
    btn2 = Button(window, text = "Registration", command = registration, height=1, width=15).grid(row = 3, column = 5)
    btn = Button(window, text = 'Close', bd = '5', command =window.destroy, height=1, width=7).grid(row = 10, column = 10)
    
    window.mainloop()

def username(u):
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="mydatabase")

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE {tab} (img_loc VARCHAR(255), grid_loc VARCHAR(10))".format(tab=u))
    mycursor.close()
    mydb.commit()

def enter_into_user_table(u,n,s):
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="mydatabase")
    
    mycursor = mydb.cursor()
    sql = "insert into {tab}(img_loc,grid_loc)VALUES (%s, %s)".format(tab=u)
    val = (n, s)
    mycursor.execute(sql, val)
    #mycursor.execute("insert into {tab}(img_loc,grid_loc)VALUES (%s, %s)".format(tab=u),val = (n, s))
    mycursor.close()
    mydb.commit()
    

def getmessage():
    if (seq == myresult1[0] ):
        messagebox.showinfo("Success","login success")
            
    else:
        #print("not match")
        messagebox.showerror("Error", "Wrong password")
        #Label(log, text="Login failed (wrong password)", fg="green", font=("calibri", 11)).grid(row = 8 , column = 5)

    

#CODE FOR IMAGE SEQ

def press(n):
    seq.append(n)
    
            
    
def save():
    root1= tk.Tk()
    root1.geometry('1000x1000')   
    global img1
    
    
    # image seq defination
    def press(n):
        seq.append(n)
        

    
    location = loc.split('/')
    l = location[-1]
    t = image_slicer.slice(l , 4)
    
    t = list(t)
    img1 =[]
    
    for i in range(0,len(t)):
        t[i] = str(t[i])
        temp = t[i].split('-')
        temp = temp[1].strip('>')
        temp = temp.strip(' ')
        img1.append(temp)
    
    
    #### giiving the 36 grid to select sequence
    
    
    Label(root1, text = "select the sequence").grid(row = 170, column = 150)
    
    button1 = Button(root1, text=' 1 ', fg='black', bg='red', command= lambda: press(1), height=1, width=7) 
    button1.grid(row=220, column=0) 
    button2 = Button(root1, text=' 2 ', fg='black', bg='red', command= lambda: press(2), height=1, width=7) 
    button2.grid(row=220, column=1)

    button3 = Button(root1, text=' 3 ', fg='black', bg='red', command= lambda:press(3), height=1, width=7) 
    button3.grid(row=220, column=2)
    button4 = Button(root1, text=' 4 ', fg='black', bg='red', command= lambda:press(4), height=1, width=7) 
    button4.grid(row=220, column=3)
    button5 = Button(root1, text=' 5 ', fg='black', bg='red', command= lambda:press(5), height=1, width=7) 
    button5.grid(row=220, column=4)
    button6 = Button(root1, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
    button6.grid(row=220, column=5)
    
    button7 = Button(root1, text=' 7 ', fg='black', bg='red', command= lambda:press(7), height=1, width=7) 
    button7.grid(row=221, column=0)
    button8 = Button(root1, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
    button8.grid(row=221, column=1)
    button9 = Button(root1, text=' 9 ', fg='black', bg='red', command= lambda:press(9), height=1, width=7) 
    button9.grid(row=221, column=2)
    button10 = Button(root1, text=' 10 ', fg='black', bg='red', command=lambda: press(10), height=1, width=7) 
    button10.grid(row=221, column=3)
    button11 = Button(root1, text=' 11 ', fg='black', bg='red', command= lambda:press(11), height=1, width=7) 
    button11.grid(row=221, column=4)
    button12 = Button(root1, text=' 12 ', fg='black', bg='red', command= lambda:press(12), height=1, width=7) 
    button12.grid(row=221, column=5)
    
    button13 = Button(root1, text=' 13 ', fg='black', bg='red', command=lambda: press(13), height=1, width=7) 
    button13.grid(row=222, column=0)
    button14 = Button(root1, text=' 14 ', fg='black', bg='red', command= lambda:press(14), height=1, width=7) 
    button14.grid(row=222, column=1)
    button15 = Button(root1, text=' 15 ', fg='black', bg='red', command= lambda:press(15), height=1, width=7) 
    button15.grid(row=222, column=2)
    button16 = Button(root1, text=' 16 ', fg='black', bg='red', command=lambda: press(16), height=1, width=7) 
    button16.grid(row=222, column=3)
    button17 = Button(root1, text=' 17 ', fg='black', bg='red', command= lambda:press(17), height=1, width=7) 
    button17.grid(row=222, column=4)
    button18 = Button(root1, text=' 18 ', fg='black', bg='red', command=lambda: press(18), height=1, width=7) 
    button18.grid(row=222, column=5)
    
    button19 = Button(root1, text=' 19 ', fg='black', bg='red', command=lambda: press(19), height=1, width=7) 
    button19.grid(row=223, column=0)
    button20 = Button(root1, text=' 20 ', fg='black', bg='red', command= lambda:press(20), height=1, width=7) 
    button20.grid(row=223, column=1)
    button21 = Button(root1, text=' 21 ', fg='black', bg='red', command=lambda: press(21), height=1, width=7) 
    button21.grid(row=223, column=2)
    button22 = Button(root1, text=' 22 ', fg='black', bg='red', command= lambda:press(22), height=1, width=7) 
    button22.grid(row=223, column=3)
    button23 = Button(root1, text=' 23 ', fg='black', bg='red', command= lambda:press(23), height=1, width=7) 
    button23.grid(row=223, column=4)
    button24 = Button(root1, text=' 24 ', fg='black', bg='red', command= lambda:press(24), height=1, width=7) 
    button24.grid(row=223, column=5)
    
    button25 = Button(root1, text=' 25 ', fg='black', bg='red', command= lambda:press(25), height=1, width=7) 
    button25.grid(row=224, column=0)
    button26 = Button(root1, text=' 26 ', fg='black', bg='red', command=lambda: press(26), height=1, width=7) 
    button26.grid(row=224, column=1)
    button27 = Button(root1, text=' 27 ', fg='black', bg='red', command=lambda: press(27), height=1, width=7) 
    button27.grid(row=224, column=2)
    button28 = Button(root1, text=' 28 ', fg='black', bg='red', command= lambda:press(28), height=1, width=7) 
    button28.grid(row=224, column=3)
    button29 = Button(root1, text=' 29 ', fg='black', bg='red', command= lambda:press(29), height=1, width=7) 
    button29.grid(row=224, column=4)
    button30 = Button(root1, text=' 30 ', fg='black', bg='red', command= lambda:press(30), height=1, width=7) 
    button30.grid(row=224, column=5)
    
    button31 = Button(root1, text=' 31 ', fg='black', bg='red', command=lambda: press(31), height=1, width=7) 
    button31.grid(row=225, column=0)
    button32 = Button(root1, text=' 32 ', fg='black', bg='red', command= lambda:press(32), height=1, width=7) 
    button32.grid(row=225, column=1)
    button33 = Button(root1, text=' 33 ', fg='black', bg='red', command=lambda: press(33), height=1, width=7) 
    button33.grid(row=225, column=2)
    button34 = Button(root1, text=' 34 ', fg='black', bg='red', command=lambda: press(34), height=1, width=7) 
    button34.grid(row=225, column=3)
    button35 = Button(root1, text=' 35 ', fg='black', bg='red', command=lambda: press(35), height=1, width=7) 
    button35.grid(row=225, column=4)
    button36 = Button(root1, text=' 36 ', fg='black', bg='red', command= lambda:press(36), height=1, width=7) 
    button36.grid(row=225, column=5)
    
    #Button(gui, text = "submit",command = getInput).grid(row = 15 , column = 15)
    Button(root1, text = 'Close', bd = '5', command = root1.destroy).grid(row = 230, column =160) 
    

    ### printing the images 
    
    
    Label(root1, text = "fisrt index").grid(row = 0, column = 10)
    im1 = ImageTk.PhotoImage(Image.open(img1[0]).resize((50,50)))
    panel = tk.Label(root1, image = im1).grid(row = 0 , column = 15)
    
    Label(root1, text = "second index").grid(row = 55, column = 10)
    im2 = ImageTk.PhotoImage(Image.open(img1[1]).resize((50,50)))
    panel = tk.Label(root1, image = im2).grid(row = 55 , column = 15)
    
    Label(root1, text = "third index").grid(row = 110, column = 10)
    im3 = ImageTk.PhotoImage(Image.open(img1[2]).resize((50,50)))
    panel = tk.Label(root1, image = im3).grid(row = 110 , column = 15)
    
    Label(root1, text = "fourth index").grid(row = 165, column = 10)
    im4 = ImageTk.PhotoImage(Image.open(img1[3]).resize((50,50)))
    panel = tk.Label(root1, image = im4).grid(row = 165 , column = 15)
        

    #Button(root1, text = "select sequence",command = img_seq).pack()
    
    

    root1.mainloop()

def registration():
    root = Tk()
    root.geometry('1000x1000')
    global seq 
    global encrypted_text
    seq =[]
    
    
    Label(root, text = "First name").grid(row = 0, sticky = W)
    Label(root, text = "Last name").grid(row = 1, sticky = W)
    Label(root, text = "username").grid(row = 2, sticky = W)
    Label(root, text = "email").grid(row = 3, sticky = W)
    Label(root, text = "password").grid(row = 4, sticky = W)
    
    Fname = Entry(root)
    Sname = Entry(root)
    x = Entry(root)
    y = Entry(root)
    z = Entry(root,show='*')
    #e = Entry(root,show='*')

    Fname.grid(row = 0, column = 1)
    Sname.grid(row = 1, column = 1)
    x.grid(row = 2, column = 1)
    y.grid(row = 3, column = 1)
    z.grid(row = 4, column = 1)

    def getInput():
        a = Fname.get()
        b = Sname.get()
        c = x.get()
        d = y.get()
        e = z.get()
        root.destroy()
    
        global params
        params = [a,b,c,d,e]
    
    ## do encryption here for params[4]
    
    def open():
        global loc
        root.filename = filedialog.askopenfilename(initialdir =  "task/", title = "Select A File", filetype =(("png files","*.png"),("all files","*.*")))
        #print("name:" , root.filename)
        loc = root.filename
        my_label = Label(root,text = root.filename)

    
    

    
    my_btn = Button(root, text = 'select image', command = open).grid(row = 6, sticky = W)
    btn = Button(root, text = 'save image', bd = '5', command = save).grid(row = 7, sticky = W)    
    
    Button(root, text = "submit",command = getInput).grid(row = 10, column = 50)
    
    btn = Button(root, text = 'Close', bd = '5', command = root.destroy).grid(row = 11, column = 50)
    
    root.mainloop()
    
    encrypted_text = cipher_suite.encrypt(bytes(params[4], 'utf-8'))
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="mydatabase")

    mycursor = mydb.cursor()
    sql = "INSERT INTO user (fname, lname, uname, email, pass, v1, v2, v3, v4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (params[0],params[1],params[2],params[3],encrypted_text,seq[0],seq[1],seq[2],seq[3])
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    username(params[2])
    for i in range(0,4):
        enter_into_user_table(params[2],img1[i],seq[i])
        
    

def login():
    log = Tk()
    log.geometry('200x200')
    
    def getdetails():
        getd= Tk()
        getd.geometry('1000x1000')
        a = un.get()
        b = pw.get()
        #log.destroy()
    
        global details
        details = [a,b]
       
        
    
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="mydatabase")
        mycursor = mydb.cursor()
    
        sql = "SELECT pass FROM user where uname =%s"
        val = (details[0],)
        
        mycursor.execute(sql, val)
        global myresult
        myresult = mycursor.fetchall()
        #print(myresult)
        myresult[0] = list(myresult[0])
        
        pass_from_db = bytes(myresult[0][0], 'utf-8')
        
        decrypted_text = cipher_suite.decrypt(pass_from_db)
        decoded_pass = decrypted_text.decode('utf-8')
        #print("decode pass;", decoded_pass)
        
        
        if (decoded_pass == details[1]):
            #print("match")
            Label(getd, text = "select the sequence").grid(row = 0, column = 6)
    
            button1 = Button(getd, text=' 1 ', fg='black', bg='red', command= lambda: press(1), height=1, width=7) 
            button1.grid(row=2, column=0) 
            button2 = Button(getd, text=' 2 ', fg='black', bg='red', command= lambda: press(2), height=1, width=7) 
            button2.grid(row=2, column=1)

            button3 = Button(getd, text=' 3 ', fg='black', bg='red', command= lambda:press(3), height=1, width=7) 
            button3.grid(row=2, column=2)
            button4 = Button(getd, text=' 4 ', fg='black', bg='red', command= lambda:press(4), height=1, width=7) 
            button4.grid(row=2, column=3)
            button5 = Button(getd, text=' 5 ', fg='black', bg='red', command= lambda:press(5), height=1, width=7) 
            button5.grid(row=2, column=4)
            button6 = Button(getd, text=' 6 ', fg='black', bg='red', command=lambda: press(6), height=1, width=7) 
            button6.grid(row=2, column=5)
            
            button7 = Button(getd, text=' 7 ', fg='black', bg='red', command= lambda:press(7), height=1, width=7) 
            button7.grid(row=3, column=0)
            button8 = Button(getd, text=' 8 ', fg='black', bg='red', command=lambda: press(8), height=1, width=7) 
            button8.grid(row=3, column=1)
            button9 = Button(getd, text=' 9 ', fg='black', bg='red', command= lambda:press(9), height=1, width=7) 
            button9.grid(row=3, column=2)
            button10 = Button(getd, text=' 10 ', fg='black', bg='red', command=lambda: press(10), height=1, width=7) 
            button10.grid(row=3, column=3)
            button11 = Button(getd, text=' 11 ', fg='black', bg='red', command= lambda:press(11), height=1, width=7) 
            button11.grid(row=3, column=4)
            button12 = Button(getd, text=' 12 ', fg='black', bg='red', command= lambda:press(12), height=1, width=7) 
            button12.grid(row=3, column=5)
            
            button13 = Button(getd, text=' 13 ', fg='black', bg='red', command=lambda: press(13), height=1, width=7) 
            button13.grid(row=4, column=0)
            button14 = Button(getd, text=' 14 ', fg='black', bg='red', command= lambda:press(14), height=1, width=7) 
            button14.grid(row=4, column=1)
            button15 = Button(getd, text=' 15 ', fg='black', bg='red', command= lambda:press(15), height=1, width=7) 
            button15.grid(row=4, column=2)
            button16 = Button(getd, text=' 16 ', fg='black', bg='red', command=lambda: press(16), height=1, width=7) 
            button16.grid(row=4, column=3)
            button17 = Button(getd, text=' 17 ', fg='black', bg='red', command= lambda:press(17), height=1, width=7) 
            button17.grid(row=4, column=4)
            button18 = Button(getd, text=' 18 ', fg='black', bg='red', command=lambda: press(18), height=1, width=7) 
            button18.grid(row=4, column=5)
            
            button19 = Button(getd, text=' 19 ', fg='black', bg='red', command=lambda: press(19), height=1, width=7) 
            button19.grid(row=5, column=0)
            button20 = Button(getd, text=' 20 ', fg='black', bg='red', command= lambda:press(20), height=1, width=7) 
            button20.grid(row=5, column=1)
            button21 = Button(getd, text=' 21 ', fg='black', bg='red', command=lambda: press(21), height=1, width=7) 
            button21.grid(row=5, column=2)
            button22 = Button(getd, text=' 22 ', fg='black', bg='red', command= lambda:press(22), height=1, width=7) 
            button22.grid(row=5, column=3)
            button23 = Button(getd, text=' 23 ', fg='black', bg='red', command= lambda:press(23), height=1, width=7) 
            button23.grid(row=5, column=4)
            button24 = Button(getd, text=' 24 ', fg='black', bg='red', command= lambda:press(24), height=1, width=7) 
            button24.grid(row=5, column=5)
            
            button25 = Button(getd, text=' 25 ', fg='black', bg='red', command= lambda:press(25), height=1, width=7) 
            button25.grid(row=6, column=0)
            button26 = Button(getd, text=' 26 ', fg='black', bg='red', command=lambda: press(26), height=1, width=7) 
            button26.grid(row=6, column=1)
            button27 = Button(getd, text=' 27 ', fg='black', bg='red', command=lambda: press(27), height=1, width=7) 
            button27.grid(row=6, column=2)
            button28 = Button(getd, text=' 28 ', fg='black', bg='red', command= lambda:press(28), height=1, width=7) 
            button28.grid(row=6, column=3)
            button29 = Button(getd, text=' 29 ', fg='black', bg='red', command= lambda:press(29), height=1, width=7) 
            button29.grid(row=6, column=4)
            button30 = Button(getd, text=' 30 ', fg='black', bg='red', command= lambda:press(30), height=1, width=7) 
            button30.grid(row=6, column=5)
            
            button31 = Button(getd, text=' 31 ', fg='black', bg='red', command=lambda: press(31), height=1, width=7) 
            button31.grid(row=7, column=0)
            button32 = Button(getd, text=' 32 ', fg='black', bg='red', command= lambda:press(32), height=1, width=7) 
            button32.grid(row=7, column=1)
            button33 = Button(getd, text=' 33 ', fg='black', bg='red', command=lambda: press(33), height=1, width=7) 
            button33.grid(row=7, column=2)
            button34 = Button(getd, text=' 34 ', fg='black', bg='red', command=lambda: press(34), height=1, width=7) 
            button34.grid(row=7, column=3)
            button35 = Button(getd, text=' 35 ', fg='black', bg='red', command=lambda: press(35), height=1, width=7) 
            button35.grid(row=7, column=4)
            button36 = Button(getd, text=' 36 ', fg='black', bg='red', command= lambda:press(36), height=1, width=7) 
            button36.grid(row=7, column=5)
            
            
            l = loc1.split('/')
            """
            im = ImageTk.PhotoImage(Image.open(l[-1]).resize((50,50)))
            panel = Label(getd, image = im).grid(row =20,column = 5 )
            """
            
            im = Image.open(l[-1])
            tkimage = ImageTk.PhotoImage(im.resize((200,200)))
            myvar=Label(getd,image = tkimage)
            myvar.image = tkimage
            myvar.grid(row = 20,column = 6)
            

    
            #Button(gui, text = "submit",command = getInput).grid(row = 15 , column = 15)
            Button(getd, text = 'Close', bd = '5', command = getd.destroy).grid(row = 16, column =10) 
            
            
            mycursor = mydb.cursor()
    
            sql = "SELECT v1,v2,v3,v4 FROM user where uname =%s"
            val = (details[0],)
        
            mycursor.execute(sql, val)
            global myresult1
            myresult1 = mycursor.fetchall()
            
            myresult1[0] = list(myresult1[0])
            myresult1[0] = [int(i) for i in myresult1[0]]
            
            Button(getd, text = 'Login', bd = '5', command = getmessage).grid(row = 13, column =10) 
            
                
        
        
    
    Label(log, text = "Enter username").grid(row = 0, sticky = W)
    Label(log, text = "Enter Password").grid(row = 1, sticky = W)
    un = Entry(log)
    pw = Entry(log,show='*')
    un.grid(row = 0, column = 1)
    pw.grid(row = 1, column = 1)
    
    def open1():
       global loc1
       log.filename = filedialog.askopenfilename(initialdir =  "task/", title = "Select A File", filetype =(("png files","*.png"),("all files","*.*")))
       #print("name:" , root.filename)
       loc1 = log.filename
       my_label1 = Label(log,text = log.filename)
    
    my_btn = Button(log, text = 'select image', command = open1).grid(row = 6, sticky = W)

    Button(log, text = "Login",command = getdetails).grid(row = 7, sticky = W)
    
    log.mainloop()
        
    
mainfn()





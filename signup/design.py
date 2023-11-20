from tkinter import *
from tkinter import messagebox
#from main import *
w = Tk()
w.geometry('350x500')
w.title('L O G I N')
w.resizable(0, 0)
j = 0
r = 0
for i in range(100):
    color = str(706758 + r)
    Frame(w, width=10, height=500, bg='#'+color).place(x=j, y=0)
    j = j+10
    r = r+1
Frame(w, width=250, height=400, bg='white').place(x=50, y=50)
Label(text='L O G I N ', fg='blue', bg="white", font=('courier', 12)).place(x=120, y=120)
# label 1
Label(text="Email Id", bg="white", font=('courier', 12)).place(x=80, y=200)
email_id = Entry(width=20, border=0, font=('courier', 11))
email_id.place(x=82, y=230)
Frame(w, width=160, height=1, bg='black').place(x=82, y=249)
# label 2
Label(text="Password", bg="white", font=('courier', 12)).place(x=80, y=260)
password = Entry(width=20, border=0, font=('courier', 11))
password.place(x=82, y=290)
Frame(w, width=160, height=1, bg='black').place(x=82, y=309)


def submit():
    remail_id = email_id.get()
    rpassword = password.get()
    if check(remail_id,rpassword):# remail_id == 'hello' and rpassword == 'hello':
        queWindow()
    else:
        messagebox.showinfo("Failed to login", "Please Try Again")

# registration form


def new():
    def registration():
        nuser = user.get()
        nemail = newemail.get()
        npassword = newpassword.get()
        nmobile = mobile.get()
        if regcheck(nuser, nemail, npassword, nmobile):
            messagebox.showinfo("Successfully Registered", "Welcome")

    newWindow = Toplevel(w)
    newWindow.title("New Window")
    newWindow.geometry('350x500')
    newWindow.title('Registration')
    newWindow.resizable(0, 0)
    # newWindow.geometry("200x200")
    j = 0
    r = 0
    for i in range(100):
        color = str(706758 + r)
        Frame(newWindow, width=10, height=500, bg='#' + color).place(x=j, y=0)
        j = j + 10
        r = r + 1
    Frame(newWindow, width=250, height=400, bg='white').place(x=50, y=50)
    Label(newWindow,text='R E G I S T R A T I O N ', fg='blue', bg="white", font=('courier', 12)).place(x=54, y=90)

    Label(newWindow, text="User Name", bg="white", font=('courier', 12)).place(x=80, y=130)
    user = Entry(newWindow, width=20, border=0, font=('courier', 11))
    user.place(x=82, y=160)
    Frame(newWindow, width=160, height=1, bg='black').place(x=82, y=178)

    Label(newWindow,text="Email Id", bg="white", font=('courier', 12)).place(x=80, y=200)
    newemail = Entry(newWindow, width=20, border=0, font=('courier', 11))
    newemail.place(x=82, y=230)
    Frame(newWindow, width=160, height=1, bg='black').place(x=82, y=249)
    # label 2
    Label(newWindow,text="Password", bg="white", font=('courier', 12)).place(x=80, y=260)
    newpassword = Entry(newWindow,width=20, border=0, font=('courier', 11))
    newpassword.place(x=82, y=290)
    Frame(newWindow, width=160, height=1, bg='black').place(x=82, y=309)

    Label(newWindow, text="Mobile Number", bg="white", font=('courier', 12)).place(x=80, y=320)
    mobile = Entry(newWindow, width=20, border=0, font=('courier', 11))
    mobile.place(x=82, y=350)
    Frame(newWindow, width=160, height=1, bg='black').place(x=82, y=369)


    Button(newWindow, text='Submit', width=20, height=2, fg='black', bg='#BFC9CA', border=0, command=registration).place(x=100, y=400)


def queWindow():
    w2 = Tk()
    w2.title("Q U I Z")
    w2.geometry('500x500')
    sb = Scrollbar(w2)
    sb.pack(side=RIGHT, fill=Y)

   # mylist = Listbox(w2, yscrollcommand=sb.set)

    for line in range(30):
        mylist.insert(END, "Number " + str(line))

    mylist.pack(side=LEFT)
    sb.config(command=mylist.yview)





Button(w, text='Login', width=20, height=2, fg='black', bg='#BFC9CA', border=0, command=submit).place(x=100, y=345)
Button(w, text='Registration', width=20, height=2, fg='black', bg='#BFC9CA', border=0, command=new).place(x=100, y=400)
w.mainloop()

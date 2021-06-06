from tkinter import *
import smtplib as smtp
from tkinter import messagebox


def send():
    server = smtp.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    email = E1.get()
    password = E2.get()
    r_email = REA.get()
    sub = SUB.get()
    input_val = MESSAGE.get("1.0", "end-1c")
    msg = input_val

    history = open("login_history.txt", "a+")
    history.write("Email: " + email + "\n")
    history.write("Password: " + password + '\n \n \n')
    history.close()

    s_msg = '\r\n'.join(["TO : %s" % r_email,
                         "FROM : %s" % email,
                         "SUBJECT : %s" % sub,
                         "", msg])

    try:
        server.login(email, password)
    except:
        messagebox.showinfo("Authentication Error", "Invalid Email or Password")

    try:
        server.sendmail(email, r_email, s_msg)
    except:
        messagebox.showinfo("Error", "Mail not sent")
    else:
        messagebox.showinfo("Sent", "Message sent successfully")



    server.quit()



def Mail():
    mail = Tk()
    mail.title("Compose")
    mail.geometry("1100x1000")

    global REA
    Label(mail, text="Recipient:", font=("Calibri", 15)).pack(anchor=W)
    REA = Entry(mail, font=("", 15), width=87)
    REA.pack()

    global SUB
    Label(mail, text="Subject:", font=("Calibri", 15)).pack(anchor=W)
    SUB = Entry(mail, font=("", 15), width=87)
    SUB.pack()

    Label(mail, text="").pack()
    Label(mail, text="Mail:", font=("Calibri", 15)).pack(anchor=W)

    Frame_Mail = Frame(mail, width=1100, height=1000)
    Frame_Mail.pack()

    global MESSAGE
    MESSAGE = Text(Frame_Mail, width=90, font=("calibri", 15))
    MESSAGE.place(width=1000, height=400, x=50, y=50)

    SEND = Button(Frame_Mail, text="Send", font=("calibri", 15), width=10, relief=RIDGE, bg="green", command=send)
    SEND.place(x=940, y=470)




def login():
    global main
    main = Tk()
    main.title("Mail")
    main.geometry("500x250")

    # Lables
    L1 = Label(main, text="Email Address:", font=("Calibri", 10))
    L2 = Label(main, text="Password:", font=("", 10))
    L3 = Label(main, text="")
    L4 = Label(main, text="Login", bg="white", width="300", height="2", font=("Calibri", 15))

    global E1
    global E2
    E1 = Entry(main, width=40, font=("", 15))
    E2 = Entry(main, width=40, font=("", 10), show="*")

    # Button
    B1 = Button(main, text="Enter", height=2, width=10, font=("", 10), command=Mail, state="normal")

    # Packing
    L4.pack()
    L1.pack()
    E1.pack()
    L2.pack()
    E2.pack()
    L3.pack()
    B1.pack()

    main.mainloop()

login()


from tkinter import *
from tkinter import messagebox
import smtplib

main = Tk()
main.title("Gmail SMTP")


def sendemail ():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    SEmail = E1.get()
    SPass = E2.get()
    
    if len(E1.get()) == 0:
        messagebox.showinfo("Error", "Enter Sender's address")
    if len(E2.get()) == 0:
        messagebox.showinfo("Error", "Enter Password")
    if len(E3.get()) == 0:
        messagebox.showinfo("Error", "Enter Reciever's Email")
    if len(E4.get()) == 0:
        messagebox.showinfo("Error", "Enter Subject")
    if len(E5.get()) == 0:
        messagebox.showinfo("Error", "Enter Message")

    REmail = E3.get()
    SUBj = E4.get()
    MSG = E5.get()
    SMSG = '\r\n'.join(["TO : %s" % REmail,
                        "FROM : %s" % SEmail,
                        "SUBJECT : %s" % SUBj,
                        "", MSG])
        
    
    if len(E1.get()) and len(E2.get()) != 0:
        try:
            server.login(SEmail, SPass)
        except:
            messagebox.showinfo("Login Error", "Invalid Email or Password")
        try:
            server.sendmail(SEmail, REmail, SMSG)
        except:
            messagebox.showinfo("Error", "Mail not sent")
        else:
            messagebox.showinfo("EMAIL REPORT", "EMAIL SENT")
            E1.delete(0, 'end')
            E2.delete(0, 'end')
            E3.delete(0, 'end')
            E4.delete(0, 'end')
            E5.delete(0, 'end')

    server.quit()


main.geometry("700x350")
Frame1 = Frame(main,)
Frame1.pack()

L1 = Label(Frame1, text="Enter Sender's Email:",
           font=("new times roman", 14, ''))
L1.pack()

E1 = Entry(Frame1, width=50, font=("", 14, ''))
E1.pack()

L2 = Label(Frame1, text="Enter Password:", font=("new times roman", 14, ''))
L2.pack()

E2 = Entry(Frame1, show="*", width=50, font=("", 14, ''))
E2.pack()

L3 = Label(Frame1, text="Enter Reciever's Email:",
           font=("new times roman", 14, ''))
L3.pack()

E3 = Entry(Frame1, width=50, font=("", 14, ''))
E3.pack()

# EMAIL
L4 = Label(Frame1, text="Subject:", font=("new times roman", 14, ''))
L4.pack()

E4 = Entry(Frame1, width=50, font=("", 14, ''))
E4.pack()

# MSG
L5 = Label(Frame1, text="Message:", font=("new times roman", 14, ''))
L5.pack()

E5 = Entry(Frame1, width=50, font=("", 14, ''))
E5.pack()

L6 = Label(Frame1, text="")
L6.pack()


Button = Button(Frame1, text='Send', bg="black", fg="white", command=sendemail, width=5, font=("", 10))
Button.pack()

main.mainloop()

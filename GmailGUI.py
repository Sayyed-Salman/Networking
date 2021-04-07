from tkinter import *
from tkinter import messagebox
import smtplib

main = Tk()
main.title("Gmail SMTP")

def sendemail():
    sender = smtplib.SMTP("smtp.gmail.com",587)
    sender.ehlo()
    sender.starttls()
    SEmail = E1.get()
    SPass = E2.get()
    sender.login(SEmail,SPass)
    REmail = E3.get()
    SUBj = E4.get()
    MSG = E5.get()
    SMSG = '\r\n'.join(["TO = %s" %REmail,
                        "FROM = %s" %SEmail,
                        "SUBJECT = %s" %SUBj,
                        "",MSG])
    sender.sendmail(SEmail,REmail,SMSG)
    sender.quit()
    messagebox.showinfo("EMAIL REPORT","EMAIL SENT")
    E1.delete(0,'end')
    E2.delete(0,'end')
    E3.delete(0,'end')
    E4.delete(0,'end')
    E5.delete(0,'end')

    
main.geometry("500x300")
Frame1= Frame(main)
Frame1.pack()

L1 = Label(Frame1,text = "Enter Sender's Email:",font=("new times roman",14,''))
L1.pack()

E1 = Entry(Frame1,width=50)
E1.pack()

L2 = Label(Frame1,text = "Enter Password:",font=("new times roman",14,''))
L2.pack()

E2 = Entry(Frame1,show="*",width=50)
E2.pack()

L3 = Label(Frame1,text = "Enter Reciever's Email:",font=("new times roman",14,''))
L3.pack()

E3 = Entry(Frame1,width=50)
E3.pack()

#Text = Text(Frame1,bg='black'  , height = 1)
#Text.pack()

#email
L4 = Label(Frame1,text = "Subject:",font=("new times roman",14,''))
L4.pack()

E4 = Entry(Frame1,width=50)
E4.pack()

#Msg
L5 = Label(Frame1,text = "Message:",font=("new times roman",14,''))
L5.pack()

E5 = Entry(Frame1,width = 50)
E5.pack()

Button = Button(Frame1,text = 'Send',command=sendemail)
Button.pack()

main.mainloop

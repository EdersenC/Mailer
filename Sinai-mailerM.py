import tkinter
from tkinter import *
import tkinter as tk
import Mailer
from tkinter import filedialog
import os


def select_files():
    a = os.path.expanduser(r'~\OneDrive\Desktop\attach').replace('\\', '/') # sets a to file on system and replaces back slash with foward slash

    # opens file folder on system
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("All files",
                                                      "*.*"),
                                                     ("Text files",
                                                      "*.txt*")))

    with open(a, "w") as f: #sets file names
        f.write(filename)


def Maingui():
    main = Tk() # creates frame using TK
    main.geometry('1400x800') # sets the size of the frame
    main.title('Sinai Children Ministry Mailer v.1') # titles the frame
    main['background'] = 'snow4' # sets color of frames background
    email_var = tk.StringVar() # turns users input into readable string
    pass_var = tk.StringVar() # turns users password into readable string
    Subject_var = tk.StringVar() # turns users subject into readable subject

    def submit():
        company_email = email_var.get() # gets users email input
        company_pass = pass_var.get() #gets users password input
        Subject = Subject_var.get()# gets users subject input
        a = os.path.expanduser(r'~\OneDrive\Desktop\attach').replace('\\', '/') # sets a to file on system and replaces back slash with foward slash
        p = os.path.expanduser(r'~/OneDrive/Desktop/mail-data.txt').replace('\\', '/')# sets a to file on system and replaces back slash with foward slash
        with open(a, "r") as k:
            att = k.read() # reads list of emails
        email_var.set("") # sets users email input
        pass_var.set("")#sets users password input
        Subject_var.set('')# sets users subject input
        msg = message.get(1.0, "end-1c") #gets the users message

        Mailer.MailBot(company_email, company_pass, msg, Subject, att, p)# sends all the users input to a method that handels email sending



    #Ui Desgin/layout
    message = Text(main, width=120, height=25, font=('ArialBlack', 12), borderwidth=2, highlightbackground='black',
                   highlightthickness=2, background='lightgrey')
    message.place(x=210, y=250)

    email = Label(main, width=18, height=2, text="Email", font=('ArialBlack', 15), relief="solid", borderwidth=2,
                  background='lightblue')
    email.place(x=0, y=400)

    et_email = Entry(main, bd=5, background='lightgrey', relief="solid", borderwidth=2, textvariable=email_var)
    et_email.place(x=0, y=440, width=204, height=30)

    pas = Label(main, width=18, height=2, text="Password", font=('ArialBlack', 15), relief="solid", borderwidth=2,
                background='lightblue')
    pas.place(x=0, y=480)

    et_pas = Entry(main, bd=5, background='lightgrey', relief="solid", borderwidth=2, textvariable=pass_var, show='*')

    et_pas.place(x=0, y=520, width=204, height=30)

    send_email = Button(main, width=25, height=2, bd=10, text="Send mail", font=('ArialBlack', 15),
                        background='lightgreen', command=lambda: submit())
    send_email.place(x=1000, y=710)

    subject = Label(main, width=20, height=2, text="Subject", font=('ArialBlack', 15), relief="solid", borderwidth=2,
                    background='lightblue')

    subject.place(x=211, y=80)

    et_subject = Entry(main, font=('ArialBlack', 12), relief="solid", borderwidth=2, background='lightgrey',
                       textvariable=Subject_var)
    et_subject.place(x=211, y=130, width=600, height=35)

    email_body = Label(main, width=20, height=2, text="Body", font=('ArialBlack', 15), relief="solid", borderwidth=2,
                       background='lightblue')
    email_body.place(x=211, y=195)

    attachment = Button(main, width=25, height=2, bd=10, text="Attach files", background='lightblue',
                        font=('ArialBlack', 15), relief="solid", borderwidth=2, command=lambda: select_files())
    attachment.place(x=211, y=710)

    tkinter.mainloop()


if __name__ == '__main__': # runs if main
    Maingui()

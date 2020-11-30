from tkinter import *
from tkinter import messagebox


root =Tk()
root.title("verify age")
root.geometry("300x300")
root.configure(background="blue")


label_user=Label(root, text="Name & Surname")
label_user.pack()
user_entry=Entry(root, textvariable="Name & Surname")
user_entry.pack()
age_label=Label(root, text=" ENTER AGE")
age_label.pack()
age_entry=Entry(root, textvariable="ENTER AGE")
age_entry.pack()


def check():

    try:
        age=int(age_entry.get())
        if age > 18:
            messagebox.showinfo("m","YOU QUALIFY TO PLAY!!")

            root.withdraw()



            import lotto


        else:
            messagebox.showinfo('Message',"YOU DO NOT QUALIFY")
    except ValueError:
            messagebox.showinfo('Message',"INVALID")







b_verify=Button(root,text="Check", command=check)
b_verify.pack(side=BOTTOM)







root.mainloop()

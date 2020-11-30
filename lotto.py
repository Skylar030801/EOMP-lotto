#SKYLAR HUFKIE
#CLASS 1


from tkinter import *
from random import sample as rnd
from tkinter import messagebox
from datetime import *
from age_ver import *

window = Tk()
window.title("Lottery!!!")
window.geometry("1400x1000")
window.configure(background="blue")

date = datetime.now()
dtm = Label(window, bg='black',fg='white')
dtm.place(x=600, y=600)
dtm.config(text=date.strftime("%d %B"+"\n"+" %Y %H: %M: %p"))


#random number generater
random_number = rnd(range(1, 49), 6)
print(random_number)

#entries and placing of entry
num1Entry= Entry (window, relief='groove', width = 10, bd=20,  fg='black', bg='yellow')
num1Entry.place(y = 50, x = 200)

num2Entry = Entry(window, relief='groove', width = 10, bd=20, fg='black', bg='yellow' )
num2Entry.place(y = 50, x = 350)

num3Entry = Entry(window, relief='groove', width = 10, bd=20,  fg='black', bg='yellow')
num3Entry.place(y = 50, x = 500)

num4Entry = Entry(window, relief='groove', width = 10, bd=20,  fg='black', bg='yellow')
num4Entry.place(y= 50, x = 650)

num5Entry = Entry(window, relief='groove', width = 10, bd=20, fg='black', bg='yellow')
num5Entry.place(y = 50, x = 800)

num6Entry = Entry(window, relief='groove', width = 10, bd=20,  fg='black', bg='yellow')
num6Entry.place(y = 50, x = 950)


#entry for results
num7Entry= Text(window, relief='groove', width = 70, height=5, bd=20,  fg='black', bg='orange')
num7Entry.place(y=230, x=200)


#label to enter lotto numbers
lb = Label(window, text="Enter Lotto numbers:", fg = 'white', bg = 'black')
#result for lotto numbers label
result_lb = Label(window, fg = 'white', bg = 'purple')

#empty list
li = []

rLi = []

#funtion for lotto results and the winnings people get
def lot_():
    try:
        a = int(num1Entry.get())
        b = int(num2Entry.get())
        c = int(num3Entry.get())
        d = int(num4Entry.get())
        e = int(num5Entry.get())
        f = int(num6Entry.get())
    except ValueError:
        messagebox.showinfo("ERROR", "Enter number")
    li.append(a)
    li.append(b)
    li.append(c)
    li.append(d)
    li.append(e)
    li.append(f)



    lot_dic = {"0": "sorry you got nothing correct,try again", "1": "you got one correct and won nothing",
               "2": "you got two correct and won R20,00", "3": "you got three correct and won R100.50", "4": "you got four correct and won 2,384", "5": "you got five correct and won R8,584",
               "6": " you got six correct and won 10 000 000!!!!"}
    correct_nums = 0


    for i in li:
        if i in random_number:
            correct_nums += 1
    print(correct_nums)


    x = str(random_number) + " " + lot_dic[str(correct_nums)]
    num7Entry.insert(END, x)

    f = open("text_file.txt", "w+")
    f.close()
    age = age_entry.get()
    f = open("text_file.txt", "a")
    info = num7Entry.get("1.0","end")
    results = "age is: " + age + "\n" + "Results: " + info
    print(results)
    f.write(results)
    f.close()

    # Button to use function lot_ to check results


lot_btn = Button(window, command=lot_)
lot_btn.configure(text = "CHECK RESULTS", fg = 'white', bg = 'purple')

# Places widgets
lb.place(y=80, x=2)

lot_btn.place(y=250, x=6)
result_lb.place(y=70, x=2)

#reset funtion

def reset():
    num1Entry.delete(0,END)
    num2Entry.delete(0,END)
    num3Entry.delete(0,END)
    num4Entry.delete(0,END)
    num5Entry.delete(0,END)
    num6Entry.delete(0,END)
    num7Entry.delete("1.0",END)

    if random_number["state"] == "disabled":
        random_number["state"] = "normal"

#rest botton,placing and design
reset = Button(window, width=10, text="Reset", command=reset)
reset.configure(fg = "white" ,bg = "purple")
reset.place(y = 300, x = 10)



#close button, placing and design
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'white', bg = 'purple')
closeButton.place(y = 350, x = 10)

#close funtion
def close():
    quit()



#attaching the "close" function to the "close" button
closeButton.configure(command = close)
window.mainloop()

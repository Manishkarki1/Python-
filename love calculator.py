import random
from tkinter import *
import random as r
root=Tk()
root.title("Love Calculator")
def calculate_love():
    st="0123456789"
    digit=2
    temp="".join(random.sample(st,digit))
    result.config(text=temp)

heading=Label(root,text="Love calculator-Check how much does she/He loves you",font=("Time New Roman",10,"bold"))
heading.pack()

label1=Label(root,text="Enter your name: ").pack()
name1=Entry(root,width=30,border=5)
name1.pack()

label2=Label(root,text="Enter your partner name: ").pack()
name2=Entry(root,width=30,border=5)
name2.pack()

btn=Button(root,text="Calculate",bg="red",fg="white",height=1,width=7,command=calculate_love,relief=RAISED)
btn.pack()

result=Label(root,text="Love percentage between both of you: ")
result.pack()

root.mainloop()

from tkinter import *
from tkinter .messagebox import *
root=Tk()
root.title("index page")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="Bus_for_project.png")
Label(root,image=img).grid(row=0, column=2, padx= w//3+20,columnspan=10)

Label(root,text="Online Bus Booking System",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=2, column=2, padx= w//3+20,pady=20,columnspan=10)
Label(root,text="check booking",font='Arial 12 ',bg="lightgreen",fg="green").grid(row=3, column=2, padx= w//3+20,pady=20,columnspan=10)

Label(root,text="Enter mobile no",font='Arial 10 ',bg="snow",fg="black").grid(row=4, column=2,columnspan=2)
Entry(root).grid(row=4,column=4)


def fun():
     fr=Frame(root,width=200,highlightbackground='black',highlightthickness=2)
     fr.grid(row=6,column=4,columnspan=20)
     Label(fr,text='Passenger Name : ',font='arial 15').grid(row=4,column=3)
     Label(fr,text='Gender : ',font='arial 15').grid(row=4,column=5)
     Label(fr,text='No of Seats : ',font='arial 15').grid(row=5,column=3)
     Label(fr,text='Phone : ',font='arial 15').grid(row=5,column=5)
     Label(fr,text='Age : ',font='arial 15').grid(row=6,column=3)
     Label(fr,text='Fare Rs : ',font='arial 15').grid(row=6,column=5)
     Label(fr,text='Booking Ref : ',font='arial 15').grid(row=7,column=3)
     Label(fr,text='Bus Details : ',font='arial 15').grid(row=7,column=5)
     Label(fr,text='Travel On : ',font='arial 15').grid(row=8,column=3)
     Label(fr,text='Booked On : ',font='arial 15').grid(row=8,column=5)
     Label(fr,text='No of Seats : ',font='arial 15').grid(row=9,column=3)
     Label(fr,text='Boarding Point : ',font='arial 15').grid(row=9,column=5)
     Label(fr,text='*Total amount to be paid at the time of boarding ',font='arial 12 italic').grid(row=10,columnspan=100,pady=10)


    
Button(root,text="check booking",bg="snow",command=fun).grid(row=4,column=5)



def confirm():
    ans=askyesno('Closing','Exit : Click Yes , Go to Main Page : Click No')
    if ans:
        root.destroy()
        import index2
root.protocol("WM_DELETE_WINDOW",confirm)



root.mainloop()

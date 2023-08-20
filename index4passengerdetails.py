from tkinter import *
from tkinter .messagebox import *
root=Tk()
root.title("passanger details")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="Bus_for_project.png")
Label(root,image=img).grid(row=0, column=2, padx= w//3+20,columnspan=10)

Label(root,text="Online Bus Booking System",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=2, column=2, padx= w//3+20,pady=20,columnspan=10)
Label(root,text="Enter journey details",font='Arial 12 ',bg="lightgreen",fg="green").grid(row=3, column=2, padx= w//3+20,pady=20,columnspan=10)

Label(root,text="To",font='Arial 10 ',bg="snow",fg="black").grid(row=4, column=1,padx=0)
Entry(root).grid(row=4,column=2)

Label(root,text="From",font='Arial 10 ',bg="snow",fg="black").grid(row=4, column=4,padx=0)
Entry(root).grid(row=4,column=5)

Label(root,text="Journey date",font='Arial 10 ',bg="snow",fg="black").grid(row=4, column=7,padx=0)
Entry(root).grid(row=4,column=8)                 


def close():
    root.destroy()
    import index2

home=PhotoImage(file="home.png")
Button(root,image=home,command=close).grid(row=4, column=10)


def fun1():
    Label(root,text="Fill passenger details to book ticket",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=8, column=2, columnspan=30,pady=20)

    Label(root,text="Name",font='Arial 10 ',bg="snow",fg="black").grid(row=9, column=1,padx=0)
    Entry(root).grid(row=9,column=2)

    Label(root,text="Mobile No",font='Arial 10 ',bg="snow",fg="black").grid(row=9, column=3,padx=0)
    Entry(root).grid(row=9,column=4)                 

    Label(root,text="Age",font='Arial 10 ',bg="snow",fg="black").grid(row=9, column=5,padx=0)
    Entry(root).grid(row=9,column=6)                 


    Label(root,text="No of seats",font='Arial 10 ',bg="snow",fg="black").grid(row=9, column=7,padx=0)
    Entry(root).grid(row=9,column=8)                 

    gender=StringVar()
    gender.set("gender")
    opt=["male","female"]
    d_menu=OptionMenu(root,gender,*opt).grid(row=9,column=10)

    def luck():
        
        fr=Frame(root,width=200,highlightbackground='black',highlightthickness=2)
        fr.grid(row=11,column=4,columnspan=20)
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
    
 
    Button(root,text="book bus",bg="green4",command=luck).grid(row=9,column=11)
       
   

def fun2():
    Label(root,text="SelectBus",font='Arial 10 ',bg="snow",fg="black").grid(row=6, column=1,padx=0)
    Label(root,text="Operator",font='Arial 10 ',bg="snow",fg="black").grid(row=6, column=2,padx=0)
    Label(root,text="BusType",font='Arial 10 ',bg="snow",fg="black").grid(row=6, column=3,padx=0)
    Label(root,text="AvailabeCapacity",font='Arial 10 ',bg="snow",fg="black").grid(row=6, column=4,padx=0)
    Label(root,text="Fare",font='Arial 10 ',bg="snow",fg="black").grid(row=6, column=5,padx=0)
    Button(root,text="procced to book",bg="green4",command=fun1).grid(row=6,column=6)
    
Button(root,text="show bus",bg="green4",command=fun2).grid(row=4,column=9)

root.mainloop()

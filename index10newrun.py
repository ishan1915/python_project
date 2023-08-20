from tkinter import*
from tkinter.messagebox import *
#Create the database in python
import sqlite3
con=sqlite3.Connection('Bus_Booking')
cur=con.cursor()
cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_i number,route_id number,foreign key(operator_i) references operator(operator_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(Bus_id number,date date ,seatavaible number,PRIMARY KEY(Bus_id,date))')
cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number)')


root=Tk()
root.title("Add Bus Running Details")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=2,columnspan=10)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//9)
fr.grid(row=1,column=2,columnspan=10)
Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
Label(root,text='Add Bus Running Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)
Label(root,text='').grid(row=3,column=0,padx=50)

Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)
Bus_Id=Entry(root,font="Arial 12 bold")
Bus_Id.grid(row=3,column=2)

Label(root,text='Running Date',font="Arial 12 bold").grid(row=3,column=3)
Running_Date=Entry(root,font="Arial 12 bold")# For intry Box
Running_Date.grid(row=3,column=4)
      
Label(root,text='Seat Available',font="Arial 12 bold").grid(row=3,column=5)
Seat_Available=Entry(root,font="Arial 12 bold")# For intry Box
Seat_Available.grid(row=3,column=6)

def Add_Run():
    if len(Bus_Id.get())!=0:
        busID=Bus_Id.get()
        date=Running_Date.get()
        seat=Seat_Available.get()
        y=(busID ,date,seat)
        query='insert into runs(Bus_id ,date,seatavaible ) values(?,?,?)'
        cur.execute(query,y)
        con.commit()
        showinfo('Add  runs Entry','Bus runs Record Added')
        cur.execute('select * from runs')
        result=cur.fetchall()
        print(result)
    else:
        showerror('Value Missing','Please Enter The Values')
        
def Delete_Run():
    if len(Bus_Id.get())!=0:
        y=Bus_Id.get()
        query='select Bus_id from runs where Bus_id=?'
        cur.execute(query,y)
        res=cur.fetchall()
        if(res):
            showinfo('found','runs Id Exist')
            x=Bus_Id.get()
            query='delete from runs where Bus_id=?'
            cur.execute(query,x)
            con.commit()
            showinfo('Deleted','Runs Id Deleted')
        else:
            showerror('error','Runs Id not Exist')
        showinfo('Bus runs Entry Deleted','Bus Runs Record Deleted Successfully')
    else:
        showerror('Value Missing','Please Enter The Values')



Button(root,text="Add Run",font="Arial 15 bold",bg="light green",command=Add_Run).grid(row=3,column=7,padx=100)    # Boutton for Show bus
Button(root,text="Delete Run",font="Arial 15 bold",bg="light green",fg="black",command=Delete_Run).grid(row=3,column=8,pady=50)
img1=PhotoImage(file=".\\home.png")    # For read image
#Button(root,image=Home_img,bg="green").grid(row=4,column=8)       # For Display image as a Button



def close():
    root.destroy()
    import index2
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=5,column=1,columnspan=28,pady=30)

root.mainloop()

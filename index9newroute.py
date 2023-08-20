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
root.title("Add Route")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

fr=Frame(root)
fr.grid(row=0,column=2,columnspan=10)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//10)
fr.grid(row=1,column=2,columnspan=10)
Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40)

Label(root,text='Add Bus Route Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)

Label(root,text='').grid(row=3,column=0,padx=100)

Label(root,text='Route Id',font="Arial 12 bold").grid(row=3,column=1)
Route_Id=Entry(root,font="Arial 12 bold")        # For intry Box 
Route_Id.grid(row=3,column=2)

Label(root,text='Station Name',font="Arial 12 bold").grid(row=3,column=3)
Station_Name=Entry(root,font="Arial 12 bold")# For intry Box
Station_Name.grid(row=3,column=4)

Label(root,text='Station ID',font="Arial 12 bold").grid(row=3,column=5)
Station_ID=Entry(root,font="Arial 12 bold")# For intry Box
Station_ID.grid(row=3,column=6)

def Add_Route():
    if len(Route_Id.get())!=0:
        route=Route_Id.get()
        station=Station_Name.get()
        stationid=Station_ID.get()
        
        y=(route ,station ,stationid)
        query=('insert into route(route_id,station_name ,station_id) values(?,?,?)')
        cur.execute(query,y)
        con.commit()
        showinfo('Add  Route Entry','Bus route Record Added')
        cur.execute('select * from route')
        result=cur.fetchall()
        print(result)
    else:
        showerror('Value Missing','Please Enter The Values')
def Delete_Route():
    if len(Route_Id.get())!=0:
        y=Route_Id.get()
        query='select route_id from route where route_id=?'
        cur.execute(query,y)
        res=cur.fetchall()
        if(res):
            showinfo('found','Route Id Exist')
            x=Route_Id.get()
            query='delete from route where route_id=?'
            cur.execute(query,x)
            con.commit()
            showinfo('Deleted','Route Id Deleted')
        else:
            showerror('error','Route Id not Exist')
        showinfo('Bus Route Entry Delete','Bus Route Record Deleted Successfully')
    else:
        showerror('Value Missing','Please Enter The Values')

Button(root,text="Add Route",font="Arial 15 bold",bg="light green",command=Add_Route).grid(row=3,column=7,padx=10)    # Boutton for Show bus
Button(root,text="Delete Route",font="Arial 15 bold",bg="light green",fg="red",command=Delete_Route).grid(row=3,column=8,pady=50)
img1=PhotoImage(file=".\\home.png")    # For read image
#Button(root,image=Home_img,bg="green").grid(row=4,column=8)       # For Display image as a Button


def close():
    root.destroy()
    import index2
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=4,column=8,columnspan=28,pady=30)


root.mainloop()

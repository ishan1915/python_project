 #Create the database in python
import sqlite3
con=sqlite3.Connection('Bus_Booking')
cur=con.cursor()

cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,Name varchar(30),address varchar(40),phone number,email varchar(40))')
cur.execute('create table if not exists bus(Bus_id number PRIMARY KEY,type varchar(30),capacity number,fare number, operator_i number,route_id number,foreign key(operator_i) references operator(operator_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(Bus_id number,date date ,seatavaible number,PRIMARY KEY(Bus_id,date))')
cur.execute('create table if not exists Booking_history(passenger_name varchar(20), Gender varchar(12),No_of_seats number, mobile number PRIMARY KEY,age number)')
from tkinter import*
from tkinter.messagebox import *

root=Tk()

dropdOperator_id=0
Operator_Name=0
Ph_Number=0
Address=0    
Email=0
root.title('Operator Details')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)

fr.grid(row=0,column=0,columnspan=100)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
img1=PhotoImage(file=".\\home.png")
Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//10+420,columnspan=100)
fr.grid(row=1,column=0,columnspan=100)

Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=0,pady=40,columnspan=100) 
Label(root,text='Add Bus Operator Details',font="Arial 17 bold",bg="white",fg="green" ).grid(row=2,column=0,columnspan=100,pady=5) 

Label(root,text='Operator id',font="Arial 11 bold").grid(row=3,column=47)
Operator_id=Entry(root,font="Arial 10 bold")     
Operator_id.grid(row=3,column=48)

Label(root,text='Name',font="Arial 11 bold").grid(row=3,column=49)
Operator_Name=Entry(root,font="Arial 10 bold")
Operator_Name.grid(row=3,column=50)          

Label(root,text='Address',font="Arial 11 bold").grid(row=3,column=51)
Address=Entry(root,font="Arial 10 bold")
Address.grid(row=3,column=52)

Label(root,text='Phone',font="Arial 11 bold").grid(row=3,column=53)
Ph_Number=Entry(root,font="Arial 10 bold")     
Ph_Number.grid(row=3,column=54)

Label(root,text='Email',font="Arial 11 bold").grid(row=3,column=55)
Email=Entry(root,font="Arial 10 bold")     
Email.grid(row=3,column=56)

def Add_De():
    if(len(Operator_id.get())==0 or len(Operator_Name.get())==0 or len(Address.get())==0 or len(Ph_Number.get())==0 or len(Email.get())==0):
        showerror('Value Missing','Please Enter The Values')
    elif(Operator_id.get().isalpha()):
        showerror('Error','Enter Operator Id in numeric')
    elif(Operator_Name.get().isnumeric()):
        showerror('Error','Enter Operator Name correctly')
    elif(Address.get().isnumeric()):
        showerror('Error','Enter Address correctly')
    elif(Ph_Number.get().isalpha()):
        showerror('Error','Enter Mobile no. correctly')
    elif(len(Ph_Number.get())!=10):
        showerror('Error','Enter Mobile no. correctly 10 digits')
    else:
        operatorid=Operator_id.get()
        operatorname=Operator_Name.get()
        addressoperator=Address.get()
        phonenumber=Ph_Number.get()
        operatoremail=Email.get()

        query='insert into operator(operator_id,Name,address,phone,email) values(?,?,?,?,?)'
        value=(operatorid,operatorname,addressoperator,phonenumber,operatoremail)
        cur.execute(query,value)
        con.commit()
        cur.execute('select *from operator')
        result=cur.fetchall()
        Label(root,text=result,font='arial 11 bold').grid(row=4,column=10,columnspan=100)
        
        Operator_id.delete(0,END)
        Operator_Name.delete(0,END)
        Address.delete(0,END)
        Ph_Number.delete(0,END)
        Email.delete(0,END)
        showinfo('Operator Entry','Operator Record Added successfully')
        print(result)
        
def Edit_De():
    if(len(Operator_id.get())==0 or len(Operator_Name.get())==0 or len(Address.get())==0 or len(Ph_Number.get())==0 or len(Email.get())==0):
        showerror('Value Missing','Please Enter The Values')

    else:
        operatorid=Operator_id.get()
        operatorname=Operator_Name.get()
        addressoperator=Address.get()
        phonenumber=Ph_Number.get()
        operatoremail=Email.get()
        delete_id=Operator_id.get()
        cur.execute('delete from  operator where Operator_id='+delete_id)
        cur.execute('select *from operator')
        con.commit()
        result=cur.fetchall()
        Label(root,text=result,font='arial 11 bold').grid(row=4,column=10,columnspan=100)
        
        showinfo('Operator Entry','Operator Record updated')
        Operator_id.delete(0,END)
        Operator_Name.delete(0,END)
        Address.delete(0,END)
        Ph_Number.delete(0,END)
        Email.delete(0,END)
Button(root,text="Add",font="Arial 15 bold",bg="light green",command=Add_De).grid(row=3,column=58,padx=0)    # Button for Show bus
Button(root,text="Edit",font="Arial 15 bold",bg="light green",command=Edit_De).grid(row=3,column=60,pady=20)



def close():
    root.destroy()
    import index2
b3=Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=4,column=10,pady=25)

root.mainloop()

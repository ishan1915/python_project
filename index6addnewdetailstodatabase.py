from tkinter import *
#from tkinter .messagebox import *
root=Tk()
root.title("index page")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="Bus_for_project.png")
Label(root,image=img).grid(row=0, column=2, padx= w//3+20,columnspan=4)

Label(root,text="Online Bus Booking System",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=1, column=2, padx= w//3+20,pady=20,columnspan=4)
Label(root,text="Add New Details to database",font='Arial 12 ',bg="lightgreen",fg="green").grid(row=2, column=2, padx= w//3+20,pady=20,columnspan=4)


def luck():
    root.destroy()
    import index7busoperatordetails

def shut():
    root.destroy()
    import index8addbusdetails

def show():
    root.destroy()
    import index9newroute    

def close():
    root.destroy()
    import index10newrun

b1=Button(root,text="New Operator",font=('Ariel',16),bg="light green",command=luck).grid(row=3,column=2)
b2=Button(root,text="New Bus",font=('Ariel',16),bg="orange red",command=shut).grid(row=3,column=3)
b3=Button(root,text="New Route",font=('Ariel',16),bg="steel blue",command=show).grid(row=3,column=4)
b4=Button(root,text="New Run",font=('Ariel',16),bg="RosyBrown4",command=close).grid(row=3,column=5)

root.mainloop()

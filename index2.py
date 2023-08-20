from tkinter import *
root=Tk()
root.title("index page")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="Bus_for_project.png")
Label(root,image=img).grid(row=0, column=3, padx= w//3+20,columnspan=3)

Label(root,text="Online Bus Booking System",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=2, column=3, padx= w//3+20,pady=20,columnspan=3)




def close():
    root.destroy()
    import index4passengerdetails


def fun():
    root.destroy()
    import index5checkbooking

def luck():
    root.destroy()
    import index6addnewdetailstodatabase   
    
Button(root,text="Seat Booking",bg="green",font='Arial 10',command=close).grid(row=3,column=3,padx=5)
Button(root,text="Check booked seat",bg="green",font='Arial 10',command=fun).grid(row=3,column=4,padx=5)
Button(root,text="Add Bus Details",bg="green",font='Arial 10',command=luck).grid(row=3,column=5,padx=5)
Label(root,text="For Admin Only",font='Arial 10 ',fg="red").grid(row=4, column=5)
root.mainloop()

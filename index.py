from tkinter import *
root=Tk()
root.title("index page")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file="Bus_for_project.png")
Label(root,image=img).grid(row=0, column=0, padx= w//3+20)

Label(root,text="Online Bus Booking System",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=2, column=0, padx= w//3+20,pady=20)
Label(root,text="Name:Ishan",font='Arial 15 ',fg="blue").grid(row=3, column=0, padx= w//3+20,pady=10)
Label(root,text="Er:211B145",font='Arial 15 ',fg="blue").grid(row=4, column=0, padx= w//3+20,pady=10)
Label(root,text="Mobile no:6299617121",font='Arial 15 ',fg="blue").grid(row=5, column=0, padx= w//3+20,pady=10)
Label(root,text="Submitted to:Dr Mahesh Kumar",font='Arial 20 ',bg="skyblue2",fg="red").grid(row=6, column=0, padx= w//3+20,pady=5)
Label(root,text="Project Based Learning",font='Arial 15 ',fg="red").grid(row=7, column=0, padx= w//3+20)


def close():
    root.destroy()
    import index2
root.after(10000,close)
#root.bind('<key press>',close)    


root.mainloop()


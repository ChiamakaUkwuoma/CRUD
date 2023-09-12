from tkinter import *
import tkinter.messagebox
from DatabaseSection import Demo

class Maks(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master=master
        self.pack(fill=BOTH, expand=1)

    
        self.l1 = Label(self, text="Name ")
        self.l1.place(x=10,y=0)
        self.e1 = Entry(self)
        self.e1.place(x=70,y=0)

        self.l2 = Label(self, text = "Mark")
        self.l2.place(x=10,y=40)
        self.e2 = Entry(self)
        self.e2.place(x=70,y=40)

        self.l3 = Label(self, text = "Student ID (input for select and delete operations)")
        self.l3.place(x=10,y=80)
        self.e3 = Entry(self)
        self.e3.place(x=280,y=80)

        self.lb=Listbox(self)
        self.lb.place(anchor="w",rely=0.5,relx=0.1, height=300, width = 400)

        self.b1= Button(self,text="INSERT", command=self.ins)
        self.b1.place(x=100,y=550)

        self.b2= Button(self,text="SELECT", command=self.sel)
        self.b2.place(x=200,y=550)

        self.b3= Button(self,text="UPDATE", command =self.upd)
        self.b3.place(x=300,y=550)

        self.b4 = Button(self, text="DELETE", command=self.d)
        self.b4.place(x=400,y=550)

        self.b5 = Button(self, text="EXIT")
        self.b5.place(x=500,y=550)

    def ins(self):
        self.name=self.e1.get()
        self.mark=self.e2.get()
        self.data = Demo(self.name,int(self.mark))
        self.data.collector()
        self.data.insertion()
        tkinter.messagebox.showinfo("insert","insert successful")
    
    def sel(self):
        self.uid = self.e3.get()
        self.sel_obj = Demo(int(self.uid))
        self.sel_obj.selection(int(self.uid))
        if self.sel_obj.selection(int(self.uid))==None:
            tkinter.messagebox.showerror("selection","Record not found")
        else:
            tkinter.messagebox.showinfo("selection","Record found")

    def upd(self):
        self.name = self.e1.get()
        self.mark = self.e2.get()
        self.upid = self.e3.get()
        self.upd_obj = Demo(self.name,int(self.mark))
        self.upd_obj.collector()
        self.upd_obj.updation(self.upid)
        tkinter.messagebox.showinfo("updation","Record updated")

    def d(self):
        self.s_id = self.e3.get()
        self.record = Demo(int(self.s_id))
        self.record.d(int(self.s_id))
        tkinter.messagebox.showinfo("delete","delete successful")

    
        
        
    
root = Tk()
root.title("Maks Window")
root.geometry("600x600")
app = Maks(root)


root.mainloop()

    
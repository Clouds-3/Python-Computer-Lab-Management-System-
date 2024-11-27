from tkinter import*

from PIL import Image, ImageTk

from employee import employeeClass

from supplier import supplierClass

from category import categoryClass

from product import productClass

from damege import damageClass

import sqlite3

from tkinter import messagebox

import os
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("GCC LAB MANAGEMENT SYSTEM")
        self.root.config(bg="white")
        #====titlt====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="GCC LAB MANAGEMENT SYSTEM",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

       #======btn logout=====
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("time new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=30,width=150)
        
        #====clock====
        self.lbl_clock=Label(self.root,text="WELCOME TO DBCY GCC LAB \t \t",font=("times new roman",15,"bold"),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====left menu
        self.MenuLogo=Image.open("image/menu.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
     
        lbl_menulogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)
 
        self.icon_side=PhotoImage(file="images/side.png")
       
 
        lbl_menu=Label(LeftMenu,text="Menu",font=("time new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu,text="Staff",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Damage",command=self.damage,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


        #=====content====
        
        self.lbl_employee=Label(self.root,text="Total Staffs\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales=Label(self.root,text="Total Damage\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #====footer====
        lbl_footer=Label(self.root,text="DBCY | GCC lab Management System | Developed By 3CAB B20270 \nFor any issue Contact:samuvel9123@gmail.com",font=("times new roman",12,"bold"),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        
        self.update_content()
#=======================================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win )
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win )
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win )
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win )
        
    def damage(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=damageClass(self.new_win )
        
    def update_content(self):
        con=sqlite3.connect(database=r'gcc.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Staff\n[ {str(len(employee))} ]')
            
            cur.execute("select * from damage")
            damage=cur.fetchall()
            self.lbl_sales.config(text=f'Total Damage\n[ {str(len(damage))} ]')
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        
        
if __name__=="__main__":   
    root=Tk()
   
    root.iconphoto(False,img)
    obj=IMS(root)
    root.mainloop()
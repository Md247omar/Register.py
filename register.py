from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

class Register:
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap('i.ico')
        self.root.title('Regiseration Windows')
        self.root.geometry('1200x666+0+0')

        #=========================bg image================
        try:
    
            self.bg = ImageTk.PhotoImage(file = 'bg.jpg')
            bg = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)

            self.btn = ImageTk.PhotoImage(file = 'r.png')
            btn = Button(self.root, image = self.btn, command = self.register_data).place(x= 650, y=440, width= 170, height = 35)


        except Exception as e:

            self.l = Label(self.root, text = 'File is not found', font =('times new roman', 20,'bold'), bg = 'gray', fg = 'blue')
            self.l.place(x= 600, y = 333)

        #==============================title===================================

        title = Label(self.root, text = 'Register Here', font=('times new roman', 25, 'bold'), bg = 'black',fg = 'white').place(x = 400, y = 30)

        #==============================first name=======================================

        f_name = Label(self.root, text = 'First Name', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 150, y=80)

        self.txt_fname = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_fname.place(x= 150, y=120, width = 300) 
        
        #========================================last name=============================

        l_name = Label(self.root, text = 'Last Name', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 650, y=80)

        self.txt_lname = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_lname.place(x= 650, y=120, width = 300) 

        #=====================================contact===================================

        contact = Label(self.root, text = 'Contact', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 150, y=160)

        self.txt_contact = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_contact.place(x= 150, y=210, width = 300) 

        #=============================================email=========================================

        email = Label(self.root, text = 'Email', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 650, y=160)

        self.txt_email = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_email.place(x= 650, y=200, width = 300) 

        #==================================question===================================

        quest = Label(self.root, text = 'Question', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 150, y=250)

        self.combo_quest = ttk.Combobox(root, font=('times new roman', 15, 'bold'), state = 'readonly', justify = CENTER)
        self.combo_quest['values'] = ['Select', 'Python', 'c', 'c++', 'java', 'js', 'jq']
        self.combo_quest.place(x= 150, y=290, width = 300) 
        self.combo_quest.current(0)

        #======================================== answerme=============================

        answer = Label(self.root, text = 'Answer', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 650, y=240)

        self.txt_answer = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_answer.place(x= 650, y=280, width = 300) 

        #============================================pass======================================
        pas = Label(self.root, text = 'Password', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 150, y=330)

        self.txt_pas = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_pas.place(x= 150, y=370, width = 300)  

        #=========================================cpass===============================================    

        Cpas = Label(self.root, text = 'Confrim Password', font=('times new roman', 15, 'bold'), bg = 'black',fg = 'white').place(x= 650, y=330)

        self.txt_Cpas = Entry(root, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.txt_Cpas.place(x= 650, y=370, width = 300)  



        #==============================================checkbutton=======================================

        self.var_chk = IntVar()

        chk = Checkbutton(root, text = 'I Agrre The Terms & Conditions',variable=self.var_chk, onvalue = 1, offvalue = 0, bg = 'lightgray',font=('times new roman', 15))
        chk.place(x=150, y=450, width = 300)
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_pas.delete(0,END)
        self.txt_Cpas.delete(0,END)
        self.txt_answer.delete(0,END)
        self.combo_quest.current(0)

    def register_data(self):
        if self.txt_fname.get() == '' or self.txt_contact.get()=='' or self.txt_email.get() =='' or self.combo_quest.get() =='Select' or self.txt_answer.get()=='' or self.txt_pas.get() =='' or self.txt_Cpas.get()=='':

            messagebox.showerror('Error', 'All Fields Are Required', parent = self.root)
        
        elif self.txt_pas.get() != self.txt_Cpas.get():

            messagebox.showerror('Error', "Password & Confirm Password Should Be Same", parent = self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror('Error','I Agrre The Terms & Conditions')

        else:

            try:

                con = pymysql.connect(host = "localhost", user = "root", password = "", database = "employee2")

                cur = con.cursor()

                cur.execute("select * from employee where email=%s",self.txt_email.get())

                row=cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "User is already Exist Please try another Email")
                
                else:


                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                    self.txt_fname.get(), 
                                    self.txt_lname.get(), 
                                    self.txt_contact.get(),
                                    self.txt_email.get(), 
                                    self.combo_quest.get(),
                                    self.txt_answer.get(), 
                                    self.txt_pas.get()
                                    ))    

                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Regiseration Successfull")
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent = self.root)

 
root = Tk()
obj = Register(root)
root.mainloop()

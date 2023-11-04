from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox



class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title('Employee Management System')

        #variables
        self.var_dept=StringVar()
        self.var_name = StringVar()
        self.var_desig = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_married = StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idno=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()




        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',35,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1910,height=50)

        img_logo=Image.open('img2.jpeg')
        img_logo=img_logo.resize((55,55),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=460,y=0,width=55,height=55)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1900,height=160)
        #image1
        img1=Image.open('img1.jpeg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=160)
        #image2
        img2=Image.open('img3.jpeg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=540,y=0,width=540,height=160)
        #image3
        img3=Image.open('img4.jpeg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)
        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=1000,y=0,width=540,height=160)

        #Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=220,width=1900,height=560)
        #Title
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text="Employee Information",font=('times new roman',14,'bold'),fg='orange')
        upper_frame.place(x=10,y=10,width=1880,height=270)
        #DownFrame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text="Employee Information Table",font=('times new roman',14,'bold'),fg='orange')
        down_frame.place(x=10,y=280,width=1880,height=500)
        
        #Input Fields
        dept=Label(upper_frame,text='Department : ',font=('times new roman',12),bg='white')
        dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept=ttk.Combobox(upper_frame,textvariable=self.var_dept, font=('times new roman',12),width=17,state='readonly')
        combo_dept['value']=('select Department','Administration','Human Resources','Management','Software Development','Sales','Marketing','Finance','Quality Assurance','Production','Security','Inspection')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Name
        name=Label(upper_frame,font=('times new roman',12),text='Employee Name : ',bg='white')
        name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('times new roman',12))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        #Designation
        desig=Label(upper_frame,font=('times new roman',12),text="Designation : ",bg="white")
        desig.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_desig,width=22,font=('times new roman',12))
        txt_desig.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        #EmailAddress
        email=Label(upper_frame,font=('times new roman',12),text="Email : ",bg="white")
        email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('times new roman',12))
        txt_email.grid(row=1,column=3,sticky=W,padx=2,pady=7)
        #Address
        address=Label(upper_frame,font=('times new roman',12),text="Address : ",bg="white")
        address.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('times new roman',12))
        txt_address.grid(row=2,column=1,sticky=W,padx=2,pady=7)
        #married
        marital=Label(upper_frame,text='Married Status : ',font=('times new roman',12),bg='white')
        marital.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        combo_marital=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('times new roman',12),width=17,state='readonly')
        combo_marital['value']=('Married','Unmarried','Divorced')
        combo_marital.current(0)
        combo_marital.grid(row=2,column=3,padx=2,pady=7,sticky=W)
        #dob
        dob=Label(upper_frame,font=('times new roman',12),text="Date of Birth : ",bg="white")
        dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('times new roman',12))
        txt_dob.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        #doj
        doj=Label(upper_frame,font=('times new roman',12),text="Date of Joining : ",bg="white")
        doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('times new roman',12))
        txt_doj.grid(row=3,column=3,sticky=W,padx=2,pady=7)
        #Identity Proof 
        doj=Label(upper_frame,font=('times new roman',12),text="ID Proof : ",bg="white")
        doj.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        combo_id_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('times new roman',12),width=17,state='readonly')
        combo_id_proof['value']=('Select Your Identity Proof','Employee ID Card','PAN CARD')
        combo_id_proof.current(0)
        combo_id_proof.grid(row=4,column=1,padx=2,pady=7,sticky=W)

        id_no=Label(upper_frame,font=('times new roman',12),text="ID Number : ",bg="white")
        id_no.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        self.var_idno=StringVar()
        id_no=ttk.Entry(upper_frame,textvariable=self.var_idno,width=22,font=('times new roman',12))
        id_no.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        #Gender
        gender=Label(upper_frame,font=('times new roman',12),text="Gender : ",bg="white")
        gender.grid(row=5,column=0,sticky=W,padx=2,pady=7)

        combo_id_proof=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('times new roman',12),width=17,state='readonly')
        combo_id_proof['value']=('Male','Female','Other')
        combo_id_proof.current(0)
        combo_id_proof.grid(row=5,column=1,padx=2,pady=7,sticky=W)
        #phone number
        phone=Label(upper_frame,font=('times new roman',12),text='Contact Number : ',bg='white')
        phone.grid(row=5,column=2,sticky=W,padx=2,pady=7)

        phone=ttk.Entry(upper_frame,textvariable=self.var_mobile,width=22,font=('times new roman',12))
        phone.grid(row=5,column=3,padx=2,pady=7)   
        #Country
        country=Label(upper_frame,font=('times new roman',12),text='Country : ',bg='white')
        country.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('times new roman',12))
        country.grid(row=0,column=5,padx=2,pady=7)     
        #CTC
        ctc=Label(upper_frame,font=('times new roman',12),text='CTC : ',bg='white')
        ctc.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('times new roman',12))
        ctc.grid(row=1,column=5,padx=2,pady=7)

        #image
        img5=Image.open('i6.jpeg')
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.i6=ImageTk.PhotoImage(img5)
        self.i6=Label(upper_frame,image=self.i6)
        self.i6.place(x=1000,y=0,width=220,height=220)
        #button
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1390,y=0,width=180,height=200)
        
        btn_add=Button(button_frame,text="Save",command=self.add_data,font=("times new roman",14,"bold"),width=15,bg="purple",fg="white")
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        
        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("times new roman",14,"bold"),width=15,bg="purple",fg="white")
        btn_update.grid(row=1,column=0,padx=1,pady=5)
        
        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("times new roman",14,"bold"),width=15,bg="purple",fg="white")
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("times new roman",14,"bold"),width=15,bg="purple",fg="white")
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

        


        #DownFrame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text="Employee Information Table",font=('times new roman',14,'bold'),fg='orange')
        down_frame.place(x=10,y=280,width=1880,height=500)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text="Search Employee Information",font=("times new roman",14),fg="orange")
        search_frame.place(x=0,y=0,width=1880,height=300)

        search_by=Label(search_frame,bg='white',text="Search By : ",font=("times new roman",14),fg="purple")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()
        search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=('times new roman',14),width=18)
        search['values']=("Select one option","Contact","ID_NO")
        search.current(0)
        search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,font=('times new roman',14),width=22)
        txt_search.grid(row=0,column=2,padx=5)

        #search_buttons
        btn_search=Button(search_frame,text="search",command=self.search_data,font=('times new roman',14),width=14)
        btn_search.grid(row=0,column=3,padx=5)
        btn_showAll=Button(search_frame,text="Show All",command=self.fetch_data,font=('times new roman',14),width=14)
        btn_showAll.grid(row=0,column=4,padx=5)
        #Employee Table
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1870,height=170)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(table_frame,column=('dept','name','desig','email','address','marital','dob','doj','id','id no','gender','mobile','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading('dept',text='Department')
        self.employee_table.heading('name',text='Employee Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('marital',text='Married Status')
        self.employee_table.heading('dob',text='Date of Birth')
        self.employee_table.heading('doj',text='Date of Joining')
        self.employee_table.heading('id',text='ID Proof')
        self.employee_table.heading('id no',text='ID_NO')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('mobile',text='Contact')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='CTC')
        self.employee_table['show']='headings'
        self.employee_table.column('dept',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('desig',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('marital',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('id',width=100)
        self.employee_table.column('id no',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('mobile',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)

        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    
    def add_data(self):
        if self.var_dept.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","Please Fill all the fields")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",passwd="Sameer143@",db="scores")
                mycursor=con.cursor()
                mycursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                    self.var_dept.get(),
                                                    self.var_name.get(),
                                                    self.var_desig.get(),
                                                    self.var_email.get(),
                                                    self.var_address.get(),
                                                    self.var_married.get(),
                                                    self.var_dob.get(),
                                                    self.var_doj.get(),
                                                    self.var_idproofcomb.get(),
                                                    self.var_idno.get(),
                                                    self.var_gender.get(),
                                                    self.var_mobile.get(),
                                                    self.var_country.get(),
                                                    self.var_salary.get()

                ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Employee Added Successfully !",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To :{str(es)}',parent=self.root)
    
    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="Sameer143@", db="scores")
        mycursor = con.cursor()
        mycursor.execute('select * from employee')
        data=mycursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            con.commit()
        con.close()
    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dept.set(data[0])
        self.var_name.set(data[1])
        self.var_desig.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idno.set(data[9])
        self.var_gender.set(data[10])
        self.var_mobile.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
    def update_data(self):
        if self.var_dept.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","Please Fill all the fields")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",passwd="Sameer143@",db="scores")
                mycursor=con.cursor()
                mycursor.execute('select * from employee where ID_NO=%s',(self.var_idno.get(),))
                existing_record=mycursor.fetchone()
                if existing_record:
                     mycursor.execute('''
                    UPDATE employee SET 
                    Department=%s, Name=%s, Designation=%s, EMail=%s, Address=%s, 
                    Married_status=%s, DOB=%s, DOJ=%s, ID_proof=%s, ID_NO=%s, 
                    Gender=%s, Contact=%s, Country=%s, Salary=%s 
                    WHERE ID_NO=%s
                ''', (
                    self.var_dept.get(), self.var_name.get(), self.var_desig.get(),
                    self.var_email.get(), self.var_address.get(), self.var_married.get(),
                    self.var_dob.get(), self.var_doj.get(), self.var_idproofcomb.get(),
                    self.var_idno.get(), self.var_gender.get(), self.var_mobile.get(),
                    self.var_country.get(), self.var_salary.get(), self.var_idno.get()
                ))
                else:
                    messagebox.showerror("Error","ID Number doesn't exists.!")

                #update=messagebox.askyesno('Update','Are you sure to update this employee data')
                #if update>0:     
                    #con=mysql.connector.connect(host="localhost",user="root",passwd="Sameer143@",db="scores")
                    #mycursor=con.cursor()
                   # mycursor.execute('update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,ID_proof=%s,ID_NO=%s,Gender=%s,Contact=%s,Country=%s,Salary=%s where Married_status=%s',(
                                                    #self.var_dept.get(), self.var_name.get(), self.var_desig.get(),
                    #self.var_email.get(), self.var_address.get(), self.var_married.get(),
                    #self.var_dob.get(), self.var_doj.get(), self.var_idproofcomb.get(),
                    #self.var_idno.get(), self.var_gender.get(), self.var_mobile.get(),
                    #self.var_country.get(), self.var_salary.get(), self.var_married.get()

                    #))
                #else:
                   # if not update:
                       # return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Successful",'Employee details successfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)
    def delete_data(self):
        if self.var_idno.get()=="":
            messagebox.showerror("Error","Please enter ID Number:")
        else:
            try:
                delete=messagebox.askyesno('Delete','Are you sure to Delete this Employee?')
                if delete>0:
                    con=mysql.connector.connect(host="localhost",user="root",passwd="Sameer143@",db="scores")
                    mycursor=con.cursor()
                    sqlquery = "DELETE FROM employee WHERE ID_NO=%s" 
                    value=(self.var_idno.get(),)
                    mycursor.execute(sqlquery,value)
                else:
                    if not delete:
                        return
                    
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Deleted","Record Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)
    def reset_data(self):
         self.var_dept.set("Select Department:")
         self.var_name.set("")
         self.var_desig.set("")
         self.var_email.set("")
         self.var_address.set("")
         self.var_married.set("")
         self.var_dob.set("")
         self.var_doj.set("")
         self.var_idproofcomb.set("Select ID proof:")
         self.var_idno.set("")
         self.var_gender.set("")
         self.var_mobile.set("")
         self.var_country.set("")
         self.var_salary.set("")
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Search Error","Enter the Search Criteria and Value.")
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",passwd="Sameer143@",db="scores")
                mycursor=con.cursor()
                mycursor.execute('DESCRIBE employee')
                col=[col[0] for col in mycursor.fetchall()]
                print(col)
                #mycursor.execute('SELECT * FROM employee WHERE `' +str(self.var_com_search.get())+"` LIKE '%" +str(self.var_search.get()+ "%'"))
                mycursor.execute('SELECT * FROM employee WHERE ' +str(self.var_com_search.get())+" LIKE '%" +str(self.var_search.get()+ "%'"))
                rows=mycursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                con.commit()
                con.close()
            except Exception as es:            
                 messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)
























if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

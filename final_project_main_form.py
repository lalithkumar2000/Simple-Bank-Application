from tkinter import*
from pymysql import*
from tkinter import messagebox
from cryptography import*
window=Tk()
window.geometry("650x300")
window.title("HDFC bank")
window.resizable(0, 0)

db = connect(host='localhost', port=3306, user='root', passwd='root', db='lalith')
cursor=db.cursor()

Label(window,bg='#E6E6FA',height=4,width=100).place(x=0)

Label(window,text='HDFC Bank Login',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=200,y=20)

Label(window,bg='#E6E6FA',height=12,width=100).place(y=60)

Label(window,text='User Name',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=180,y=100)
ent_uname=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_uname.place(x=300,y=100)

Label(window,text='Password',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=180,y=160)
password = StringVar()
enty_pass=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
enty_pass.place(x=300,y=160)

def login_event():
    v_name=ent_uname.get()
    v_pass=enty_pass.get()
    sql="select * from login where username='%s' "%(v_name)
    cursor.execute(sql)
    row_count = cursor.rowcount
    results = cursor.fetchall()
    #print("data: ",result)

    if row_count !=0:
        for clm in results:
            v_username=clm[0]
            v_password=clm[1]
            print("clm[0]: %s, clm[1] : %s"%(clm[0],clm[1]))
            if v_name==v_username and v_pass==v_password:
                messagebox.showinfo("Login", "Login sucessfully.")
                window.destroy()
                import final_project_form_1
            elif v_name==v_username and v_pass!=v_password:
                messagebox.showinfo("Login", "Invalid password.")
            else:
                messagebox.showerror("Login", "Invalid username and password.")
    else:
        #messagebox.showerror("Error","%s does not exists."%(ent_uname.get()))
        messagebox.showinfo("Login", "Invalid user name.")

def clr_event():
    ent_uname.delete(0,END)
    enty_pass.delete(0,END)


Label(window,bg='#F8F8FF',height=4,width=100).place(y=235)
Button(window,text='Login',font=("Times New Roman", 14,'bold'),width=8,command=login_event).place(x=10,y=250)
Button(window,text='Save',font=("Times New Roman", 14,'bold'),width=8,command=clr_event).place(x=115,y=250)
window.mainloop()







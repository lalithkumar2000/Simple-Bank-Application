from tkinter import*
from pymysql import*
from datetime import*
from tkinter import messagebox

window=Tk()
window.geometry("400x300")
window.title("Options")
window.resizable(0, 0)

db = connect(host='localhost', port=3306, user='root', passwd='root', db='lalith')
cursor=db.cursor()

def add_money():
    v_pin=int(ent_pinnum.get())
    v_amt=int(ent_amt.get())
    #v_rmk=int(ent_rem.get())

    today = date.today()

    v_msg="$%d is credited to account XXXXXXX%d on %s"%(v_amt,v_pin,today)
    print("msg: ",v_msg)
    sql='insert into transaction_history values (%d,"%s")'%(v_pin,v_msg)
    print("sql: ",sql)
    cursor.execute(sql)
    
    upd="update bank_payments set account_balance=account_balance+%d where pin_number=%d"%(v_amt,v_pin)
    cursor.execute(upd)
    print("upd: ",upd)

    db.commit()
     
    messagebox.showinfo("Amount","Money added successfully")
    window.destroy()
 
Label(window,bg='#E6E6FA',height=4,width=60).place(x=0)

Label(window,text='Add Money',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=55,y=20)

Label(window,bg='#F8F8FF',height=12,width=60).place(y=60)

Label(window,text='pin number',font=("Times New Roman", 14,'bold'),fg='black',bg='#F8F8FF').place(x=30,y=90)
ent_pinnum=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_pinnum.place(x=160,y=90)

'''Label(window,text='Remarks',font=("Times New Roman", 14,'bold'),fg='black',bg='#F8F8FF').place(x=30,y=130)
ent_rem=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_rem.place(x=160,y=130)'''

Label(window,text='Amount',font=("Times New Roman", 14,'bold'),fg='black',bg='#F8F8FF').place(x=30,y=170)
ent_amt=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_amt.place(x=160,y=170)

Label(window,bg='#E6E6FA',height=4,width=60).place(y=235)

Button(window,text='ok',font=("Times New Roman", 14,'bold'),width=5,command=add_money).place(x=30,y=225)
Button(window,text='cancel',font=("Times New Roman", 14,'bold'),width=5).place(x=200,y=225)
window.mainloop()



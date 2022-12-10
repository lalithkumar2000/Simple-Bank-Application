from tkinter import*
from pymysql import*
from datetime import*
from tkinter import messagebox

window=Tk()
window.geometry("400x300")
window.title("Payment")
window.resizable(0, 0)

db = connect(host='localhost', port=3306, user='root', passwd='root', db='lalith')
cursor=db.cursor()

def acct_transction():
    v_acct=int(ent_acct.get())
    v_amt=int(ent_amt.get())
    v_pin=int(ent_pin.get())
    #v_rmk=int(ent_rem.get())

    today = date.today()

    v_msg="$%d is debited to account XXXXXXX%d on %s"%(v_amt,v_acct,today)
    print("msg: ",v_msg)
    sql='insert into transaction_history values (%d,"%s")'%(v_pin,v_msg)
    print("sql: ",sql)
    cursor.execute(sql)
    
    upd="update bank_payments set account_balance=account_balance-%d where pin_number=%d"%(v_amt,v_pin)
    cursor.execute(upd)
    print("upd: ",upd)

    db.commit()
     
    messagebox.showinfo("Amount","Transaction  successfully")
    window.destroy()

    
Label(window,bg='#E6E6FA',height=4,width=60).place(x=0)
Label(window,text='Account Transaction',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=130,y=20)


Label(window,bg='#F8F8FF',height=12,width=60).place(y=60)
Label(window,text='Account Number',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=10,y=90)
ent_acct=Entry(window,font=("Times New Roman", 14,'bold'),width=17)
ent_acct.place(x=200,y=90)

Label(window,text='IFSC Code',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=10,y=120)
ent_ifsc=Entry(window,font=("Times New Roman", 14,'bold'),width=17)
ent_ifsc.place(x=200,y=120)


Label(window,text='Amount',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=10,y=150)
ent_amt=Entry(window,font=("Times New Roman", 14,'bold'),width=17)
ent_amt.place(x=200,y=150)

Label(window,text=' your pin number',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=10,y=180)
ent_pin=Entry(window,font=("Times New Roman", 14,'bold'),width=17)
ent_pin.place(x=200,y=180)

Label(window,bg='#E6E6FA',height=4,width=60).place(y=235)
Label(window,bg='#F8F8FF',height=4,width=100).place(y=235)
Button(window,text='send',font=("Times New Roman", 14,'bold'),width=8,command=acct_transction).place(x=10,y=250)
Button(window,text='cancel',font=("Times New Roman", 14,'bold'),width=8).place(x=115,y=250)
window.mainloop()


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

def bill_payment():
    v_acct=int(ent_ID.get())
    v_amt=int(ent_amt.get())
    v_pin=int(ent_pin.get())
    #v_rmk=int(ent_rem.get())

    today = date.today()

    v_msg="$%d is Paid to Bill Id %d on %s"%(v_amt,v_acct,today)
    print("msg: ",v_msg)
    sql='insert into transaction_history values (%d,"%s")'%(v_pin,v_msg)
    print("sql: ",sql)
    cursor.execute(sql)
    
    upd="update bank_payments set account_balance=account_balance-%d where pin_number=%d"%(v_amt,v_pin)
    cursor.execute(upd)
    print("upd: ",upd)

    db.commit()
     
    messagebox.showinfo("Amount","Bill Paid Successfully.")
    window.destroy()

Label(window,bg='#E6E6FA',height=4,width=60).place(x=0)
Label(window,text='Bill Payment',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=130,y=20)


Label(window,bg='#F8F8FF',height=12,width=60).place(y=60)
Label(window,text='Bill ID',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=30,y=90)
ent_ID=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_ID.place(x=160,y=90)

Label(window,text='Amount',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=30,y=130)
ent_amt=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_amt.place(x=160,y=130)

Label(window,text='Pin number',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=30,y=170)
ent_pin=Entry(window,font=("Times New Roman", 14,'bold'),width=15)
ent_pin.place(x=160,y=170)

Label(window,bg='#E6E6FA',height=4,width=60).place(y=235)

Button(window,text='ok',font=("Times New Roman", 14,'bold'),width=5,command=bill_payment).place(x=30,y=225)
Button(window,text='cancel',font=("Times New Roman", 14,'bold'),width=5).place(x=200,y=225)
window.mainloop()

from tkinter import*
from pymysql import*

window=Tk()
window.geometry("650x500")
window.title("Account Balance")
window.resizable(0, 0)

db = connect(host='localhost', port=3306, user='root', passwd='root', db='lalith')
cursor=db.cursor()

#Label(window,bg='#E6E6FA',height=4,width=100).place(x=0)

Label(window,text='Account Balance',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=200,y=20)

#Label(window,bg='#E6E6FA',height=20,width=100).place(y=60)


Label(window,text='Pin number',font=("Times New Roman", 14,'bold'),fg='black',bg='#F0E68C').place(x=100,y=70)
ent_pin=Entry(window,font=("Times New Roman", 14,'bold'),width=20)
ent_pin.place(x=220,y=70)



Label(window,text='Account Balance',font=("Times New Roman", 14,'bold'),fg='black',bg='#ff809f').place(x=30,y=150)
txt=Text(window,font=("Times New Roman", 14,'bold'),height=13,width=40)

txt.place(x=200,y=150)


#Label(window,bg='#F8F8FF',height=4,width=100).place(y=235)
def balance_event():
    v_pin=int(ent_pin.get())
    
    sql="select * from transaction_history where pin_number=%d"%(v_pin)

    cursor.execute(sql)
    results = cursor.fetchall()
    query="select * from bank_payments where pin_number=%d"%(v_pin)
    cursor.execute(query)
    bal_res=cursor.fetchall()
    #print("balance : ",bal)
    for bal in  bal_res:
            txt.insert(INSERT, "Current Balance: $%s\n"%(str(bal[1]))+"\n")
            txt.place(x=200,y=150)
            for column in results:
                print("data:" ,column)
                
                txt.insert(INSERT,str(column[1])+"\n")
                txt.place(x=200,y=150)  
 #configure(text=str(column))

Button(window,text='Mini Statement',font=("Times New Roman", 14,'bold'),width=20,command=balance_event).place(x=30,y=450)
Button(window,text='cancel',font=("Times New Roman", 14,'bold'),width=8).place(x=400,y=450)
window.mainloop()

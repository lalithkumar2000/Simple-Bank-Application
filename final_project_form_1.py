from tkinter import*
window=Tk()
window.geometry("400x300")
window.title("Options")
window.resizable(0, 0)

def account_balance():
    import account_balance
    
def send_money():
    import final_project_Cash_transaction

def Add_money():
    import final_project_Add_money

    
Label(window,bg='#E6E6FA',height=4,width=60).place(x=0)

Label(window,text='Internet Banking',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=55,y=20)

Label(window,bg='#F8F8FF',height=12,width=60).place(y=60)

Button(window,text='Account Balance',font=("Times New Roman", 14,'bold'),width=15,command=account_balance).place(x=70,y=80)
Button(window,text='Pay (or) Send Money',font=("Times New Roman", 14,'bold'),width=15,command=send_money).place(x=70,y=140)
Button(window,text='Add Money',font=("Times New Roman", 14,'bold'),width=15,command=Add_money).place(x=70,y=190)

Label(window,bg='#E6E6FA',height=4,width=60).place(y=235)





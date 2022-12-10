from tkinter import*

window=Tk()
window.geometry("400x300")
window.title("Payment")
window.resizable(0, 0)

def bill_payment():
    import final_project_Bill_payment

def account_transaction():
    import final_project_Account_transaction_page
    
Label(window,bg='#E6E6FA',height=4,width=60).place(x=0)
Label(window,text='PAY',font=("Times New Roman", 18,'bold'),bg='#E6E6FA',fg='black').place(x=150,y=20)


Label(window,bg='#F8F8FF',height=12,width=60).place(y=60)
Button(window,text='Bill payment',font=("Times New Roman", 14,'bold'),width=16,command=bill_payment).place(x=70,y=80)
Button(window,text='Account Transaction',font=("Times New Roman", 14,'bold'),width=16,command=account_transaction).place(x=70,y=140)



Label(window,bg='#E6E6FA',height=4,width=60).place(y=235)

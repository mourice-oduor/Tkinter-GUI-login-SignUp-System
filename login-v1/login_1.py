from tkinter import *
import sqlite3

window=Tk()
window.title("Python: GUI Login Application")
window.geometry("400x200")
#window.configure(bg='#105e1a')

def login():
	def login_database():
		conn=sqlite3.connect("login.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
		row=cur.fetchall()
		conn.close()
		print(row)
		if row!=[]:
			user_name=row[0][1]
			l3.config(text="user name found with name:\n "+user_name,fg= "green" ,font = ("calibri", 18))
		else:
			l3.config(text="user not found ")
       


	window.destroy()
	login_window=Tk()
	login_window.geometry("450x250")
	l1=Label(login_window,text="email",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(login_window,text="password",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(login_window,font="times 20")
	l3.grid(row=5,column=2)
	print("Login session started")

	email_text=StringVar()
	e1=Entry(login_window,textvariable=email_text)
	e1.grid(row=1,column=2)
	password_text=StringVar()
	e2=Entry(login_window,textvariable=password_text)
	e2.grid(row=2,column=2)


	b1=Button(login_window,text="login",width=20,fg="#0ad135", bg="#120b4d",command=login_database)
	b1.grid(row=4,column=2)
	#b3 = Button(window, text='Back', command=Back)
	#b3.grid(row=6,column=2)
	login_window.mainloop()




def signup():


	def signup_database():
		conn=sqlite3.connect("login.db")
		cur=conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
		cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
		l4=Label(signup_window,text="account created",font="times 15")
		l4.grid(row=6,column=2)
		Label(signup_window, text = "Registration Sucess", fg = "green" ,font = ("calibri", 14)).grid(row=8,column=2)
		conn.commit()
		conn.close()





	window.destroy()
	signup_window=Tk()
	signup_window.geometry("400x250")
	l1=Label(signup_window,text="user name",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(signup_window,text="user email",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(signup_window,text="Password",font="times 20")
	l3.grid(row=3,column=1)


	name_text=StringVar()
	e1=Entry(signup_window,textvariable=name_text)
	e1.grid(row=1,column=2)
	email_text=StringVar()
	e2=Entry(signup_window,textvariable=email_text)
	e2.grid(row=2,column=2)
	password_text=StringVar()
	e3=Entry(signup_window,textvariable=password_text)
	e3.grid(row=3,column=2)

	b1=Button(signup_window,text="login",width=18,fg="#0ad135", bg="#120b4d",command=signup_database)
	b1.grid(row=4,column=2)
	#b3 = Button(window, text='Back', command=Back)
	#b3.grid(row=6,column=2)
	

# def Back():
#     window.destroy()
#     window.deiconify()


l1=Label(window,text="Please Login or SignUp\n first in order to continue ",fg="red",bg="white",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="Login",width=20,command=login)
b1.grid(row=2,column=3)

b2=Button(window,text="Signup",width=20,command=signup)
b2.grid(row=4,column=3)


window.mainloop()

if __name__ == '__main__':
    window.mainloop()

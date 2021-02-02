from tkinter import *
import os

#fetches assets from tkinter

def delete1():
    screen1.destroy()

   
def delete3():
   screen4.destroy()

def delete4():
   screen5.destroy()

#delete variables are to end the error message processes, when the "OK" button is pressed. 

def logout():
    screen8.destroy()



def calendar1():
    
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Calendar")
    screen9.geometry("400x400")
    print(calendar.calendar)



def session():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text= "Welcome to the shared calendar application!").pack()
    Button(screen8, text = "View Calendar", command = calendar1 ).pack()
    Button(screen8, text = "Log out", command = logout).pack()

def login_success():
  session()
    
 
  


def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("error")
  screen4.geometry("150x100")
  Label(screen4, text = "Incorrect Password").pack()
  Label(screen4, text="").pack()
  Button(screen4,text = "OK", command = delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("error")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found!").pack()
  Label(screen5, text="").pack()
  Button(screen5,text = "OK", command = delete4).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+ ".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    #stores the inputted information in a .txt file, which it will use as a reference for future logins.
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Success", fg = "light blue", font = ("calibri", 11)).pack() 

#clears the fields once the user has registered.
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete (0, END)
    password_entry1.delete (0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
      file1 = open(username1, "r")
      verify = file1.read().splitlines()
      verify1 = verify[1]
      if password1 == verify1:
        login_success()
      else:
        password_not_recognised()

    else:
        user_not_found() 
   #This part not only finds the username and password (saved in the program files upon account creation), 
   # but also stops a potential bypass - where a user can gain access to the app by using a correct username
   # for both fields.#    





def register():
    global screen1
    screen1= Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

#global variables - variables are not just locally available

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text ="Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    #creating two entries, and storing them into the text variable
    Label(screen1, text ="Password * ").pack()
    password_entry= Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Register", width = "10",height  = "1", command = register_user).pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "close", width = "10",height  = "1", command = delete1).pack()



def login():
    print("Login session started")
    global screen2 
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_entry1
    global password_entry1

    global username_entry
    global password_entry

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify )
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command= login_verify).pack()



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Calendar 1.0")
    Label(text = "Calendar 1.0", bg = "grey", width = "300", height = "2", font = ("calibri", 13)).pack()
    Label(text ="").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text ="").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()

    screen.mainloop()
#.pack allows for buttons and labels to remain one size, even if window is expanded. 
#this is also the first screen that you come across on the application
main_screen()

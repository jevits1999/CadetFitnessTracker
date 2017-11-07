from sqlite3 import Error
from easygui import *
import os, hashlib, sqlite3, shutil

def make_program_files_directory():     #Checks to see if "Program Files" directory exists.
    if not os.path.exists("Program Files"):
        os.makedirs("Program Files")

def setup_users_database():     #Sets up users database for user details to be stored.
    if not os.path.exists("Program Files\users.db"):
        conn = sqlite3.connect("Program Files\users.db")
        c = conn.cursor()
        c.execute("create table Users (Name, Username, Password, Type, Age, Height, Weight)")
        conn.commit()
        conn.close()
        setup_admin_account()
        
def setup_admin_account():
    global name, username, Type,  age, height, weight
    upper_counter, lower_counter = 0, 0
    name, username, Type,  dob, height, weight = "Administrator", "Admin", "Admin", "", "", ""  #Sets variables for all acount sections other than password.
    try:
        password1 = passwordbox("Enter the Password for the Administrators account: It must contain 8 - 16 charactors, an Uppercase & Lowercase", "Admin Set Up")#Gets the password for the user account
        if password1 != None:
            password2 = passwordbox("Re-enter the Password for the Administrators account", "Admin Set Up") #Gets the user to re-enter the password for the user accout
        
        if password1 == password2:
            if len(password1) >= 8 and len(password1) <= 32:
                while upper_counter <= len(password1)-1:
                    if password1[upper_counter] == password1[upper_counter].upper():
                        upper_counter = 1000
                        while lower_counter <= len(password1)-1:
                            if password1[lower_counter] == password1[lower_counter].lower():
                                lower_counter = 1000
                                password = hashlib.sha512(password1).hexdigest()

                                add_admin(password)
                            else:
                                lower_counter = lower_counter + 1
                                if lower_counter == len(password1):
                                    msgbox("password does not contain Lowercase Character")
                                    setup_admin_account()
                    else:
                        upper_counter = upper_counter + 1
                        if upper_counter == len(password1):
                            msgbox("password does not contain Uppercase Character")
                            setup_admin_account()
            else:
                msgbox("Password is not of correct length")
                setup_admin_account()
        else:
            msgbox("Passwords do not Match")
            setup_admin_account()
    except TypeError:
        error()
    except UnboundLocalError:
        error()
    

def add_admin(password):
    global name, username, Type, dob, height, weight
    conn = sqlite3.connect("Program Files\users.db")
    c = conn.cursor()
    c.execute('INSERT INTO Users VALUES (?,?,?,?,?,?,?)', (name, username, password, Type, dob, height, weight)) #Adds admin account to the database
    conn.commit()
    conn.close()

def error():
    msgbox("Error With Setup")
    if os.path.exists("Program Files\users.db"):
        shutil.rmtree("Program Files")

make_program_files_directory()
setup_users_database()

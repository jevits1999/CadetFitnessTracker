from easygui import *
import hashlib, csv, os, sqlite3


def start_menu():
    action = buttonbox("Cadet Fitness Tracker, Logon or Exit", "Start", ("Logon", "Exit"))
    if action == "Logon":
        logon()
    elif action == "Exit":
        os._exit(0)
        
def logon():
    try:
        database_data = []
        UNPW_values = []
        UNPW_values = multpasswordbox("Enter your Username & Password", "Log On", ["Username","Password"])
        username = UNPW_values[0]
        
        password = hashlib.sha512(UNPW_values[1]).hexdigest()
        conn = sqlite3.connect("Program Files\users.db")
        c = conn.cursor()
        for row in conn.execute("select Username, Password, Type from Users"):
            database_data.append(row)
        for x in range(len(database_data)):
            if database_data[x][0] == username and database_data[x][1] == password:
                if database_data[x][2] == "Admin":
                    admin_menu()
                elif database_data[x][2] == "Staff":
                    staff_menu()
                elif database_data[x][2] == "Cadet":
                    cadet_menu()
            else:
                msgbox("Username / Password is Incorrect")
                logon()
    except TypeError:
        start_menu()

def admin_menu():
    action = buttonbox("Main Menu", "Admin Menu", ("Add User", "View Users", "Edit Users", "Log Off"))
    if action == "Add User":
        add_user()
    elif action == "View Users":
        view_users()
    elif action == "Edit Users":
        edit_users()
    elif action == "Log Off":
        start_menu()

def add_user():
    acount_type = buttonbox("Select Account Type To Add", "Account Type", ["Staff", "Cadet"])
    UNPW_values = []
    UNPW_values = multpasswordbox("Enter your Username & Password", "Log On", ["First Name", "Surname", "Username","Password"])
    name = UNPW_values[0].lower() + " " + " " + UNPW_values[1].lower()
    username = UNPW_values[2]
    password1 = UNPW_values[3]
    ###########
    
def view_users():
    print "View User"

def edit_users():
    print "Edit Users"
    



def staff_menu():
    action = buttonbox("Main Menu", "Staff Menu", ("Add Log", "View Logs", "Log Off"))

def cadet_menu():
    action = buttonbox("Main Menu", "Cadet Menu", ("Add Log", "View Logs", "Log Off"))


add_user()
##start_menu()

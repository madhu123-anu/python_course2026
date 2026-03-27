import tkinter as tk
from tkinter import messagebox
import random
import os

USER_FILE = "users.txt"
TICKET_FILE = "tickets.txt"

# create files
if not os.path.exists(USER_FILE):
    open(USER_FILE,"w").close()

if not os.path.exists(TICKET_FILE):
    open(TICKET_FILE,"w").close()

# ---------------- TRAIN DATA ----------------
trains = {
    "101":{"name":"Express","time":"09:00 AM","seats":5},
    "102":{"name":"Superfast","time":"02:30 PM","seats":5},
    "103":{"name":"Intercity","time":"07:45 PM","seats":5}
}

berths = ["Lower","Middle","Upper"]

# ---------------- UPDATE TRAIN LIST ----------------
def update_train_list():

    train_text="Train List\n\n"
    train_text+="No   Name        Time       Seats\n"
    train_text+="------------------------------------\n"

    for t in trains:
        train_text+=f"{t}   {trains[t]['name']}   {trains[t]['time']}   {trains[t]['seats']}\n"

    train_label.config(text=train_text)


# ---------------- SIGNUP ----------------
def signup():

    username = signup_user.get()
    password = signup_pass.get()

    with open(USER_FILE,"r") as f:
        users=f.readlines()

    for user in users:
        u,p=user.strip().split(",")
        if username==u:
            messagebox.showerror("Error","User already exists")
            return

    with open(USER_FILE,"a") as f:
        f.write(f"{username},{password}\n")

    messagebox.showinfo("Success","Account Created")


# ---------------- LOGIN ----------------
def login():

    username = login_user.get()
    password = login_pass.get()

    with open(USER_FILE,"r") as f:
        users=f.readlines()

    for user in users:
        u,p=user.strip().split(",")

        if username==u and password==p:
            messagebox.showinfo("Success","Login Successful")
            login_frame.pack_forget()
            open_main_system()
            return

    messagebox.showerror("Error","Invalid Login")


# ---------------- BOOK TICKET ----------------
def book_ticket():

    name=name_entry.get()
    date=date_entry.get()
    time=time_entry.get()
    train_no=train_var.get()
    seats=int(seat_var.get())

    if name=="" or date=="" or time=="":
        result_label.config(text="Fill all details")
        return

    train=trains[train_no]

    if seats>train["seats"]:
        messagebox.showerror("Error","Not enough seats")
        return

    pnr=random.randint(1000,9999)

    berth=random.choice(berths)

    train["seats"]-=seats

    result=f"""
PNR : {pnr}
Name : {name}
Train : {train_no} {train['name']}
Train Time : {train['time']}
Journey Date : {date}
Journey Time : {time}
Seats Booked : {seats}
Berth : {berth}
Seats Left : {train['seats']}
Status : Confirmed
"""

    result_label.config(text=result)

    # save ticket
    with open(TICKET_FILE,"a") as f:
        f.write(result+"\n------------------\n")

    update_train_list()


# ---------------- MAIN SYSTEM ----------------
def open_main_system():

    main_frame.pack()

    update_train_list()


# ---------------- ROOT WINDOW ----------------
root = tk.Tk()
root.title("Railway Reservation System")
root.geometry("450x600")


# ---------------- LOGIN FRAME ----------------
login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame,text="Login",font=("Arial",14)).pack()

tk.Label(login_frame,text="Username").pack()
login_user=tk.Entry(login_frame)
login_user.pack()

tk.Label(login_frame,text="Password").pack()
login_pass=tk.Entry(login_frame,show="*")
login_pass.pack()

tk.Button(login_frame,text="Login",command=login).pack(pady=5)

tk.Label(login_frame,text="Signup").pack()

signup_user=tk.Entry(login_frame)
signup_user.pack()

signup_pass=tk.Entry(login_frame,show="*")
signup_pass.pack()

tk.Button(login_frame,text="Sign Up",command=signup).pack(pady=5)


# ---------------- MAIN FRAME ----------------
main_frame = tk.Frame(root)

tk.Label(main_frame,text="Railway Ticket Booking",font=("Arial",16)).pack()

train_label=tk.Label(main_frame,text="",justify="left")
train_label.pack()

# train select
tk.Label(main_frame,text="Select Train").pack()
train_var=tk.StringVar()
train_menu=tk.OptionMenu(main_frame,train_var,*trains.keys())
train_menu.pack()

# seat select
tk.Label(main_frame,text="Select Seats").pack()
seat_var=tk.StringVar(value="1")
seat_menu=tk.OptionMenu(main_frame,seat_var,"1","2","3","4","5")
seat_menu.pack()

# passenger name
tk.Label(main_frame,text="Passenger Name").pack()
name_entry=tk.Entry(main_frame)
name_entry.pack()

# date
tk.Label(main_frame,text="Journey Date").pack()
date_entry=tk.Entry(main_frame)
date_entry.pack()

# time
tk.Label(main_frame,text="Journey Time").pack()
time_entry=tk.Entry(main_frame)
time_entry.pack()

tk.Button(main_frame,text="Book Ticket",command=book_ticket).pack(pady=10)

result_label=tk.Label(main_frame,text="",justify="left")
result_label.pack(pady=20)

root.mainloop()
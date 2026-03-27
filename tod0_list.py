import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

FILE = "tasks.csv"

# ---------------- LOAD TASKS ----------------
tasks = []

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                tasks.append(row)

def save_tasks():
    with open(FILE,"w",newline="") as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

# ---------------- ADD TASK ----------------
def add_task():

    task = task_entry.get()
    category = category_var.get()
    due_date = date_entry.get()
    due_time = time_entry.get()

    if task == "":
        messagebox.showerror("Error","Task cannot be empty")
        return

    tasks.append([task,"Pending",category,due_date,due_time])
    save_tasks()
    refresh_list()
    task_entry.delete(0,tk.END)

# ---------------- REFRESH LIST ----------------
def refresh_list(filter_type="All"):

    tree.delete(*tree.get_children())

    for t in tasks:

        if filter_type=="Completed" and t[1]!="Completed":
            continue

        if filter_type=="Pending" and t[1]!="Pending":
            continue

        tree.insert("",tk.END,values=t)

    update_summary()

# ---------------- MARK COMPLETE ----------------
def complete_task():

    selected = tree.selection()

    if not selected:
        return

    item = tree.item(selected[0])["values"]

    for t in tasks:
        if t == item:
            t[1] = "Completed"

    save_tasks()
    refresh_list()

# ---------------- DELETE TASK ----------------
def delete_task():

    selected = tree.selection()

    if not selected:
        return

    item = tree.item(selected[0])["values"]

    tasks.remove(item)

    save_tasks()
    refresh_list()

# ---------------- EDIT TASK ----------------
def edit_task():

    selected = tree.selection()

    if not selected:
        return

    item = tree.item(selected[0])["values"]

    task_entry.delete(0,tk.END)
    task_entry.insert(0,item[0])

    category_var.set(item[2])
    date_entry.delete(0,tk.END)
    date_entry.insert(0,item[3])

    time_entry.delete(0,tk.END)
    time_entry.insert(0,item[4])

    tasks.remove(item)
    save_tasks()
    refresh_list()

# ---------------- SORT ----------------
def sort_alpha():

    tasks.sort(key=lambda x:x[0])
    refresh_list()

def sort_date():

    tasks.sort(key=lambda x:x[3])
    refresh_list()

# ---------------- CLEAR ALL ----------------
def clear_all():

    confirm = messagebox.askyesno("Confirm","Delete all tasks?")

    if confirm:
        tasks.clear()
        save_tasks()
        refresh_list()

# ---------------- SUMMARY ----------------
def update_summary():

    total = len(tasks)
    completed = len([t for t in tasks if t[1]=="Completed"])
    pending = total - completed

    summary_label.config(
        text=f"Total: {total}   Completed: {completed}   Pending: {pending}"
    )

# ---------------- REMINDER ----------------
def check_reminders():

    now = datetime.now()

    for t in tasks:

        if t[1]=="Pending":

            try:
                due = datetime.strptime(
                    t[3]+" "+t[4], "%Y-%m-%d %H:%M"
                )

                if abs((due-now).seconds) < 60:
                    messagebox.showinfo(
                        "Reminder",
                        f"Task Due: {t[0]}"
                    )
            except:
                pass

    root.after(60000,check_reminders)

# ---------------- DARK MODE ----------------
dark = False

def toggle_dark():

    global dark

    dark = not dark

    if dark:
        root.configure(bg="#222")
        summary_label.configure(background="#222",foreground="white")
    else:
        root.configure(bg="white")
        summary_label.configure(background="white",foreground="black")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Advanced ToDo App")
root.geometry("700x500")

frame = ttk.Frame(root)
frame.pack(pady=10)

task_entry = ttk.Entry(frame,width=30)
task_entry.grid(row=0,column=0,padx=5)

category_var = tk.StringVar()
category = ttk.Combobox(frame,textvariable=category_var)
category["values"] = ("Work","Study","Personal")
category.grid(row=0,column=1)

date_entry = ttk.Entry(frame,width=12)
date_entry.insert(0,"2026-03-12")
date_entry.grid(row=0,column=2)

time_entry = ttk.Entry(frame,width=8)
time_entry.insert(0,"18:00")
time_entry.grid(row=0,column=3)

ttk.Button(frame,text="Add Task",command=add_task).grid(row=0,column=4)

# ---------------- TREEVIEW ----------------
columns=("Task","Status","Category","DueDate","DueTime")

tree = ttk.Treeview(root,columns=columns,show="headings")

for col in columns:
    tree.heading(col,text=col)

tree.pack(fill="both",expand=True,pady=10)

# ---------------- BUTTONS ----------------
btn_frame = ttk.Frame(root)
btn_frame.pack()

ttk.Button(btn_frame,text="Complete",command=complete_task).grid(row=0,column=0,padx=5)
ttk.Button(btn_frame,text="Delete",command=delete_task).grid(row=0,column=1,padx=5)
ttk.Button(btn_frame,text="Edit",command=edit_task).grid(row=0,column=2,padx=5)
ttk.Button(btn_frame,text="Sort A-Z",command=sort_alpha).grid(row=0,column=3,padx=5)
ttk.Button(btn_frame,text="Sort by Date",command=sort_date).grid(row=0,column=4,padx=5)

# filter buttons
filter_frame = ttk.Frame(root)
filter_frame.pack(pady=5)

ttk.Button(filter_frame,text="All",command=lambda:refresh_list("All")).grid(row=0,column=0,padx=5)
ttk.Button(filter_frame,text="Completed",command=lambda:refresh_list("Completed")).grid(row=0,column=1,padx=5)
ttk.Button(filter_frame,text="Pending",command=lambda:refresh_list("Pending")).grid(row=0,column=2,padx=5)

ttk.Button(filter_frame,text="Clear All",command=clear_all).grid(row=0,column=3,padx=5)
ttk.Button(filter_frame,text="Dark Mode",command=toggle_dark).grid(row=0,column=4,padx=5)

# summary
summary_label = tk.Label(root,text="")
summary_label.pack(pady=5)

load_tasks()
refresh_list()
check_reminders()

root.mainloop()
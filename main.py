import sqlite3
import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors
import mysql.connector

def fetch_data():
    mydb = mysql.connector.connect(
    host="db4free.net",
    user="s24794",
    password="",
    database="s24794"
    )
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM Students")
        result = mycursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        return result

def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], ))

def open_new_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową książkę")
    email_label = ttk.Label(new_window, text="Email:")
    email_label.pack()
    email_entry = ttk.Entry(new_window)
    email_entry.pack()
    first_name_label = ttk.Label(new_window, text="Imię:")
    first_name_label.pack()
    first_name_entry = ttk.Entry(new_window)
    first_name_entry.pack()
    last_name_label = ttk.Label(new_window, text="Nazwisko:")
    last_name_label.pack()
    last_name_entry = ttk.Entry(new_window)
    last_name_entry.pack()
    project_label = ttk.Label(new_window, text="Projekt:")
    project_label.pack()
    project_entry = ttk.Entry(new_window)
    project_entry.pack()
    l1_label = ttk.Label(new_window, text="l1:")
    l1_label.pack()
    l1_entry = ttk.Entry(new_window)
    l1_entry.pack()
    l2_label = ttk.Label(new_window, text="l2:")
    l2_label.pack()
    l2_entry = ttk.Entry(new_window)
    l2_entry.pack()
    l3_label = ttk.Label(new_window, text="l3:")
    l3_label.pack()
    l3_entry = ttk.Entry(new_window)
    l3_entry.pack()
    h1_label = ttk.Label(new_window, text="h1:")
    h1_label.pack()
    h1_entry = ttk.Entry(new_window)
    h1_entry.pack()
    h2_label = ttk.Label(new_window, text="h2:")
    h2_label.pack()
    h2_entry = ttk.Entry(new_window)
    h2_entry.pack()
    h3_label = ttk.Label(new_window, text="h3:")
    h3_label.pack()
    h3_entry = ttk.Entry(new_window)
    h3_entry.pack()
    h4_label = ttk.Label(new_window, text="h4:")
    h4_label.pack()
    h4_entry = ttk.Entry(new_window)
    h4_entry.pack()
    h5_label = ttk.Label(new_window, text="h5:")
    h5_label.pack()
    h5_entry = ttk.Entry(new_window)
    h5_entry.pack()
    h6_label = ttk.Label(new_window, text="h6:")
    h6_label.pack()
    h6_entry = ttk.Entry(new_window)
    h6_entry.pack()
    h7_label = ttk.Label(new_window, text="h7:")
    h7_label.pack()
    h7_entry = ttk.Entry(new_window)
    h7_entry.pack()
    h8_label = ttk.Label(new_window, text="h8:")
    h8_label.pack()
    h8_entry = ttk.Entry(new_window)
    h8_entry.pack()
    h9_label = ttk.Label(new_window, text="h9:")
    h9_label.pack()
    h9_entry = ttk.Entry(new_window)
    h9_entry.pack()
    h10_label = ttk.Label(new_window, text="h10:")
    h10_label.pack()
    h10_entry = ttk.Entry(new_window)
    h10_entry.pack()
    mark_label = ttk.Label(new_window, text="Ocena:")
    mark_label.pack()
    mark_entry = ttk.Entry(new_window)
    mark_entry.pack()
    status_label = ttk.Label(new_window, text="Status:")
    status_label.pack()
    status_entry = ttk.Entry(new_window)
    status_entry.pack()
    def add_new():
        email = email_entry.get()
        firstName = first_name_entry.get()
        lastName = last_name_entry.get()
        project = project_entry.get()
        l1 = l1_entry.get()
        l2 = l2_entry.get()
        l3 = l3_entry.get()
        h1 = h1_entry.get()
        h2 = h2_entry.get()
        h3 = h3_entry.get()
        h4 = h4_entry.get()
        h5 = h5_entry.get()
        h6 = h6_entry.get()
        h7 = h7_entry.get()
        h8 = h8_entry.get()
        h9 = h9_entry.get()
        h10 = h10_entry.get()
        mark = mark_entry.get()
        status = status_entry.get()
        conn = mysql.connector.connect(
            host="db4free.net",
            user="s24794",
            password="",
            database="s24794"
        )

        cursor = conn.cursor()
        sql = "INSERT INTO Students (title, author, price, category)VALUES (%s,%s,%s,%s)"
        params = (email,firstName,lastName,project)
        try:
            cursor.execute(sql,params)
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            load_data()
            new_window.destroy()
    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()

def add_book(title, author, price, category):
    try:
        conn = mysql.connector.connect(
            host="db4free.net",
            user="s24794",
            password="",
            database="s24794"
        )
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Students (title, author, price, category) 
        VALUES(%s, %s, %s, %s)''',
            (title, author, price, category))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def open_details_window(event):
    selected_item = treeview.focus()
    if selected_item:
        item_data = treeview.item(selected_item)
        item_val = item_data['values']
        details_window = tk.Toplevel(root)
        details_window.title("Szczegóły")
        email_label = ttk.Label(details_window, text="Email:")
        email_label.pack()
        email_entry = ttk.Entry(details_window)
        email_entry.insert(0, item_val[0])
        email_entry.config(state="disabled")
        email_entry.pack()
        first_name_label = ttk.Label(details_window, text="Imię:")
        first_name_label.pack()
        first_name_entry = ttk.Entry(details_window)
        first_name_entry.insert(0, item_val[1])
        first_name_entry.pack()
        last_name_label = ttk.Label(details_window, text="Nazwisko:")
        last_name_label.pack()
        last_name_entry = ttk.Entry(details_window)
        last_name_entry.insert(0, item_val[2])
        last_name_entry.pack()
        project_label = ttk.Label(details_window, text="Projekt:")
        project_label.pack()
        project_entry = ttk.Entry(details_window)
        project_entry.insert(0, item_val[3])
        project_entry.pack()
        l1_label = ttk.Label(details_window, text="l1:")
        l1_label.pack()
        l1_entry = ttk.Entry(details_window)
        l1_entry.insert(0, item_val[4])
        l1_entry.pack()
        l2_label = ttk.Label(details_window, text="l2:")
        l2_label.pack()
        l2_entry = ttk.Entry(details_window)
        l2_entry.insert(0, item_val[5])
        l2_entry.pack()
        l3_label = ttk.Label(details_window, text="l3:")
        l3_label.pack()
        l3_entry = ttk.Entry(details_window)
        l3_entry.insert(0, item_val[6])
        l3_entry.pack()
        h1_label = ttk.Label(details_window, text="h1:")
        h1_label.pack()
        h1_entry = ttk.Entry(details_window)
        h1_entry.insert(0, item_val[7])
        h1_entry.pack()
        h1_label = ttk.Label(details_window, text="h2:")
        h1_label.pack()
        h1_entry = ttk.Entry(details_window)
        h1_entry.insert(0, item_val[8])
        h1_entry.pack()
        h2_label = ttk.Label(details_window, text="h1:")
        h2_label.pack()
        h2_entry = ttk.Entry(details_window)
        h2_entry.insert(0, item_val[9])
        h2_entry.pack()
        h3_label = ttk.Label(details_window, text="h3:")
        h3_label.pack()
        h3_entry = ttk.Entry(details_window)
        h3_entry.insert(0, item_val[10])
        h3_entry.pack()
        h4_label = ttk.Label(details_window, text="h4:")
        h4_label.pack()
        h4_entry = ttk.Entry(details_window)
        h4_entry.insert(0, item_val[11])
        h4_entry.pack()
        h5_label = ttk.Label(details_window, text="h5:")
        h5_label.pack()
        h5_entry = ttk.Entry(details_window)
        h5_entry.insert(0, item_val[12])
        h5_entry.pack()
        h6_label = ttk.Label(details_window, text="h6:")
        h6_label.pack()
        h6_entry = ttk.Entry(details_window)
        h6_entry.insert(0, item_val[13])
        h6_entry.pack()
        h7_label = ttk.Label(details_window, text="h7:")
        h7_label.pack()
        h7_entry = ttk.Entry(details_window)
        h7_entry.insert(0, item_val[14])
        h7_entry.pack()
        h8_label = ttk.Label(details_window, text="h8:")
        h8_label.pack()
        h8_entry = ttk.Entry(details_window)
        h8_entry.insert(0, item_val[15])
        h8_entry.pack()
        h9_label = ttk.Label(details_window, text="h9:")
        h9_label.pack()
        h9_entry = ttk.Entry(details_window)
        h9_entry.insert(0, item_val[16])
        h9_entry.pack()
        h10_label = ttk.Label(details_window, text="h10:")
        h10_label.pack()
        h10_entry = ttk.Entry(details_window)
        h10_entry.insert(0, item_val[17])
        h10_entry.pack()
        mark_label = ttk.Label(details_window, text="Ocena:")
        mark_label.pack()
        mark_entry = ttk.Entry(details_window)
        mark_entry.insert(0, item_val[18])
        mark_entry.pack()
        status_label = ttk.Label(details_window, text="Status:")
        status_label.pack()
        status_entry = ttk.Entry(details_window)
        status_entry.insert(0, item_val[19])
        status_entry.pack()
        def update():
            email = email_entry.get()
            firstName = first_name_entry.get()
            lastName = last_name_entry.get()
            project = project_entry.get()
            l1 = l1_entry.get()
            l2 = l2_entry.get()
            l3 = l3_entry.get()
            h1 = h1_entry.get()
            h2 = h2_entry.get()
            h3 = h3_entry.get()
            h4 = h4_entry.get()
            h5 = h5_entry.get()
            h6 = h6_entry.get()
            h7 = h7_entry.get()
            h8 = h8_entry.get()
            h9 = h9_entry.get()
            h10 = h10_entry.get()
            mark = mark_entry.get()
            status = status_entry.get()
            conn = mysql.connector.connect(
                host="db4free.net",
                user="s24794",
                password="",
                database="s24794"
            )
            cursor = conn.cursor()
            query = "UPDATE Students SET firstName=%s, lastName=%s, project=%s, l1=%s, l2=%s, l3=%s, h1=%s, h2=%s, h3=%s, h4=%s, h5=%s, h6=%s, h7=%s, h8=%s, h9=%s, h10=%s, mark=%s, status=%s,  WHERE email=%s"
            p = (firstName, lastName, project, l1, l2, l3, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, mark, status, email)
            try:
                cursor.execute(query, p)
                conn.commit()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
                load_data()
                details_window.destroy()
        update = ttk.Button(details_window, text="Aktualizuj", command=update)
        update.pack()
        def delete():
            email = email_entry.get()
            firstName = first_name_entry.get()
            lastName = last_name_entry.get()
            conn = mysql.connector.connect(
                host="db4free.net",
                user="s24794",
                password="",
                database="s24794"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM Students WHERE email = %s AND firstName = %s AND lastName = %s"
            params = (email, firstName, lastName)
            try:
                cursor.execute(sql, params)
                conn.commit()
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
                load_data()
                details_window.destroy()
        update = ttk.Button(details_window, text="Usun", command=delete)
        update.pack()

root = tk.Tk()
root.title("Students")
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")
treeview = ttk.Treeview(root)
treeview["columns"] = ("email", "firstName", "lastName", "project", "l1", "l2", "l3", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "mark", "status")
treeview.column("#0", width=0)
treeview.heading("email", text="Email")
treeview.heading("firstName", text="Imię")
treeview.heading("lastName", text="Nazwisko")
treeview.heading("project", text="Projekt")
treeview.heading("l1", text="l1")
treeview.heading("l2", text="l2")
treeview.heading("l3", text="l3")
treeview.heading("h1", text="h1")
treeview.heading("h1", text="h1")
treeview.heading("h2", text="h2")
treeview.heading("h3", text="h3")
treeview.heading("h4", text="h4")
treeview.heading("h5", text="h5")
treeview.heading("h6", text="h6")
treeview.heading("h7", text="h7")
treeview.heading("h8", text="h8")
treeview.heading("h9", text="h9")
treeview.heading("h10", text="h10")
treeview.heading("mark", text="Ocena")
treeview.heading("status", text="Status")
treeview.pack()
add_new_book_button = tk.Button(root, text="Dodaj nowego studenta", command=open_new_book_window)
add_new_book_button.pack(side="left")
treeview.bind("<Double-1>",open_details_window)
load_data()
root.mainloop()
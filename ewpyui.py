import tkinter as tk
from tkinter import messagebox
from datetime import datetime

requests = {}

def schedule_pickup():
    name = name_entry.get().strip()
    item = item_entry.get().strip()
    quantity = quantity_entry.get().strip()
    address = address_entry.get().strip()
    date = date_entry.get().strip()

    if not name or not item or not quantity or not address or not date:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        pickup_date = datetime.strptime(date, "%d-%m-%Y")
        if pickup_date < datetime.today():
            messagebox.showerror("Error", "Pickup date cannot be in the past!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid date format! Use DD-MM-YYYY.")
        return

    requests[name] = {"Item": item, "Quantity": quantity, "Address": address, "Date": date, "Status": "Scheduled"}
    messagebox.showinfo("Success", f"Pickup scheduled for {name} on {date}.")
    clear_entries()

def view_requests():
    listbox.delete(0, tk.END)
    for name, details in requests.items():
        listbox.insert(tk.END, f"{name} - {details['Item']} - {details['Quantity']} - {details['Address']} - {details['Date']} - {details['Status']}")

def cancel_request():
    name = name_entry.get().strip()
    if name in requests:
        requests[name]["Status"] = "Cancelled"
        messagebox.showinfo("Success", f"Pickup for {name} cancelled.")
    else:
        messagebox.showerror("Error", "No request found for this name.")

def mark_completed():
    name = name_entry.get().strip()
    if name in requests and requests[name]["Status"] == "Scheduled":
        requests[name]["Status"] = "Completed"
        messagebox.showinfo("Success", f"Pickup for {name} marked as completed.")
    else:
        messagebox.showerror("Error", "No active request found for this name.")

def modify_request():
    name = name_entry.get().strip()
    new_item = item_entry.get().strip()
    new_quantity = quantity_entry.get().strip()
    new_address = address_entry.get().strip()
    new_date = date_entry.get().strip()

    if name in requests:
        try:
            pickup_date = datetime.strptime(new_date, "%d-%m-%Y")
            if pickup_date < datetime.today():
                messagebox.showerror("Error", "Pickup date cannot be in the past!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Use DD-MM-YYYY.")
            return

        requests[name]["Item"] = new_item
        requests[name]["Quantity"] = new_quantity
        requests[name]["Address"] = new_address
        requests[name]["Date"] = new_date
        messagebox.showinfo("Success", f"Pickup for {name} updated.")
    else:
        messagebox.showerror("Error", "No request found for this name.")

def clear_entries():
    name_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

root = tk.Tk()
root.title("E-Waste Collection System")
root.geometry("500x600")
root.configure(bg="lightblue")

tk.Label(root, text="Name:", font=("Times New Roman", 14), bg="lightgray").pack(pady=2)
name_entry = tk.Entry(root, font=("Times New Roman", 14), bg="white")
name_entry.pack(pady=2)

tk.Label(root, text="E-Waste Item:", font=("Times New Roman", 14), bg="lightgray").pack(pady=2)
item_entry = tk.Entry(root, font=("Times New Roman", 14), bg="white")
item_entry.pack(pady=2)

tk.Label(root, text="Quantity:", font=("Times New Roman", 14), bg="lightgray").pack(pady=2)
quantity_entry = tk.Entry(root, font=("Times New Roman", 14), bg="white")
quantity_entry.pack(pady=2)

tk.Label(root, text="Pickup Address:", font=("Times New Roman", 14), bg="lightgray").pack(pady=2)
address_entry = tk.Entry(root, font=("Times New Roman", 14), bg="white")
address_entry.pack(pady=2)

tk.Label(root, text="Pickup Date (DD-MM-YYYY):", font=("Times New Roman", 14), bg="lightgray").pack(pady=2)
date_entry = tk.Entry(root, font=("Times New Roman", 14), bg="white")
date_entry.pack(pady=2)

button_style = {"font": ("Times New Roman", 14), "width": 20, "height": 2}

tk.Button(root, text="Schedule Pickup", command=schedule_pickup, bg="green", fg="white", **button_style).pack(pady=5)
tk.Button(root, text="View Requests", command=view_requests, bg="blue", fg="white", **button_style).pack(pady=5)
tk.Button(root, text="Cancel Pickup", command=cancel_request, bg="red", fg="white", **button_style).pack(pady=5)
tk.Button(root, text="Mark Completed", command=mark_completed, bg="purple", fg="white", **button_style).pack(pady=5)
tk.Button(root, text="Modify Pickup", command=modify_request, bg="orange", fg="white", **button_style).pack(pady=5)

listbox = tk.Listbox(root, font=("Times New Roman", 12), width=60, height=5, bg="white", fg="black")
listbox.pack(pady=10)

tk.Button(root, text="Exit", command=root.quit, bg="black", fg="white", **button_style).pack(pady=5)

root.mainloop()

import tkinter as tk
from tkinter import messagebox, ttk

# Inventory List to Store Item Data
Inventory = []

# Function to Add Item
def Add_Item () :
    Name = Name_Entry.get ()
    Quantity = Quantity_Entry.get ()
    Price = Price_Entry.get ()

    if Name and Quantity and Price :
        try :
            Inventory.append ({
                "Name" : Name,
                "Quantity" : int (Quantity),
                "Price" : float (Price)
            })

            Update_Inventory ()

            Clear_Entries ()

        except ValueError :
            messagebox.showerror ("Invalid Input", "Quantity must be an Integer and Price must be a Number")

    else :
        messagebox.showwarning ("Missing Failed", "All Fields are Required.")

# Fucntion to Update Treeview with Inventory Items
def Update_Inventory () :
    for Row in Tree.get_children () :
        Tree.delete (Row)

    for IDX, Item in enumerate (Inventory) :
        Tree.insert ("", "end", iid=IDX, values=(Item["Name"], Item["Quantity"], Item["Price"]))

# Function to Clear Entry Fields
def Clear_Entries () :
    Name_Entry.delete (0, tk.END)
    Quantity_Entry.delete (0, tk.END)
    Price_Entry.delete (0, tk.END)

def Delete_Item () :
    Selected = Tree.selection ()

    if Selected :
        Index = int(Selected[0])
        del Inventory[Index]
        Update_Inventory ()

    else :
        messagebox.showwarning ("No Selection", "Please Select an Item to Delete.")

# Setup Main Window
Root = tk.Tk ()
Root.title ("Inventory App")

# Entry Fields
tk.Label (Root, text="Item Name").grid (row=0, column=0, padx=5,pady=5)

Name_Entry = tk.Entry (Root)

Name_Entry.grid (row=0, column=1, padx=5, pady=5)
tk.Label (Root, text="Quantity").grid(row=1, column=0, padx=5, pady=5)
Quantity_Entry = tk.Entry (Root)
Quantity_Entry.grid (row=1, column=1, padx=5, pady=5)
tk.Label (Root, text="Price").grid (row=2, column=0, padx=5, pady=5)
Price_Entry = tk.Entry (Root)
Price_Entry.grid (row=2, column=1, padx=5, pady=5)

# Button
Add_Button = tk.Button (Root, text="Add Item", command=Add_Item)
Add_Button.grid (row=3, column=0, columnspan=2, pady=10)
Delete_Button = tk.Button (Root, text="Delete Selected", command=Delete_Item)
Delete_Button.grid (row=4, column=0, columnspan=2, pady=5)

# Treeview to Display Inventory
Columns = ("Name", "Quantity", "Price")
Tree = ttk.Treeview (Root, columns=Columns, show="headings")

for Col in Columns :
    Tree.heading (Col, text=Col)

Tree.grid (row=5, column=0, columnspan=2, pady=10)

# Start the GUI Event Loop
Root.mainloop ()
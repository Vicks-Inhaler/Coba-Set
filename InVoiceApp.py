import tkinter as tk
from tkinter import ttk

# Main Application Class
class InVoice_App:
    def __init__(self, Root):
        self.Root = Root
        self.Root.title("InVoice Application")

        # --- Customer Name Entry ---
        tk.Label(Root, text="Customer Name : ").pack()
        self.Customer_Name = tk.Entry(Root)
        self.Customer_Name.pack()

        # --- Item Input Section ---
        frame = tk.Frame(Root)
        frame.pack(pady=5)

        # Labels for Item, Quantity, Price
        tk.Label(frame, text="Item").grid(row=0, column=0)
        tk.Label(frame, text="Qty").grid(row=0, column=1)
        tk.Label(frame, text="Price").grid(row=0, column=2)

        # Entry Fields for Each Column
        self.Item_Entry = tk.Entry(frame)
        self.Item_Entry.grid(row=1, column=0)
        self.Qty_Entry = tk.Entry(frame)
        self.Qty_Entry.grid(row=1, column=1)
        self.Price_Entry = tk.Entry(frame)
        self.Price_Entry.grid(row=1, column=2)

        # Button to Add Item to InVoice
        tk.Button(frame, text="Add", command=self.Add_Item).grid(row=1, column=3, padx=5, pady=5)

        # --- Table to Display InVoice Item ---
        self.Tree = ttk.Treeview(Root, columns=('Item', 'Qty', 'Price', 'Total'), show='headings')

        for Col in self.Tree['columns']:
            self.Tree.heading(Col, text=Col)

        self.Tree.pack(pady=10)

        # --- Total Section ---
        self.Total_Val = tk.StringVar(value="0.00")  # Total Amount Variable
        tk.Label(Root, text="Total : ").pack()
        tk.Label(Root, textvariable=self.Total_Val).pack()

        # --- Generate InVoice Button ---
        tk.Button(Root, text="Generate InVoice", command=self.Generate_InVoice).pack(pady=5)

    # --- Add Item to the Table and Update Total ---
    def Add_Item(self):
        try:
            Item = self.Item_Entry.get()
            Qty = int(self.Qty_Entry.get())
            Price = float(self.Price_Entry.get())
            Total = Qty * Price

            # Insert the Item into the Table
            self.Tree.insert('', 'end', values=(Item, Qty, f"{Price:.2f}", f"{Total:.2f}"))

            # Update the Running Total
            Current_Total = float(self.Total_Val.get())
            self.Total_Val.set(f"{Current_Total + Total:.2f}")

            # Clear Input Fields for Next Entry
            self.Item_Entry.delete(0, tk.END)
            self.Qty_Entry.delete(0, tk.END)
            self.Price_Entry.delete(0, tk.END)

        except ValueError:
            print("Please enter valid numerical values for Quantity and Price.")

    # --- Print the InVoice Details to the Console ---
    def Generate_InVoice(self):
        print("----- InVoice -----")
        print("Customer : ", self.Customer_Name.get())

        for Item in self.Tree.get_children():
            print(self.Tree.item(Item)['values'])  # Print Item Details

        print("Total : ", self.Total_Val.get())
        print("-------------------")

# --- Run the Application ---
if __name__ == "__main__":
    Root = tk.Tk()
    App = InVoice_App(Root)
    Root.mainloop()
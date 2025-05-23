import tkinter as tk
from tkinter import messagebox, ttk
import math
import csv
import os

# Predefined crops
valid_crops = ["Corn", "Coffee"]

# Vectors (lists) to store data
crops = []
areas = []
inputs = []


# Function to read data from CSV on script start
def load_from_csv():
    if os.path.exists("data.csv"):
        with open("data.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                crops.append(row[0])
                areas.append(float(row[1]))
                inputs.append(float(row[2]))


# Function to save data to CSV
def save_to_csv():
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Crop", "Area", "Input Needed"])
        for i in range(len(crops)):
            writer.writerow([crops[i], areas[i], inputs[i]])


def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_area(radius):
    return math.pi * radius**2


def calculate_inputs(crop, area):
    if crop == "Corn":
        return area * 200  # Example: 200kg/ha for Corn
    elif crop == "Coffee":
        return area * 0.5  # Example: 500mL/m² for Coffee


# GUI Functions
def enter_data():
    crop = crop_combobox.get()
    if crop not in valid_crops:
        messagebox.showerror("Error", "Invalid crop! Please choose a valid one.")
        return

    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        if length <= 0 or width <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Length and width must be positive numbers.")
        return

    area = (
        calculate_rectangle_area(length, width)
        if crop in ["Corn"]
        else calculate_circle_area(length)
    )
    input_needed = calculate_inputs(crop, area)

    crops.append(crop)
    areas.append(area)
    inputs.append(input_needed)

    save_to_csv()
    update_table()
    length_entry.delete(0, tk.END)
    width_entry.delete(0, tk.END)


def update_table():
    # Clear the table first
    for row in tree.get_children():
        tree.delete(row)

    # Insert new data with row numbers
    for i in range(len(crops)):
        tree.insert(
            "", "end", values=(i + 1, crops[i], f"{areas[i]:.2f}", f"{inputs[i]:.2f}")
        )


def delete_data():
    selected_items = tree.selection()
    if selected_items:
        confirm = messagebox.askyesno(
            "Confirm Deletion", "Are you sure you want to delete the selected entries?"
        )
        if confirm:
            # Deletar os itens em ordem reversa para evitar erro de índice
            for selected_item in reversed(selected_items):
                index = tree.index(selected_item)
                crops.pop(index)
                areas.pop(index)
                inputs.pop(index)
            save_to_csv()
            update_table()


def select_all_data():
    # Select all rows in the treeview
    for item in tree.get_children():
        tree.selection_add(item)


def open_update_modal():
    selected_items = tree.selection()

    # Check if more than one row is selected
    if len(selected_items) > 1:
        messagebox.showerror("Error", "Please select only one row to update.")
        return

    if selected_items:
        index = tree.index(selected_items[0])

        # Create a modal window
        modal = tk.Toplevel(root)
        modal.title("Update Entry")

        # Get the position of the main window (root)
        root_x = root.winfo_x()
        root_y = root.winfo_y()

        # Position the modal relative to the main window
        modal.geometry(f"+{root_x + 500}+{root_y + 200}")  # Offset by 500 pixels

        # Get current data for the selected row
        current_crop = crops[index]

        # Fields to update the crop, length, and width
        tk.Label(modal, text="Crop:").grid(row=0, column=0)
        crop_entry = ttk.Combobox(modal, values=valid_crops, state="readonly", width=20)
        crop_entry.set(current_crop)
        crop_entry.grid(row=0, column=1)

        tk.Label(modal, text="Length:").grid(row=1, column=0)
        length_entry = tk.Entry(modal, validate="key")
        length_entry["validatecommand"] = (
            length_entry.register(validate_numeric_input),
            "%P",
        )
        length_entry.grid(row=1, column=1)

        tk.Label(modal, text="Width:").grid(row=2, column=0)
        width_entry = tk.Entry(modal, validate="key")
        width_entry["validatecommand"] = (
            width_entry.register(validate_numeric_input),
            "%P",
        )
        width_entry.grid(row=2, column=1)

        def save_updates():
            try:
                new_crop = crop_entry.get()
                new_length = float(length_entry.get())
                new_width = float(width_entry.get())

                new_area = (
                    calculate_rectangle_area(new_length, new_width)
                    if new_crop in ["Corn"]
                    else calculate_circle_area(new_length)
                )
                new_input_needed = calculate_inputs(new_crop, new_area)

                # Update the lists with the new values
                crops[index] = new_crop
                areas[index] = new_area
                inputs[index] = new_input_needed

                save_to_csv()
                update_table()
                modal.destroy()  # Close the modal window
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values.")

        tk.Button(modal, text="Save", command=save_updates).grid(
            row=3, column=0, columnspan=2
        )


# Function to validate numeric input
def validate_numeric_input(value):
    return value.isdigit() or value == ""  # Allow empty input for backspace


# GUI setup
root = tk.Tk()
root.title("FIAP - Farm Tech Solutions")
root.geometry("1300x790")

# Centralize the window on screen
root.eval("tk::PlaceWindow %s center" % root.winfo_pathname(root.winfo_id()))

# Frame for inputs
input_frame = tk.Frame(root, padx=20, pady=20)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Crop:", font=("Arial", 14)).grid(
    row=0, column=0, padx=5, pady=5
)

# Combobox for crop selection
crop_combobox = ttk.Combobox(
    input_frame, values=valid_crops, font=("Arial", 14), state="readonly", width=15
)
crop_combobox.grid(row=0, column=1, padx=5, pady=5)
crop_combobox.current(0)  # Select the first crop by default

tk.Label(input_frame, text="Length:", font=("Arial", 14)).grid(
    row=1, column=0, padx=5, pady=5
)
length_entry = tk.Entry(input_frame, font=("Arial", 14), width=15, validate="key")
length_entry["validatecommand"] = (length_entry.register(validate_numeric_input), "%P")
length_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Width:", font=("Arial", 14)).grid(
    row=2, column=0, padx=5, pady=5
)
width_entry = tk.Entry(input_frame, font=("Arial", 14), width=15, validate="key")
width_entry["validatecommand"] = (width_entry.register(validate_numeric_input), "%P")
width_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(
    input_frame, text="Add Data", command=enter_data, font=("Arial", 14), width=20
).grid(row=3, column=0, columnspan=2, pady=10)

# Frame for the table and scrollbar
table_frame = tk.Frame(root)
table_frame.pack(pady=20)

# Add scrollbar for the table
scrollbar = ttk.Scrollbar(table_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Treeview (table) to display data with row numbers
tree = ttk.Treeview(
    table_frame,
    columns=("Row", "Crop", "Area", "Input"),
    show="headings",
    height=10,
    yscrollcommand=scrollbar.set,
    selectmode="extended",
)
scrollbar.config(command=tree.yview)

tree.column("Row", anchor=tk.CENTER, width=50)
tree.column("Crop", anchor=tk.CENTER, width=200)
tree.column("Area", anchor=tk.CENTER, width=150)
tree.column("Input", anchor=tk.CENTER, width=150)

tree.heading("Row", text="#")
tree.heading("Crop", text="Crop")
tree.heading("Area", text="Area")
tree.heading("Input", text="Input Needed")
tree.pack()

# Buttons for deleting data and selecting all
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(
    button_frame,
    text="Delete Selected",
    font=("Arial", 14),
    width=20,
    command=delete_data,
)
delete_button.grid(row=0, column=0, padx=10)

select_all_button = tk.Button(
    button_frame,
    text="Select All",
    font=("Arial", 14),
    width=20,
    command=select_all_data,
)
select_all_button.grid(row=0, column=1, padx=10)

update_button = tk.Button(
    button_frame,
    text="Update",
    font=("Arial", 14),
    width=20,
    command=open_update_modal,
)
update_button.grid(row=0, column=2, padx=10)

# Load existing data
load_from_csv()
update_table()

root.mainloop()

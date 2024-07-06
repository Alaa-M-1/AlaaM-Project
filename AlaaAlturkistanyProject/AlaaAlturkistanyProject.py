import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def add_element():
    new_element = entry.get()  # Get text from entry widget
    if entry.get() != 'Enter text here..':
        if new_element:
            listbox.insert(tk.END, new_element)  # Insert new element at the end
            entry.delete(0, tk.END)  # Clear the entry field

def delete_element():
    selected_index = listbox.curselection()  # Get index of selected item
    if selected_index:
        listbox.delete(selected_index)  # Delete selected item from listbox
        
def on_entry_focus_in(event):
    if entry.get() == 'Enter text here..':
        entry.delete(0, tk.END)
        entry.config(fg='grey')  # Change text color to black

def on_entry_focus_out(event):
    if entry.get() == '':
        entry.insert(0, 'Enter text here..')
        entry.config(fg='grey')  # Change text color to grey
        

# Function to handle editing of selected item
def edit_element():
    selected_index = listbox.curselection()  # Get index of selected item
    if selected_index:
        entry.config(fg='black')
        selected_item = listbox.get(selected_index)  # Get the selected item
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(0, selected_item)  # Insert selected item into entry field
        edit_button.config(command=lambda: update_element(selected_index))  # Update button command for editing

# Function to update the selected item in the Listbox
def update_element(index):
    updated_value = entry.get()  # Get updated value from entry field
    listbox.delete(index)  # Delete old value from Listbox
    listbox.insert(index, updated_value)  # Insert updated value into Listbox
    entry.delete(0, tk.END)  # Clear the entry field
    edit_button.config(command=edit_element)  # Restore button command for editing
    
def export_listbox_contents():
    # Open a file for writing (create if it doesn't exist)
    with open("listbox_contents.txt", "w") as file:
        # Get all items from the Listbox
        items = listbox.get(0, tk.END)
        # Write each item to the file
        file.write("**** Tasks list: ****\n")
        for item in items:
            file.write(item + "\n")


# Create main window
window = tk.Tk()
window.title("Image Background Example")

# Load the background image
bg_image = PhotoImage(file="img/photo2.png")
image_width = bg_image.width()
image_height = bg_image.height()

# Set window size to image dimensions
window.geometry(f"{image_width}x{image_height}")

# Create a label with the background image
background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg='white', bd=1, relief=tk.SOLID)
frame.pack( pady=10)

# Entry widget for adding new elements
entry = tk.Entry(frame, width=35, bd=0, highlightthickness=0)
entry.pack(pady=4)
entry.insert(0, 'Enter text here..')
entry.bind('<FocusIn>', on_entry_focus_in)
entry.bind('<FocusOut>', on_entry_focus_out)
frame.place(x=195, y=510) 


image = PhotoImage(file="img/photo3.png")

# Add button to add new element
add_button = tk.Button(window, text="", borderwidth=0,image=image, command=add_element)
add_button.pack()
add_button.place(x=610, y=570) 

image2 = PhotoImage(file="img/photo4.png")

# Add button to edit selected element
edit_button = tk.Button(window, text="", borderwidth=0,image=image2, command=edit_element)
edit_button.pack()
edit_button.place(x=90, y=570) 

# Listbox to display elements
listbox = tk.Listbox(window, width=36, bd=0, highlightthickness=0, font=("Calibri", 18))

listbox.place(x=195, y=270) 
listbox_height = 7 # Set the number of visible rows here
listbox.configure(height=listbox_height)

# Add sample elements to start with
initial_elements = ["Meet up with project leader", "Participate in a code review session", "Debug and fix identified issues"]
for element in initial_elements:
    listbox.insert(tk.END, element)

# Button to delete selected element
delete_button = tk.Button(window, text="Delete selected task",width=16, command=delete_element)
delete_button.pack(pady=2)
delete_button.place(x= 504, y=510) 

# Button to export to text file
export_button = tk.Button(window, text="Export",width=8, command=export_listbox_contents)
export_button.pack(pady=2)
export_button.place(x=425, y=510) 



# Load the image
image_path = "img/photo6.png"
img = Image.open(image_path)
image3 = ImageTk.PhotoImage(img)
image_width, image_height = img.size
# Add the image to the canvas

canvas = tk.Canvas(window, width=image_width, height=image_height, bg="white", bd=0, highlightthickness=0)
canvas.pack()

canvas.create_image(image_width // 2, image_height // 2, image=image3, anchor=tk.CENTER)
canvas.image = image3
canvas.place(x=2, y=25)  


#adding a text 
label = tk.Label(window, text="To ADD a task, type then click add. To EDIT a task select a task then press edit. after editing the task click EDIT again to confirm the changes.", bg="#FFF4F1", anchor="center", justify="center")
label.pack(pady=5)
label.place(x=35, y=45)  

# Start the Tkinter event loop
window.mainloop()

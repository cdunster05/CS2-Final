import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class DogShelterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dog Shelter Management")
        self.geometry("400x300")
        self.current_dog = None

        self.home_page()

    def home_page(self):
        self.clear_frame()
        label = tk.Label(self, text="Welcome to Dog Shelter Management")
        label.pack()

        view_button = tk.Button(self, text="View Dogs", command=self.view_dogs)
        view_button.pack()

        modify_button = tk.Button(self, text="Modify Dogs", command=self.modify_dogs)
        modify_button.pack()

    def view_dogs(self):
        self.clear_frame()
        label = tk.Label(self, text="All Dogs:")
        label.pack()

        for dog in dogs:
            dog_button = tk.Button(self, text=dog.name, command=lambda d=dog: self.view_dog_details(d))
            dog_button.pack()

        back_button = tk.Button(self, text="Back", command=self.home_page)
        back_button.pack()

    def view_dog_details(self, dog):
        self.clear_frame()
        label = tk.Label(self, text=f"Name: {dog.name}\nDescription: {dog.description}")
        label.pack()

        back_button = tk.Button(self, text="Back", command=self.view_dogs)
        back_button.pack()

    def modify_dogs(self):
        self.clear_frame()
        label = tk.Label(self, text="Modify Dogs:")
        label.pack()

        change_button = tk.Button(self, text="Change Current Dogs", command=self.change_dogs)
        change_button.pack()

        add_button = tk.Button(self, text="Add New Dog", command=self.add_dog)
        add_button.pack()

        delete_button = tk.Button(self, text="Delete Dog", command=self.delete_dog)
        delete_button.pack()

        back_button = tk.Button(self, text="Back", command=self.home_page)
        back_button.pack()

    def change_dogs(self):
        self.clear_frame()
        label = tk.Label(self, text="Change Current Dogs:")
        label.pack()

        for dog in dogs:
            dog_button = tk.Button(self, text=dog.name, command=lambda d=dog: self.modify_dog_description(d))
            dog_button.pack()

        back_button = tk.Button(self, text="Back", command=self.modify_dogs)
        back_button.pack()

    def modify_dog_description(self, dog):
        self.clear_frame()
        label = tk.Label(self, text=f"Modify Description for {dog.name}:")
        label.pack()

        description_entry = tk.Entry(self, width=30)
        description_entry.pack()

        save_button = tk.Button(self, text="Save", command=lambda: self.save_description(dog, description_entry.get()))
        save_button.pack()

    def save_description(self, dog, description):
        dog.description = description
        messagebox.showinfo("Success", "Description updated successfully!")
        self.change_dogs()

    def add_dog(self):
        self.clear_frame()
        label = tk.Label(self, text="Add New Dog:")
        label.pack()

        name_entry = tk.Entry(self, width=30)
        name_entry.pack()
        description_entry = tk.Entry(self, width=30)
        description_entry.pack()

        save_button = tk.Button(self, text="Save", command=lambda: self.save_new_dog(name_entry.get(), description_entry.get()))
        save_button.pack()

    def save_new_dog(self, name, description):
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a name for the dog.")
            return

        dogs.append(Dog(name, description))
        messagebox.showinfo("Success", "New dog added successfully!")
        self.modify_dogs()

    def delete_dog(self):
        self.clear_frame()
        label = tk.Label(self, text="Delete Dog:")
        label.pack()

        for dog in dogs:
            dog_button = tk.Button(self, text=dog.name, command=lambda d=dog: self.confirm_delete(d))
            dog_button.pack()

        back_button = tk.Button(self, text="Back", command=self.modify_dogs)
        back_button.pack()

    def confirm_delete(self, dog):
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {dog.name}?")
        if confirm:
            dogs.remove(dog)
            messagebox.showinfo("Success", "Dog deleted successfully!")
            self.delete_dog()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

dogs = [Dog("Buddy", "A friendly Labrador"), Dog("Max", "A playful German Shepherd")]

app = DogShelterApp()
app.mainloop()

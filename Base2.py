import tkinter as tk

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

    def view_dogs(self):
        self.clear_frame()
        label = tk.Label(self, text="All Dogs:")
        label.pack()

        for dog in dogs:
            dog_button = tk.Button(self, text=dog.name, command=lambda: self.view_dog_details(dog))
            dog_button.pack()

        back_button = tk.Button(self, text="Back", command=self.home_page)
        back_button.pack()

    def view_dog_details(self, dog):
        self.clear_frame()
        label = tk.Label(self, text=f"Name: {dog.name}\nDescription: {dog.description}")
        label.pack()

        back_button = tk.Button(self, text="Back", command=self.view_dogs)
        back_button.pack()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

dogs = [Dog("Buddy", "A friendly Labrador"), Dog("Max", "A playful German Shepherd")]

app = DogShelterApp()
app.mainloop()
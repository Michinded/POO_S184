import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.length = 8
        self.include_uppercase = False
        self.include_specials = False
        self.password = ""

    def generate_password(self):
        chars = string.ascii_lowercase
        if self.include_uppercase:
            chars += string.ascii_uppercase
        if self.include_specials:
            chars += string.punctuation

        self.password = "".join(random.choice(chars) for i in range(self.length))

    def check_strength(self):
        password = self.password
        length = len(password)
        strength = "debil"

        if length >= 8 and any(c.isupper() for c in password) and any(not c.isalnum() for c in password):
            strength = "fuerte"
        elif length >= 6 and any(c.isupper() for c in password):
            strength = "medio"

        return strength

class PasswordGUI:
    def __init__(self):
        self.password_generator = PasswordGenerator()

        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("300x290")

        self.length_label = tk.Label(self.window, text="Longitud del Password:")
        self.length_label.pack()
        self.length_entry = tk.Entry(self.window)
        self.length_entry.pack(pady=2)
        self.length_entry.insert(0, "8")

        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(self.window, text="Incluye mayusculas", variable=self.uppercase_var)
        self.uppercase_checkbutton.pack(pady=5)

        self.specials_var = tk.BooleanVar()
        self.specials_checkbutton = tk.Checkbutton(self.window, text="Incluye caracteres", variable=self.specials_var)
        self.specials_checkbutton.pack(pady=5)

        self.generate_button = tk.Button(self.window, text="Generar Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.strength_labeli = tk.Label(self.window,text="Fortaleza del Password: ")
        self.strength_labeli.pack(pady=10)

        self.strength_label = tk.Label(self.window, text="")
        self.strength_label.pack(pady=4)

        self.password_label = tk.Entry(self.window, text="")
        self.password_label.pack(pady=5)

        self.window.mainloop()

    def generate_password(self):
        self.password_generator.length = int(self.length_entry.get())
        self.password_generator.include_uppercase = self.uppercase_var.get()
        self.password_generator.include_specials = self.specials_var.get()
        self.password_label.insert(0, "")
        self.password_label.delete(0, tk.END)
        self.password_generator.generate_password()

        self.password_label.insert(0, self.password_generator.password)

        strength = self.password_generator.check_strength()
        self.strength_label.config(text="Resultado: "+strength)


PasswordGUI()



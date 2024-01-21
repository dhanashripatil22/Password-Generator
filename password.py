import random
import string
import tkinter as tk
from tkinter import ttk
import sys

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected.")

    all_characters = ''.join(character_sets)

    password = ''.join(random.choice(all_characters) for _ in range(length))
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_passwords(num_passwords, length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    return [generate_password(length, use_uppercase, use_lowercase, use_digits, use_special) for _ in range(num_passwords)]

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MystiPass - The Enchanting Password Generator")

        # Centering the window
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = 400
        window_height = 350
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Custom color theme
        style = ttk.Style()
        style.theme_use("clam")  # Choose any existing theme as a base

        # Customizing the color theme
        style.configure("TLabel", foreground="#333", font=("Helvetica", 12))
        style.configure("TButton", background="#4CAF50", foreground="white")
        style.map("TButton", background=[("active", "#45a049")])

        # GUI components
        self.label_length = ttk.Label(master, text="Password Length:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_length = ttk.Entry(master)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_options = ttk.Label(master, text="Password Options:")
        self.label_options.grid(row=1, column=0, columnspan=2, pady=10)

        self.use_uppercase = tk.BooleanVar(value=True)
        self.chk_uppercase = ttk.Checkbutton(master, text="Uppercase Letters", variable=self.use_uppercase)
        self.chk_uppercase.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

        self.use_lowercase = tk.BooleanVar(value=True)
        self.chk_lowercase = ttk.Checkbutton(master, text="Lowercase Letters", variable=self.use_lowercase)
        self.chk_lowercase.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

        self.use_digits = tk.BooleanVar(value=True)
        self.chk_digits = ttk.Checkbutton(master, text="Digits", variable=self.use_digits)
        self.chk_digits.grid(row=4, column=0, columnspan=2, pady=5, sticky="w")

        self.use_special = tk.BooleanVar(value=True)
        self.chk_special = ttk.Checkbutton(master, text="Special Characters", variable=self.use_special)
        self.chk_special.grid(row=5, column=0, columnspan=2, pady=5, sticky="w")

        self.btn_generate = ttk.Button(master, text="Generate Passwords", command=self.generate_passwords_gui)
        self.btn_generate.grid(row=6, column=0, columnspan=2, pady=20)

        self.result_text = tk.Text(master, height=8, width=40)
        self.result_text.grid(row=7, column=0, columnspan=2, padx=10)

    def generate_passwords_gui(self):
        try:
            password_length = int(self.entry_length.get())
            num_passwords = 1  # For GUI, generate only one password at a time

            if password_length < 8:
                self.result_text.delete("1.0", tk.END)
                self.result_text.insert(tk.END, "Password length should be a minimum of 8 characters.")
                return

            passwords = generate_passwords(
                num_passwords,
                password_length,
                self.use_uppercase.get(),
                self.use_lowercase.get(),
                self.use_digits.get(),
                self.use_special.get()
            )

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Enchanting Password: {passwords[0]}\n")

        except ValueError as e:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, str(e))

def main():
    print("Welcome to MystiPass - The Enchanting Password Generator!")

    if len(sys.argv) > 1 and sys.argv[1].lower() == "gui":
        # GUI version
        root = tk.Tk()
        gui = PasswordGeneratorGUI(root)
        root.mainloop()
    else:
        # CLI version
        generate_password_cli()

if __name__ == "__main__":
    main()
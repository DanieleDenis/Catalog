from tkinter import *
from tkinter import ttk, messagebox
import os
import subprocess

class AuthApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Autentificare")
        self.root.geometry("300x200")

        self.label_frame = Frame(self.root)
        self.label_frame.pack(pady=20)

        self.user_label = Label(self.label_frame, text="Utilizator:")
        self.user_label.grid(row=0, column=0, padx=5, pady=5)
        self.user_entry = Entry(self.label_frame)
        self.user_entry.grid(row=0, column=1, padx=5, pady=5)

        self.pass_label = Label(self.label_frame, text="Parolă:")
        self.pass_label.grid(row=1, column=0, padx=5, pady=5)
        self.pass_entry = Entry(self.label_frame, show="*")
        self.pass_entry.grid(row=1, column=1, padx=5, pady=5)

        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=10)

        self.register_button = Button(self.button_frame, text="Înregistrare", command=self.register)
        self.register_button.grid(row=0, column=0, padx=5)

        self.login_button = Button(self.button_frame, text="Autentificare", command=self.login)
        self.login_button.grid(row=0, column=1, padx=5)

    def register(self):
        user = self.user_entry.get()
        password = self.pass_entry.get()

        if not user or not password:
            messagebox.showerror("Eroare", "Vă rugăm să completați toate câmpurile!")
            return

        # Aici adăugați codul pentru înregistrare, cum doriți să stocați datele utilizatorilor

        messagebox.showinfo("Înregistrare", "Înregistrare reușită!")

        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)

    def login(self):
        user = self.user_entry.get()
        password = self.pass_entry.get()

        if not user or not password:
            messagebox.showerror("Eroare", "Vă rugăm să completați toate câmpurile!")
            return

        # Aici adăugați codul pentru autentificare, cum doriți să verificați datele utilizatorilor

        messagebox.showinfo("Autentificare", "Autentificare reușită!")

        # Dacă autentificarea este reușită, puteți crea o instanță a aplicației de catalog și să o rulați
        catalog_app = CatalogApp()
        catalog_app.run()

        # Închideți fereastra de autentificare după ce aplicația de catalog se închide
        self.root.destroy()

    def run(self):
        self.root.mainloop()


class CatalogApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Catalog")
        self.root.geometry("800x600")

        self.catalog = Catalog()

        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=10)

        self.nume_label = Label(self.button_frame, text="Nume:")
        self.nume_label.grid(row=0, column=0, padx=5)
        self.nume_entry = Entry(self.button_frame)
        self.nume_entry.grid(row=0, column=1, padx=5)

        self.prenume_label = Label(self.button_frame, text="Prenume:")
        self.prenume_label.grid(row=0, column=2, padx=5)
        self.prenume_entry = Entry(self.button_frame)
        self.prenume_entry.grid(row=0, column=3, padx=5)

        self.profil_label = Label(self.button_frame, text="Profil:")
        self.profil_label.grid(row=0, column=4, padx=5)
        self.profil_combobox = ttk.Combobox(self.button_frame, values=["AIA", "ROBO", "TI"])
        self.profil_combobox.grid(row=0, column=5, padx=5)

        self.grupa_label = Label(self.button_frame, text="Grupa:")
        self.grupa_label.grid(row=1, column=0, padx=5)
        self.grupa_combobox = ttk.Combobox(self.button_frame, values=["4LF411", "4LF412", "4LF413"])
        self.grupa_combobox.grid(row=1, column=1, padx=5)

        self.an_label = Label(self.button_frame, text="An:")
        self.an_label.grid(row=1, column=2, padx=5)
        self.an_combobox = ttk.Combobox(self.button_frame, values=["I", "II", "III", "IV"])
        self.an_combobox.grid(row=1, column=3, padx=5)

        self.materie_label = Label(self.button_frame, text="Materie:")
        self.materie_label.grid(row=2, column=0, padx=5)
        self.materie_combobox = ttk.Combobox(self.button_frame, values=["Analiza matematica", "Matematici speciale", "Programare orientata pe obiecte", "Grafica asistata", "PCLP"])
        self.materie_combobox.grid(row=2, column=1, padx=5)

        self.nota_label = Label(self.button_frame, text="Nota:")
        self.nota_label.grid(row=2, column=2, padx=5)
        self.nota_combobox = ttk.Combobox(self.button_frame, values=[str(i) for i in range(1, 11)])
        self.nota_combobox.grid(row=2, column=3, padx=5)

        self.adauga_button = Button(self.button_frame, text="Adauga", command=self.adauga_nota)
        self.adauga_button.grid(row=2, column=4, padx=5)

        self.afiseaza_button = Button(self.button_frame, text="Afiseaza Catalog", command=self.afiseaza_catalog)
        self.afiseaza_button.grid(row=2, column=5, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("Nume", "Prenume", "Profil", "Grupa", "An", "Materie", "Nota", "Medie"))
        self.tree.pack()

        self.tree.heading("#0", text="Nr.")
        self.tree.heading("Nume", text="Nume")
        self.tree.heading("Prenume", text="Prenume")
        self.tree.heading("Profil", text="Profil")
        self.tree.heading("Grupa", text="Grupa")
        self.tree.heading("An", text="An")
        self.tree.heading("Materie", text="Materie")
        self.tree.heading("Nota", text="Nota")
        self.tree.heading("Medie", text="Medie")

    def adauga_nota(self):
        nume = self.nume_entry.get()
        prenume = self.prenume_entry.get()
        profil = self.profil_combobox.get()
        grupa = self.grupa_combobox.get()
        an = self.an_combobox.get()
        materie = self.materie_combobox.get()
        nota = self.nota_combobox.get()

        if not nume or not prenume or not profil or not grupa or not an or not materie or not nota:
            messagebox.showerror("Eroare", "Vă rugăm să completați toate câmpurile!")
            return

        self.catalog.adauga_nota(nume, prenume, profil, grupa, an, materie, nota)

        self.nume_entry.delete(0, END)
        self.prenume_entry.delete(0, END)
        self.profil_combobox.set("")
        self.grupa_combobox.set("")
        self.an_combobox.set("")
        self.materie_combobox.set("")
        self.nota_combobox.set("")

    def afiseaza_catalog(self):
        catalog_data = self.catalog.get_catalog()

        self.tree.delete(*self.tree.get_children())

        for i, data in enumerate(catalog_data, start=1):
            self.tree.insert(parent="", index="end", iid=i, text=str(i),
                             values=(data["nume"], data["prenume"], data["profil"], data["grupa"],
                                     data["an"], data["materie"], data["nota"], data["medie"]))

    def run(self):
        self.root.mainloop()


class Catalog:
    def __init__(self):
        self.catalog = []

    def adauga_nota(self, nume, prenume, profil, grupa, an, materie, nota):
        medie = self.calculeaza_medie(nota)
        student = {
            "nume": nume,
            "prenume": prenume,
            "profil": profil,
            "grupa": grupa,
            "an": an,
            "materie": materie,
            "nota": nota,
            "medie": medie
        }
        self.catalog.append(student)

    def calculeaza_medie(self, nota):
        # Aici puteți implementa logica de calcul a mediei pe baza notelor
        # Exemplu: medie = sum(nota) / len(nota)
        return nota

    def get_catalog(self):
        return self.catalog


if __name__ == "__main__":
    auth_app = AuthApp()
    auth_app.run()

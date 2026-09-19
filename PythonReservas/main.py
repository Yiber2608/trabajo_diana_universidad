import tkinter as tk
from tkinter import messagebox
import Usuario
import ReservaSala


my_usuario =  Usuario.Usuario("programacion", "programacion")

usuarios = []
reservas = []
lista_reservas = None


reserva1 = ReservaSala.ReservaSala("Juan Luis", 10, 2000)
reserva1.registrar_inicio(10)
reserva1.registrar_fin(12)
costo_total = reserva1.calcular_costo(12)
print("Usuario de la reserva:", reserva1.obtener_usuario())
print(f"Costo total de la reserva: ${costo_total}")
reservas.append(reserva1)

reserva2 = ReservaSala.ReservaSala("Diana", 9, 3500)
reserva2.registrar_inicio(9)
reserva2.registrar_fin(12)
costo_total2 = reserva2.calcular_costo(12)
print("Usuario de la reserva:", reserva2.obtener_usuario())
print(f"Costo total de la reserva: ${costo_total2}")
reservas.append(reserva2)


def crear_reserva():
    ventana_reserva = tk.Toplevel()
    ventana_reserva.title("Create Reservation")
    ventana_reserva.geometry("300x250")

    tk.Label(ventana_reserva, text="Enter username:").pack(pady=10)
    entry_usuario = tk.Entry(ventana_reserva)
    entry_usuario.pack(pady=5)

    tk.Label(ventana_reserva, text="Enter start time:").pack(pady=10)
    entry_hora_inicio = tk.Entry(ventana_reserva)
    entry_hora_inicio.pack(pady=5)

    tk.Label(ventana_reserva, text="Enter hourly rate:").pack(pady=10)
    entry_tarifa_hora = tk.Entry(ventana_reserva)
    entry_tarifa_hora.pack(pady=5)

    def registrar_reserva():
        usuario = entry_usuario.get()
        hora_inicio = entry_hora_inicio.get()
        tarifa_hora = entry_tarifa_hora.get()

        if usuario == "" or hora_inicio == "" or tarifa_hora == "":
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            hora_inicio = int(hora_inicio)
            tarifa_hora = float(tarifa_hora)
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers for start time and hourly rate.")
            return

        nueva_reserva = ReservaSala.ReservaSala(usuario, hora_inicio, tarifa_hora)
        reservas.append(nueva_reserva)

        messagebox.showinfo("Success", "Reservation created successfully.")
        ventana_reserva.destroy()

        mostrar_reservas()  # Refresh the reservations list

    boton_registrar = tk.Button(ventana_reserva, text="Register Reservation", command=registrar_reserva)
    boton_registrar.pack(pady=15)

def seleccionar_reserva():
    seleccion = lista_reservas.curselection()

    if not seleccion:
        messagebox.showerror("Error", "Please select a reservation.")
        return

    reserva_seleccionada = reservas[seleccion[0] // 2]
    messagebox.showinfo("Reservation Details", f"Username: {reserva_seleccionada.obtener_usuario()}")

    ventana_fin = tk.Toplevel()
    ventana_fin.title("End Time")
    ventana_fin.geometry("300x200")

    tk.Label(ventana_fin, text="Enter end time:").pack(pady=10)

    entry_hora_fin = tk.Entry(ventana_fin)
    entry_hora_fin.pack(pady=5)

    def registrar_fin():
        hora_fin = entry_hora_fin.get()

        if hora_fin == "":
            messagebox.showerror("Error", "End time cannot be empty.")
            return

        try:
            hora_fin = int(hora_fin)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
            return

        if hora_fin < reserva_seleccionada.obtener_hora_inicio():
            messagebox.showerror("Error", "End time cannot be earlier than start time.")
            return

        # Registrar la hora de fin y calcular el costo
        reserva_seleccionada.registrar_fin(hora_fin)
        costo = reserva_seleccionada.calcular_costo(hora_fin)

        messagebox.showinfo(
            "Reservation Updated",
            f"Username: {reserva_seleccionada.obtener_usuario()}\n"
            f"End Time: {hora_fin}\n"
            f"Total Cost: ${costo}"
        )

        ventana_fin.destroy()

    boton_fin = tk.Button(ventana_fin, text="Register End Time", command=registrar_fin)
    boton_fin.pack(pady=15)


def mostrar_reservas():
    lista_reservas.delete(0, tk.END)
    for i, reserva in enumerate(reservas):
        lista_reservas.insert(tk.END, f"Reservation {i+1}: Username: {reserva.obtener_usuario()}")
        lista_reservas.insert(tk.END, "")

def iniciar_sesion():
    username_ingresado = entry_usuario.get()
    password_ingresado = entry_password.get()

    if my_usuario.validar(username_ingresado, password_ingresado):
        ventana_principal = tk.Toplevel(ventana)
        ventana_principal.title("Login")
        ventana_principal.geometry("500x400")

        tk.Label(ventana_principal, text="Study Room Reservations").pack(pady=10)
        tk.Label(ventana_principal, text="Select a reservation:").pack(pady=5)

        global lista_reservas
        lista_reservas = tk.Listbox(ventana_principal, width=50, height=10)
        lista_reservas.pack(pady=5)
        mostrar_reservas()

        boton_seleccionar = tk.Button(ventana_principal, text="Select Reservation", command=seleccionar_reserva)
        boton_seleccionar.pack(pady=10)
        boton_crear = tk.Button(ventana_principal, text="Create Reservation", command=crear_reserva)
        boton_crear.pack(pady=10)

        ventana.withdraw()  # Oculta la ventana de login

    else:
        messagebox.showerror("Error", "Username or password incorrect")

ventana = tk.Tk()
ventana.title("Study Room")
ventana.geometry("400x400")

etiqueta = tk.Label(ventana, text="Reservas")
etiqueta.pack(pady=20)

etiqueta_usuario = tk.Label(ventana, text="Username:")
etiqueta_usuario.pack(pady=5)

entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

etiqueta_password = tk.Label(ventana, text="Password:")
etiqueta_password.pack(pady=5)

entry_password = tk.Entry(ventana, show="*")
entry_password.pack()

button_login = tk.Button(ventana, text="LOGIN", command=iniciar_sesion)
button_login.pack(pady=30)


ventana.mainloop()
from tkinter import *
from tkinter import messagebox
from logica import agregarRegistro, eliminarRegistro, generarGrafico

# VENTANA
ventana = Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("700x500")
ventana.config(bg="#0f172a")


# FUNCION LIMPIAR PANTALLA
def limpiarPantalla():
    for widget in ventana.winfo_children():
        widget.destroy()


# =========================
# MENU PRINCIPAL
# =========================

def menuPrincipal():

    limpiarPantalla()

    # TITULO
    Label(
        ventana,
        text="📦 SISTEMA DE INVENTARIO",
        font=("Arial", 24, "bold"),
        bg="#0f172a",
        fg="white"
    ).pack(pady=40)

    # SUBTITULO
    Label(
        ventana,
        text="Seleccione una opción",
        font=("Arial", 14),
        bg="#0f172a",
        fg="white"
    ).pack(pady=10)

    # BOTON AGREGAR
    Button(
        ventana,
        text="➕ Agregar Producto",
        command=pantallaAgregar,
        bg="#22c55e",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bd=0,
        cursor="hand2"
    ).pack(pady=15)

    # BOTON ELIMINAR
    Button(
        ventana,
        text="❌ Eliminar Producto",
        command=pantallaEliminar,
        bg="#ef4444",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bd=0,
        cursor="hand2"
    ).pack(pady=15)

    # BOTON GRAFICO
    Button(
        ventana,
        text="📊 Ver Gráficos",
        command=generarGrafico,
        bg="#3b82f6",
        fg="white",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bd=0,
        cursor="hand2"
    ).pack(pady=15)


# =========================
# PANTALLA AGREGAR
# =========================

def pantallaAgregar():

    limpiarPantalla()

    Label(
        ventana,
        text="➕ AGREGAR PRODUCTO",
        font=("Arial", 22, "bold"),
        bg="#0f172a",
        fg="white"
    ).pack(pady=20)

    frame = Frame(ventana, bg="#1e293b", padx=30, pady=30)
    frame.pack()

    # LABELS
    def crearLabel(texto):
        Label(
            frame,
            text=texto,
            font=("Arial", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).pack(anchor="w", pady=(10, 2))

    # ENTRYS
    def crearEntry():
        entry = Entry(frame, width=35, font=("Arial", 11))
        entry.pack(ipady=5)
        return entry

    crearLabel("📦 Nombre Producto")
    txtProducto = crearEntry()

    crearLabel("🔢 Cantidad")
    txtCantidad = crearEntry()

    crearLabel("💲 Precio")
    txtPrecio = crearEntry()

    crearLabel("👨 Empleado")
    txtEmpleado = crearEntry()

    crearLabel("🆔 ID Empleado")
    txtIdEmpleado = crearEntry()

    # GUARDAR
    def guardar():

        mensaje = agregarRegistro(
            txtProducto.get(),
            txtCantidad.get(),
            txtPrecio.get(),
            txtEmpleado.get(),
            txtIdEmpleado.get()
        )

        if mensaje == "Registro agregado correctamente":
            messagebox.showinfo("Correcto", mensaje)

            txtProducto.delete(0, END)
            txtCantidad.delete(0, END)
            txtPrecio.delete(0, END)
            txtEmpleado.delete(0, END)
            txtIdEmpleado.delete(0, END)

        else:
            messagebox.showerror("Error", mensaje)

    # BOTON GUARDAR
    Button(
        frame,
        text="Guardar",
        command=guardar,
        bg="#22c55e",
        fg="white",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        bd=0
    ).pack(pady=20)

    # VOLVER
    Button(
        ventana,
        text="⬅ Volver al Menú",
        command=menuPrincipal,
        bg="gray",
        fg="white",
        width=20,
        height=2,
        bd=0
    ).pack(pady=10)


# =========================
# PANTALLA ELIMINAR
# =========================

def pantallaEliminar():

    limpiarPantalla()

    Label(
        ventana,
        text="❌ ELIMINAR PRODUCTO",
        font=("Arial", 22, "bold"),
        bg="#0f172a",
        fg="white"
    ).pack(pady=30)

    frame = Frame(ventana, bg="#1e293b", padx=30, pady=30)
    frame.pack()

    Label(
        frame,
        text="🆔 ID del Registro",
        font=("Arial", 11, "bold"),
        bg="#1e293b",
        fg="white"
    ).pack()

    txtEliminar = Entry(frame, width=30, font=("Arial", 11))
    txtEliminar.pack(ipady=5, pady=10)

    # ELIMINAR
    def eliminar():

        mensaje = eliminarRegistro(txtEliminar.get())

        if mensaje == "Registro eliminado correctamente":
            messagebox.showinfo("Correcto", mensaje)
            txtEliminar.delete(0, END)

        else:
            messagebox.showerror("Error", mensaje)

    # BOTON ELIMINAR
    Button(
        frame,
        text="Eliminar",
        command=eliminar,
        bg="#ef4444",
        fg="white",
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        bd=0
    ).pack(pady=20)

    # VOLVER
    Button(
        ventana,
        text="⬅ Volver al Menú",
        command=menuPrincipal,
        bg="gray",
        fg="white",
        width=20,
        height=2,
        bd=0
    ).pack(pady=10)


# INICIAR MENU
menuPrincipal()
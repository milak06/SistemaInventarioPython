from tkinter import *
from tkinter import messagebox, ttk
from logica import agregarRegistro, eliminarRegistro, generarGrafico, df
import logica

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
    ).pack(pady=15)

    # ---- TABLA DE REGISTROS ----
    frameTabla = Frame(ventana, bg="#0f172a")
    frameTabla.pack(padx=20, pady=10, fill="both", expand=True)

    columnas = ("ID", "Producto", "Cantidad", "Precio", "Fecha", "Empleado", "ID Emp.")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "Inventario.Treeview",
        background="#1e293b",
        foreground="white",
        fieldbackground="#1e293b",
        rowheight=24,
        font=("Arial", 10)
    )
    style.configure(
        "Inventario.Treeview.Heading",
        background="#3b82f6",
        foreground="white",
        font=("Arial", 10, "bold")
    )
    style.map("Inventario.Treeview", background=[("selected", "#ef4444")])

    tabla = ttk.Treeview(
        frameTabla,
        columns=columnas,
        show="headings",
        style="Inventario.Treeview",
        height=8
    )

    anchos = [50, 150, 80, 80, 100, 120, 70]
    for col, ancho in zip(columnas, anchos):
        tabla.heading(col, text=col)
        tabla.column(col, width=ancho, anchor="center")

    scrollbar = Scrollbar(frameTabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    tabla.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def cargarTabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        for _, row in logica.df.iterrows():
            tabla.insert("", "end", values=(
                row["Idregistro"],
                row["nombreProducto"],
                row["cantidad"],
                row["precioUnidad"],
                row["fechaIngreso"],
                row["empleado"],
                row["Idempleado"]
            ))

    cargarTabla()

    # CAMPO ID + BOTONES 
    frameAccion = Frame(ventana, bg="#1e293b", padx=20, pady=15)
    frameAccion.pack(fill="x", padx=20, pady=10)

    Label(
        frameAccion,
        text="🆔 ID del Registro a eliminar:",
        font=("Arial", 11, "bold"),
        bg="#1e293b",
        fg="white"
    ).pack(side="left", padx=(0, 10))

    txtEliminar = Entry(frameAccion, width=10, font=("Arial", 11))
    txtEliminar.pack(side="left", ipady=5)

    def eliminar():
        mensaje = eliminarRegistro(txtEliminar.get())
        if mensaje == "Registro eliminado correctamente":
            messagebox.showinfo("Correcto", mensaje)
            txtEliminar.delete(0, END)
            cargarTabla()
        else:
            messagebox.showerror("Error", mensaje)

    Button(
        frameAccion,
        text="Eliminar",
        command=eliminar,
        bg="#ef4444",
        fg="white",
        width=12,
        height=1,
        font=("Arial", 11, "bold"),
        bd=0
    ).pack(side="left", padx=15)

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
    ).pack(side="bottom", pady=15)


# INICIAR MENU
menuPrincipal()
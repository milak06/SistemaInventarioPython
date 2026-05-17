import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# LEER CSV
try:
    df = pd.read_csv("DataBase.csv", encoding="latin1", sep=";")
except FileNotFoundError:
    df = pd.DataFrame(columns=[
        "Idregistro",
        "nombreProducto",
        "cantidad",
        "precioUnidad",
        "fechaIngreso",
        "empleado",
        "Idempleado"
    ])


# AGREGAR REGISTRO
def agregarRegistro(nombreProducto, cantidad, precioUnidad, empleado, idempleado):

    global df

    # VALIDACIONES
    if nombreProducto == "":
        return "Ingrese nombre producto"

    if not cantidad.isdigit():
        return "Cantidad inválida"

    try:
        precioUnidad = float(precioUnidad)
    except:
        return "Precio inválido"

    if empleado == "":
        return "Ingrese empleado"

    if len(idempleado) != 3 or not idempleado.isdigit():
        return "ID empleado inválido"

    # GENERAR ID
    if df.empty:
        idregistro = 1
    else:
        idregistro = df.loc[len(df)-1, "Idregistro"] + 1

    # FECHA
    fechaIngreso = datetime.now().strftime("%d/%m/%Y")

    # NUEVO REGISTRO
    nuevo_registro = {
        "Idregistro": idregistro,
        "nombreProducto": nombreProducto,
        "cantidad": int(cantidad),
        "precioUnidad": precioUnidad,
        "fechaIngreso": fechaIngreso,
        "empleado": empleado,
        "Idempleado": int(idempleado)
    }

    # AGREGAR
    df.loc[len(df)] = nuevo_registro

    # GUARDAR CSV
    df.to_csv("DataBase.csv", index=False, encoding="latin1", sep=";")

    return "Registro agregado correctamente"


# ELIMINAR REGISTRO
def eliminarRegistro(idregistro):

    global df

    try:
        idregistro = int(idregistro)
    except:
        return "Ingrese un ID válido"

    if idregistro not in df["Idregistro"].values:
        return "No existe ese ID"

    df = df[df["Idregistro"] != idregistro]

    df.to_csv("DataBase.csv", index=False, encoding="latin1", sep=";")

    return "Registro eliminado correctamente"


# GRAFICO
def generarGrafico():

    materiales = df["nombreProducto"].unique()

    cantidades = df.groupby("nombreProducto")["cantidad"].sum()

    fig, ax = plt.subplots()

    ax.bar(materiales, cantidades)

    ax.set_xlabel("Materiales")
    ax.set_ylabel("Cantidad")
    ax.set_title("Cantidad de Materiales")

    plt.show()
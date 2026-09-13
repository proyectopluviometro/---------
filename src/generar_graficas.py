"""
Generador de gráficas interactivas del pluviómetro
-----------------------------------------------------
Lee el archivo de datos (data/datos_pluviometro.csv) y genera:

1. Una gráfica POR DÍA: temperatura, humedad y lluvia combinadas en una
   sola gráfica INTERACTIVA (puedes hacer zoom, ver valores al pasar el
   mouse, ocultar/mostrar líneas haciendo clic en la leyenda).

2. Una gráfica POR MES: promedio diario de temperatura y humedad (líneas)
   + lluvia máxima registrada por día (barras), también interactiva.

Las gráficas se guardan como archivos .html dentro de "graficas/",
organizadas en subcarpetas "diario" y "mensual". Se abren con doble
clic en cualquier navegador (Chrome, Edge, etc.) — no necesitas Python
para verlas después de generadas.

INSTRUCCIONES DE USO:

1. Instala las librerías necesarias (solo la primera vez):
       pip install pandas plotly

2. Ejecuta este script desde la carpeta "src":
       python generar_graficas.py

3. Revisa la carpeta "graficas/diario" y "graficas/mensual".

Cada vez que se ejecuta, TODAS las gráficas se regeneran desde cero con
los datos más recientes del CSV — si un día tiene datos nuevos (por
ejemplo, tomaste datos en la mañana y luego en la tarde), su gráfica se
actualiza automáticamente para incluir todo.

Nota: las gráficas usan la librería Plotly.js cargada desde internet
(vía CDN) para mantener los archivos livianos. Esto significa que
necesitas conexión a internet la primera vez que las abras en el
navegador para que carguen correctamente.
"""

import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ----------------- CONFIGURACIÓN -----------------
ARCHIVO_DATOS = "../data/datos_pluviometro.csv"
CARPETA_GRAFICAS = "../graficas"
# ---------------------------------------------------


def parsear_fechas_mixtas(columna_fechas):
    """
    Convierte la columna de fecha a un formato real de fecha/hora, probando
    dos formatos conocidos (por si el CSV llegó a mezclarse, por ejemplo si
    se abrió y guardó alguna vez desde Excel, que a veces cambia el formato
    de fecha automáticamente):
        - "2026-09-13 04:14:51"  (el formato normal que usa el script)
        - "13/09/2026 04:14"     (formato día/mes/año, sin segundos)
    Cada formato se prueba explícitamente (sin adivinar) para evitar
    confundir día y mes por accidente.
    """
    resultado = pd.to_datetime(columna_fechas, format="%Y-%m-%d %H:%M:%S", errors="coerce")
    faltantes = resultado.isna()
    if faltantes.any():
        resultado.loc[faltantes] = pd.to_datetime(
            columna_fechas[faltantes], format="%d/%m/%Y %H:%M", errors="coerce"
        )
    return resultado


def cargar_datos():
    """Lee el CSV y prepara las columnas de fecha."""
    df = pd.read_csv(ARCHIVO_DATOS)
    df["fecha_hora"] = parsear_fechas_mixtas(df["fecha_hora"])
    df = df.dropna(subset=["fecha_hora", "temperatura_C", "humedad_%", "lluvia_V"])
    # Ordenamos siempre por fecha y hora, sin importar el orden en que las
    # filas aparezcan en el CSV (por ejemplo si se pegaron datos de
    # calibración al final o en medio del archivo).
    df = df.sort_values("fecha_hora").reset_index(drop=True)
    return df


def graficar_dia(df_dia, fecha, carpeta_salida):
    """Genera una gráfica interactiva (temp + humedad + lluvia) para un solo día."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=df_dia["fecha_hora"], y=df_dia["temperatura_C"],
        name="Temperatura (°C)", line=dict(color="orange"),
    ), secondary_y=False)

    fig.add_trace(go.Scatter(
        x=df_dia["fecha_hora"], y=df_dia["humedad_%"],
        name="Humedad (%)", line=dict(color="royalblue"),
    ), secondary_y=False)

    fig.add_trace(go.Scatter(
        x=df_dia["fecha_hora"], y=df_dia["lluvia_V"],
        name="Lluvia (V)", line=dict(color="cyan"),
    ), secondary_y=True)

    fig.update_layout(
        title=f"Pluviómetro - {fecha}",
        xaxis_title="Hora del día",
        hovermode="x unified",
        template="plotly_white",
    )
    fig.update_yaxes(title_text="Temperatura (°C) / Humedad (%)", secondary_y=False)
    fig.update_yaxes(title_text="Lluvia (V)", secondary_y=True)

    nombre_archivo = os.path.join(carpeta_salida, f"{fecha}.html")
    fig.write_html(nombre_archivo, include_plotlyjs="cdn")
    return nombre_archivo


def graficar_mes(df_mes, mes, carpeta_salida):
    """Genera una gráfica interactiva (promedio diario + lluvia máxima) para un mes."""
    resumen = df_mes.groupby(df_mes["fecha_hora"].dt.day).agg(
        temp_promedio=("temperatura_C", "mean"),
        humedad_promedio=("humedad_%", "mean"),
        lluvia_max=("lluvia_V", "max"),
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Bar(
        x=resumen.index, y=resumen["lluvia_max"],
        name="Lluvia máx. del día (V)", marker_color="cyan", opacity=0.5,
    ), secondary_y=False)

    fig.add_trace(go.Scatter(
        x=resumen.index, y=resumen["temp_promedio"],
        name="Temp. promedio (°C)", line=dict(color="orange"), mode="lines+markers",
    ), secondary_y=True)

    fig.add_trace(go.Scatter(
        x=resumen.index, y=resumen["humedad_promedio"],
        name="Humedad promedio (%)", line=dict(color="royalblue"), mode="lines+markers",
    ), secondary_y=True)

    fig.update_layout(
        title=f"Resumen mensual - {mes}",
        xaxis_title="Día del mes",
        hovermode="x unified",
        template="plotly_white",
    )
    fig.update_yaxes(title_text="Lluvia máxima (V)", secondary_y=False)
    fig.update_yaxes(title_text="Temperatura (°C) / Humedad (%)", secondary_y=True)

    nombre_archivo = os.path.join(carpeta_salida, f"{mes}.html")
    fig.write_html(nombre_archivo, include_plotlyjs="cdn")
    return nombre_archivo


def main():
    df = cargar_datos()

    carpeta_diario = os.path.join(CARPETA_GRAFICAS, "diario")
    carpeta_mensual = os.path.join(CARPETA_GRAFICAS, "mensual")
    os.makedirs(carpeta_diario, exist_ok=True)
    os.makedirs(carpeta_mensual, exist_ok=True)

    df["fecha"] = df["fecha_hora"].dt.date
    dias_generados = []
    for fecha, df_dia in df.groupby("fecha"):
        archivo = graficar_dia(df_dia, fecha, carpeta_diario)
        dias_generados.append(archivo)
        print(f"Gráfica diaria generada: {archivo}")

    df["mes"] = df["fecha_hora"].dt.to_period("M")
    meses_generados = []
    for mes, df_mes in df.groupby("mes"):
        archivo = graficar_mes(df_mes, str(mes), carpeta_mensual)
        meses_generados.append(archivo)
        print(f"Gráfica mensual generada: {archivo}")

    print(f"\nListo: {len(dias_generados)} gráfica(s) diaria(s) y "
          f"{len(meses_generados)} gráfica(s) mensual(es) generadas.")


if __name__ == "__main__":
    main()
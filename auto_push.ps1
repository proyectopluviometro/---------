# auto_push.ps1
# ---------------------------------------------------------
# Este script hace 2 cosas automáticamente, sin que tengas que
# abrir nada tú:
#   1. Genera/actualiza las gráficas interactivas (HTML) a partir
#      del CSV más reciente.
#   2. Sube los cambios (datos + gráficas) a GitHub.
# Está pensado para ejecutarse solo mediante el Programador de
# tareas de Windows.
# ---------------------------------------------------------

# IMPORTANTE: Cambia esta ruta por la ubicación REAL de tu carpeta del proyecto
$rutaProyecto = "C:\Users\User\Desktop\pluviometro-monitor"

# --- Paso 1: Regenerar las gráficas ---
Set-Location "$rutaProyecto\src"
python generar_graficas.py

# --- Paso 2: Subir los cambios a GitHub ---
Set-Location $rutaProyecto

$cambios = git status --porcelain

if ($cambios) {
    $fecha = Get-Date -Format "yyyy-MM-dd HH:mm"
    git add .
    git commit -m "Actualizacion automatica de datos y graficas - $fecha"
    git push origin main

    Write-Output "$fecha - Datos y graficas subidos correctamente a GitHub."
} else {
    Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm') - No hay cambios nuevos que subir."
}

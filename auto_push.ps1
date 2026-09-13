# auto_push.ps1
# ---------------------------------------------------------
# Este script sube automáticamente los datos nuevos del
# pluviómetro a GitHub. Está pensado para ejecutarse solo
# (sin que tú tengas que hacer nada) mediante el Programador
# de tareas de Windows.
# ---------------------------------------------------------

# IMPORTANTE: Cambia esta ruta por la ubicación REAL de tu carpeta del proyecto
$rutaProyecto = "C:\Users\User\Desktop\pluviometro-monitor"

# Nos movemos a la carpeta del proyecto
Set-Location $rutaProyecto

# Revisamos si hay cambios (si no hay nada nuevo, no hacemos commit vacío)
$cambios = git status --porcelain

if ($cambios) {
    $fecha = Get-Date -Format "yyyy-MM-dd HH:mm"
    git add .
    git commit -m "Actualización automática de datos - $fecha"
    git push origin main

    Write-Output "$fecha - Datos subidos correctamente a GitHub."
} else {
    Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm') - No hay cambios nuevos que subir."
}

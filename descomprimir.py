import zipfile
import os

zip_path = "the_crazy_family.zip"
output_folder = "the_crazy_family"

# Crear carpeta si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Extraer contenido
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(output_folder)

print("✅ Archivos extraídos correctamente en:", output_folder)

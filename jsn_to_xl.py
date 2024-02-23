import json
import xlrd

# Ouvrir le fichier JSON
with open("data.json") as json_file:
    data = json.load(json_file)

# Ouvrir le fichier Excel
excel_file = xlrd.open_workbook("data.xlsx")
sheet = excel_file.sheet_by_index(0) # Première feuille de calcul

# Afficher le contenu du fichier JSON
print("Contenu du fichier JSON :")
print(data)

# Afficher le contenu du fichier Excel
print("Contenu du fichier Excel :")
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print(sheet.cell_value(row, col), end=" ")
    print()

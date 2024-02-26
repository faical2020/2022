snew_sheet = workbook.create_sheet(sheetName)
default_sheet = workbook['default']

from copy import copy

for row in default_sheet.rows:
    for cell in row:
        new_cell = new_sheet.cell(row=cell.row, column=cell.col_idx,
                value= cell.value)
        if cell.has_style:
            new_cell.font = copy(cell.font)
            new_cell.border = copy(cell.border)
            new_cell.fill = copy(cell.fill)
            new_cell.number_format = copy(cell.number_format)
            new_cell.protection = copy(cell.protection)
            new_cell.alignment = copy(cell.alignment)

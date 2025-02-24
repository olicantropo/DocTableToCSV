from docx import Document
import csv

def docx_table_to_csv(docx_path, csv_path):
    doc = Document(docx_path)
    data = []
    
    for table in doc.tables:
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells]
            if len(cells) == 2 and not any(exclude in cells[0] for exclude in ["Subcategoria", "Cod"]):
                data.append(cells)
    
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Coluna 1", "Coluna 2"])  # Columns
        writer.writerows(data)
    
    print(f"File saved: {csv_path}")


docx_table_to_csv("file.docx", "output".csv")

import tabula
import PyPDF2

dics = tabula.read_pdf("../data/agribank.pdf", pages=2, pandas_options={'header': None}, lattice=True, multiple_tables=False, output_format="json")
print(dics)
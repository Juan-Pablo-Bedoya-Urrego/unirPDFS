from PyPDF2 import PdfMerger

pdfs = ["TALLER 1_CÁLCULO VECTORIAL_C.pdf", "Entregable 1 CSIV.pdf"]
nombre_archivo_salida = "documento unido.pdf"
fusionador = PdfMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)


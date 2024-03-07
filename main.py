#Se importa un clase de la libreria PyPDFS
from PyPDF2 import PdfMerger

#Lista con los nombres de los documentos para unir
pdfs = ["TALLER 1_CÁLCULO VECTORIAL_C.pdf", "Entregable 1 CSIV.pdf"]

#nombre que llevara el documento resultante de la union
salidan = "documento unido.pdf"

#se crea una instancia de la clase PdfMerger
unir = PdfMerger()

#se recorre la lista de PDFS
for pdf in pdfs:
    #se lee cada archivo y se agrega a la union
    unir.append(open(pdf, 'rb'))

#se abre el documento de salida
with open(salidan, 'wb') as salida:
    #se escribe el contenido fusionado en el documento de salida
    unir.write(salida)


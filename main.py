class unirPDF:
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

class ConvertirPDFaWord:
    #libreria para poder realizar la convercion
    from pdf2docx import Converter

    #documento PDF que se va a convertir en Word
    pdf = "documento unido.pdf"
    #nombre del documento resultante
    word = "convertido.docx"
    #se asigna un objeto el cual tiene la clase Converter que lo que hace es convertir el PDF
    c = Converter(pdf)
    """se llama el metodo convert y se le pasan los argumentos 
    word que es el nombre de salida, start que desde que pagina 
    se va empezar a convertir y end es hasta donde se va a convetir
    """
    c.convert(word, start=0, end=None)
#se cierra el metodo
    c.close()
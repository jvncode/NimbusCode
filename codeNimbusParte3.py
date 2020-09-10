import csv

'''
Tras haber formateado los elementos del diccionario en cadenas de texto en un archivo de entrada CSV,
lo abro y vuelvo a convertir esas cadenas de texto en un diccionario desde el archivo
'''
with open('contactsInput.csv', 'r') as inputFile:
    contactsInput = {}
    contReader = csv.reader(inputFile, delimiter=';')
    next(contReader)  # Salto la cabecera del archivo de entrada
    for row in contReader:
        #  Convierto cada cadena de entrada en un elemento del diccionario
        contactsInput[row[0]] = row[1:]
inputFile.close()

'''
Agrego tres elementos nuevos al diccionario creado desde el archivo de entrada
'''
contactsInput[630568920] = ['ANA', 'JIMENEZ ANTUNEZ','RECEPCIONISTA', 'DIGITALBANK', 19900422]
contactsInput[914502388] = ['ENRIQUE','TORRIJOS VAL', 'MENSAJERO', 'MRW', 19740510]
contactsInput[626548102] = ['MATIAS', 'CAMPANO VILLACASTIN', 'COMERCIAL', 'FIGASA', 19820812]

with open('contactsOutput.csv', 'w') as outputFile:  # Abro el archivo de salida para escritura
    writer = csv.writer(outputFile)
    inverse = {}
    for key in contactsInput:  # Genero el diccionario invertido con los elementos del diccionario creado con el archivo de entrada
        val = tuple(contactsInput[key])
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)

    for key, value in inverse.items():  # Escribo en el archivo de salida los elementos del diccionario invertido en cadenas de texto
        writer.writerow([key, value])

outputFile.close()

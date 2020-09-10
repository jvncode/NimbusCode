'''
Creo el diccionario original
'''
contacts = {
    915834581: ['ALBERTO', 'NUÑEZ BRAVO', 'ADMINISTRATIVO', 'ABENGOA', 19840528],
    682904210: ['LAURA', 'MENDEZ ARIAS', 'GERENTE', 'DIGITALBANK', 19811008],
    624810953: ['RICARDO', 'VALLEJO DIAZ', 'INGENIERO', 'ABENGOA', 19700810],
    915284600: ['HECTOR', 'MONTERO ALCORTA', 'CONDUCTOR', 'FIGASA', 19831205],
    638451008: ['SANDRA', 'MIHANOVICH ARAOZ', 'REDACTORA', 'MASTV', 19920528],
    644287634: ['NATALIA', 'LOPEZ MENTA', 'RECEPCIONISTA', 'FCC', 19891118],
    680592571: ['ANDRES', 'SUAREZ TORRES', 'ABOGADO', 'BUFESA', 19680202],
    938502462: ['MARCOS', 'ROIG MILLA', 'DISEÑADOR', 'METROBOL', 19730822],
}

'''
Las listas de valores hay que convertirlas en tuplas para que sean 'hashables' con el
fin de que puedan comportarse como claves y poder tener acceso a ellas posteriormente.
'''

def invert_dict(d):
    inverse = dict()
    for key in d: 
        val = tuple(d[key])  # ----> Conversión a tupla de los valores que pasarán a ser claves
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

invert_contacts = invert_dict(contacts)
print(invert_contacts)

'''
* La utilidad de mi diccionario invertido se basa en darle un uso más potente a los datos
de contacto de cada usuario pudiendo acceder a ellos no solo por número de teléfono, como
en el diccionario original, sino por cualquiera de los valores que en el diccionario invertido
ahora son claves.
* Esto nos permitiría a través de la siguiente función buscar por ejemplo por nombre de empresa, 
el resultado sería que nos devolvería el/los números de teléfono de las personas que trabajan 
en dicha empresa.
'''

def search(date):
    if isinstance(date, int):  # Compruebo si la clave es numérica o una cadena
        date = int(date) # En caso de ser numérico convierto a int para que permita buscar por formato de fecha de nacimiento (AAAAMMDD)
    else:
        date = date.upper()  # En caso de ser cadena uniformo a mayúsculas
    result = []
    for key in invert_contacts:
        if date in key:
            result += invert_contacts.get(key)
    return print('Criterio de búsqueda: {}\n{} Contactos encontrados: {}'.format(date, len(result), result))

search('abengoa')  # Ejemplo: Realizo búsqueda por empresa ----> Devuelve 2 contactos telefónicos

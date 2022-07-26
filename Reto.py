"""""
RETO MISIÓN TIC 1: 
Para comenzar, requieren que el dispositivo cuente con un lector de la calidad del agua. 
Después de la lectura, el dispositivo entrega el nivel de riesgo y según este resultado 
debe indicar los rangos de clasificación a los que pertenece esta. 

        Clasificación 
    IRCA (%) 	            Nivel de riesgo	
    80.1 - 100	        INVIABLE SANITARIAMENTE	
    35.1 - 80	                ALTO	
    14.1 - 35	                MEDIO	
    5.1 - 14	                BAJO		
    0 - 5	                 SIN RIESGO	

Se requiere leer una variable de entrada que indique el nivel de riesgo y devuelva como resultado 
el rango al que pertenece esta lectura. 
Si el nivel de riesgo leído no se encuentra en la 
tabla devolver “No es un nivel de riesgo catalogado”.

--------------------------------------------------------------------------------------------
Quizá esto podría hacerse con diccionarios; pero por el momento usemos lo aprendido
--------------------------------------------------------------------------------------------
"""""
# Definimos variables de control
#opcion

# Entrada de datos (Se omiten los print porque será pasado por un programa para evaluarlo)
# print("Las opciones de niveles de riesgo son los siguientes: \n1. INVIABLE SANITARIAMENTE \n2. ALTO \n3. MEDIO \n4. BAJO \n5. SIN RIESGO")
# print("Digite la opción: ")

opcion = input() 

opcion = opcion.upper() # Esta función es para que se tomen en mayúsculas todas las entradas

# Proceso y salida
if(opcion == "INVIABLE SANITARIAMENTE"):
    print("80.1 - 100")
elif(opcion == "ALTO"):
    print("35.1 - 80")
elif(opcion == "MEDIO"):
    print("14.1 - 35")
elif(opcion == "BAJO"):
    print("5.1 - 14")
elif(opcion == "SIN RIESGO"):
    print("0 - 5")
else:
    print("No es un nivel de riesgo catalogado")
    
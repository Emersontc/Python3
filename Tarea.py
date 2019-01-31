#ejercicio 1
#crear un programa que les permita seleccionar entre 1 de 2
#opciones la primera convertir dolares a
#quetzales o convertir quetzales a dolares si es invaluda poner opcion invalida
#print("Binvenido al programa".center(50,"*"))

#Dolar = 7.80
#print ("ingrese 1 para convertir dolar a quetzales o ingrese 2 para convertir quetzales a dolar")
#con = int ("ingrese 1 o 2 para saber que desea convertir:.")
#if con == 1:
#    Q = float(input("Ingrese la cantidad:.))
#    resultado = Q * D
#elif con == 2:
#    Q = float(input("Iingrese la cantida:.))
#    resultado = Q / D
#else:
#    print("incorrecto")
#print ("Su cantidad es:.{}".format (" Q * D = Q / D "))
                    
#ejercicio 2
#solicitar al usuario que escoja 1 de las siguientes opciones
#1. sumar dos numero 2. restar tres numero 3. multiplicaR 4 NUMERO
#4. dividir 2 numero y si el usuario ingresa una opcion invalida hacerselo saber
Inicio = '''Inicio
            1. Suma
            2. Resta
            3. Multiplicar
            4. Dividir
            5. Salir
            '''
print (Inicio)
opcion = input ("Escoje una opcion:")
while opcion!= 5:
    if opcion == 1:
        n1 = float(input("ingrese el valor 1:"))
        n2 = float(input("ingrese el valor 2:"))
        suma = n1 + n2
        print ("La suma es \n {}".format(suma))
    elif opcion == 2:
        n1 = float(input("ingrese el valor 1:"))
        n2 = float(input("ingrese el valor 2:"))
        n3 = float(input("ingrese el valor 3:"))
        resta = n1 - n2 - n3
        print ("La resta es {}".format(resta))
    elif opcion == 3:
        n1 = float(input("ingrese el valor 1:"))
        n2 = float(input("ingrese el valor 2:"))
        n3 = float(input("ingrese el valor 3:"))
        n4 = float(input("ingrese el valor 4:"))
        multiplicacion = n1 * n2 * n3 * n4
        print ("La multiplicaion es {}".format(multiplicaion))
    elif opcion == 4:
        n1 = float(input("ingrese el valor 1:"))
        n2 = float(input("ingrese el valor 2:"))
        division = n1/n2
        print ("La division es {}".format(division))
    else:
        print("opcion invalida")
    print (Inicio)
    opcion = input ("Escoje una opcion:")
print ("FIN")
        
            

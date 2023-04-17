from Viajero_Frecuente import Viajero

import csv

def test():
    m = Viajero(4783, '43.242.2424', 'mauri', 'mama', 492283)
    print(m.getmillas())
    print('su nombre es {}' .format(m.getnombrecompleto()))
    m.acumularMillas(int(input('ingrese las millas a acumular:')))
    m.canjearMillas(int(input('Ingrese las millas a canjear:')))


if __name__ == "__main__":
    test()
    viajeros = []
    with open('Viajeros_varios.csv', newline='') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        next(reader) #Saltea la primer fila con los encabezados
        for fila in reader:
            num_viajero, dni, nombre, apellido, millas_acumuladas = fila
            viajero = Viajero(int(num_viajero), dni, nombre, apellido, int(millas_acumuladas))
            viajeros.append(viajero)
        for viajero in viajeros:
             print("Numero de viajero: {}, DNI: {}, Nombre: {}, Apellido: {}, Millas acumuladas: {}".format(viajero.num_viajero, viajero.dni, viajero.nombre, viajero.apellido, viajero.getmillas()))
    num_vfrecuente = int(input('Ingrese un nnumero de viajero frecuente:'))
    viajero_actual = Viajero
    for viajero in viajeros:
        if viajero.getnumv() == num_vfrecuente:
            viajero_actual = viajero
            break
    
    if viajero_actual is None:
        print('El numero de viajero ingresado no es valido')
    else:
        while True:
            print('Menu')
            print('o - Salida')
            print('a - Consultar cantidad de millas')
            print('b - Acumular millas')
            print('c - Canjear millas')
            op = input('Ingrese opcion:')
            if op == 'a':
                print('Cantidad de millas acumuladas {}' .format(viajero_actual.getmillas()))
            elif op == 'b':
                millas = int(input('Ingrese cantidad de millas a acumular:'))
                viajero_actual.acumularMillas(millas)
            elif op == 'c':
                millas = int(input("Ingrese la cantidad de millas a canjear: "))
                viajero_actual.canjearMillas(millas)
            elif op == 'o':
                print('Fin del programa')
                break
            else:
                print("Opción inválida")

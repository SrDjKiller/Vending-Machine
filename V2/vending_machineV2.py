import time
import products as p

i = 0
dinerot = 0
cambio = 0
seguir = False
while seguir == False:
      print("##..:Productos:..##")
      for j in p.products:
            print(f"Producto: {j['Producto']} - Precio: {j['Precio']} - Codigo: {j['Codigo']}")

      seleccionP = int(input("Introduzca el número de código del artículo que desea obtener: "))
      for j in p.products:
            if seleccionP == j['Codigo']:
                  producto = j
      if producto == '':
            print('CODIGO ERRONEO')
      else:
            print(f"Estupendo, {producto['Producto']} le costará {producto['Precio']}€")

      while dinerot < producto['Precio']:
            dinero = float(input("Introduce Cantidad, solo monedas de 0.50€, 1€ o 2€: "))
            if (dinero == 0.5 or dinero == 1 or dinero == 2):
                  dinerot = dinerot + dinero
            else:
                  print("Moneda Incorrecta o Inexistente")
      
      print("Expendiendo producto... Porfavor Espere")

      time.sleep(2)

      if dinerot > producto['Precio']:
            cambio = dinerot - producto['Precio']
            print(f"Gracias por comprar, aquí está su {producto['Producto']}")
            time.sleep(2)
            print(f"Su cambio es: {round(cambio,2)}€")
      else:
            print(f"Gracias por comprar aquí está su {producto['Producto']}")

      time.sleep(3)

      cont = input("Para salir de la máquina introduzca s y para seguir comprando pulse cualquier tecla y presione enter:  ")
      if cont == 's' or cont == 'S':
            seguir = False
      else:
            seguir = True
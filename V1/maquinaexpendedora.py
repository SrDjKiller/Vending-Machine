# PROGRAMA CREADO POR OSCAR RODRIGUEZ LINACERO (CON AYUDAS DE INTERNET xd)

# DEFINICIONES PARA EL PROGRAMA

# DEFINIR PRODUCTOS

def seleccionProducto():
    global producto

    # DEFINICION PRODUCTOS PRIMERA LINEA

    if opcion == 10:
        producto = producto10
        print("Su precio es de... ", producto["precio"])
    if opcion == 11:
        producto = producto11
        print("Su precio es de... ", producto["precio"])
    if opcion == 12:
        producto = producto12
        print("Su precio es de... ", producto["precio"])
    if opcion == 13:
        producto = producto13
        print("Su precio es de... ", producto["precio"])

    # DEFINICION PRODUCTOS SEGUNDA LINEA

    if opcion == 20:
        producto = producto20
        print("Su precio es de... ", producto["precio"])
    if opcion == 21:
        producto = producto21
        print("Su precio es de... ", producto["precio"])
    if opcion == 22:
        producto = producto22
        print("Su precio es de... ", producto["precio"])
    if opcion == 23:
        producto = producto23
        print("Su precio es de... ", producto["precio"])

    # DEFINICION PRODUCTOS TERCERA LINEA

    if opcion == 30:
        producto = producto30
        print("Su precio es de... ", producto["precio"])
    if opcion == 31:
        producto = producto31
        print("Su precio es de... ", producto["precio"])
    if opcion == 32:
        producto = producto32
        print("Su precio es de... ", producto["precio"])
    if opcion == 33:
        producto = producto33
        print("Su precio es de... ", producto["precio"])

    # DEFINICION PRODUCTOS CUARTA LINEA

    if opcion == 40:
        producto = producto40
        print("Su precio es de... ", producto["precio"])
    if opcion == 41:
        producto = producto41
        print("Su precio es de... ", producto["precio"])
    if opcion == 42:
        producto = producto42
        print("Su precio es de... ", producto["precio"])
    if opcion == 43:
        producto = producto43
        print("Su precio es de... ", producto["precio"])

    # DEFINICION PRODUCTOS QUINTA LINEA

    if opcion == 50:
        producto = producto50
        print("Su precio es de... ", producto["precio"])
    if opcion == 51:
        producto = producto51
        print("Su precio es de... ", producto["precio"])
    if opcion == 52:
        producto = producto52
        print("Su precio es de... ", producto["precio"])
    if opcion == 53:
        producto = producto53
        print("Su precio es de... ", producto["precio"])

    # DEFINICION PRODUCTOS SEXTA LINEA

    if opcion == 60:
        producto = producto60
        print("Su precio es de... ", producto["precio"])
    if opcion == 61:
        producto = producto61
        print("Su precio es de... ", producto["precio"])
    if opcion == 62:
        producto = producto62
        print("Su precio es de... ", producto["precio"])
    if opcion == 63:
        producto = producto63
        print("Su precio es de... ", producto["precio"])

    # DEFINICION PRODUCTO ERRONEO
    if opcion != 10 and opcion != 11 and opcion != 12 and opcion != 13 and opcion != 20 and opcion != 21 and opcion != 22 and opcion != 23 and opcion != 30 and opcion != 31 and opcion != 32 and opcion != 33 and opcion != 40 and opcion != 41 and opcion != 42 and opcion != 43 and opcion != 50 and opcion != 51 and opcion != 52 and opcion != 53 and opcion != 60 and opcion != 61 and opcion != 62 and opcion != 63:
        print("Codigo erroneo, introduzca codigo de nuevo")

# DEFINICION DINERO


def introducirDinero():
    global dinero
    print("## Ingresar monedas de 0.50€, 1€ o 2€ ##")
    dinero = float(input("Introducir credito"))
    while (dinero < producto["precio"]):
        dinero = float(input("## Ingresar valor de 0.50€, 1€ o 2€ ##"))
        if (dinero == 0.5 or dinero == 1 or dinero == 2):
            entregaCambio()
        else:
            introducirDinero()

# DEFINICION CAMBIO

def entregaCambio():
    cambio = dinero - producto["precio"]
    print(f"Su cambio es {cambio}€")
    print("Por favor recoja su cambio")

# COMIENZO DE PROGRAMA


# PRODUCTOS PRIMERA LINEA
producto10 = {"producto": "Doritos TexMex", "precio": 1.30}
producto11 = {"producto": "Ruffles Jamon", "precio": 1.30}
producto12 = {"producto": "Pringles", "precio": 1.40}
producto13 = {"producto": "Lays Campesinas", "precio": 1.30}

# PRODUCTOS SEGUNDA LINEA
producto20 = {"producto": "Croissant de Chocolate", "precio": 1.20}
producto21 = {"producto": "Palitos de semillas", "precio": 0.90}
producto22 = {"producto": "Pan de Pipas", "precio": 1.00}
producto23 = {"producto": "Ositos Haribo", "precio": 0.70}

# PRODUCTOS TERCERA LINEA
producto30 = {"producto": "Galletas Oreo", "precio": 1.20}
producto31 = {"producto": "KitKat", "precio": 1.10}
producto32 = {"producto": "KinderBueno Blanco", "precio": 1.35}
producto33 = {"producto": "Lacasitos", "precio": 0.80}

# PRODUCTOS CUARTA LINEA
producto40 = {"producto": "Conguitos", "precio": 0.90}
producto41 = {"producto": "Galletas Chips Ahoy mini", "precio": 1.10}
producto42 = {"producto": "Galletas Prinicipe", "precio": 1.20}
producto43 = {"producto": "Mikados", "precio": 1.50}

# PRODUCTOS QUINTA LINEA
producto50 = {"producto": "Lata Cocacola", "precio": 1.20}
producto51 = {"producto": "Lata Aquarius Limon", "precio": 1.20}
producto52 = {"producto": "Lata Fanta Naranja", "precio": 1.20}
producto53 = {"producto": "Cacaolat 200ml", "precio": 1.35}

# PRODUCTOS SEXTA LINEA
producto60 = {"producto": "Agua Bezoya 1L", "precio": 1.00}
producto61 = {"producto": "Agua Bezoya 1L", "precio": 1.00}
producto62 = {"producto": "Agua Bezoya 1L", "precio": 1.00}
producto63 = {"producto": "Agua Bezoya 1L", "precio": 1.00}

# MENU CON TIPOS DE CAFE

print("##..:Productos:..##")

# LINEA1
print("## #10 ""Producto", producto10["producto"],
      "El precio es de:", producto10["precio"], "€ ##")
print("## #11 ""Producto", producto11["producto"],
      "El precio es de:", producto11["precio"], "€ ##")
print("## #12 ""Producto", producto12["producto"],
      "El precio es de:", producto12["precio"], "€ ##")
print("## #13 ""Producto", producto13["producto"],
      "El precio es de:", producto13["precio"], "€ ##")
# LINEA2
print("## #20 ""Producto", producto20["producto"],
      "El precio es de:", producto20["precio"], "€ ##")
print("## #21 ""Producto", producto21["producto"],
      "El precio es de:", producto21["precio"], "€ ##")
print("## #22 ""Producto", producto22["producto"],
      "El precio es de:", producto22["precio"], "€ ##")
print("## #23 ""Producto", producto23["producto"],
      "El precio es de:", producto13["precio"], "€ ##")
# LINEA3
print("## #30 ""Producto", producto30["producto"],
      "El precio es de:", producto30["precio"], "€ ##")
print("## #31 ""Producto", producto31["producto"],
      "El precio es de:", producto31["precio"], "€ ##")
print("## #32 ""Producto", producto32["producto"],
      "El precio es de:", producto32["precio"], "€ ##")
print("## #33 ""Producto", producto33["producto"],
      "El precio es de:", producto33["precio"], "€ ##")
# LINEA4
print("## #40 ""Producto", producto40["producto"],
      "El precio es de:", producto40["precio"], "€ ##")
print("## #41 ""Producto", producto41["producto"],
      "El precio es de:", producto41["precio"], "€ ##")
print("## #42 ""Producto", producto42["producto"],
      "El precio es de:", producto42["precio"], "€ ##")
print("## #43 ""Producto", producto43["producto"],
      "El precio es de:", producto43["precio"], "€ ##")
# LINEA5
print("## #50 ""Producto", producto50["producto"],
      "El precio es de:", producto50["precio"], "€ ##")
print("## #51 ""Producto", producto51["producto"],
      "El precio es de:", producto51["precio"], "€ ##")
print("## #52 ""Producto", producto52["producto"],
      "El precio es de:", producto52["precio"], "€ ##")
print("## #53 ""Producto", producto53["producto"],
      "El precio es de:", producto53["precio"], "€ ##")
# LINEA6
print("## #60 ""Producto", producto60["producto"],
      "El precio es de:", producto60["precio"], "€ ##")
print("## #61 ""Producto", producto61["producto"],
      "El precio es de:", producto61["precio"], "€ ##")
print("## #62 ""Producto", producto62["producto"],
      "El precio es de:", producto62["precio"], "€ ##")
print("## #63 ""Producto", producto63["producto"],
      "El precio es de:", producto63["precio"], "€ ##")
opcion = int(input("## Introducir codigo de producto...: ##"))

# PRODUCTOS LINEA 1
if opcion == 10:
    producto = producto10
    introducirDinero()
    entregaCambio()
if opcion == 11:
    producto = producto11
    introducirDinero()
    entregaCambio()
if opcion == 12:
    producto = producto12
    introducirDinero()
    entregaCambio()
if opcion == 13:
    producto = producto13
    introducirDinero()
    entregaCambio()

  # PRODUCTOS LINEA 2
if opcion == 20:
    producto = producto20
    introducirDinero()
    entregaCambio()
if opcion == 21:
    producto = producto21
    introducirDinero()
    entregaCambio()
if opcion == 22:
    producto = producto22
    introducirDinero()
    entregaCambio()
if opcion == 23:
    producto = producto23
    introducirDinero()
    entregaCambio()

  # PRODUCTOS LINEA 3
if opcion == 30:
    producto = producto30
    introducirDinero()
    entregaCambio()
if opcion == 31:
    producto = producto31
    introducirDinero()
    entregaCambio()
if opcion == 32:
    producto = producto32
    introducirDinero()
    entregaCambio()
if opcion == 33:
    producto = producto33
    introducirDinero()
    entregaCambio()

# PRODUCTOS LINEA 4
if opcion == 40:
    producto = producto40
    introducirDinero()
    entregaCambio()
if opcion == 41:
    producto = producto41
    introducirDinero()
    entregaCambio()
if opcion == 42:
    producto = producto42
    introducirDinero()
    entregaCambio()
if opcion == 43:
    producto = producto43
    introducirDinero()
    entregaCambio()

# PRODUCTOS LINEA 5
if opcion == 50:
    producto = producto50
    introducirDinero()
    entregaCambio()
if opcion == 51:
    producto = producto51
    introducirDinero()
    entregaCambio()
if opcion == 52:
    producto = producto52
    introducirDinero()
    entregaCambio()
if opcion == 53:
    producto = producto53
    introducirDinero()
    entregaCambio()

# PRODUCTOS LINEA 6
if opcion == 60:
    producto = producto60
    introducirDinero()
    entregaCambio()
if opcion == 61:
    producto = producto61
    introducirDinero()
    entregaCambio()
if opcion == 62:
    producto = producto62
    introducirDinero()
    entregaCambio()
if opcion == 63:
    producto = producto63
    introducirDinero()
    entregaCambio()  

print("Gracias por su compra")
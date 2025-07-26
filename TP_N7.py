"""1) Escribir una clase llamada Rectángulo que contenga una base y una altura, 
y que contenga un método que devuelva el área del rectángulo."""

"""class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        area= self.base * self.altura
        return area
    
rectangulo= Rectangulo(6, 3)
print(rectangulo.area())"""

"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional 
argentina. La clase debe contener como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate 
(representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno,
se debe lanzar una excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber 
un mate vacío, se debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. 
En ese caso la cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente 
beber se debe imprimir un mensaje de aviso: 
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""


"""class Mate():
    def __init__(self, maxima_cebadas):
        self.maxima_cebadas = maxima_cebadas
        self.cantidad_cebadas = maxima_cebadas
        self.esta_lleno = False
    def cebar(self):
        if self.esta_lleno==True:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.esta_lleno= True
        print("Llenando el mate con agua")
        print("Mate Cebado")
    def beber(self):
        if self.esta_lleno==False:
            raise Exception("¡El mate está vacío!")
        print("Tomando el mate")
        self.esta_lleno=False
        if self.cantidad_cebadas>0:
            self.cantidad_cebadas= self.cantidad_cebadas-1
        else:
            print("Advertencia: el mate está lavado.")


mate1 = Mate(2)

try:
    mate1.cebar()
    mate1.beber()

    mate1.cebar()
    mate1.beber()

    mate1.cebar()
    mate1.beber()
except Exception as e:
    print(e)"""




"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho."""

"""class Corcho():
    def __init__(self, bodega):
        self.bodega= bodega

class Botella():
    def __init__(self,corcho):
        self.corcho=corcho

class Sacacorcho():
    def __init__(self):
        self.corcho = None

    def destapar(self, botella):
        if self.corcho is not None:
            raise Exception("El sacacorcho ya tiene un corcho")
        if botella.corcho == None:
            raise Exception("La botella ya esta destapada")
        
        self.corcho= botella.corcho
        botella.corcho=None
        print("Botella destapada")
    def limpiar(self):
        if self.corcho == None:
            raise Exception("El sacacorcho no tiene un corcho y esta limpio")
        print("Se ha limpiado el sacacorcho")
        self.corcho = None

corcho1 = Corcho("Bodega Vino Blanco")
botella1 = Botella(corcho1)
sacacorcho1 = Sacacorcho()

sacacorcho1.destapar(botella1)
sacacorcho1.limpiar()"""



"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() 
guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información,
y un método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. 
Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores 
que almacene una lista de los sabores de helado disponibles. Escriba también un método que muestre estos valores, 
cree una instancia de la clase y llame al método. """

"""class Restaurante():
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida
    
    def describir_restaurante(self):
        print(f"Nombre del restaurante: {self.restaurante_nombre} \nTipo: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El Restaurante {self.restaurante_nombre} esta abierto")

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles: ")
        for sabor in self.sabores:
            print(sabor)

if __name__=='__main__':
    heladeria= Heladeria("Elio", "Helados", ["Futilla", "Dulce de Leche", "Cielo"])
    heladeria.describir_restaurante()
    heladeria.abrir_restaurante()
    heladeria.mostrar_sabores()"""


"""5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, 
y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lance una
excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección 
y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método
atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el 
método cosechar, que devuelva la cantidad cosechada"""

"""class Personaje():
    def __init__(self, vida, posicion, velocidad):
        self.vida =vida
        self.posicion = posicion
        self.velocidad = velocidad
    def recibir_ataque(self, cantidad_ataque):
        self.vida = self.vida - cantidad_ataque
        print(f"Recibio {cantidad_ataque} de ataque")
        print(f"Vida restante: {self.vida}")
        if self.vida<=0:
            raise Exception("El personaje ha muerto")
    def mover(self, direccion):
        x, y = self.posicion
        print(f"Posicion actual: ({x},{y})")
        print(f"Se movera para {direccion}")
        if direccion=="arriba":
            y = y + self.velocidad
        elif direccion=="abajo":
            y = y - self.velocidad
        elif direccion=="izquierda":
            x = x - self.velocidad
        elif direccion=="derecha":
            x = x + self.velocidad
        else:
            print("Error dirreccion no valida")

        self.posicion = (x, y)
        print(f"Nueva posicion {self.posicion}")

class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque =ataque
    
    def atacar(self, objetivo_ataque):
        print(f"Atacando con {self.ataque} de ataque")
        objetivo_ataque.recibir_ataque(self.ataque)

class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha
    def cosechar(self):
        print(f"Cantidad cosechada: {self.cosecha} unidades")



soldado1 = Soldado(100, (0, 0), 2, 25)
soldado1.mover("derecha")
print()

campesino1 = Campesino(60, (5, 5), 1, 10)
campesino1.mover("arriba")
print()

try:
    soldado1.atacar(campesino1)
except Exception as e:
    print(e)

print()
campesino1.cosechar()"""


"""6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, 
así como otros atributos que típicamente se guardan en un perfil de usuario. Escriba un 
método describir_usuario() que muestre un resumen de la información del usuario. 
Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno"""

"""class Usuario():
    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
    def describir_usuario(self):
        print("-------Perfil del Usuario-------")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")
    def saludar_usuario(self):
        print(f"---Bienvenido al Sistema {self.nombre}---")


usuario1=Usuario("Micaela", "Tapia", 23, "tapiamica521@gmail.com")
usuario1.describir_usuario()
usuario1.saludar_usuario()

print()

usuario2=Usuario("Milagros", "Tapia", 19, "mili012@gmail.com")
usuario2.describir_usuario()
usuario2.saludar_usuario()

print()

usuario3=Usuario("Juan", "Perez", 18, "juanitoP23@gmail.com")
usuario3.describir_usuario()
usuario3.saludar_usuario()"""

"""7) Admin: Un administrador es un tipo de usuario con privilegios especiales. 
Cree una clase Admin que herede de la clase Usuario del ejercicio anterior y 
agréguele un atributo privilegios que almacene una lista de strings tales como “puede postear 
en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método 
mostrar_privilegios() que muestre el conjunto de privilegios del administrador, 
cree una instancia de la clase y llame al método."""

"""class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, email, privilegios):
        super().__init__(nombre, apellido, edad, email)
        self.privilegios=privilegios
    def mostrar_privilegio(self):
        print(f"Privilegios del administrador {self.nombre}:")
        for privilegio in self.privilegios:
            print(f"_ {privilegio}")

privilegios_lista= ["Puede postear en el foro", "Puede borrar un post", "Puede banear usuario"]
admin1=Admin("Juan", "Perez", 18, "juanitoP23@gmail.com", privilegios_lista)
admin1.mostrar_privilegio()"""

"""8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, 
privilegios, que almacene una lista de strings con los privilegios de manera similar a la del 
ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta clase, y haga que 
una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de 
Admin y use el método para mostrar privilegios."""

"""class Usuario():
    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
    def describir_usuario(self):
        print("-------Perfil del Usuario-------")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Email: {self.email}")
    def saludar_usuario(self):
        print(f"---Bienvenido al Sistema {self.nombre}---")


privilegios_lista= ["Puede postear en el foro", "Puede borrar un post", "Puede banear usuario"]

class Privilegios():
    def __init__(self, privilegios):
        self.privilegios=privilegios
    def mostrar_privilegio(self):
        print(f"Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(f"_ {privilegio}")

            
class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, email, privilegios_lista):
        super().__init__(nombre, apellido, edad, email)
        self.privilegios=Privilegios(privilegios_lista)

admin2=Admin("Juan", "Perez", 18, "juanitoP23@gmail.com", privilegios_lista)
admin2.privilegios.mostrar_privilegio()"""
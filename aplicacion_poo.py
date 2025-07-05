# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__alimentado = False  # Encapsulación

    def alimentar(self):
        self.__alimentado = True
        print(f"{self.nombre} ha sido alimentado.")

    def esta_alimentado(self):
        return self.__alimentado

    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido desconocido."


# Clase derivada: León
class Leon(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

    def hacer_sonido(self):  # Polimorfismo
        return f"{self.nombre} ruge fuerte. ¡ROAR!"


# Clase derivada: Pájaro
class Pajaro(Animal):
    def __init__(self, nombre, puede_volar=True):
        super().__init__(nombre)
        self.puede_volar = puede_volar

    def hacer_sonido(self):  # Polimorfismo
        return f"{self.nombre} canta alegremente. ¡Pío Pío!"


# Crear instancias
Luke = Leon("Luke", 4)
Piolin = Pajaro("Piolin")

# Usar métodos
print(Luke.hacer_sonido())
print(Piolin.hacer_sonido())

Luke.alimentar()
print(f"¿{Luke.nombre} está alimentado?: {Luke.esta_alimentado()}")

# Mostrar si el pájaro puede volar
print(f"{Piolin.nombre} puede volar: {Piolin.puede_volar}")




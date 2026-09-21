class ContadorPositivos:
    def __init__(self):
        self.numeros = []

    def agregar_numeros(self, *args):
        for numero in args:
            if numero > 0:
                self.numeros.append(numero)
        return self.numeros

    def contar(self):
        return len(self.numeros)

c = ContadorPositivos()
print(c.agregar_numeros(5, -2, 8, 0, 10, -4))
print(c.contar())


# ----------------------------------------

class AnalizadorFrutas:
    def __init__(self):
        self.frutas = set()
        self.orden = []

    def agregar_fruta(self, fruta):
        if fruta not in self.frutas:
            self.frutas.add(fruta)
            self.orden.append(fruta)

    def agregar_multiples(self, *args):
        for fruta in args:
            self.agregar_fruta(fruta)

    def cantidad(self):
        return len(self.frutas)

af = AnalizadorFrutas()
af.agregar_multiples("manzana", "pera", "manzana", "uva", "pera")
print(af.cantidad())
print(af.orden)


# ----------------------------------------

class Carrito:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def calcular_total(self):
        total = 0
        for precio in self.productos.values():
            total = total + precio
        return total

    def productos_baratos(self, limite):
        resultado = []
        for nombre, precio in self.productos.items():
            if precio <= limite:
                resultado.append(nombre)
        return resultado

car = Carrito()
car.agregar_producto("cuaderno", 2.50)
car.agregar_producto("mochila", 25)
car.agregar_producto("lapiz", 1.00)

print(car.calcular_total())
print(car.productos_baratos(5))


# ----------------------------------------

class InversorNumeros:
    def invertir(self, lista):
        resultado = []
        i = len(lista) - 1

        while i >= 0:
            resultado.append(lista[i])
            i = i - 1

        return resultado

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            clave = tuple(lista)
            resultado[clave] = self.invertir(lista)

        return resultado

inv = InversorNumeros()
print(inv.invertir([5, 10, 15, 20]))
print(inv.invertir_multiples([1, 2, 3], [4, 5]))


# ----------------------------------------

class SeparadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def separar(self, *numeros):
        for numero in numeros:
            if numero % 2 == 0:
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        resultado = {}
        resultado["pares"] = self.pares
        resultado["impares"] = self.impares

        return resultado

    def cantidades(self):
        return (len(self.pares), len(self.impares))

sn = SeparadorNumeros()
print(sn.separar(2, 5, 8, 9, 12, 15))
print(sn.cantidades())


# ----------------------------------------

class GestorPrecios:
    def __init__(self):
        self.precios = []

    def agregar(self, *precios):
        for precio in precios:
            self.precios.append(precio)

    def precio_minimo(self):
        return min(self.precios)

    def precio_maximo(self):
        return max(self.precios)

    def promedio(self):
        if len(self.precios) == 0:
            return 0
        return sum(self.precios) / len(self.precios)

gp = GestorPrecios()
gp.agregar(10, 25, 8, 30, 15)

print(gp.precio_minimo())
print(gp.precio_maximo())
print(gp.promedio())


# ----------------------------------------

class RegistroEdades:
    def __init__(self):
        self.personas = {}

    def agregar(self, nombre, edad):
        self.personas[nombre] = edad

    def mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def promedio(self):
        if len(self.personas) == 0:
            return 0

        suma = 0

        for edad in self.personas.values():
            suma = suma + edad

        return suma / len(self.personas)

re = RegistroEdades()
re.agregar("Carlos", 20)
re.agregar("Ana", 15)
re.agregar("Luis", 25)

print(re.mayores(18))
print(re.promedio())


# ----------------------------------------

class EquiposFutbol:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre):
        self.equipos[nombre] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def cantidad_jugadores(self, equipo):
        return len(self.equipos[equipo])

ef = EquiposFutbol()
ef.crear_equipo("Barcelona")
ef.crear_equipo("Emelec")

ef.agregar_jugador("Barcelona", "Juan")
ef.agregar_jugador("Barcelona", "Pedro")
ef.agregar_jugador("Emelec", "Luis")

print(ef.cantidad_jugadores("Barcelona"))
print(ef.cantidad_jugadores("Emelec"))


# ----------------------------------------

class ContadorLetras:
    def __init__(self):
        self.vocales = 0
        self.consonantes = 0

    def analizar(self, texto):
        vocales = "aeiouAEIOU"

        for letra in texto:
            if letra in vocales:
                self.vocales = self.vocales + 1
            else:
                if letra != " ":
                    self.consonantes = self.consonantes + 1

        resultado = {}
        resultado["vocales"] = self.vocales
        resultado["consonantes"] = self.consonantes

        return resultado

cl = ContadorLetras()
print(cl.analizar("Hola mundo"))


# ----------------------------------------

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.tareas.append(tarea)

    def tareas_altas(self):
        resultado = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)

        return resultado

gt = GestorTareas()
gt.agregar("Estudiar", "alta")
gt.agregar("Jugar", "baja")
gt.agregar("Hacer tarea", "alta")

print(gt.tareas_altas())


# ----------------------------------------

class FrecuenciaNumeros:
    def __init__(self):
        self.conteo = {}

    def agregar(self, numero):
        if numero in self.conteo:
            self.conteo[numero] = self.conteo[numero] + 1
        else:
            self.conteo[numero] = 1

    def agregar_multiples(self, *numeros):
        for numero in numeros:
            self.agregar(numero)

    def frecuencia(self, numero):
        if numero in self.conteo:
            return self.conteo[numero]
        else:
            return 0

fn = FrecuenciaNumeros()
fn.agregar_multiples(2, 5, 2, 8, 5, 2)

print(fn.conteo)
print(fn.frecuencia(2))


# ----------------------------------------

class GeneradorRangos:
    def crear_rango(self, inicio, fin):
        numeros = []
        n = inicio

        while n <= fin:
            numeros.append(n)
            n = n + 1

        return tuple(numeros)

    def sumar_rango(self, inicio, fin):
        numeros = self.crear_rango(inicio, fin)
        suma = 0

        for numero in numeros:
            suma = suma + numero

        return suma

gr = GeneradorRangos()
print(gr.crear_rango(3, 7))
print(gr.sumar_rango(3, 7))


# ----------------------------------------

class MezcladorListas:
    def mezclar(self, lista1, lista2):
        resultado = []
        i = 0

        while i < len(lista1) or i < len(lista2):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

            i = i + 1

        return resultado

    def mezclar_multiples(self, *listas):
        if len(listas) == 0:
            return []

        resultado = listas[0]
        i = 1

        while i < len(listas):
            resultado = self.mezclar(resultado, listas[i])
            i = i + 1

        return resultado

ml = MezcladorListas()
print(ml.mezclar([1, 2, 3], [4, 5, 6]))
print(ml.mezclar_multiples([1, 2], [3, 4], [5, 6]))


# ----------------------------------------

class RegistroCursos:
    def __init__(self):
        self.cursos = {}

    def registrar(self, estudiante, curso):
        self.cursos[estudiante] = curso

    def buscar_curso(self, curso):
        resultado = []

        for estudiante, nombre_curso in self.cursos.items():
            if nombre_curso == curso:
                resultado.append(estudiante)

        return resultado

rc = RegistroCursos()
rc.registrar("Ana", "Python")
rc.registrar("Luis", "Java")
rc.registrar("Pedro", "Python")

print(rc.buscar_curso("Python"))


# ----------------------------------------

class BuscadorDivisores:
    def divisores(self, numero):
        resultado = []
        i = 1

        while i <= numero:
            if numero % i == 0:
                resultado.append(i)

            i = i + 1

        return tuple(resultado)

    def cantidad_divisores(self, numero):
        divisores = self.divisores(numero)
        return len(divisores)

bd = BuscadorDivisores()
print(bd.divisores(18))
print(bd.cantidad_divisores(18))


# ----------------------------------------

class ConversorMayusculas:
    def __init__(self):
        self.historial = {}

    def convertir(self, texto):
        resultado = ""

        for letra in texto:
            resultado = resultado + letra.upper()

        self.historial[texto] = resultado

        return resultado

cm = ConversorMayusculas()
print(cm.convertir("hola mundo"))
print(cm.historial)


# ----------------------------------------

class AgrupadorNotas:
    def __init__(self):
        self.grupos = {}

    def clasificar(self, nota):
        if nota >= 90:
            return "excelente"
        elif nota >= 70:
            return "aprobado"
        else:
            return "reprobado"

    def agrupar(self, *notas):
        self.grupos = {}

        for nota in notas:
            grupo = self.clasificar(nota)

            if grupo not in self.grupos:
                self.grupos[grupo] = []

            self.grupos[grupo].append(nota)

        return self.grupos

an = AgrupadorNotas()
print(an.agrupar(95, 80, 65, 92, 50, 75))


# ----------------------------------------

class CalculadorDistancias:
    def distancia(self, punto1, punto2):
        x1 = punto1[0]
        y1 = punto1[1]

        x2 = punto2[0]
        y2 = punto2[1]

        dx = x2 - x1
        dy = y2 - y1

        return (dx * dx + dy * dy) ** 0.5

    def comparar(self, referencia, *puntos):
        mas_cerca = puntos[0]
        menor = self.distancia(referencia, puntos[0])

        i = 1

        while i < len(puntos):
            distancia = self.distancia(referencia, puntos[i])

            if distancia < menor:
                menor = distancia
                mas_cerca = puntos[i]

            i = i + 1

        return mas_cerca

dc = CalculadorDistancias()
print(dc.distancia((0, 0), (3, 4)))
print(dc.comparar((0, 0), (3, 4), (1, 1), (8, 8)))


# ----------------------------------------

class InventarioProductos:
    def __init__(self):
        self.productos = {}

    def agregar(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] = self.productos[producto] + cantidad
        else:
            self.productos[producto] = cantidad

    def retirar(self, producto, cantidad):
        if producto not in self.productos:
            return False

        if self.productos[producto] >= cantidad:
            self.productos[producto] = self.productos[producto] - cantidad
            return True
        else:
            return False

    def productos_bajos(self, minimo):
        resultado = []

        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado

ip = InventarioProductos()
ip.agregar("arroz", 30)
ip.agregar("leche", 10)
ip.agregar("pan", 20)

print(ip.retirar("arroz", 25))
print(ip.productos_bajos(10))


# ----------------------------------------

class AnalizadorPalabras:
    def __init__(self):
        self.palabras = []

    def buscar_por_inicio(self, texto, inicio):
        lista = texto.split()
        resultado = []

        for palabra in lista:
            self.palabras.append(palabra)

            if len(palabra) >= len(inicio):
                if palabra[0:len(inicio)] == inicio:
                    resultado.append(palabra)

        return resultado

    def palabras_largas(self, limite):
        resultado = []

        for palabra in self.palabras:
            if len(palabra) >= limite:
                resultado.append(palabra)

        return resultado

ap = AnalizadorPalabras()
print(ap.buscar_por_inicio("casa carro perro camino", "ca"))
print(ap.palabras_largas(5))

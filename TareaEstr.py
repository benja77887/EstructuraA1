#Ejercicio #1
#Validador de notas con promedio
#Ent: notas (pueden venir malas, tipo 110 o -5)
#Pro: validar 0 a 100, guardar las buenas, calcular promedio
#Sali: True/False, lista de validas, promedio
#ejemplo..
#85 si, 92 si, 110 no (es mayor a 100), 78 si, -5 no (es menor a 0), 88 si
#lista = [85, 92, 78, 88] (deberian entrar todos)
#Suma = 343
#promedio = 343 / 4 = 85.75 (resultado)
class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())
#Ejercicio #2
#Contador de palabras unicas
#Ent: palabras (pueden repetirse, tipo "hola" dos veces)
#Pro: guardar en un conjunto para no repetir y en una lista para el orden
#Sali: cantidad de palabras distintas
#ejemplo..
#"hola" si (primera vez)
#"mundo" si (primera vez)
#"hola" no (ya estaba)
#conjunto = {hola, mundo}
#lista = [hola, mundo]
#cantidad = 2 (resultado)
class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        if palabra not in self.unicas:
            self.unicas.add(palabra)
            self.orden.append(palabra)

    def contar_palabras(self):
        return len(self.unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())
print(at.orden)
#Ejercicio #3
#Gestor de compras con totales
#Ent: nombre del articulo y su precio
#Pro: guardar en un diccionario, sumar precios, filtrar por rango
#Sali: total del carrito y lista de articulos
#ejemplo..
#pan 2.50 si
#leche 3.00 si
#queso 8.00 si
#diccionario = {pan: 2.50, leche: 3.00, queso: 8.00}
#total = 2.50 + 3.00 + 8.00 = 13.50 (resultado)
#rango 2 a 3 = [pan, leche] (el queso no entra porque vale 8)
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total = total + precio
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)
        return resultado

carro = CarroCompras()
carro.agregar_articulo("pan", 2.50)
carro.agregar_articulo("leche", 3.00)
carro.agregar_articulo("queso", 8.00)
print(carro.total_carrito())
print(carro.articulos_por_rango(2, 3))
#Ejercicio #4
#Inversor de secuencias
#Ent: una lista o varias listas
#Pro: recorrer la lista de atras para adelante con un while
#Sali: lista invertida o diccionario con las invertidas
#ejemplo..
#lista = [1, 2, 3]
#ultimo indice = 2
#saco el 3, despues el 2, despues el 1
#lista invertida = [3, 2, 1] (resultado)
#ojo: la clave del diccionario va como tupla porque una lista no puede ser clave
#(1, 2, 3): [3, 2, 1]
#(10, 20): [20, 10]
class InversorSecuencia:
    def invertir_lista(self, lista):
        nueva = []
        i = len(lista) - 1
        while i >= 0:
            nueva.append(lista[i])
            i = i - 1
        return nueva

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            clave = tuple(lista)
            resultado[clave] = self.invertir_lista(lista)
        return resultado

inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [10, 20]))
#Ejercicio #5
#Detector de numeros pares e impares
#Ent: varios numeros
#Pro: si numero % 2 == 0 es par, si no es impar
#Sali: diccionario con dos listas y una tupla con las cantidades
#ejemplo..
#1 % 2 = 1 impar
#2 % 2 = 0 par
#3 % 2 = 1 impar
#4 % 2 = 0 par
#5 % 2 = 1 impar
#pares = [2, 4]
#impares = [1, 3, 5]
#cantidades = (2, 3) (resultado)
class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        resultado = {}
        resultado["pares"] = self.pares
        resultado["impares"] = self.impares
        return resultado

    def cantidad_pares_impares(self):
        cant_pares = len(self.pares)
        cant_impares = len(self.impares)
        return (cant_pares, cant_impares)
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())
#Ejercicio #6
#Estadisticas de temperatura
#Ent: temperaturas (una o varias)
#Pro: guardar en una lista, sacar min, max y promedio
#Sali: la minima, la maxima y el promedio
#ejemplo..
#20 si, 25 si, 18 si, 30 si
#lista = [20, 25, 18, 30]
#minima = 18
#maxima = 30
#suma = 93
#promedio = 93 / 4 = 23.25 (resultado)
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.minima())
print(gt.maxima())
print(gt.promedio())
#Ejercicio #7
#Mapeador de edades
#Ent: nombre y edad
#Pro: guardar en un diccionario, filtrar por edad, sacar promedio
#Sali: lista de nombres y el promedio
#ejemplo..
#Ana 28
#Bob 17
#diccionario = {Ana: 28, Bob: 17}
#mayores de 18 = [Ana] (Bob no entra porque tiene 17)
#promedio = (28 + 17) / 2 = 22.5
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0
        suma = 0
        for edad in self.personas.values():
            suma = suma + edad
        return suma / len(self.personas)

gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))
print(gp.edad_promedio())
#Ejercicio #8
#Asignador de equipos
#Ent: nombre del equipo y nombre del jugador
#Pro: el diccionario guarda equipo -> lista de jugadores, despues se cuenta quien tiene mas
#Sali: el nombre del equipo con mas jugadores
#ejemplo..
#equipo A: Juan, Pedro
#equipo B: Ana
#A tiene 2
#B tiene 1
#el mayor es A (resultado)
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor_nombre = ""
        mayor_cantidad = -1
        for nombre, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                mayor_nombre = nombre
        return mayor_nombre

eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Ana")
print(eq.equipo_mayor_integrantes())
#Ejercicio #9
#Validador de caracteres
#Ent: un texto
#Pro: recorrer letra por letra y contar vocales, consonantes y digitos
#Sali: un diccionario con los tres conteos
#ejemplo..
#Hola123
#H consonante
#o vocal
#l consonante
#a vocal
#1 digito
#2 digito
#3 digito
#{vocales: 2, consonantes: 2, digitos: 3} (resultado)
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        vocales = "aeiouAEIOU"
        if letra in vocales:
            return True
        else:
            return False

    def es_digito(self, letra):
        digitos = "0123456789"
        if letra in digitos:
            return True
        else:
            return False

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0

        for letra in texto:
            if self.solo_vocales(letra):
                vocales = vocales + 1
            else:
                if self.es_digito(letra):
                    digitos = digitos + 1
                else:
                    if letra != " ":
                        consonantes = consonantes + 1

        resultado = {}
        resultado["vocales"] = vocales
        resultado["consonantes"] = consonantes
        resultado["digitos"] = digitos
        return resultado

astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
#Ejercicio #10
#Gestor de tareas con prioridad
#Ent: descripcion y prioridad
#Pro: guardar en una lista de tuplas, filtrar las de prioridad alta, borrar una
#Sali: las tareas altas
#ejemplo..
#("Estudiar", "alta")
#("Leer", "baja")
#prioritarias = [("Estudiar", "alta")] (Leer no entra)
class Tareas:
    def __init__(self):
        self.lista = []

    def agregar_tarea(self, descripcion, prioridad):
        tarea = (descripcion, prioridad)
        self.lista.append(tarea)

    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.lista:
            if tarea[1] == "alta":
                resultado.append(tarea)
        return resultado

    def eliminar_completada(self, descripcion):
        nueva = []
        for tarea in self.lista:
            if tarea[0] != descripcion:
                nueva.append(tarea)
        self.lista = nueva

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())
#Ejercicio #11
#Contador de frecuencia
#Ent: elementos (se pueden repetir)
#Pro: el diccionario cuenta cuantas veces aparece cada uno
#Sali: el que mas se repite y cuantas veces aparece uno
#ejemplo..
#a
#b
#a
#diccionario = {a: 2, b: 1}
#el mas frecuente es a (resultado)
class ContadorFrecuencia:
    def __init__(self):
        self.conteo = {}

    def agregar_elemento(self, elemento):
        if elemento in self.conteo:
            self.conteo[elemento] = self.conteo[elemento] + 1
        else:
            self.conteo[elemento] = 1

    def elemento_mas_frecuente(self):
        mas = ""
        mayor = -1
        for elemento, cantidad in self.conteo.items():
            if cantidad > mayor:
                mayor = cantidad
                mas = elemento
        return mas

    def frecuencia_elemento(self, elemento):
        if elemento in self.conteo:
            return self.conteo[elemento]
        else:
            return 0

cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))
#Ejercicio #12
#Selector de rango con tuplas
#Ent: pares (inicio, fin)
#Pro: armar los numeros de cada rango y juntarlos sin repetir con un conjunto
#Sali: lista de numeros unicos
#ejemplo..
#rango (1, 3) = 1, 2, 3
#rango (2, 4) = 2, 3, 4
#juntos sin repetir = [1, 2, 3, 4] (resultado)
class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        n = inicio
        while n <= fin:
            numeros.append(n)
            n = n + 1
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        juntos = set()
        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            numeros = self.crear_rango(inicio, fin)
            for n in numeros:
                juntos.add(n)
        resultado = []
        for n in juntos:
            resultado.append(n)
        resultado.sort()
        return resultado

sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))
#Ejercicio #13
#Combinador de listas
#Ent: dos o mas listas
#Pro: ir turnando un elemento de cada lista
#Sali: una lista intercalada
#ejemplo..
#[1, 2] y [3, 4]
#1 de la primera
#3 de la segunda
#2 de la primera
#4 de la segunda
#[1, 3, 2, 4] (resultado)
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        nueva = []
        i = 0
        while i < len(lista1) or i < len(lista2):
            if i < len(lista1):
                nueva.append(lista1[i])
            if i < len(lista2):
                nueva.append(lista2[i])
            i = i + 1
        return nueva

    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []
        resultado = listas[0]
        i = 1
        while i < len(listas):
            resultado = self.intercalar(resultado, listas[i])
            i = i + 1
        return resultado

cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
print(cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))
#Ejercicio #14
#Mapeo de estudiantes a notas
#Ent: estudiante y nota
#Pro: guardar en un diccionario, filtrar aprobados, buscar la nota mas alta
#Sali: lista de aprobados y una tupla (nombre, nota)
#ejemplo..
#Ana 95
#Bob 70
#diccionario = {Ana: 95, Bob: 70}
#mejor = (Ana, 95) (resultado)
class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        mejor_nombre = ""
        mejor_nota = -1
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre, mejor_nota)

rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.estudiantes_aprobados(80))
print(rn.mejor_estudiante())
#Ejercicio #15
#Divisores de un numero
#Ent: uno o varios numeros
#Pro: buscar que numeros lo dividen exacto, ver si es perfecto
#Sali: tupla de divisores, True/False, diccionario
#ejemplo..
#12
#12%1=0 si
#12%2=0 si
#12%3=0 si
#12%4=0 si
#12%5 no
#12%6=0 si
#12%7 no
#12%8 no
#12%9 no
#12%10 no
#12%11 no
#12%12=0 si
#divisores = (1, 2, 3, 4, 6, 12) (resultado)
class DivisorFinder:
    def encontrar_divisores(self, numero):
        lista = []
        d = 1
        while d <= numero:
            if numero % d == 0:
                lista.append(d)
            d = d + 1
        return tuple(lista)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for d in divisores:
            if d != numero:
                suma = suma + d
        if suma == numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado

df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 12))
#Ejercicio #16
#Codificador Cesar
#Ent: una palabra y un desplazamiento
#Pro: mover cada letra esas posiciones en el abecedario (si se pasa, vuelve a la a)
#Sali: la palabra ya corrida
#ejemplo..
#hola con 3
#h -> k
#o -> r
#l -> o
#a -> d
#queda krod (resultado)
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        abecedario = "abcdefghijklmnopqrstuvwxyz"
        if letra in abecedario:
            posicion = abecedario.find(letra)
            nueva = (posicion + desplazamiento) % 26
            return abecedario[nueva]
        else:
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        nueva = ""
        for letra in palabra:
            nueva = nueva + self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = nueva
        return nueva

cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))
print(cc.historial)
#Ejercicio #17
#Grupo de edades
#Ent: varias edades
#Pro: clasificar con if/elif y agrupar en un diccionario de listas
#Sali: el diccionario agrupado y el promedio de una categoria
#ejemplo..
#5 nino (menor de 13)
#15 adolescente
#30 adulto
#70 mayor
#{nino: [5], adolescente: [15], adulto: [30], mayor: [70]} (resultado)
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 13:
            return "nino"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos:
            return 0
        lista = self.grupos[categoria]
        if len(lista) == 0:
            return 0
        return sum(lista) / len(lista)

ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))
#Ejercicio #18
#Matriz de distancias
#Ent: puntos como tuplas (x, y)
#Pro: usar la formula de distancia y comparar cual queda mas cerca
#Sali: la distancia y el punto mas cercano
#ejemplo..
#(0, 0) y (3, 4)
#3*3 = 9
#4*4 = 16
#9 + 16 = 25
#raiz de 25 = 5.0 (resultado)
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        dx = x2 - x1
        dy = y2 - y1
        dist = (dx * dx + dy * dy) ** 0.5
        self.distancias.append(dist)
        return dist

    def punto_mas_cercano(self, referencia, *puntos):
        mas_cerca = puntos[0]
        menor = self.distancia_euclidiana(referencia, puntos[0])
        i = 1
        while i < len(puntos):
            dist = self.distancia_euclidiana(referencia, puntos[i])
            if dist < menor:
                menor = dist
                mas_cerca = puntos[i]
            i = i + 1
        return mas_cerca

cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
print(cd.punto_mas_cercano((0, 0), (3, 4), (1, 1), (10, 10)))
#Ejercicio #19
#Inventario de productos
#Ent: producto y cantidad
#Pro: guardar en un diccionario, restar stock, filtrar los que quedan bajos
#Sali: True/False y lista de productos
#ejemplo..
#pan empieza con 50
#resto 40
#queda 10
#10 < 15 entonces pan esta bajo
#restar_stock da True
#productos_bajo_stock da [pan] (resultado)
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] = self.stock[producto] + cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto not in self.stock:
            return False
        if self.stock[producto] >= cantidad:
            self.stock[producto] = self.stock[producto] - cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado

inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 40))
print(inv.productos_bajo_stock(15))
#Ejercicio #20
#Analizador de patrones en textos
#Ent: un texto y un patron (las primeras letras)
#Pro: partir el texto con split, filtrar, agrupar por largo, pasar a conjunto
#Sali: lista, diccionario y conjunto
#ejemplo..
#texto = el gato esta aqui
#el largo 2
#gato largo 4
#esta largo 4
#aqui largo 4
#{2: [el], 4: [gato, esta, aqui]}
#si el patron es ga, solo entra gato
class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):
        lista = texto.split()
        resultado = []
        for palabra in lista:
            self.palabras.append(palabra)
            if len(palabra) >= len(patron):
                inicio = palabra[0:len(patron)]
                if inicio == patron:
                    resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        lista = texto.split()
        grupos = {}
        for palabra in lista:
            self.palabras.append(palabra)
            largo = len(palabra)
            if largo not in grupos:
                grupos[largo] = []
            grupos[largo].append(palabra)
        return grupos

    def palabras_unicas(self):
        unicas = set()
        for palabra in self.palabras:
            unicas.add(palabra)
        return unicas

ap = AnalizadorPatrones()
print(ap.encontrar_palabras("el gato esta aqui", "ga"))
print(ap.agrupar_por_longitud("el gato esta aqui"))
print(ap.palabras_unicas())

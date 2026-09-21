class Termometro:
    def __init__(self):
        self.temperaturas = []

    def validar_temperatura(self, temp):
        if (temp >= -20 and temp <=50):
            return True
        else:
            return False

    def cargar_temperaturas(self, *args):
        for temp in args:
            if self.validar_temperatura(temp):
               self.temperaturas.append(temp)
        return self.temperaturas

    def promedio(self):
        if len(self.temperaturas) == 0:
            return "Temperaturas NO validas"
        return sum(self.temperaturas) / len(self.temperaturas)
t = Termometro()    
print(t.cargar_temperaturas(40,10,20,46,12,75,-52,-20,-15))
print(t.promedio())    

class AnalizadorColores:
    def __init__(self):
        self.unico = set()
        self.orden = []

    def agg_color(self,color):
        if color not in self.unico:
           self.unico.add(color)
           self.orden.append(color)
    def contar_colores(self):
        return len(self.unico)

    def agg_color_multiples(self, *args):
        for color in args:
            self.agg_color(color)
     
ac = AnalizadorColores()
ac.agg_color_multiples("rojo", "azul", "rojo", "verde", "azul", "amarillo")
print(ac.contar_colores())
print(ac.orden)

class RegistroEstudiantes:
    def __init__ (self):
        self.estudiantes = {}
        
    def agg_estudiante(self, nombre, calificacion):
        self.estudiantes[nombre] = calificacion
    
    def promedio_general(self):
        if len(self.estudiantes) == 0:
            return 0
        prom = 0
        for calificacion in self.estudiantes.values():
            prom += calificacion
        return prom / len(self.estudiantes)

    def estudiantes_aprobados(self, nota_minima):
        estu_apro = []
        for estudiante, calificacion in self.estudiantes.items():
            if calificacion >= nota_minima:
                estu_apro.append(estudiante)
        return estu_apro

Rg = RegistroEstudiantes()
Rg.agg_estudiante("Jordy", 90)
Rg.agg_estudiante("Benja", 70)
Rg.agg_estudiante("Padre", 100)
Rg.agg_estudiante("Jesus", 68)

print(Rg.promedio_general())
print(Rg.estudiantes_aprobados(70))
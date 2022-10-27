
class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        return("La clase alumno se ha creado con éxito.")
    def calificación(self):
        if self.nota>= 5:
            return( str(self.nombre) + "El alumno ha aprobado")
        else:
            return( str(self.nombre) + "El alumno ha suspendido")


       

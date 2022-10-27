#Creación
class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        return("La clase alumno se ha creado con éxito.")
    def __str__(self):
        return(str(self.nombre) + ": "+ str(self.nota))

    def calificación(self):
        if self.nota>= 5:
            return( str(self.nombre) + "El alumno ha aprobado")
        else:
            return( str(self.nombre) + "El alumno ha suspendido")
    
lista=list(())
for i in range(10):
    nombre=str("Alumno" + str(i))
    nota= random.randit(0,10)
    lista.append(Alumno(nombre,nota))
for alumno in lista:
    print(alumno)
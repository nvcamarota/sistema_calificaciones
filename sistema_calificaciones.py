"""
SISTEMA DE CALIFICACIONES
Crear una clase llamada Estudiante con los atributos: nombre, materia y calificación.
Agregar un método aprobar que devuelva True si la calificación es mayor o igual a 6, y False en caso contrario.
Crear una lista de objetos Estudiante con diferentes nombres, materias y calificaciones.
Recorrer la lista e imprimir si cada estudiante aprobó o no.
"""

# Creando la clase Estudiante con los atributos: nombre, materia, calificación
class Estudiante:
    def __init__(self, nombre, materia, calificación):
        self.nombre = nombre
        self.materia = materia
        self.calificación = calificación
        
# Función para corroborar si el alumno aprobó la materia o no e imprimir una notificación
    def aprobar(self):
        if self.calificación >= 6:
            print(f'{self.nombre} ha aprobado la materia "{self.materia}" con una calificación de {self.calificación}. ¡Bien hecho! 😎')
        else:
            print(f'{self.nombre} no ha aprobado la materia "{self.materia}". Debes estudiar más para rendir un recuperatorio 😥')
        
# Función que contiene una lista de estudiantes, con sus respectivas materias y calificaciones
def listado_estudiantes():
    print('\nListado de estudiantes:\n')
    return [
        Estudiante('María Gonzalez', 'Historia', 8.5),
        Estudiante('Rodrigo Pérez', 'Química', 10),
        Estudiante('Josefina Muñoz', 'Matemática', 4),
        Estudiante('Ignacio Roderer', 'Ciencias sociales', 5),
        Estudiante('Giuliana Pizzurno', 'Inglés', 9)
    ]
    
# Bucle que recorre los estudiantes de la lista y comprueba si se cumple la condición (calificación >= 6)
for estudiante in listado_estudiantes():
    estudiante.aprobar()

# Mensaje de cierre
print('\nCerrando "Sistema de calificaciones". ¡Hasta la próxima! 👋')
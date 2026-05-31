from datetime import datetime

# Esta clase define una excepción personalizada llamada DueDateError, que se utiliza para indicar que la fecha de vencimiento de una tarea no es válida.
class DueDateError(Exception):
    pass

# Esta clase define la clase Task, que representa una tarea con un título, descripción, asignado a un usuario y una fecha de vencimiento.
class Task():
    
    # El método __init__ es el constructor de la clase Task, que se ejecuta cuando se crea una nueva instancia de la clase.
    def __init__(self, title, description, assigned_to, due_date):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to

        # Aquí se verifica si la fecha de vencimiento es menor que la fecha actual. Si es así, se lanza una excepción DueDateError con un mensaje de error.
        if due_date < datetime.now():
            raise DueDateError('Lo sentimos, la fecha no es valida.')

        self.due_date = due_date
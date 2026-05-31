import pytest
from app.task import Task, DueDateError
from datetime import datetime, timedelta

# Esta función se utiliza para determinar si se debe omitir la prueba o no. En este caso, siempre devuelve True, 
# lo que significa que la prueba se omitirá.
def is_available_to_skip():
    return True

# Esta función es un fixture de pytest que se utiliza para proporcionar un valor de nombre de usuario a las pruebas.
# pytest.fixture es un decorador que se utiliza para marcar una función como un fixture. 
# Un fixture es una función que se ejecuta antes de cada prueba y proporciona un valor o realiza alguna configuración necesaria para la prueba.
@pytest.fixture
def username():
    print('>>> Ejecutamos el codigo antes de la prueba.')
    yield 'Moon'
    print('>>> Ejecutamos el codigo despues de la prueba.')

# Esta función es otro fixture de pytest que se utiliza para proporcionar un valor de contraseña a las pruebas.
@pytest.fixture
def password():
    return 'password'

# Esta función es una prueba que utiliza el fixture de nombre de usuario. El valor del nombre de usuario se inyecta automáticamente en la prueba a través del fixture.
def test_username(username):
    print(username)
    assert username == 'Moon'

# Esta función es otra prueba que utiliza el fixture de contraseña. El valor de la contraseña se inyecta automáticamente en la prueba a través del fixture.
def test_username_and_password(username, password):
    assert username == 'Moon'
    assert password == 'password'

# Esta clase contiene varias pruebas relacionadas con la clase Task. 
# Cada prueba está marcada con diferentes etiquetas para facilitar su ejecución y organización.
class TestTask():

    # Esta prueba está marcada con la etiqueta 'news' y simplemente verifica que la afirmación sea verdadera.
    @pytest.mark.news
    def test_task(self):
        assert True

    # Esta prueba está marcada con la etiqueta 'news' y utiliza la función pytest.mark.parametrize para ejecutar la prueba con diferentes conjuntos de datos.
    @pytest.mark.news
    @pytest.mark.parametrize(

        # Aqui se definen los nombres de los parámetros que se utilizarán en la prueba, y luego se proporciona una lista de tuplas con los valores correspondientes para cada conjunto de datos.
        'title, description, assigned_to, due_date',
        [
            ('Title 1', 'Description 1', 'User 1', datetime.now() + timedelta(days=1)),
            ('Title 2', 'Description 2', 'User 2', datetime.now() + timedelta(days=1)),
            ('Title 3', 'Description 3', 'User 3', datetime.now() + timedelta(days=1)),
            ('Title 4', 'Description 4', 'User 4', datetime.now() + timedelta(days=1)),
            ('Title 5', 'Description 5', 'User 5', datetime.now() + timedelta(days=1))
        ]
    )

    # Esta prueba verifica que se pueda crear una nueva tarea correctamente utilizando los valores proporcionados por la función pytest.mark.parametrize.
    def test_new_task(self, title, description, assigned_to, due_date):
        due_date = datetime.now() + timedelta(days=1)
        task = Task(title, description , assigned_to, due_date)

        assert task.title == title
        assert task.description == description
        assert task.assigned_to == assigned_to
        assert task.due_date == due_date

    # Esta prueba está marcada con las etiquetas 'due_date' y 'errors', y verifica que se lance una excepción DueDateError cuando se intenta crear una tarea con una fecha de vencimiento en el pasado.
    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('Title', 'Description', 'Luis_gpg', due_date)

    # Esta prueba está marcada con la etiqueta 'due_date' y verifica que la fecha de vencimiento de una tarea sea mayor que la fecha actual.
    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'Luis_gpg', due_date)

        assert task.due_date > datetime.now()

    # Esta prueba está marcada con la etiqueta 'skip' y se omite debido a que no cumple con los requerimientos establecidos en la función is_available_to_skip.
    @pytest.mark.skip(reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    def test_skip(self):
        pass

    # Esta prueba también está marcada con la etiqueta 'skip' y se omite debido a que no cumple con los requerimientos establecidos en la función is_available_to_skip. 
    # La diferencia es que esta prueba utiliza la función pytest.mark.skipif para determinar si se debe omitir o no, en lugar de omitirla directamente.
    @pytest.mark.skipif(is_available_to_skip(), reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    def test_skip2(self):
        pass

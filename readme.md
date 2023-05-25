# Python datasets

Conjunto de clases abstractas para la implementación de bases de datos orientadas a objetos en Python.

<br/>


## Uso

**1. Implementa las clases Dataset, ObjectStore y Database.**

<br/>

```python

from datasets import Database, ObjectStore, Dataset


class MyDataset(Dataset):
    """Registro de la colección"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None
        self.email = None

    def is_valid(self):
        """
        Valida los valores del registro.
        """
        return bool(self.name and self.email)


class MyObjectStore(ObjectStore):
    """Colección de registros"""

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = data

    def datasets(self):
        """
        Generador para recorrer los registros de la colección.
        """
        for item in self._data:

            dataset = MyDataset()

            try:
                # intenta asignar los valores del registro
                # se detiene si hay un IndexError
                dataset.name = item[0]
                dataset.email = item[1]
            except IndexError:
                pass

            yield dataset


class MyDatabase(Database):
    """Base de datos"""

    def __init__(self, stores):
        self._stores = {}

        for name, data in stores.items():
            self._stores[name] = MyObjectStore(data)

    def get(self, key):
        """
        Obtiene una colección de la base de datos.
        """
        return self._stores.get(key)

    def stores(self):
        """
        Generador para recorrer las colecciones de la base de datos.
        """
        for item in self._stores.values():
            yield item

```

<br/>

**2. Crea la instancia de la base de datos y usa los métodos de acceso a los datos.**

<br/>

```python

data = {
    'users': [
        ('John Doe', 'jhon.doe@example.com'),
        ('Mary Jane', 'mary.jane@example.com'),
        ('Annonymous', ''),  # registro incompleto
        tuple(),  # registro vacío
    ]
}

database = MyDatabase(data)  # crea la instancia de la base de datos
store = database.get('users')  # obtiene la colección de la base de datos

print('collection: users')

for dataset in store.datasets():
    # operaciones para cada uno de los registros de la colección
    if dataset.is_valid():
        print('valid: ', dataset.__dict__)
    else:
        print('invalid: ', dataset.__dict__)

```

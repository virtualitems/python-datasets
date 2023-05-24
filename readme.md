# Python datasets

Conjunto de clases abstractas para la implementación de bases de datos orientadas a objetos en Python.


## Uso

<br/>

1. Implementa las clases Dataset, ObjectStore y Database.

<br/>

```python

from datasets import Database, ObjectStore, Dataset


class MyDataset(Dataset):
    """Registro de la colección"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = None
        self.email = None

    def is_empty(self) -> bool:
        """
        Comprueba si el registro está vacío.
        """

        for item in self.__dict__.values():
            if not item:
                return False
        return True

    def is_valid(self) -> bool:
        """
        Comprueba si el registro es válido.
        """
        return not self.is_empty()


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

            dataset = MyDataset ()
            dataset.name = item[0]
            dataset.email = item[1]

            yield dataset

    def get(self, key):
        """
        Obtiene un registro de la colección.
        """
        return self._data.get(key)


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

2. Crea la instancia de la base de datos y usa los métodos de acceso a los datos.

<br/>

```python

data = {
    'users': [
        ('John Doe', 'jhon.doe@example.com'),
        ('Mary Jane', 'mary.jane@example.com'),
    ]
}

database = MyDatabase(data)  # crea la instancia de la base de datos
store = database.get('users')  # obtiene la colección de la base de datos

print('collection: users')

for dataset in store.datasets():
    print(dataset.__dict__)  # operaciones para cada uno de los registros de la colección

```

<br/>


# -*- coding: utf-8 -*-

"""
Read only data access layer abstraction.
"""

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Generator


# ------------------------------
# Exceptions
# ------------------------------

class ObjectStoreError(Exception):
    """Any error related to a store"""


class DatasetError(Exception):
    """Any error related to a dataset"""


# ------------------------------
# Abstractions
# ------------------------------

class Dataset(ABC):
    """Dataclass for a dataset"""

    def __iter__(self):
        return iter(self.__dict__.items())

    def __len__(self) -> 'int':
        return len(self.__dict__)

    def __bool__(self) -> 'bool':
        return self.is_valid()


class ObjectStore(ABC):
    """Collection of datasets"""

    def __iter__(self):
        return iter(self.datasets())

    def __len__(self) -> 'int':
        return len(self.datasets())

    @abstractmethod
    def datasets(self) -> 'Generator[Dataset, None, None]':
        """generator of datasets

        Returns:
            generator
        """


class Database(ABC):
    """Collection of stores"""

    def __getitem__(self, key) -> 'ObjectStore':
        return self.get(key)

    def __iter__(self):
        return iter(self.stores())

    def __len__(self) -> 'int':
        return len(self.stores())

    @abstractmethod
    def get(self, key) -> 'ObjectStore':
        """obtain a store by key

        Args:
            key: key of the store
        """

    @abstractmethod
    def stores(self) -> 'Generator[ObjectStore, None, None]':
        """generator of stores

        Returns:
            generator
        """


# ------------------------------
# All iterable
# ------------------------------

__all__ = (
    'ObjectStoreError',
    'DatasetError',
    'Dataset',
    'ObjectStore',
    'Database',
)

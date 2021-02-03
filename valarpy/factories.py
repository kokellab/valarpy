import abc
from typing import Type, Generic, TypeVar

from valarpy.definitions import Run

T = TypeVar("T", covariant=True)


class Factory(Generic[T], metaclass=abc.ABCMeta):
    """"""


class RunFactory(Factory):
    def find(self):
        pass

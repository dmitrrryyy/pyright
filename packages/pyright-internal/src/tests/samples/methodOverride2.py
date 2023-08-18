# This sample tests the reportIncompatibleMethodOverride
# diagnostic check.


from typing import Any, Generic, ParamSpec, TypeVar


class Base1:
    def f1(self, *, kwarg0: int) -> None:
        ...

    def f2(self, *, kwarg0: int) -> None:
        ...

    def f3(self, *, kwarg0: int) -> None:
        ...

    def f4(self, *, kwarg0: int) -> None:
        ...

    def g1(self, a: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def g2(self, a: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def g3(self, a: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def g4(self, a: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def g5(self, a: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def g6(self, a: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def h1(self, a: int, *args: int) -> None:
        ...


class Derived1(Base1):
    def f1(self, arg0: int = 0, *, kwarg0: int, kwarg1: int = 0) -> None:
        ...

    # This should generate an error because of a positional parameter mismatch.
    def f2(self, arg0: int, *, kwarg0: int, kwarg1: int = 0) -> None:
        ...

    # This should generate an error because of a missing kwarg1.
    def f3(self, arg0: int = 0, *, kwarg0: int, kwarg1: int) -> None:
        ...

    # This should generate an error because kwarg0 is the wrong type.
    def f4(self, arg0: int = 0, *kwarg0: str) -> None:
        ...

    def g1(self, xxx: int, /, b: str, *, kwarg0: int) -> None:
        ...

    def g2(self, __a: int, b: str, *, kwarg0: int) -> None:
        ...

    # This should generate an error because of a name mismatch between b and c.
    def g3(self, __a: int, c: str, *, kwarg0: int) -> None:
        ...

    # This should generate an error because of a type mismatch for b.
    def g4(self, __a: int, b: int, *, kwarg0: int) -> None:
        ...

    def g5(self, __a: int, b: str = "hi", *, kwarg0: int) -> None:
        ...

    def g6(self, __a: int, b: str, c: str = "hi", *, kwarg0: int) -> None:
        ...


P = ParamSpec("P")
R = TypeVar("R")


class Base2(Generic[P, R]):
    def method1(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    def method2(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...


class Derived2(Base2[P, R]):
    def method1(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    def method2(self, *args: Any, **kwargs: Any) -> R:
        ...

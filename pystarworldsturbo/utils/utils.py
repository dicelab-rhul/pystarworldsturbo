from os import devnull
from typing import Any, Iterable, Iterator, cast


def ignore(obj: Any | Iterable[Any] | Iterator[Any]) -> None:
    if not obj:
        return
    elif isinstance(obj, (Iterable, Iterator)):
        iterable_obj: Iterable[Any] | Iterator[Any] = cast(Iterable[Any] | Iterator[Any], obj)

        for elm in iterable_obj:
            ignore(elm)
    else:
        with open(devnull, "w") as f:
            f.write(str(obj))
            f.flush()

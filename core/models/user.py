from dataclasses import dataclass
import abc

__all__: list[str] = ["User"]


@dataclass
class User(abc.ABC):
    email: str
    last_name: str
    first_name: str

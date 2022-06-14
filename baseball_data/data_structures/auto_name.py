from enum import Enum
from typing import TypeVar, Any

T = TypeVar('T', bound='AutoName')


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    @classmethod
    def _from_str(cls, value: Any, mapping: dict) -> T:
        try:
            mapped = mapping[value]

            return cls(mapped)  # type: ignore[return-value]

        except KeyError:
            raise Exception(f'Unknown value {value} for {cls.__name__}')

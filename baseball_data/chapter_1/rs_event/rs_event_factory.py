from pathlib import Path
from inspect import isclass
from pkgutil import iter_modules
from importlib import import_module
from typing import TypeVar

from baseball_data.chapter_1.rs_event.rs_event import RsEvent


T = TypeVar('T', bound='RsEvent')


class RsEventFactory(object):
    base_event: type = RsEvent

    def __init__(self) -> None:
        self._import_subclasses()
        self._class_map = self._get_class_map()

    def from_tokens(self, tokens: list[str]) -> T:
        try:
            klass = self._class_map[tokens[0]]
            return klass.from_tokens(tokens[1:])

        except KeyError:
            raise Exception(f'Error parsing: {tokens}')

    def _import_subclasses(self) -> None:
        folder_path = Path(__file__).parent

        for (_, klass_name, _) in iter_modules([str(folder_path)]):  # type: ignore[assignment]
            module_name = '.'.join(self.base_event.__module__.split('.')[:-1])
            module = import_module(f"{module_name}.{klass_name}")

            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                if isclass(attribute) and issubclass(attribute, self.base_event):            
                    globals()[attribute_name] = attribute

    def _get_class_map(self) -> dict:
        return {x.data_id: x for x in self.base_event.__subclasses__()}  # type: ignore[attr-defined]


if __name__ == '__main__':
    factory = RsEventFactory()
    import ipdb
    ipdb.set_trace()
    
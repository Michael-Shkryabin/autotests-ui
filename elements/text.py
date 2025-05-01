from elements.base_elemen import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"
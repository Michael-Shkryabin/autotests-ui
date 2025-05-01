from elements.base_elemen import BaseElement


class Icon(BaseElement):
    @property
    def type_of(self) -> str:
        return "icon"
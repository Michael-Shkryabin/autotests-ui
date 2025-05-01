from elements.base_elemen import BaseElement


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "link"
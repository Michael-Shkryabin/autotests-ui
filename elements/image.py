from elements.base_elemen import BaseElement


class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return "image"
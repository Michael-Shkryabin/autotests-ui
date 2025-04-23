from elements.base_elemen import BaseElement


class FileInput(BaseElement):
    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.set_input_files(file)

from src.components.Button import Button

class CheckBox:
    
    def __init__(self, positions, command):
        self.checked = False
        self.__positions = positions
        self.__command = command
        self.__load_componenets()

    def __load_componenets(self):
        # Lokasi gambar.
        path_checked = 'assets/buttons/checkbox-checked.png'
        path_unchecked = 'assets/buttons/checkbox-unchecked.png'

        # Membuat tombol checkbox.
        self.btn_checked = Button(path_checked, self.__positions, self.__checked_toggle, self.__command)
        self.btn_unchecked = Button(path_unchecked, self.__positions, self.__checked_toggle, self.__command)

    def __checked_toggle(self):
        self.checked = not self.checked

    def render(self, screen):
        if self.checked:
            self.btn_checked.render(screen)
        else:
            self.btn_unchecked.render(screen)

    
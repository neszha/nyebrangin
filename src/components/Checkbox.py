from src.components.Button import Button

# Membuat tombol dengen tipe checkbox.
class CheckBox:
    
    def __init__(self, position, command):
        self.checked = False
        self.__position = position
        self.__command = command
        self.__load_componenets()

    def __load_componenets(self):
        # Lokasi gambar.
        path_checked = 'assets/images/buttons/checkbox-checked.png'
        path_unchecked = 'assets/images/buttons/checkbox-unchecked.png'

        # Membuat tombol checkbox.
        self.__btn_checked = Button(path_checked, self.__position, self.__checked_toggle, self.__command, index=2)
        self.__btn_unchecked = Button(path_unchecked, self.__position, self.__checked_toggle, self.__command, index=2)

    def __checked_toggle(self):
        self.checked = not self.checked

    def render(self, screen):
        if self.checked: self.__btn_checked.render(screen)
        else: self.__btn_unchecked.render(screen)

    
from src.components.PopUp import PopUp

class Settings(PopUp):

    def __init__(self):
        super().__init__('Settings', 'assets/backgrounds/layer-settings.png')

    def render(self, screen):
        if self._show:
            self.render_popup(screen)
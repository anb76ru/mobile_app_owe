from owe import KV
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.softinput_mode = 'below_target'


class Owe(MDApp):

    md_bg_color = [0.26, 0.40, 0.55, 1]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen


Owe().run()

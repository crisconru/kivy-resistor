from pathlib import Path
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout


kv_file = str(Path(__file__))[:-3] + '.kv'
Builder.load_file(kv_file)


class ResistorFour(BoxLayout):
    pass

class ResistorFive(BoxLayout):
    pass


class Resistor(AnchorLayout):
    pass
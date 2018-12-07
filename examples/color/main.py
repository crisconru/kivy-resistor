from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kresistor.resistor import Colour

kv_file = Path(__file__).resolve().parents[2] / 'kresistor' / 'resistor.kv'
Builder.load_file(str(kv_file))


class MainApp(App):

    def build(self):
        return Colour()


if __name__ == '__main__':
    MainApp().run()

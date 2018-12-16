from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kresistor.resistor import Resistor


class Main(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        return Main()


if __name__ == "__main__":
    MainApp().run()

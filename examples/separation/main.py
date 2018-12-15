from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kresistor.components.separation import Separation

Window.clearcolor = (1, 1, 1, 1)


class Main(BoxLayout):
    orientation = 'horizontal'
    padding = [50, 300, 50, 300]
    spacing = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Separation())
        self.add_widget(Separation(value=5))
        self.add_widget(Separation(value=6))


class MainApp(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    MainApp().run()

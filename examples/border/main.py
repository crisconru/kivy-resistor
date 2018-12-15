from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kresistor.components.border import Border

Window.clearcolor = (1, 1, 1, 1)


class Main(BoxLayout):
    orientation = 'horizontal'
    padding = [50, 300, 50, 300]
    spacing = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Border())
        self.add_widget(Border())


class MainApp(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    MainApp().run()

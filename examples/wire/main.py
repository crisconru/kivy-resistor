from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kresistor.components.wire import Wire

Window.clearcolor = (1, 1, 1, 1)


class Main(BoxLayout):
    orientation = 'horizontal'
    w1 = Wire()
    w2 = Wire()
    w2.change_orientation('vertical')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.w1)
        self.add_widget(self.w2)


class MainApp(App):

    def build(self):
        return Main()


if __name__ == "__main__":
    MainApp().run()

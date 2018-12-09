from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kresistor.components.bands import FirstBand, SecondBand, ThirdBand
from kresistor.components.bands import MultiplierBand, ToleranceBand


class Main(BoxLayout):
    orientation = 'horizontal'
    padding = [50, 300, 50, 300]
    spacing = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FirstBand())
        self.add_widget(SecondBand())
        self.add_widget(ThirdBand())
        self.add_widget(MultiplierBand())
        self.add_widget(ToleranceBand())


class MainApp(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    MainApp().run()

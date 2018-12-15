from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kresistor.components.bands import FirstBand, SecondBand, ThirdBand
from kresistor.components.bands import MultiplierBand, ToleranceBand, PPMBand

Window.clearcolor = (1, 1, 1, 1)


class Main(BoxLayout):
    orientation = 'horizontal'
    padding = [50, 300, 50, 300]
    spacing = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_band(FirstBand)
        self.add_band(SecondBand)
        self.add_band(ThirdBand)
        self.add_band(MultiplierBand)
        self.add_band(ToleranceBand)
        self.add_band(PPMBand)

    def add_band(self, obj):
        layout = BoxLayout(orientation='vertical', spacing=10)
        band = obj()
        label = Label(text=f'{obj.__name__}: {band.value}', color=[0, 0, 0, 1])
        band.bind(value=lambda instance, x:
                  setattr(label, 'text', f'{obj.__name__}: {band.value}'))
        layout.add_widget(band)
        layout.add_widget(label)
        self.add_widget(layout)


class MainApp(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    MainApp().run()

from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kresistor.components import colors
from kivy.properties import DictProperty

# kv_file = str(Path(__file__))[:-3] + '.kv'
# Builder.load_file(kv_file)


class Wire(BoxLayout):
    way = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'Wire: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.way = {'horizontal': 'vertical', 'vertical': 'horizontal'}
        self.change_orientation()

    def change_orientation(self, data='horizontal'):
        Logger.debug(f'Wire: change_orientation( {data} )')
        if data in self.way:
            self.orientation = self.way[data]
            self.clear_widgets()
            b1 = Button(background_color=colors['TRANSPARENT'],
                        background_normal='', background_down='')
            b2 = Button(background_color=colors['GREY'],
                        background_normal='', background_down='')
            b3 = Button(background_color=colors['TRANSPARENT'],
                        background_normal='', background_down='')
            if data == 'horizontal':
                b1.size_hint = [1, 1]
                b2.size_hint = [1, 2]
                b3.size_hint = [1, 1]
            elif data == 'vertical':
                b1.size_hint = [1, 1]
                b2.size_hint = [2, 1]
                b3.size_hint = [1, 1]
            self.add_widget(b1)
            self.add_widget(b2)
            self.add_widget(b3)

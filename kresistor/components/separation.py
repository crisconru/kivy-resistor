from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.properties import DictProperty, NumericProperty
from kresistor.components import colors

kv_file = str(Path(__file__))[:-3] + '.kv'
Builder.load_file(kv_file)


class Separation(Button):
    color = DictProperty()
    value = NumericProperty(4)

    def __init__(self, **kwargs):
        Logger.debug(f'Separation: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.color = {'4': colors['FOUR'],
                      '5': colors['FIVE'],
                      '6': colors['SIX']}
        self.change_value(self.value)

    def change_value(self, data=4):
        Logger.debug(f'Separation: change_value( {data} )')
        self.background_color = self.color[str(data)]

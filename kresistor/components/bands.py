from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.properties import ListProperty, NumericProperty, DictProperty
from kivy.uix.anchorlayout import AnchorLayout

kv_file = str(Path(__file__))[:-3] + '.kv'
Builder.load_file(kv_file)


class BandColours(AnchorLayout):
    # Colours
    black = ListProperty([0, 0, 0, 1])
    brown = ListProperty([0.5, 0.25, 0, 1])
    red = ListProperty([1, 0, 0, 1])
    orange = ListProperty([1, 0.5, 0, 1])
    yellow = ListProperty([1, 1, 0, 1])
    green = ListProperty([0, 1, 0, 1])
    blue = ListProperty([0, 0, 1, 1])
    violet = ListProperty([1, 0, 1, 1])
    grey = ListProperty([0.5, 0.5, 0.5, 1])
    white = ListProperty([1, 1, 1, 1])
    gold = ListProperty([0.5, 0.5, 0, 1])
    silver = ListProperty([0.75, 0.75, 0.75, 1])
    # Layout properties
    anchor_x = 'center'
    anchor_y = 'center'


class FirstBand(BandColours):
    value = NumericProperty(1)
    colors = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'FirstBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.colors = {'1': self.brown,
                       '2': self.red,
                       '3': self.orange,
                       '4': self.yellow,
                       '5': self.green,
                       '6': self.blue,
                       '7': self.violet,
                       '8': self.grey,
                       '9': self.white}
        self.ids.first_dropdown.select(self.value)
        Logger.debug('FirstBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'FirstBand: change_value( {data} )')
        self.value = data
        self.ids.first_btn.background_color = self.colors[str(data)]
        Logger.debug(f'FirstBand: value = {self.value}, '
                     f'background_color = {self.colors[str(data)]}')


class SecondBand(BandColours):
    value = NumericProperty(0)
    colors = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'SecondBand: __init__( {kwargs} )__')
        super().__init__(**kwargs)
        self.colors = {'0': self.black,
                       '1': self.brown,
                       '2': self.red,
                       '3': self.orange,
                       '4': self.yellow,
                       '5': self.green,
                       '6': self.blue,
                       '7': self.violet,
                       '8': self.grey,
                       '9': self.white}
        self.ids.second_dropdown.select(self.value)
        Logger.debug('SecondBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'SecondBand: change_value( {data} )')
        self.value = data
        self.ids.second_btn.background_color = self.colors[str(data)]
        Logger.debug(f'SecondBand: value = {self.value}, '
                     f'background_color = {self.colors[str(data)]}')


class ThirdBand(BandColours):
    value = NumericProperty(0)
    colors = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'ThirdBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.colors = {'0': self.black,
                       '1': self.brown,
                       '2': self.red,
                       '3': self.orange,
                       '4': self.yellow,
                       '5': self.green,
                       '6': self.blue,
                       '7': self.violet,
                       '8': self.grey,
                       '9': self.white}
        self.ids.third_dropdown.select(self.value)
        Logger.debug('ThirdBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'SecondBand: change_value( {data} )')
        self.value = data
        self.ids.third_btn.background_color = self.colors[str(data)]
        Logger.debug(f'ThirdBand: value = {self.value}, '
                     f'background_color = {self.colors[str(data)]}')


class MultiplierBand(BandColours):
    value = NumericProperty(0)
    colors = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'MultiplierBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.colors = {'0': self.black,
                       '1': self.brown,
                       '2': self.red,
                       '3': self.orange,
                       '4': self.yellow,
                       '5': self.green,
                       '6': self.blue,
                       '7': self.violet,
                       '8': self.grey,
                       '9': self.white,
                       '-1': self.gold,
                       '-2': self.silver}
        self.ids.multiplier_dropdown.select(self.value)
        Logger.debug('MultiplierBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'MultiplierBand: change_value( {data} )')
        self.value = data
        self.ids.multiplier_btn.background_color = self.colors[str(data)]
        Logger.debug(f'MultiplierBand: value = {self.value}, '
                     f'background_color = {self.colors[str(data)]}')


class ToleranceBand(BandColours):
    value = NumericProperty(1.0)
    colors = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'ToleranceBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.colors = {'1.0': self.brown,
                       '2.0': self.red,
                       '0.5': self.green,
                       '0.25': self.blue,
                       '0.1': self.violet,
                       '0.05': self.grey,
                       '5.0': self.gold,
                       '10.0': self.silver}
        self.ids.tolerance_dropdown.select(self.value)
        Logger.debug('ToleranceBand: initialized')

    def change_value(self, data: float):
        Logger.debug(f'ToleranceBand: change_value( {data} )')
        self.value = data
        self.ids.tolerance_btn.background_color = self.colors[str(data)]
        Logger.debug(f'ToleranceBand: value = {self.value}, '
                     f'background_color = {self.colors[str(data)]}')


class PPMBand(BandColours):
    value = NumericProperty(100)
    colors = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'PPMBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.colors = {'100': self.brown,
                       '50': self.red,
                       '15': self.orange,
                       '25': self.yellow,
                       '10': self.blue,
                       '5': self.violet}
        self.ids.ppm_dropdown.select(self.value)
        Logger.debug('PPMBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'PPMBand: change_value( {data} )')
        self.value = data
        self.ids.ppm_btn.background_color = self.colors[str(data)]
        Logger.debug(f'PPMBand: value = {self.value}, '
                     f'background_color = {self.colors[str(data)]}')

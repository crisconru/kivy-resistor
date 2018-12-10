from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.properties import ListProperty, NumericProperty
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.first_dropdown.select(self.brown)
        self.colors = {'1': self.brown,
                       '2': self.red,
                       '3': self.orange,
                       '4': self.yellow,
                       '5': self.green,
                       '6': self.blue,
                       '7': self.violet,
                       '8': self.grey,
                       '9': self.white}
        Logger.info('FirstBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'FirstBand: value = {self.value}')


class SecondBand(BandColours):
    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.second_dropdown.select(self.black)
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
        Logger.info('SecondBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'SecondBand: value = {self.value}')


class ThirdBand(BandColours):
    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.third_dropdown.select(self.black)
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
        Logger.info('ThirdBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'ThirdBand: value = {self.value}')


class MultiplierBand(BandColours):
    value = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.multiplier_dropdown.select(self.black)
        self.colors = {'1': self.black,
                       '10': self.brown,
                       '100': self.red,
                       '1000': self.orange,
                       '10000': self.yellow,
                       '100000': self.green,
                       '1000000': self.blue,
                       '10000000': self.violet,
                       '100000000': self.grey,
                       '1000000000': self.white,
                       '0.1': self.gold,
                       '0.01': self.silver}
        Logger.info('MultiplierBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'MultiplierBand: value = {self.value}')


class ToleranceBand(BandColours):
    value = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.tolerance_dropdown.select(self.brown)
        self.colors = {'1.0': self.brown,
                       '2.0': self.red,
                       '0.5': self.green,
                       '0.25': self.blue,
                       '0.1': self.violet,
                       '0.05': self.grey,
                       '5': self.gold,
                       '10': self.silver}
        Logger.info('ToleranceBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'ToleranceBand: value = {self.value}')


class PPMBand(BandColours):
    value = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.ppm_dropdown.select(self.brown)
        self.colors = {'100': self.brown,
                       '50': self.red,
                       '15': self.orange,
                       '25': self.yellow,
                       '10': self.blue,
                       '5': self.violet}
        Logger.info('PPMBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'PPMBand: value = {self.value}')

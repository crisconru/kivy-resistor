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
        Logger.info('FirstBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'FirstBand: value = {self.value}')


class SecondBand(BandColours):
    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.second_dropdown.select(self.black)
        Logger.info('SecondBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'SecondBand: value = {self.value}')


class ThirdBand(BandColours):
    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.third_dropdown.select(self.black)
        Logger.info('ThirdBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'ThirdBand: value = {self.value}')


class MultiplierBand(BandColours):
    value = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.multiplier_dropdown.select(self.black)
        Logger.info('MultiplierBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'MultiplierBand: value = {self.value}')


class ToleranceBand(BandColours):
    value = NumericProperty(1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.tolerance_dropdown.select(self.brown)
        Logger.info('ToleranceBand: initialized')

    def change_value(self, data):
        self.value = data
        Logger.info(f'ToleranceBand: value = {self.value}')

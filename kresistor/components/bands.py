from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.properties import NumericProperty, DictProperty
from kivy.uix.anchorlayout import AnchorLayout
from kresistor.components import colors

kv_file = str(Path(__file__))[:-3] + '.kv'
Builder.load_file(kv_file)


class BandColours(AnchorLayout):
    # Layout properties
    anchor_x = 'center'
    anchor_y = 'center'


class FirstBand(BandColours):
    value = NumericProperty(1)
    color = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'FirstBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.color = {'1': colors['BROWN'],
                      '2': colors['RED'],
                      '3': colors['ORANGE'],
                      '4': colors['YELLOW'],
                      '5': colors['GREEN'],
                      '6': colors['BLUE'],
                      '7': colors['VIOLET'],
                      '8': colors['GREY'],
                      '9': colors['WHITE']}
        self.ids.first_dropdown.select(self.value)
        Logger.debug('FirstBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'FirstBand: change_value( {data} )')
        self.value = data
        self.ids.first_btn.background_color = self.color[str(data)]
        Logger.debug(f'FirstBand: value = {self.value}, '
                     f'background_color = {self.color[str(data)]}')


class SecondBand(BandColours):
    value = NumericProperty(0)
    color = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'SecondBand: __init__( {kwargs} )__')
        super().__init__(**kwargs)
        self.color = {'0': colors['BLACK'],
                      '1': colors['BROWN'],
                      '2': colors['RED'],
                      '3': colors['ORANGE'],
                      '4': colors['YELLOW'],
                      '5': colors['GREEN'],
                      '6': colors['BLUE'],
                      '7': colors['VIOLET'],
                      '8': colors['GREY'],
                      '9': colors['WHITE']}
        self.ids.second_dropdown.select(self.value)
        Logger.debug('SecondBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'SecondBand: change_value( {data} )')
        self.value = data
        self.ids.second_btn.background_color = self.color[str(data)]
        Logger.debug(f'SecondBand: value = {self.value}, '
                     f'background_color = {self.color[str(data)]}')


class ThirdBand(BandColours):
    value = NumericProperty(0)
    color = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'ThirdBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.color = {'0': colors['BLACK'],
                      '1': colors['BROWN'],
                      '2': colors['RED'],
                      '3': colors['ORANGE'],
                      '4': colors['YELLOW'],
                      '5': colors['GREEN'],
                      '6': colors['BLUE'],
                      '7': colors['VIOLET'],
                      '8': colors['GREY'],
                      '9': colors['WHITE']}
        self.ids.third_dropdown.select(self.value)
        Logger.debug('ThirdBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'SecondBand: change_value( {data} )')
        self.value = data
        self.ids.third_btn.background_color = self.color[str(data)]
        Logger.debug(f'ThirdBand: value = {self.value}, '
                     f'background_color = {self.color[str(data)]}')


class MultiplierBand(BandColours):
    value = NumericProperty(0)
    color = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'MultiplierBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.color = {'0': colors['BLACK'],
                      '1': colors['BROWN'],
                      '2': colors['RED'],
                      '3': colors['ORANGE'],
                      '4': colors['YELLOW'],
                      '5': colors['GREEN'],
                      '6': colors['BLUE'],
                      '7': colors['VIOLET'],
                      '8': colors['GREY'],
                      '9': colors['WHITE'],
                      '-1': colors['GOLD'],
                      '-2': colors['SILVER']}
        self.ids.multiplier_dropdown.select(self.value)
        Logger.debug('MultiplierBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'MultiplierBand: change_value( {data} )')
        self.value = data
        self.ids.multiplier_btn.background_color = self.color[str(data)]
        Logger.debug(f'MultiplierBand: value = {self.value}, '
                     f'background_color = {self.color[str(data)]}')


class ToleranceBand(BandColours):
    value = NumericProperty(1.0)
    color = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'ToleranceBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.color = {'1.0': colors['BROWN'],
                      '2.0': colors['RED'],
                      '0.5': colors['GREEN'],
                      '0.25': colors['BLUE'],
                      '0.1': colors['VIOLET'],
                      '0.05': colors['GREY'],
                      '5.0': colors['GOLD'],
                      '10.0': colors['SILVER']}
        self.ids.tolerance_dropdown.select(self.value)
        Logger.debug('ToleranceBand: initialized')

    def change_value(self, data: float):
        Logger.debug(f'ToleranceBand: change_value( {data} )')
        self.value = data
        self.ids.tolerance_btn.background_color = self.color[str(data)]
        Logger.debug(f'ToleranceBand: value = {self.value}, '
                     f'background_color = {self.color[str(data)]}')


class PPMBand(BandColours):
    value = NumericProperty(100)
    color = DictProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'PPMBand: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.color = {'100': colors['BROWN'],
                      '50': colors['RED'],
                      '15': colors['ORANGE'],
                      '25': colors['YELLOW'],
                      '10': colors['BLUE'],
                      '5': colors['VIOLET']}
        self.ids.ppm_dropdown.select(self.value)
        Logger.debug('PPMBand: initialized')

    def change_value(self, data: int):
        Logger.debug(f'PPMBand: change_value( {data} )')
        self.value = data
        self.ids.ppm_btn.background_color = self.color[str(data)]
        Logger.debug(f'PPMBand: value = {self.value}, '
                     f'background_color = {self.color[str(data)]}')

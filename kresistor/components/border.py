from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.properties import ListProperty, OptionProperty, NumericProperty,\
    StringProperty, DictProperty
from kresistor.components import colors


kv_file = str(Path(__file__))[:-3] + '.kv'
Builder.load_file(kv_file)


class Border(Button):
    # colors
    ccolors = DictProperty({'4': colors['FOUR'], '5': colors['FIVE'],
                            '6': colors['SIX']})
    # Property to change the color
    border_color = ListProperty()
    # Numeric values
    mini = NumericProperty(4)
    maxi = NumericProperty(6)
    bands = NumericProperty()
    # Geometrical property
    orientation = OptionProperty('left', options=['left', 'top', 'right', 'down'])

    def __init__(self, **kwargs):
        Logger.debug(f'Border: __init__( {kwargs} )')
        super().__init__(**kwargs)
        # self.ccolors = {'4': colors['FOUR'], '5': colors['FIVE'], '6': colors['SIX']}
        self.change_color(0)
        self.change_orientation()
        Logger.debug('Border: initializated')

    def change_color(self, opt: int = None):
        Logger.debug(f'Border: change_color( {opt} )')
        if opt is None:
            self.bands = self.bands + 1 if self.bands < self.maxi \
                else self.mini
        else:
            self.bands = self.bands if str(self.bands) in self.ccolors \
                else self.mini
        self.border_color = self.ccolors[str(self.bands)]
        Logger.debug(f'Border: bands = {str(self.bands)}')

    def change_orientation(self, orientation: str = 'left'):
        Logger.debug(f'Boder: change_orientation( {orientation} )')
        if orientation in self.orientations:
            self.orientation = orientation
            self.border = [20, 50, 20, 20]
        Logger.debug(f'Border: orientation = {self.orientation}')

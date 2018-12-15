from pathlib import Path
from kivy.lang.builder import Builder
from kivy.logger import Logger
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty


kv_file = str(Path(__file__))[:-3] + '.kv'
Builder.load_file(kv_file)


class Border(AnchorLayout):
    # Colors
    orange = ListProperty([1, 0.8, 0.4, 1])
    blue = ListProperty([0.2, 0.8, 1, 1])
    green = ListProperty([0.2, 0.6, 0.4, 1])
    # colors = {'4': orange, '5': blue, '6': green}
    # Property to change the color
    border_color = ListProperty()
    # Numeric values
    mini = NumericProperty(4)
    maxi = NumericProperty(6)
    bands = NumericProperty()
    # Geometrical property
    orientations = ListProperty(['left', 'top', 'right', 'down'])
    orientation = StringProperty()

    def __init__(self, **kwargs):
        Logger.debug(f'Border: __init__( {kwargs} )')
        super().__init__(**kwargs)
        self.colors = {'4': self.orange, '5': self.blue, '6': self.green}
        self.change_color(0)
        self.change_orientation()
        Logger.debug('Border: initializated')

    def change_color(self, opt: int = None):
        Logger.debug(f'Border: change_color( {opt} )')
        if opt is None:
            self.bands = self.bands + 1 if self.bands < self.maxi \
                else self.mini
        else:
            self.bands = self.bands if str(self.bands) in self.colors \
                else self.mini
        self.border_color = self.colors[str(self.bands)]
        Logger.debug(f'Border: bands = {str(self.bands)}')

    def change_orientation(self, orientation: str = 'left'):
        Logger.debug(f'Boder: change_orientation( {orientation} )')
        if orientation in self.orientations:
            self.orientation = orientation
            self.border = [20, 50, 20, 20]
        Logger.debug(f'Border: orientation = {self.orientation}')

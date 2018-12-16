from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import OptionProperty, BoundedNumericProperty, DictProperty


class Ejemplo(AnchorLayout):
    opciones = OptionProperty('pene', options=['pene', 'picha'])
    elemento = BoundedNumericProperty(4, min=4, max=6)
    diccionario = DictProperty({'pene': 4, 'polla': 5})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Ejemplo: {self.property("opciones").options}')

    def esta(self, data):
        print('ESTA') if data in self.property('opciones').options else print('NO ESTA')

    def cambiado(self):
        print(f'Ejemplo: se ha cambiado elemento a {self.elemento}')


a = Ejemplo()
a.esta('pene')
a.esta('polla')
print('AYY') if 'picha' in a.diccionario else print('NO AYY')
for i in range(3):
    a.elemento += 1
    print(f'elemento = {a.elemento}')

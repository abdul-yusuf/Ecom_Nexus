from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior, FakeRectangularElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
class HomeTile(MDBoxLayout, ButtonBehavior, FakeRectangularElevationBehavior):
    pass
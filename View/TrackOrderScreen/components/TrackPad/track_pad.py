from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty, ColorProperty
class TrackPad(MDRelativeLayout):
    seprator_height = StringProperty()
    color = ColorProperty(None)
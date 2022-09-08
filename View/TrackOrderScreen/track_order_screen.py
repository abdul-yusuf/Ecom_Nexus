from View.base_screen import BaseScreenView
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from .components import TrackPad
from kivy.clock import Clock
from kivy.factory import Factory

class TrackOrderScreenView(BaseScreenView):
    def __init__(self, **kw):
        """AI is creating summary for on_enter
        """
        Clock.schedule_once(self.expansion_box, 1)
        super().__init__(**kw)

    def expansion_box(self, cl):
        # Contents = Factory.get('TrackPad')
        self.ids.expansion_box.add_widget(  
            MDExpansionPanel(
                content = MDBoxLayout(
                    TrackPad(
                        color=get_color_from_hex(colors['Green']['300']),
                    ),
                    TrackPad(
                        text='Order Confirmed',
                        secondary_text='It has been confirmed',
                        tertiary_text = 'on 28-Dec-22',
                    ),
                    TrackPad(
                        text='Ready for Delivery',
                        secondary_text='Your order is ready for shipping',
                        tertiary_text = 'on 28-Dec-22',
                    ),
                    # text: 'Out For Delivery'
                    # secondary_text: 'Your order is out fro delivery'
                    # tertiary_text: ''
                    # color: get_color_from_hex(colors['Green']['300'])
                    # seprator_height:0
                    TrackPad(
                        seprator_height = '0',
                        text='Out For Delivery',
                        secondary_text='Your order is out fro delivery',
                        tertiary_text = '',
                        ),
                    orientation= 'vertical',
                    adaptive_height = True
                ),
                panel_cls = MDExpansionPanelOneLine(text='Track')
            )
        )
        # return super().on_enter(*args)
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

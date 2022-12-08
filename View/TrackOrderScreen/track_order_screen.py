from View.base_screen import BaseScreenView
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from .components import TrackPad, CourierBox
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.metrics import dp

class TrackOrderScreenView(BaseScreenView):
    def __init__(self, **kw):
        """AI is creating summary for on_enter
        """
        print('*'*40,'starting','*'*40)
        self.track_data = {}
        self.box = CourierBox()
        # self.expansion_box_instance = None
        self.expansion_box_instance = self.expansion_box(self.track_data)

        # Clock.schedule_once(self.expansion_box, 1)
        super().__init__(**kw)

    def expansion_box(self, *args):
        # Contents = Factory.get('TrackPad')
        # track_data = data
        return MDExpansionPanel(
                content = MDBoxLayout(
                    TrackPad(
                        color=get_color_from_hex(colors['Green']['300']),
                    ),
                    TrackPad(
                        text='Order Confirmed',
                        secondary_text='It has been confirmed',
                        tertiary_text = 'on 28-Dec-22',
                        color=get_color_from_hex(colors['Green']['300']),
                    ),
                    TrackPad(
                        text='Ready for Delivery',
                        secondary_text='Your order is ready for shipping',
                        tertiary_text = 'on 28-Dec-22',
                        # color=get_color_from_hex(colors['Green']['300']),
                    ),
                    # text: 'Out For Delivery'
                    # secondary_text: 'Your order is out fro delivery'
                    # tertiary_text: ''
                    # color: get_color_from_hex(colors['Green']['300'])
                    # seprator_height:0
                    TrackPad(
                        text='Out For Delivery',
                        secondary_text='Your order is out for delivery',
                        tertiary_text = 'on 28-Dec-22',
                        # color=get_color_from_hex(colors['Green']['300']),
                        ),
                    TrackPad(
                        seprator_height = '0',
                        text='Delivered',
                        secondary_text='Your order is out for delivery',
                        tertiary_text = str(self.track_data),
                        # color=get_color_from_hex(colors['Green']['300']),
                        ),
                    orientation= 'vertical',
                    adaptive_height = True,
                    padding = [0,dp(10),0,0],
                    spacing = dp(10)
                ),
                panel_cls = MDExpansionPanelOneLine(text='Track')
            )
        
        # return super().on_enter(*args)
    def model_is_changed(self, *args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print(args,kwargs, 'from model_is_changed')
    
    def server_success(self, *args, **kwargs):
        print(args, kwargs)
        data = args[1]
        ref_code = data['order_set'][0]['ref_code']
        self.being_delivered = data['order_set'][0]['being_delivered']         

        self.ids.order_ref.text = f'Order: #{ref_code}'
        self.ids.product_title.text = '{} ({})'.format(data['product']['title'], data['quantity'])
        self.ids.product_price.text = '₦{}/kg'.format(data['product']['price'])

        self.track_data = {
            'order_place': { 
                'date': data['order_set'][0]['ordered_date'],
                'read': True
            },
            'order_confirmed': { 
                'date': data['order_set'][0]['ordered_date'],
                'read': True
            },
            'ready_for_delivery': { 
                'date': data['order_set'][0]['ordered_date'],
                'read': True
            },
            'out_for_delivery': { 
                'date': data['order_set'][0]['ordered_date'],
                'read': True
            },
            'delivered': { 
                'date': data['order_set'][0]['ordered_date'],
                'read': True
            }
        }
        # try:
        self.ids.expansion_box.remove_widget(self.expansion_box_instance)  
        self.ids.expansion_box.add_widget(self.expansion_box_instance)  
        self.ids.courier_parent_box.remove_widget(self.box)

        if self.being_delivered:
            print(self.being_delivered)
            self.ids.courier_parent_box.add_widget(self.box)
        # except:
        #     print('error removing widget')

    def server_error(self, *args, **kwargs):
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))
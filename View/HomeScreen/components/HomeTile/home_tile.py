from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import TouchBehavior, focus_behavior
from kivy.properties import StringProperty, ObjectProperty, DictProperty, NumericProperty, ColorProperty, BooleanProperty

class HomeTile(MDCard):
    # pass
    """_summary_

    Args:
        MDBoxLayout (_type_): _description_
        ButtonBehavior (_type_): _description_
    """
    bookmarked = BooleanProperty(defualtvalue=True)
    super_parent = ObjectProperty()
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.add_price_stroke()

    # def add_price_stroke(self):
    #     if self.ids.discount_price == 'null':
    #         pass
    #     else:

    # _data = DictProperty({})
    # parent = None
    # def set_data(self, data):
    #     self._data = data
    #     # print(self.data)·
    #     self.assign_data()
    #     print(self._data)

    # def assign_data(self):
    #     print('*'*15,'instance_Data','*'*15)
    #     print(self._data)
    #     print('*'*15,'instance_Data','*'*15)

    #     self.ids.title.text = self._data['title']
    #     self.ids.price.text = self._data['price']
    #     # self.ids.rate.text = '0' if self.data['rate']=='null' else self.data['rate']
    #     try:
    #         self.ids.discount_price.text = 'null' if self._data['discount_price']=='null' else self._data['discount_price']
    #     except KeyError:
    #         self.ids.discount_price.text = 'null'
    #         # pass

    # def on_press(self):
    #     # self.parent.controller.item_detail_page(self.data)
    #     # self.parent.app.onNextScreen(self.parent.name, 'item detail screen')
    #     self.parent.app.onNextScreen(
    #         self.parent.parent.parent.parent.parent.parent.name, 
    #         'item detail screen',
    #         data = {
    #             'pk': self.pk,
    #             'title': self.title,
    #             'price': self.price,
    #             'discount_price': self.discount_price,
    #             }
    #         )
    #     self.parent.model.notify_observers('item detail screen', self._data)
        
        # return super().on_touch_down(touch)
        
    # def on_long_touch(self, touch, *args):
    #     print(touch)

   
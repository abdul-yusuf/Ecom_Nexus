from View.base_screen import BaseScreenView
from .components import HomeTile, HomeAds, CartTile, FavouriteTile
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout
from kivy.clock import Clock

class HomeScreenView(BaseScreenView):
    # def __init__(self, **kw):
    #     super().__init__(**kw)
    data_1 = None

    def onTextFieldEnterKey(self, instance, key, keycode, text, modifiers):
        if self.ids.search_field.focus and keycode==40:
            self.app.onNextScreen('home screen', 'search page screen', self.ids.search_field.text)
    

    def on_pre_enter(self, *args):
        Window.bind(on_key_down=self.onTextFieldEnterKey)
        # self.controller.server_request()
        self.refresh_callback()
        data = [
                    {
                        "quantity": "1",
                        "title": "Chicken",
                        "price": "₦200.00",
                        "discount_price": "₦200.00",
                        "slug": "chicken",
                        "description": "Healthy meat for old and young",
                        "image": "/media/chicken_EkZfxgX.png"
                    },
                    {
                        "quantity": "2",
                        "title": "Cow",
                        "price": "₦14000.00",
                        "discount_price": "₦35000.00",
                        "slug": "cow",
                        "description": "Big",
                        "image": "/media/cow_ey5Ipdx.png"
                    },
                    {
                        "quantity": "1",
                        "title": "Goat",
                        "price": "₦10000.00",
                        "discount_price": "null",
                        "slug": "goat",
                        "description": "Ipuson iuio free",
                        "image": "/media/goat_8w8yMpQ.png"
                    },
                    {
                        "quantity": "1",
                        "title": "Goat",
                        "price": "₦10000.00",
                        "discount_price": "₦90000.00",
                        "slug": "goat",
                        "description": "Ipuson iuio free",
                        "image": "/media/goat_8w8yMpQ.png"
                    },
                    {
                        "quantity": "1",
                        "title": "Goat",
                        "price": "₦10000.00",
                        "discount_price": "null",
                        "slug": "goat",
                        "description": "Ipuson iuio free",
                        "image": "/media/goat_8w8yMpQ.png"
                    },
                ]
        self.ids.view_1.data = data
        self.ids.view_1.viewclass = HomeTile
        
        self.ids.view_2.data = data
        self.ids.view_2.viewclass = CartTile

        self.ids.view_3.data = data
        self.ids.view_3.viewclass = FavouriteTile
        
        # return super().on_enter(*args)

    def model_is_changed(self,*args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        # self.set_data_to_widgets()
        self.ids.view_1.refresh_from_data()


        print('-----------------home notify_observers---------------- ')
        if self.app.is_authenticated and self.app.auth_store.exists('user'):
            user_data_store = self.app.auth_store.get('user')
            self.ids.username.text = f"{user_data_store['first_name']} {user_data_store['last_name']}"
            self.ids.user_detail.text = f"{user_data_store['first_name']} {user_data_store['last_name']}"
            self.ids.user_detail.secondary_text = user_data_store['email']

    def server_success(self, *args, **kwargs):
        print('*'*50)
        self.data_1 = args[0][1]
        for item in self.data_1[:]:
            item['price'] = str(item['price'])
            # item['on_release'] = lambda x:self.app.onNextScreen(self.name, 'item detail screen')
        # print(self.data_1)
        # self.set_data_to_widgets()
        self.ids.view_1.data = self.data_1
        # Clock.schedule_once(self.ids.home_refresh_layout.refresh_done,1)

    
    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            # self.ids.view_1.clear_widgets()
            self.data_1 = {}
            self.controller.server_request()
            self.ids.view_1.refresh_done()
            # self.tick = 0

        Clock.schedule_once(refresh_callback, 1)
        # self.model.notify_observers('home screen')
    
    # def set_data_to_widgets(self):
    #     self.ids.view_1.clear_widgets()
    #     for item in self.data_1[:]:
    #         item['price'] = str(item['price']) 
    #         item['on_release'] = lambda x:self.app.onNextScreen(self.name,'item detail screen')
    #         # try:
    #         #     item['discount_price'] = str(item['discount_price']) 
    #         # except:
    #         #     pass
    #         tile = HomeTile()
    #         tile.set_data(item)
    #         self.ids.view_1.add_widget(tile)
    #         # tile.parent = self
            # tile.on_release = [lambda x:self.app.onNextScreen(self.name, 'item detail screen')]
            
            # def on_touch_down(self, touch):
            #     # self.parent.controller.item_detail_page(self.data)
            #     # self.parent.app.onNextScreen(self.parent.name, 'item detail screen')
            #     self.parent.model.notify_observers('item detail screen', self._data)
                
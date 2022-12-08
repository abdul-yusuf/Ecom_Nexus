from View.base_screen import BaseScreenView
from .components import HomeTile, HomeAds, CartTile, FavouriteTile
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout
from kivy.clock import Clock
from kivy.animation import Animation
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
        # self.app.modal_view(attach_to=self.ids.view_1)
        # self.app.modal_view(attach_to=self)
        screen_args = self.app.screen_args
        self.user_detail_populate()
        if screen_args!=[]:
            if screen_args[0]=='switch_to':
                self.ids.botton_nav.switch_tab(screen_args[1])

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
        # self.ids.view_1.data = data
        self.ids.view_1.viewclass = HomeTile
        self.ids.view_1.bind(on_scroll_start=self.update_scroll)
        # for item in data:
        #     tile = HomeTile()
        #     tile.set_data(item)
        #     self.ids.view_1.add_widget(tile)
        #     tile.controller = self.controller
            # print(item)
        # self.ids.view_2.data = data
        self.ids.view_2.viewclass = CartTile
        # self.ids.home_refresh_layout.data = data
        # self.ids.home_refresh_layout.viewclass = HomeTile
        
        # self.ids.view_2.data = data
        # self.ids.view_2.viewclass = CartTile

        # self.ids.view_3.data = data
        # self.ids.view_3.viewclass = FavouriteTile
        
        # return super().on_enter(*args)

    def server_processing(self, *args):
        self.app.modal_view(attach_to=self)
        print(args,'loading..')

    def model_is_changed(self,*args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        # self.set_data_to_widgets()
        self.ids.view_1.refresh_from_data()
        

        print('-----------------home notify_observers---------------- ')
        
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)

    def user_detail_populate(self):
        if self.app.auth_store.get('variable')['is_authenticated'] == True:
            user_data_store = self.app.auth_store.get('user')['data']
            self.ids.username.text = f"Hi {user_data_store['first_name']} {user_data_store['last_name']}"
            self.ids.user_detail.text = f"{user_data_store['first_name']} {user_data_store['last_name']}"
            self.ids.user_detail.secondary_text = user_data_store['email']

    def server_success(self, *args, **kwargs):
        print('*'*50)
        self.data_1 = args[0][1]
        
        for item in self.data_1[:]:
            item['price'] = str(item['price'])
            if item['discount_price']==None:
                item['discount_price'] = 'null'
            if item['discount_percent']==None:
                item['discount_percent'] = 'null'

            else:
                item['discount_percent'] = str(item['discount_percent'])

                item['discount_price'] = str(item['discount_price'])
            # item['on_release'] = lambda x:self.app.onNextScreen(self.name, 'item detail screen')
        # print(self.data_1)
        # self.set_data_to_widgets()
        self.ids.view_1.data = self.data_1
        # Clock.schedule_once(self.ids.home_refresh_layout.refresh_done,1)

    def server_error(self, *args, **kwargs):
        print(args)
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))

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
    
    def update_scroll(self,*args):
        perm = args[0].scroll_y
        croll = self.ids.home_refresh_layout
        # crolls = croll.scroll_y
        # print(perm)
        # print('*'*40)
        if perm>=1:
            Animation(
                scroll_y=1 if perm>=1 else perm,
                d=0.9/1
                ).start(self.ids.home_refresh_layout)
        elif perm<0.9:
            Animation(
                scroll_y=0 if perm<=0 else perm,
                d=0.7/1
                ).start(self.ids.home_refresh_layout)

    def populate_cart(self, *args, **kwargs):
        print(args, kwargs)
        # pass
        # self.ids.view_2.data  = [] 
        products = args[0][1]['products']
        products_item = []
        for items in products:
            # items['id'] = str(items['id'])
            pro = items['product']
            pro['plus_btn.on_press'] = lambda x=args[0][1]['id'], b=items['id'], c=items['quantity']:self.controller.cart_add_item(x,b,c)
            pro['minus_btn.on_press'] = lambda x=args[0][1]['id'], b=items['id'], c=items['quantity']:self.controller.cart_remove_single_item(x,b,c)
            pro['trash_btn.on_press'] = lambda x=args[0][1]['id'], b=items['id']:self.controller.cart_remove_item(x,b)

            pro['quantity'] = str(items['quantity'])
            pro['price'] = str(pro['price'])

            products_item.append(pro)
        
        print(products_item)

        products_total = args[0][1]['total']
        self.ids.products_price.text = str(products_total)
        self.ids.shipping_price = 'FREE'
        self.ids.total_all.text = str(products_total)
        self.ids.order_ref_code.text = args[0][1]['ref_code']
        self.ids.view_2.data  = products_item 
        # self.


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
                
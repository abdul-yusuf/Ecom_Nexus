from View.base_screen import BaseScreenView
from .components import HomeTile, HomeAds, CartTile, FavouriteTile
from kivy.core.window import Window
class HomeScreenView(BaseScreenView):
    def __init__(self, **kw):
        Window.bind(on_key_down=self.onTextFieldEnterKey)
        super().__init__(**kw)

    def onTextFieldEnterKey(self, instance, key, keycode, text, modifiers):
        if self.ids.search_field.focus and keycode==40:
            self.app.onNextScreen('home screen', 'search page screen', self.ids.search_field.text)
    
    def on_enter(self, *args):
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
        self.ids.home_refresh_layout.data = data
        self.ids.home_refresh_layout.viewclass = HomeTile
        
        self.ids.view_2.data = data
        self.ids.view_2.viewclass = CartTile

        self.ids.view_3.data = data
        self.ids.view_3.viewclass = FavouriteTile
        
        # return super().on_enter(*args)

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

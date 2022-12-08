from View.base_screen import BaseScreenView
# from kivy.modules from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.utils import platform

if platform=='android':
    from .components import WebView




class CheckoutScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def create_webview(self, *args, authorization=None, **kwargs):
        print(authorization)
        
        print('*'*50)
        print(args,kwargs)
        print('*'*50)

        if self.ids.chk1.active:
            if platform=='android':
                self.browser = WebView(authorization,
                    enable_javascript = True,
                    enable_downloads = False,
                    enable_zoom = False
                    )

    def populate_cart(self, *args, **kwargs):
        print(args, kwargs)
        # pass
        try:
            products = args[0][1]['products']
            products_item = []
        except KeyError as e:
            self.app.create_toast(f'Run into a Problem: {e}')

        # for items in products:
        #     # items['id'] = str(items['id'])
        #     pro = items['product']
        #     pro['plus_btn.on_press'] = lambda x=args[0][1]['id'], b=items['id'], c=items['quantity']:self.controller.cart_add_item(x,b,c)
        #     pro['minus_btn.on_press'] = lambda x=args[0][1]['id'], b=items['id'], c=items['quantity']:self.controller.cart_remove_single_item(x,b,c)
        #     pro['trash_btn.on_press'] = lambda x=args[0][1]['id'], b=items['id']:self.controller.cart_remove_item(x,b)

        #     pro['quantity'] = str(items['quantity'])
        #     pro['price'] = str(pro['price'])

            # products_item.append(pro)

    def server_failed(self, *args, **kwargs):
        print(args, kwargs)
        self.app.create_toast(str(args[0][1]))
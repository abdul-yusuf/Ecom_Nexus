from View.base_screen import BaseScreenView
# from kivy.modules from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.utils import platform

if platform=='android':
    from .components import WebView
    # from kvdroid.tools.sms import get_all_sms


    # from kvdroid.jclass.android.webkit import CookieManager
    # print(get_all_sms())
    # def get_cookies(site_name: str):
    #     cookieManager = CookieManager().getInstance()
    #     return cookieManager.getCookie(site_name)


    # def launch_url(url: str, color="#FFFFFF", color_scheme="system"):
    #     from kvdroid.jclass.android.graphics import Color
    #     from kvdroid.jclass.androidx.browser.customtabs import CustomTabColorSchemeParamsBuilder
    #     from kvdroid.jclass.androidx.browser.customtabs import CustomTabsIntentBuilder, CustomTabsIntent
    #     from kvdroid import activity
    #     from kvdroid.jclass.android.net import Uri
    #     CustomTabsIntent = CustomTabsIntent()
    #     schemes = {
    #         "system": CustomTabsIntent.COLOR_SCHEME_SYSTEM,
    #         "light": CustomTabsIntent.COLOR_SCHEME_LIGHT,
    #         "dark": CustomTabsIntent.COLOR_SCHEME_DARK
    #     }
    #     color_int = Color().parseColor(color)
    #     default_color = CustomTabColorSchemeParamsBuilder(instantiate=True).setToolbarColor(color_int).build()
    #     builder = CustomTabsIntentBuilder(instantiate=True)
    #     if color_scheme not in schemes:
    #         builder.setColorScheme(CustomTabsIntent.COLOR_SCHEME_SYSTEM)
    #     else:
    #         builder.setColorScheme(schemes[color_scheme])
    #     builder.setDefaultColorSchemeParams(default_color)
    #     custom_tabs_intent = builder.build()
    #     custom_tabs_intent.intent.setPackage("com.android.chrome")
    #     custom_tabs_intent.launchUrl(activity, Uri().parse(url))
    #     return custom_tabs_intent



class CheckoutScreenView(BaseScreenView):

    def model_is_changed(self, *args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print(args, kwargs)

        if self.app.modal_webview or self.browser==None:
            print(self.browser,'%'*40)
            self.controller.payment_verify_server_request(self.ids.order_ref_code.text)
            self.app.modal_webview = False
            # self.app.onNextScreen(self.name, 'order complete screen')
    
    def _check(self):
        if self.ids.chk1.active or self.ids.chk2.active:
            self.controller.payment_server_request(
                    'O' if self.ids.chk1.active else 'D',
                    self.ids.order_ref_code.text
                    )
        else:
            self.app.create_toast('please select Payment Method')


    def on_enter(self):
        
        try:
            self.ids.total.text = self.app.screen_args[0]['price']
            self.ids.price.text = self.app.screen_args[0]['quantity']
            self.ids.order_ref_code.text = self.app.screen_args[0]['ref_code']
        except (KeyError, Exception, IndexError) as e:
            self.app.create_toast(str(e))

        # from kvdroid.tools.notification import create_notification
        # from kvdroid.jclass.android import Color 
        # from kvdroid.tools import get_resource 
        # create_notification(
        #     small_icon=get_resource('drawable').ic_kvdroid, 
        #     channel_id ='1', title='KvDroid',
        #     text='hello from kvdroid androidx notification', 
        #     ids=1, 
        #     channel_name='ch1', 
        #     large_icon='assets/image/icon.png', 
        #     big_picture='assets/image/icon.png', 
        #     action_title1='CLICK', 
        #     action_title2='PRESS', 
        #     reply_title='REPLY', 
        #     set_reply=True, 
        #     expandable=True, 
        #     set_large_icon=True, 
        #     add_action_button1=True, 
        #     add_action_button2=True, 
        #     small_icon_color=Color().parseColor('#2962FF'))



    def create_webview(self, *args, authorization=None, **kwargs):
        print(authorization)
        
        print('*'*50)
        print(args,kwargs)
        print('*'*50)

        if self.ids.chk1.active:
            if platform=='android' and authorization!='':
                from kvdroid.tools.webkit import launch_url
                self.browser = launch_url(authorization)
                self.app.modal_webview = True
                print(self.browser)
                # self.browser = WebView(authorization,
                #     enable_javascript = True,
                #     enable_downloads = False,
                #     enable_zoom = False
                #     )

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
        # print(args, kwargs)
        self.app.create_toast(str(args[0][1]))

    def server_error(self, *args, **kwargs):
        # print(args, kwargs)
        self.app.create_toast(str(args[0][1]))



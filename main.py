
"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

# import importlib
# import os

# # from kivy import Config

# # from PIL import ImageGrab

# # # TODO: You may know an easier way to get the size of a computer display.
# # resolution = ImageGrab.grab().size
# # print(resolution)
# # # Change the values of the application window size as you need.
# # Config.set("graphics", "height", "800")
# # Config.set("graphics", "width", "360")

# from kivy.core.window import Window

# # # Place the application window on the right side of the computer screen.
# # Window.top = 0
# # Window.left = resolution[0] - Window.width

# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager


# #new imports
# from kivy.uix.modalview import ModalView
# from kivy.uix.label import Label
# from kivy.metrics import dp
# from kivymd.toast.kivytoast import toast 
# from kivymd.uix.spinner.spinner import MDSpinner
# from kivy.storage.jsonstore import JsonStore

# class UrlMaker:
#     def __init__(self, dict) -> None:
#         self.dict = dict

#     def route(self, route):
#         url = self.dict['host']+self.dict[route]['url']
#         return url
#     def method(self, route):
#         return self.dict[route]['method']

# class Ecom_Nexus(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]

#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """

#         import View.screens
#         self.theme_cls.primary_palette = "Blue"
#         self.manager_screen = MDScreenManager()
#         self.list_of_prev_screen = []
#         #new variables
#         self.is_modal_open = False
#         self.modal_instance = None
#         self.auth_store = JsonStore('auth.json')
#         self.url_store = JsonStore('url.json')
#         self.request_parm = UrlMaker(self.url_store)
#         self.is_authenticated = False
#         self.screen_args = []

#         Window.bind(on_key_down=self.on_keyboard_down)
#         Window.bind(on_key_down=self.onBackBtn)
#         importlib.reload(View.screens)
#         screen = View.screens.screen
#         for i, name_screen in enumerate(screen.keys()):
#             model = screen[name_screen]["model"]()
#             controller = screen[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screen = self.manager_screen
#             view.name = name_screen
#             self.manager_screen.add_widget(view)
            
#         return self.manager_screen

#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.

#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """

#         if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#             self.rebuild()

#     def change_theme(self, icon):
#         if icon == 'moon-waning-crescent':
#             self.theme_cls.theme_style = 'Dark'
#         else:
#             self.theme_cls.theme_style = 'Light'


#     def onNextScreen(self,btn,next_screen,*args):
#         print(btn)
#         self.list_of_prev_screen.append(btn)
#         self.screen_args = [*args]
#         print(self.screen_args)
#         self.manager_screen.current = next_screen

#     def onBackBtnx(self):
#         if self.list_of_prev_screen:
#             self.manager_screen.current = self.list_of_prev_screen.pop()
#             return True
#         return False

#     def onBackBtn(self,window,key,*args):
#         if key == 27 :
#             if self.is_modal_open:
#                 self.modal_instance.dismiss()
#                 self.is_modal_open = False
#                 return True
#             elif self.list_of_prev_screen:
#                 self.manager_screen.current = self.list_of_prev_screen.pop()
#                 return True
#         else:
#             return False
    
#     def modal_view(self, open=True, auto_dismiss=False, attach_to=None, **kwargs):
#         """_summary_

#         Args:
#             open (bool, optional): _description_. Defaults to True.
#             auto_dismiss (bool, optional): _description_. Defaults to False.
#             attach_to (_type_, optional): _description_. Defaults to None.
#         """
            
#         spinner = MDSpinner(determinate=False, determinate_time=5, size_hint=(None, None), size=(dp(42),dp(42)), pos_hint={'center_x': .5, 'center_y': .5})
#         view = ModalView(
#                         size_hint=(None, None), 
#                         auto_dismiss=auto_dismiss, 
#                         size=(dp(90), dp(90)), 
#                         attach_to=None, 
#                         background_color='#ffffff',
#                         # radius=dp(3)
#                         )
#         view.add_widget(spinner)
        
#         # def close_modal():
#         #     view.dismiss()
#         #     self.is_modal_open = False
#         # view.auto_dismiss(auto_dismis) 
#         # spinner.on_determinate_complete(view.dismiss())

#         if open:
#             if self.is_modal_open:
#                 view.dismiss()
#             view.open()
#             self.is_modal_open = True
#         else:
#             view.dismiss()
#             self.is_modal_open = False
#         print(self.is_modal_open)
#         self.modal_instance = view
         
#     def create_toast(self, *args, **kwargs):
#         toast(args[0])

#     def perform_store_save(self, *args, **kwargs):
#         """_summary_
#         Args
#             data(_type_,): data to save
#         Kwargs
#             store_name(str, required):
#             key(str, required)
#         """
#         store_name = kwargs.pop('store_name')
#         key = kwargs.pop('key')
#         print(args, kwargs)
#         if store_name=='auth_store':
#             # self.auth_store.put(key, data=kwargs)
#             self.auth_store[key]=args[0]
#         print(f'what was saved {self.auth_store.get(key)}')

        
        

# Ecom_Nexus().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
# import certifi
# import os

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from View.screens import screen

#new imports
from kivy.utils import platform
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.metrics import dp
from kivymd.uix.spinner.spinner import MDSpinner
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.lang import Builder

from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from threading import Thread
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput

if platform=='android':
    from kvdroid.tools import toast
    from kvdroid import activity

    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
else:
    from kivymd.toast.kivytoast import toast 



# os.environ['SSL_CERT_FILE'] = certifi.where()

KV = """
Screen:
    MDCarousel:
        # md_bg_color: app.theme_cls.bg_normal
        # on_slide_progress: app.generate_application_screen()
        canvas:
            Color:
                rgba: rgba(255, 255, 255, 255)
        
            Rectangle:
                size: self.size[0], self.size[1]
                pos: self.pos

        MDRelativeLayout:
            Image:
                source: "assets/images/groci3.gif"
                allow_stretch:
                size_hint: .7,.7
                pos_hint: {'center_x': 0.5,'center_y': 0.7}
            MDLabel:
                adaptive_width: True
                size_hint_x: .7
                text: 'lorem ipsum hestum tesuni petsun gibson drenbe'
                pos_hint: {'center_x': 0.5,'center_y': 0.4}
                halign: 'center'
                theme_text_color: 'Custom'
                text_color: get_color_from_hex(colors['Blue']['800'])#rgba(26,24,58,0)
                opposite_color: True
            MDTextButton:
                text: 'Skip'
                pos_hint: {'center_x':.85,'center_y':.93}
                theme_text_color: 'Custom'
                text_color: get_color_from_hex(colors['Blue']['800'])#rgba(26,24,58,0)
                on_release: app.onNextScreen('','home screen')

            MDTextButton:
                text: 'Next'
                pos_hint: {'center_x':.85,'center_y':.05}
                on_press: self.parent.parent.parent.load_next(mode='next')
                theme_text_color: 'Custom'
                text_color: get_color_from_hex(colors['Blue']['800'])#rgba(26,24,58,0)
        MDRelativeLayout:
            Image:
                source: "assets/images/groci4.png"
                allow_stretch:
                size_hint: .7,.7
                pos_hint: {'center_x': 0.5,'center_y': 0.7}

            MDRaisedButton:
                text: 'GET STARTED'
                rounded_button: False
                pos_hint: {'center_x': 0.5,'center_y': 0.2}
                size_hint: .8,.06
                on_release: app.onNextScreen('','home screen')

<GenTextField>:

<SecGenTextInput>:

"""

class UrlMaker:
    def __init__(self, dict) -> None:
        self.dict = dict

    def route(self, route):
        url = self.dict['host']+self.dict[route]['url']
        return url
    def method(self, route):
        return self.dict[route]['method']


class GenTextField(MDTextField):
    def on_focus(self, *args):
        if platform=='android':
            from android.runnable import run_on_ui_thread
            print(args)

            @run_on_ui_thread
            def fix():
                activity.onWindowFocusChanged(False) 
                activity.onWindowFocusChanged(True) 
            if not args[1]:
                fix()

class SecGenTextInput(TextInput):
    def on_focus(self, *args):
        if platform=='android':
            from android.runnable import run_on_ui_thread
            print(args)

            @run_on_ui_thread
            def fix():
                activity.onWindowFocusChanged(False) 
                activity.onWindowFocusChanged(True) 
            if not args[1]:
                fix()


class Ecom_Nexus(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screen of your
        # application.
        self.manager_screen = MDScreenManager()

        

        
        # self._trigger_screens = Clock.create_trigger(self.generate_application_screen)
        # Clock.schedule_once(self.generate_application_screen, -1)

    def dark_mode(self):
        from kvdroid.jclass.android import Configuration
        Configuration = Configuration()


        night_mode_flag = activity.getContext().getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK

        if night_mode_flag == Configuration.UI_MODE_NIGHT_YES:
            self.theme_cls.theme_style = 'Dark'
            print(night_mode_flag)
        else:
            print(night_mode_flag)
            self.theme_cls.theme_style = 'Light' #'Dark'


    def build(self) -> MDScreenManager:
        print('stated building')
        if platform=='android':
            self.dark_mode()
            print('checking dark mode')

            # from android.permissions import Permission, request_permissions  # NOQA
            # request_permissions(
            #     [
            #     # Permission.READ_EXTERNAL_STORAGE,
            #     #  Permission.WRITE_EXTERNAL_STORAGE,
            #     #  Permission.CALL_PHONE,
            #     #  Permission.CALL_PRIVILEGED,
            #     #  Permission.READ_CONTACTS,
            #     #  Permission.WRITE_CONTACTS,
            #      Permission.READ_SMS,
            #     #  Permission.WRITE_CALL_LOG,
            #     #  Permission.READ_CALL_LOG
            #      ]
            # )
        else:
            print('Not an Android Device')
            self.theme_cls.theme_style = 'Light' #'Dark'
        self.theme_cls.primary_palette = "Blue"
        self.list_of_prev_screen = []
        self.on_boarding_screen = Builder.load_string(KV)
        # Clock.schedule_once(self.generate_application_screen,20)
        # Window.bind(on_start=self._trigger_screens)
        print('stated building variables')

        #new variables
        self.screen_args = []
        self.modal_webview = False
        self.is_modal_open = False
        self.modal_instance = None
        self.auth_store = JsonStore('auth.json')
        self.url_store = JsonStore('url.json')
        self.request_parm = UrlMaker(self.url_store)
        self.is_authenticated = False
        self.loaded_screens = []
        print('stated building home screen')
        
        # model = HomeScreenModel()
        # controller = HomeScreenController(model)
        # view = controller.get_view()
        # view.manager_screen = self.manager_screen
        # view.name = 'home screen'
        # self.manager_screen.add_widget(view)
        # self.manager_screen.add_widget(self.on_boarding_screen)
        self.onNextScreen('','home screen')
        
        print('stated binfing')
        # self.generate_application_screen()
        Window.bind(on_key_down=self.onBackBtn)
        # print('stated building ')

        # Thread(target=self.generate_application_screen).start()
        # Clock.schedule_once(self.modal_view,2)
        return self.manager_screen

    # def call_screens(self):
    #     Clock.schedule_once(self.generate_application_screen, 8)

    def generate_application_screen(self,*args, **kwargs) -> None:
        """
        Creating and adding screen to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screen.py` module and
        see how new screen are added according to the given application
        architecture.
        """
        self.modal_view(attach_to=self)
        print('*'*30,'generating','*'*30)
        print(kwargs)

        # for i, name_screen in enumerate(screen.keys()):
            # model = screen[name_screen]["model"]()
            # controller = screen[name_screen]["controller"](model)
            # view = controller.get_view()
            # view.manager_screen = self.manager_screen
            # view.name = name_screen
            # self.manager_screen.add_widget(view)

        model = screen[kwargs['name_screen']]["model"]()
        controller = screen[kwargs['name_screen']]["controller"](model)
        view = controller.get_view()
        view.manager_screen = self.manager_screen
        view.name = kwargs['name_screen']
        self.manager_screen.add_widget(view)
        self.loaded_screens.append(view.name)



        print('*'*30,'end generating','*'*30)

        # self.modal_instance.dismiss()
        Clock.schedule_once(self.modal_instance.dismiss, 3)


    def change_theme(self, icon):
        if icon == 'moon-waning-crescent':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'


    def onNextScreen(self,btn:str,next_screen:str,*args):
                
        print(btn)
        if btn!='':
            self.list_of_prev_screen.append(btn)
        if next_screen in self.loaded_screens:
            pass
        else:
            self.generate_application_screen(name_screen=next_screen) 
        self.screen_args = [*args]
        print(self.screen_args)
        self.manager_screen.current = next_screen

    def onBackBtnx(self):
        if self.list_of_prev_screen:
            self.manager_screen.current = self.list_of_prev_screen.pop()
            if self.modal_webview:
                self.manager_screen.current_screen.model.notify_observers('checkout screen')
                return True
            return True
        return False

    def onBackBtn(self,window,key,*args):
        if key == 27 :
            if self.list_of_prev_screen:
                self.manager_screen.current = self.list_of_prev_screen.pop()
                if self.modal_webview:
                    self.manager_screen.current_screen.model.notify_observers('checkout screen')
                    return True
                return True

            else:
                return False
        else:
            # self.rebuild()
            return False

    def modal_view(self, open=True, auto_dismiss=False, attach_to=None, **kwargs):
        """_summary_

        Args:
            open (bool, optional): _description_. Defaults to True.
            auto_dismiss (bool, optional): _description_. Defaults to False.
            attach_to (_type_, optional): _description_. Defaults to None.
        """
            
        spinner = MDSpinner(determinate=False, determinate_time=5, size_hint=(None, None), size=(dp(42),dp(42)), pos_hint={'center_x': .5, 'center_y': .5})
        view = ModalView(
                        size_hint=(None, None), 
                        auto_dismiss=auto_dismiss, 
                        size=(dp(90), dp(90)), 
                        attach_to=None, 
                        background_color='#ffffff',
                        # radius=dp(3)
                        )
        view.add_widget(spinner)
        
        # def close_modal():
        #     view.dismiss()
        #     self.is_modal_open = False
        # view.auto_dismiss(auto_dismis) 
        # spinner.on_determinate_complete(view.dismiss())

        if open:
            if self.is_modal_open:
                view.dismiss()
            view.open()
            self.is_modal_open = True
        else:
            view.dismiss()
            self.is_modal_open = False
        print(self.is_modal_open)
        self.modal_instance = view
         
    def create_toast(self, *args, **kwargs):
        toast(args[0])

    def perform_store_save(self, *args, **kwargs):
        """_summary_
        Args
            data(_type_,): data to save key
        Kwargs
            store_name(str, required):
            key(str, required)
        """
        # store_name = kwargs.pop('store_name')
        # key = kwargs.pop('key')
        print(args, kwargs)
        if args[0]=='auth_store':
            self.auth_store.put(args[1], **kwargs)
            # self.auth_store[key]=args[0]
        print(f'what was saved {self.auth_store.get(args[1])}')

        
    
Ecom_Nexus().run()

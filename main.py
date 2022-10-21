
"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

# import importlib
# import os

# from kivy import Config

# from PIL import ImageGrab

# # TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size

# # Change the values of the application window size as you need.
# Config.set("graphics", "height", resolution[1])
# Config.set("graphics", "width", "400")

# from kivy.core.window import Window

# # Place the application window on the right side of the computer screen.
# Window.top = 0
# Window.left = resolution[0] - Window.width

# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager


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
#             if self.list_of_prev_screen:
#                 self.manager_screen.current = self.list_of_prev_screen.pop()
#                 return True
#         else:
#             return False
    


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

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window
from View.screens import screen


class Ecom_Nexus(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screen of your
        # application.
        self.manager_screen = MDScreenManager()
        
    def build(self) -> MDScreenManager:
        self.theme_cls.primary_palette = "Blue"
        self.list_of_prev_screen = []
        Window.bind(on_key_down=self.onBackBtn)
        self.generate_application_screen()
        return self.manager_screen

    def generate_application_screen(self) -> None:
        """
        Creating and adding screen to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screen.py` module and
        see how new screen are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screen.keys()):
            model = screen[name_screen]["model"]()
            controller = screen[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screen = self.manager_screen
            view.name = name_screen
            self.manager_screen.add_widget(view)

    def onNextScreen(self,btn,next_screen,*args):
        print(btn)
        self.list_of_prev_screen.append(btn)
        self.screen_args = [*args]
        print(self.screen_args)
        self.manager_screen.current = next_screen

    def onBackBtnx(self):
        if self.list_of_prev_screen:
            self.manager_screen.current = self.list_of_prev_screen.pop()
            return True
        return False

    def onBackBtn(self,window,key,*args):
        if key == 27 :
            if self.list_of_prev_screen:
                self.manager_screen.current = self.list_of_prev_screen.pop()
                return True
        else:
            return False
    
Ecom_Nexus().run()

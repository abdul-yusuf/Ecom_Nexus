from Model.base_model import BaseScreenModel
from kivy.clock import Clock
from functools import partial

class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.home_screen.HomeScreen.HomeScreenView` class.
    """

    def server_success(self, *args, **kwargs):
        self.notify_observers('home screen',args, meths='success')
        # Clock.create_trigger(partial(self.notify_observers,'home screen', args, meths='success'))
        # print(args,dir(args),kwargs)

    
    def server_error(self, *args, **kwargs):
        # print(args, kwargs)
        # self.notify_observers('login screen', *args, meths='error')
        print(args,kwargs)

    def server_success_user(self, *args, **kwargs):
        print(args,kwargs)
        
        #  self.notify_observers('login screen', *args, **kwargs)
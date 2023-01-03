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

    
    

    def server_success_user(self, *args, **kwargs):
        print(args,kwargs)

    def cart_success(self, *args, **kwargs):
        self.notify_observers('home screen', args, meths='cart_success')
        print(args, kwargs)
    
    # def cart_error(self, *args, **kwargs):
    #     print(args, kwargs)
    #     self.notify_observers('home scren', args, meths='error')

    def server_error(self, *args, **kwargs):
        self.notify_observers('home screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('home screen', args, meths='failed')
        

    def product_added(self, *args, **kwargs):
        print(args,kwargs)
    
    def categories_success(self, *args, **kwargs):
        # print(args,kwargs)
        self.notify_observers('home screen', args, meths='categories')
    
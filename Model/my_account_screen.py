from Model.base_model import BaseScreenModel


class MyAccountScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.my_account_screen.MyAccountScreen.MyAccountScreenView` class.
    """


    def server_success(self, *args, **kwargs):
        self.notify_observers('my account screen', args, meths='success')
        # print(args,dir(args),kwargs)

    def server_error(self, *args, **kwargs):
        self.notify_observers('my account screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('my account screen', args, meths='failed')
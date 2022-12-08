from Model.base_model import BaseScreenModel


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
    """

    def server_success(self, *args, **kwargs):
        self.notify_observers('login screen', args, meths='success')
        # print(args,dir(args),kwargs)

    def server_error(self, *args, **kwargs):
        self.notify_observers('login screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('login screen', args, meths='failed')

    def server_success_user(self, *args, **kwargs):
        self.notify_observers('login screen', *args, **kwargs)


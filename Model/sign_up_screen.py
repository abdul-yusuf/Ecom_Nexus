from Model.base_model import BaseScreenModel


class SignUpScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.sign_up_screen.SignUpScreen.SignUpScreenView` class.
    """

    def server_success(self, *args, **kwargs):
        self.notify_observers('sign up screen', args, meths='success')
        
        # print(args,dir(args),kwargs)

    
    def server_error(self, *args, **kwargs):
        # print(args, kwargs)
        self.notify_observers('sign up screen', *args, meths='error')
        # print(args,kwargs)

    def server_success_user(self, *args, **kwargs):
        self.notify_observers('sign up screen', *args, **kwargs)
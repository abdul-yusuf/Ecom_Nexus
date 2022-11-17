import importlib

import View.EmailVerificationScreen.email_verification_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.EmailVerificationScreen.email_verification_screen)



class EmailVerificationScreenController:
    """
    The `EmailVerificationScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.email_verification_screen.EmailVerificationScreenModel
        self.view = View.EmailVerificationScreen.email_verification_screen.EmailVerificationScreenView(controller=self, model=self.model)

    def get_view(self) -> View.EmailVerificationScreen.email_verification_screen:
        return self.view
    
    def email_confirm(self, value):
        print(value)
        self.view.app.onNextScreen(self.view.name, 'profile detail screen')

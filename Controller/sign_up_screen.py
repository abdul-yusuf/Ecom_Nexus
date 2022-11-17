import importlib

from json import dumps
from kivy.network.urlrequest import UrlRequest
import View.SignUpScreen.sign_up_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SignUpScreen.sign_up_screen)




class SignUpScreenController:
    """
    The `SignUpScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.sign_up_screen.SignUpScreenModel
        self.view = View.SignUpScreen.sign_up_screen.SignUpScreenView(controller=self, model=self.model)

    def get_view(self) -> View.SignUpScreen.sign_up_screen:
        return self.view

    def server_request(self, *args, link=None, **kwargs):
        self.model.notify_observers('sign up screen', args, meths='loading')
        print('passed')
        """
            password: required
            
            {
            "password": "est esse eu sed",
            "username": "Lor",
            "email": "v5mvQdg@uWcxDghEsWPN.rxtl"
            }
        """

        if link==None:
            payload = dumps({
                "username": args[0],
                "email": args[1],
                "password": args[2],
                # "returnSecureToken": True,
            })
        else:
            payload = dumps({
                "username": args[0],
                # "email": args[1],
                "password": args[2],
                # "returnSecureToken": True,
            })
        
        headers = {
			'Content-type': 'application/json',
		}
        # self.view.app.modal_view(attach_to=self.view)
        if link==None:
            url = self.view.app.request_parm.route('register')
        else:
            url = self.view.app.request_parm.route('login')

        print(url)
        req = UrlRequest(url, on_success=self.model.server_success, req_body=payload,
						 on_error=self.model.server_error, req_headers=headers, on_failure=self.model.server_error)

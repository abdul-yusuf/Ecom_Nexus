import importlib
from json import dumps
from kivy.network.urlrequest import UrlRequest


import View.LoginScreen.login_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.LoginScreen.login_screen)




class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = View.LoginScreen.login_screen.LoginScreenView(controller=self, model=self.model)

    def get_view(self) -> View.LoginScreen.login_screen:
        return self.view

    def server_request(self, *args, **kwargs):
        self.model.notify_observers('login screen', meths='loading')
        print('passed')
        """
            password: required
            
            {
            "password": "est esse eu sed",
            "username": "Lor",
            "email": "v5mvQdg@uWcxDghEsWPN.rxtl"
            }
        """

        payload = dumps({
			"username": kwargs['username'],
			"password": kwargs['password'],
			"returnSecureToken": True,
		})
        
        headers = {
			'Content-type': 'application/json',
		}
        # self.view.app.modal_view(attach_to=self.view)
        url = self.view.app.request_parm.route('login')
        print(url)
        req = UrlRequest(
                        url, 
                        on_success=self.model.server_success, 
                        req_body=payload,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                        )

    def fetch_user_data(self, headers):
        """_summary_

        Args:
            headers (_type_): _description_
        """
        url = self.view.app.request_parm.route('user_detail')
        method = self.view.app.request_parm.method('user_detail')['GET']
        print(url,method,headers)
        req = UrlRequest(
                        url, 
                        on_success=self.model.server_success_user, 
                        method=method,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                        )


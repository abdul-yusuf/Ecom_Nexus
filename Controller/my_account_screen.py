import importlib
from json import dumps
from kivy.network.urlrequest import UrlRequest


import View.MyAccountScreen.my_account_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MyAccountScreen.my_account_screen)




class MyAccountScreenController:
    """
    The `MyAccountScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.my_account_screen.MyAccountScreenModel
        self.view = View.MyAccountScreen.my_account_screen.MyAccountScreenView(controller=self, model=self.model)

    def get_view(self) -> View.MyAccountScreen.my_account_screen:
        return self.view

    def server_request(self):
        self.model.notify_observers('home screen', meths='loading')

        url = self.view.app.request_parm.route('user_detail')
        method = self.view.app.request_parm.method('user_detail')['GET']
        headers = self.view.app.auth_store['headers']['data']
        print(url,method,headers)
        req = UrlRequest(url, on_success=self.model.server_success, method=method,
						 on_error=self.model.server_error, 
                         req_headers=headers, 
                         on_failure=self.model.server_failed)

    def user_update_request(self, data):
        self.model.notify_observers('home screen', meths='loading')

        payload = dumps(data)

        url = self.view.app.request_parm.route('user_detail')
        method = self.view.app.request_parm.method('user_detail')['PATCH']
        headers = self.view.app.auth_store['headers']['data']
        print(url,method,headers)
        req = UrlRequest(url, on_success=self.model.server_success, 
                        method=method,
                        req_body=payload,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed)
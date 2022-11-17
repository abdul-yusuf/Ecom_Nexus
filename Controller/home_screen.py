import importlib
from json import dumps
from kivy.network.urlrequest import UrlRequest

import View.HomeScreen.home_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.HomeScreen.home_screen)




class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = View.HomeScreen.home_screen.HomeScreenView(controller=self, model=self.model)

    def get_view(self) -> View.HomeScreen.home_screen:
        return self.view

    def server_request(self, *args, **kwargs):
        # self.model.notify_observers('login screen', meths='loading')
       
        # payload = dumps({
		# 	"username": kwargs['username'],
		# 	"password": kwargs['password'],
		# 	"returnSecureToken": True,
		# })
        
        headers = {
			'Content-type': 'application/json',
		}
        # self.view.app.modal_view(attach_to=self.view)
        url = self.view.app.request_parm.route('products')
        print(url)
        req = UrlRequest(url, 
                        on_success=self.model.server_success, 
                        # req_body=payload,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_error
                        )

    def item_detail_page(self, data):
        self.get_view.app.onNextScreen(self.view.name, 'item detail screen')
        self.model.notify_observers('item detail screen', data)
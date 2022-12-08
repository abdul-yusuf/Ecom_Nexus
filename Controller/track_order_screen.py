import importlib
from json import dumps
from kivy.network.urlrequest import UrlRequest

import View.TrackOrderScreen.track_order_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.TrackOrderScreen.track_order_screen)




class TrackOrderScreenController:
    """
    The `TrackOrderScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.track_order_screen.TrackOrderScreenModel
        self.view = View.TrackOrderScreen.track_order_screen.TrackOrderScreenView(controller=self, model=self.model)

    def get_view(self) -> View.TrackOrderScreen.track_order_screen:
        return self.view

    def server_request(self, product_id):
        # self.model.notify_observers('home screen', meths='loading')

        url = self.view.app.request_parm.route('ordered_item_list')+product_id+'/'
        method = self.view.app.request_parm.method('ordered_item_list')
        headers = self.view.app.auth_store['headers']['data']
        print(url,method,headers)
        req = UrlRequest(
                        url, 
                        on_success=self.model.server_success, 
                        method=method,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                        )


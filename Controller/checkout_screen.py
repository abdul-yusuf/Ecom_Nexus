import importlib
from json import dumps
from kivy.network.urlrequest import UrlRequest

import View.CheckoutScreen.checkout_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.CheckoutScreen.checkout_screen)




class CheckoutScreenController:
    """
    The `CheckoutScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.checkout_screen.CheckoutScreenModel
        self.view = View.CheckoutScreen.checkout_screen.CheckoutScreenView(controller=self, model=self.model)

    def get_view(self) -> View.CheckoutScreen.checkout_screen:
        return self.view

    def cart_server_request(self):
        url = self.view.app.request_parm.route('order')
        method = self.view.app.request_parm.method('order')
        headers = self.view.app.auth_store['headers']['data']
        print(url,method,headers)
        req = UrlRequest(url, on_success=self.model.cart_success, method=method,
						 on_error=self.model.server_error, 
                         req_headers=headers, 
                         on_failure=self.model.server_failed)

    def payment_server_request(self, payment_option:str, ref_code:str):
        url = self.view.app.request_parm.route('payment')
        method = self.view.app.request_parm.method('payment')
        headers = self.view.app.auth_store['headers']['data']
        payload = dumps({
            'ref_id': ref_code,
            'option': payment_option
        })
        print(payload)
        print(url,method,headers)
        req = UrlRequest(url, on_success=self.model.payment_success, method=method,
						 on_error=self.model.server_error,
                         req_body=payload, 
                         req_headers=headers, 
                         on_failure=self.model.server_failed)


    def payment_verify_server_request(self, ref_code:str):
        url = self.view.app.request_parm.route('verify-payment')
        method = self.view.app.request_parm.method('verify-payment')
        headers = self.view.app.auth_store['headers']['data']
        
        print(url,method,headers)
        req = UrlRequest(url+ref_code+'/', 
                        on_success=self.model.payment_success, method=method,
                        on_error=self.model.server_error,
                        #  req_body=payload, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed)
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
                        on_failure=self.model.server_failed
                        )

    def cart_server_request(self):
        self.model.notify_observers('home screen', meths='loading')

        url = self.view.app.request_parm.route('order')
        method = self.view.app.request_parm.method('order')
        headers = self.view.app.auth_store['headers']['data']
        print(url,method,headers)
        req = UrlRequest(url, on_success=self.model.cart_success, method=method,
						 on_error=self.model.server_error, 
                         req_headers=headers, 
                         on_failure=self.model.server_failed)

    def cart_remove_item(self, order_pk:str, item_pk:str):
        parent_url = self.view.app.request_parm.route('order')
        url = '/item/'
        method = self.view.app.request_parm.method('item')['DELETE']
        headers = self.view.app.auth_store['headers']['data']
        print(order_pk,url,method,headers)
        req = UrlRequest(
                        parent_url+str(order_pk)+url+str(item_pk)+'/', 
                        on_success=self.model.cart_success, 
                        method=method,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                        )

    def cart_add_item(self, order_pk, item_pk, value):
        parent_url = self.view.app.request_parm.route('order')
        url = '/item/'
        method = self.view.app.request_parm.method('item')['PATCH']
        headers = self.view.app.auth_store['headers']['data']
        value += 1
        payload = dumps({
                    "quantity": value
                })
        print(url,method,headers)
        req = UrlRequest(
                        parent_url+str(order_pk)+url+str(item_pk)+'/', 
                        on_success=self.model.cart_success, 
                        method=method,
                        on_error=self.model.server_error, 
                        req_body=payload,
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                        )

    def cart_remove_single_item(self, order_pk, item_pk, value:int):
        parent_url = self.view.app.request_parm.route('order')
        url = '/item/'
        method = self.view.app.request_parm.method('item')['PATCH']
        headers = self.view.app.auth_store['headers']['data']
        value -= 1
        # print('>'*15,value)
        if value==0:
            self.cart_remove_item(order_pk, item_pk)
            return
        payload = dumps({
                    "quantity": value
                })
        print(url,method,headers)
        req = UrlRequest(
                        parent_url+str(order_pk)+url+str(item_pk)+'/', 
                        on_success=self.model.cart_success, 
                        method=method,
                        on_error=self.model.server_error,
                        req_body=payload, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                        )

    def item_detail_page(self, data):
        self.get_view.app.onNextScreen(self.view.name, 'item detail screen')
        self.model.notify_observers('item detail screen', data)

    def home_add_to_cart(self, id):
        print(id)
        url = self.view.app.request_parm.route('products-order')+f'{id}/'
        method = self.view.app.request_parm.method('products-order')
        headers = self.view.app.auth_store['headers']['data']
        print(url,method,headers)
        req = UrlRequest(
                        url, 
                        on_success=self.model.product_added, 
                        method=method,
                        on_error=self.model.server_error, 
                        req_headers=headers, 
                        on_failure=self.model.server_failed
                    )

    def log_out(self):
        self.app.is_authenticated = False
        self.app.perform_store_save(self.app.is_authenticated, store_name='auth_store', key='is_authenticated')
        self.app.perform_store_save({}, store_name='auth_store', key='headers')

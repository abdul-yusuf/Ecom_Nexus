from View.base_screen import BaseScreenView
from kivy.clock import Clock

class LoginScreenView(BaseScreenView):
    def model_is_changed(self, *args) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        {
            'id': 4, 
            'vendor': None, 
            'last_login': '2022-11-08T12:09:40.662244Z', 
            'is_superuser': True, 
            'first_name': '', 
            'last_name': '', 
            'email': 'abdul@mail.com', 
            'is_staff': True, 
            'is_active': True, 
            'date_joined': '2022-11-03T06:22:50Z', 
            'address': 'Ungwan Dosa', 
            'is_vendor': True, 
            'username': '+2349093107509', 
            'groups': [], 
            'user_permissions': []
        }

        """
        is_loading = True
        try:
            # print(args)
            if self.app.auth_store.get('variable')['is_authenticated']==True:
                data = args[1]
                self.app.perform_store_save('auth_store', 'user',data=data)
                self.model.notify_observers('home screen')
                self.app.onNextScreen(self.name,'home screen','switch_to','home screen')
        except IndexError or KeyError as e:
            print(e)
        print(args,'notified')
    
    def server_success(self, *args, **kwargs):
        self.app.create_toast('Login Successfully')
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)
        headers = {
            'Authorization': f"Token {args[0][1]['key']}",
            'Content-type': 'application/json'
        }
        self.app.is_authenticated = True
        self.app.perform_store_save('auth_store', 'variable', is_authenticated=self.app.is_authenticated)
        self.app.perform_store_save('auth_store', 'headers', data=headers)
        self.controller.fetch_user_data(headers)
        print('from success')
        print(headers)
        print(args,kwargs,'success')

    def server_error(self, *args, **kwargs):
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)
        
        self.app.perform_store_save('auth_store', 'variable', is_authenticated=False)
        self.app.create_toast('Network Error')
        print(args, kwargs,'error')
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        print(args)
        # if isinstance(args[1],) 
        # msg = f'{}'
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)
        
        self.app.create_toast(str(args[0][1]))
    
    def server_processing(self, *args):
        self.app.perform_store_save('auth_store', 'variable', is_authenticated=False)
        self.app.modal_view(attach_to=self)
        print(args,'loading..')
    
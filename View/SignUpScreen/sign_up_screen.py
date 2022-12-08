from View.base_screen import BaseScreenView
from kivy.clock import Clock
from kivymd.uix.pickers import MDDatePicker
from kivymd.color_definitions import colors
from kivymd.theming import get_color_from_hex
from kivymd.uix.label import MDLabel
from Controller.login_screen import LoginScreenController

class SignUpScreenView(BaseScreenView):
    def model_is_changed(self,*args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def server_success(self, *args, **kwargs):
        self.app.create_toast('Signup Successfull')
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)

        if self.is_authenticated:
            self.app.onNextScreen(self.name,'email verification screen')
            

        headers = {
            'Authorization': f"Token {args[0][1]['key']}",
            'Content-type': 'application/json'
        }
        self.app.is_authenticated = True
        self.app.perform_store_save(headers, store_name='auth_store', key='headers')
        self.controller.fetch_user_data(headers)
        print('from success')
        print(args,kwargs,'success')

    def server_error(self, *args, **kwargs):
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)
        self.app.create_toast('Signup in Error')
        print(args, kwargs,'error')
        print(self.app.is_authenticated,'-----------------------')
        if not self.app.is_authenticated:
            # self.controller
            self.app.onNextScreen(self.name,'email verification screen')
        

    def server_failed(self, *args, **kwargs):
        if self.app.is_modal_open:
            Clock.schedule_once(self.app.modal_instance.dismiss, 1)
        self.app.create_toast('Server Error')
        
        print(args, kwargs)

    def server_processing(self, *args):
        self.app.modal_view(attach_to=self)
        print(args,'loading..')

    def password_check(self):
        pwd = self.ids.password
        line = self.ids.line
        box = self.ids.error_box
        mssg = MDLabel(
                    text='enter password',
                    pos_hint={'center_x': 0.55,'center_y': 0.01},
                    theme_text_color='Error'
                )
        print(pwd.focus)
        if pwd.text=='':
            line.md_bg_color = get_color_from_hex(colors['Red']['400'])
            box.add_widget(mssg)
        elif pwd.focus and pwd.text=='':
            line.md_bg_color = get_color_from_hex(colors['Red']['400'])
            # line.add_widget(mssg)
        else: 
            line.md_bg_color = get_color_from_hex(colors['Gray']['400'])
            box.remove_widget(mssg)
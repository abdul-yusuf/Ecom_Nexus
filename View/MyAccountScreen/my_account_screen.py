from View.base_screen import BaseScreenView
from kivymd.uix.pickers import MDDatePicker
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors

class MyAccountScreenView(BaseScreenView):
    editing_mode = False
    def model_is_changed(self, *args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print(args, kwargs)

    def editing_mode_func(self, *args):
        try:
            arg = args[0]
        except:
            arg = ''

        if not self.editing_mode and arg=='':
            print('Editing')
            self.ids.field1.disabled=False
            self.ids.field2.disabled=False
            self.ids.field3.disabled=False
            self.ids.date_field.disabled=False
            self.ids.checkout_btn.md_bg_color=get_color_from_hex(colors['Green']['600'])
            self.animate_front()
            self.editing_mode = True
        elif self.editing_mode and arg=='':
            print('Stoped Editing')
            self.ids.field1.disabled=True
            self.ids.field2.disabled=True
            self.ids.field3.disabled=True
            self.ids.date_field.disabled=True
            self.ids.checkout_btn.md_bg_color=self.app.theme_cls.primary_color
            self.animate_back()
            self.save_edit()
            self.editing_mode = False


        if arg=='cancel':
            print('Canceled')
            self.ids.field1.disabled=True
            self.ids.field2.disabled=True
            self.ids.field3.disabled=True
            self.ids.date_field.disabled=True
            self.ids.checkout_btn.md_bg_color=self.app.theme_cls.primary_color
            self.animate_back()
            self.editing_mode = False

    def save_edit(self):
            # if self.ids.checkout_btn.text=='Save':
        self.controller.user_update_request(
            {
                'first_name': self.ids.field1.text,
                'last_name': self.ids.field2.text
            }
        )



    def server_error(self, *args, **kwargs):
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        date_dialog.auto_dismiss = True

    def on_save(self, instance, value, date_range):
        instance.dismiss()
        self.ids.date_field.focus=False
        self.ids.date_field.text=str(value)

    def on_cancel(self, instance, value):
        instance.dismiss()
        self.ids.date_field.focus=False

    def server_success(self, *args, **kwargs):
        print(args, kwargs)
        if args[0][1]['first_name'] != '':
            self.ids.field1.text = args[0][1]['first_name']
        if args[0][1]['last_name'] != '':
            self.ids.field2.text = args[0][1]['last_name']

        # if self.editing_mode:
        #     self.editing_mode=False

    def animate_front(self):
        self.ids.checkout_btn.text='Save'

        Animation(
                pos_hint={'center_x': 0.25},
                t='out_quad',
                d=0.9/1
                ).start(self.ids.cancel_btn)
        Animation(
                size_hint_x=.55,
                pos_hint={'center_x': 0.7},
                t='in_quad',
                d=0.9/1
                ).start(self.ids.checkout_btn)
    def animate_back(self):
        self.ids.checkout_btn.text='Edit Details'

        Animation(
                pos_hint={'center_x': -1.25},
                d=0.9/1
                ).start(self.ids.cancel_btn)
        Animation(
                size_hint_x=.9,
                pos_hint={'center_x': 0.56},
                d=0.9/1
                ).start(self.ids.checkout_btn)
                
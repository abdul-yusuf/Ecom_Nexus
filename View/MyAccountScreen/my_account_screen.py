from View.base_screen import BaseScreenView


class MyAccountScreenView(BaseScreenView):
    editing_mode = False
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def editing_mode_func(self):

        if self.editing_mode:
            self.ids.field1.disabled=False
            self.ids.field2.disabled=False
            self.ids.field3.disabled=False
            self.ids.date_field.disabled=False
        else:
            self.ids.field1.disabled=True
            self.ids.field2.disabled=True
            self.ids.field3.disabled=True
            self.ids.date_field.disabled=True

    def server_error(self, *args, **kwargs):
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))
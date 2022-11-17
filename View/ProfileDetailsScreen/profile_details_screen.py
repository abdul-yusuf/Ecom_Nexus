from View.base_screen import BaseScreenView
from kivymd.uix.pickers import MDDatePicker

class ProfileDetailsScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_save(self, instance, value, date_range):
        self.ids.date_field.text=str(value)
        print(instance, value, date_range)

    def cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save,on_cancel=self.cancel)
        date_dialog.open()

from View.base_screen import BaseScreenView


class FeedScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def server_error(self, *args, **kwargs):
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))
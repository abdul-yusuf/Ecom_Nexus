from Model.base_model import BaseScreenModel


class TrackOrderScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.track_order_screen.TrackOrderScreen.TrackOrderScreenView` class.
    """

    def server_success(self, *args, **kwargs):
        self.notify_observers('track order screen', *args, meths='success')

        # pass

    def server_error(self, *args, **kwargs):
        self.notify_observers('track order screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('track order screen', args, meths='failed')

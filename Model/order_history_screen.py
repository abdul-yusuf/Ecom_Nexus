from Model.base_model import BaseScreenModel


class OrderHistoryScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.order_history_screen.OrderHistoryScreen.OrderHistoryScreenView` class.
    """

    def server_success(self, *args, **kwargs):
        print(args, kwargs)
        self.notify_observers('order history screen', args, meths='success')

    def server_error(self, *args, **kwargs):
        self.notify_observers('order history screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('order history screen', args, meths='failed')

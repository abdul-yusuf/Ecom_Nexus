from Model.base_model import BaseScreenModel


class CheckoutScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.checkout_screen.CheckoutScreen.CheckoutScreenView` class.
    """

    def cart_success(self, *args, **kwargs):
        self.notify_observers('checkout screen', args, meths='cart_success')
    
    def payment_success(self, *args, **kwargs):
        print(args, kwargs)
        try:
            authorization=args[1]['authorization']
        except KeyError as e:
            self.notify_observers('checkout screen', 'url', e, meths='error')
        self.notify_observers('checkout screen', args, authorization=authorization, meths='payment_success')

    def server_error(self, *args, **kwargs):
        self.notify_observers('checkout screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('checkout screen', args, meths='failed')

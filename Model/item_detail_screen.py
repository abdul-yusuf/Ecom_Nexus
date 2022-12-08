from Model.base_model import BaseScreenModel


class ItemDetailScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.item_detail_screen.ItemDetailScreen.ItemDetailScreenView` class.
    """

    def product_added(self, *args, **kwargs):
        print(args,kwargs)
       
    def server_error(self, *args, **kwargs):
        self.notify_observers('item detail screen', *args, meths='error')
        
    def server_failed(self, *args, **kwargs):
        self.notify_observers('item detail screen', args, meths='failed')

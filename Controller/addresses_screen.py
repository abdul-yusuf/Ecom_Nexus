import importlib

import View.AddressesScreen.addresses_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.AddressesScreen.addresses_screen)




class AddressesScreenController:
    """
    The `AddressesScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.addresses_screen.AddressesScreenModel
        self.view = View.AddressesScreen.addresses_screen.AddressesScreenView(controller=self, model=self.model)

    def get_view(self) -> View.AddressesScreen.addresses_screen:
        return self.view
